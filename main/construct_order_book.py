from __future__ import annotations
import os
from collections import defaultdict
from dataclasses import dataclass, field
from itertools import takewhile
import databento as db
from databento_dbn import FIXED_PRICE_SCALE, UNDEF_PRICE, BidAskPair, MBOMsg
from sortedcontainers import SortedDict
from datetime import datetime, timezone

'''
This script is used to construct the order book for USO during regular trading hours.
'''

@dataclass
class PriceLevel:
    price: int
    size: int = 0
    count: int = 0

    def __str__(self) -> str:
        price = self.price / FIXED_PRICE_SCALE
        return f"{self.size:4} @ {price:6.2f} | {self.count:2} order(s)"

@dataclass
class LevelOrders:
    price: int
    orders: list[MBOMsg] = field(default_factory=list, compare=False)

    def __bool__(self) -> bool:
        return bool(self.orders)

    @property
    def level(self) -> PriceLevel:
        return PriceLevel(
            price=self.price,
            count=sum(1 for o in self.orders if not o.flags & db.RecordFlags.F_TOB),
            size=sum(o.size for o in self.orders),
        )

@dataclass
class Book:
    orders_by_id: dict[int, MBOMsg] = field(default_factory=dict)
    offers: SortedDict[int, LevelOrders] = field(default_factory=SortedDict)
    bids: SortedDict[int, LevelOrders] = field(default_factory=SortedDict)

    def bbo(self) -> tuple[PriceLevel | None, PriceLevel | None]:
        return self.get_bid_level(), self.get_ask_level()

    def get_bid_level(self, idx: int = 0) -> PriceLevel | None:
        if self.bids and len(self.bids) > idx:
            # Reverse for bids to get highest prices first
            return self.bids.peekitem(-(idx + 1))[1].level
        return None

    def get_ask_level(self, idx: int = 0) -> PriceLevel | None:
        if self.offers and len(self.offers) > idx:
            return self.offers.peekitem(idx)[1].level
        return None

    def get_bid_level_by_px(self, px: int) -> PriceLevel | None:
        try:
            return self._get_level(px, "B").level
        except KeyError:
            return None

    def get_ask_level_by_px(self, px: int) -> PriceLevel | None:
        try:
            return self._get_level(px, "A").level
        except KeyError:
            return None

    def get_order(self, id: int) -> MBOMsg | None:
        return self.orders_by_id.get(id)

    def get_queue_pos(self, id: int) -> int | None:
        order = self.get_order(id)
        if not order:
            return None
        level = self._get_level(order.price, order.side)
        return sum(
            order.size for order in takewhile(lambda o: o.order_id != id, level.orders)
        )

    def get_snapshot(self, level_count: int = 1) -> list[BidAskPair]:
        snapshots = []
        for level in range(level_count):
            ba_pair = BidAskPair()
            bid = self.get_bid_level(level)
            if bid:
                ba_pair.bid_px = bid.price
                ba_pair.bid_sz = bid.size
                ba_pair.bid_ct = bid.count
            ask = self.get_ask_level(level)
            if ask:
                ba_pair.ask_px = ask.price
                ba_pair.ask_sz = ask.size
                ba_pair.ask_ct = ask.count
            snapshots.append(ba_pair)
        return snapshots

    def apply(self, mbo: MBOMsg) -> None:
        # Trade, Fill, or None: no change
        if mbo.action in ("T", "F", "N"):
            return
        # Clear book: remove all resting orders
        if mbo.action == "R":
            self._clear()
            return
        # side=N is only valid with Trade, Fill, and Clear actions
        assert mbo.side in ("A", "B")
        # UNDEF_PRICE indicates the book level should be removed
        if mbo.price == UNDEF_PRICE and mbo.flags & db.RecordFlags.F_TOB:
            self._side_levels(mbo.side).clear()
            return
        # Add: insert a new order
        if mbo.action == "A":
            self._add(mbo)
        # Cancel: partially or fully cancel some size from a resting order
        elif mbo.action == "C":
            self._cancel(mbo)
        # Modify: change the price and/or size of a resting order
        elif mbo.action == "M":
            self._modify(mbo)
        else:
            raise ValueError(f"Unknown action={mbo.action}")

    def _clear(self) -> None:
        self.orders_by_id.clear()
        self.offers.clear()
        self.bids.clear()

    def _add(self, mbo: MBOMsg) -> None:
        if mbo.flags & db.RecordFlags.F_TOB:
            levels = self._side_levels(mbo.side)
            levels.clear()
            levels[mbo.price] = LevelOrders(price=mbo.price, orders=[mbo])
        else:
            level = self._get_or_insert_level(mbo.price, mbo.side)
            assert mbo.order_id not in self.orders_by_id
            self.orders_by_id[mbo.order_id] = mbo
            level.orders.append(mbo)

    def _cancel(self, mbo: MBOMsg) -> None:
        """Cancel an order."""
        try:
            order = self.orders_by_id[mbo.order_id]
            price_level = self._get_level(order.price, order.side)
            price_level.orders.remove(order)
            if not price_level.orders:
                self._remove_level(order.price, order.side)
            del self.orders_by_id[mbo.order_id]
        except KeyError:
            # Skip if we try to cancel an order that doesn't exist in our book
            # This can happen if the order was placed before our observation window
            pass

    def _modify(self, mbo: MBOMsg) -> None:
        order = self.orders_by_id.get(mbo.order_id)
        if order is None:
            # If order not found, treat it as an add
            self._add(mbo)
            return
        assert order.side == mbo.side, f"Order {order} changed side to {mbo.side}"
        level = self._get_level(order.price, order.side)
        if order.price != mbo.price:
            # Changing price loses priority
            level.orders.remove(order)
            if not level:
                self._remove_level(order.price, mbo.side)
            level = self._get_or_insert_level(mbo.price, mbo.side)
            level.orders.append(mbo)
        elif order.size < mbo.size:
            # Increasing size loses priority
            level.orders.remove(order)
            level.orders.append(mbo)
        else:
            # Update in place
            level.orders[level.orders.index(order)] = mbo
        self.orders_by_id[mbo.order_id] = mbo

    def _side_levels(self, side: str) -> SortedDict:
        if side == "A":
            return self.offers
        if side == "B":
            return self.bids
        raise ValueError(f"Invalid {side =}")

    def _get_level(self, price: int, side: str) -> LevelOrders:
        levels = self._side_levels(side)
        if price not in levels:
            raise KeyError(f"No price level found for {price =} and {side =}")
        return levels[price]

    def _get_or_insert_level(self, price: int, side: str) -> LevelOrders:
        levels = self._side_levels(side)
        if price in levels:
            return levels[price]
        level = LevelOrders(price=price)
        levels[price] = level
        return level

    def _remove_level(self, price: int, side: str) -> None:
        levels = self._side_levels(side)
        levels.pop(price)

@dataclass
class Market:
    books: defaultdict[int, defaultdict[int, Book]] = field(
        default_factory=lambda: defaultdict(lambda: defaultdict(Book)),
    )

    def get_books_by_pub(self, instrument_id: int) -> defaultdict[int, Book]:
        return self.books[instrument_id]

    def get_book(self, instrument_id: int, publisher_id: int) -> Book:
        return self.books[instrument_id][publisher_id]

    def bbo(
        self,
        instrument_id: int,
        publisher_id: int,
    ) -> tuple[PriceLevel | None, PriceLevel | None]:
        return self.books[instrument_id][publisher_id].bbo()

    def aggregated_bbo(
        self,
        instrument_id: int,
    ) -> tuple[PriceLevel | None, PriceLevel | None]:
        agg_bbo: list[PriceLevel | None] = [None, None]
        # max for bids, min for asks
        for idx, reducer in [(0, max), (1, min)]:
            all_best = [b.bbo()[idx] for b in self.books[instrument_id].values()]
            all_best = [b for b in all_best if b]
            if not all_best:
                continue
            best_price = reducer(b.price for b in all_best)
            best = [b for b in all_best if b.price == best_price]
            agg_bbo[idx] = PriceLevel(
                price=best_price,
                size=sum(b.size for b in best),
                count=sum(b.count for b in best),
            )
        return tuple(agg_bbo)

    def apply(self, mbo: MBOMsg) -> None:
        book = self.books[mbo.instrument_id][mbo.publisher_id]
        book.apply(mbo)

if __name__ == "__main__":
    # Create a historical client with your API key
    client = db.Historical("db-TrTUvBD8siexi8SwnA4c9FVWveHuj")

    # Request MBO data for USO during regular market hours, starting from midnight for synthetic snapshot
    data_path = "data/uso/order-book/arcx-pillar-20240103-full.mbo.dbn.zst"
    
    # Only download if the file doesn't exist
    if not os.path.exists(data_path):
        print(f"Downloading data to {data_path}...")
        data = client.timeseries.get_range(
            dataset="ARCX.PILLAR",
            schema="mbo",
            symbols=["USO"],
            start="2024-01-03T00:00:00",    # Start from midnight UTC to get synthetic snapshot
            end="2024-01-03T21:00:00",      # 4:00 PM EST
            path=data_path,
        )
    else:
        print(f"Using existing data from {data_path}")
        data = db.DBNStore.from_file(data_path)

    # Parse the symbology
    instrument_map = db.common.symbology.InstrumentMap()
    instrument_map.insert_metadata(data.metadata)

    # Create a market instance and process the data
    market = Market()
    snapshots = []  # Store snapshots after market open
    message_count = 0  # Debug counter
    last_print_time = None  # Track time between snapshots
    # Define market open time (9:00 AM EST / 14:00 UTC)
    market_open_time = datetime(2024, 1, 3, 14, 0, 0, tzinfo=timezone.utc)

    print("\nProcessing data and building order book...")
    print("(Including synthetic snapshot from midnight UTC for complete book state)")

    for mbo in data:
        ts = mbo.pretty_ts_recv
        message_count += 1
        market.apply(mbo)

        # Only start collecting snapshots after market open
        if ts >= market_open_time:
            # Store snapshots in the first few milliseconds after market open
            # Only store if at least 1 millisecond has passed since last snapshot
            if (mbo.flags & db.RecordFlags.F_LAST and 
                len(snapshots) < 10 and
                (last_print_time is None or (ts - last_print_time).total_seconds() >= 0.001)):
                
                symbol = instrument_map.resolve(mbo.instrument_id, ts.date()) or "USO"
                best_bid, best_offer = market.aggregated_bbo(mbo.instrument_id)
                snapshots.append((ts, symbol, best_bid, best_offer))
                last_print_time = ts

    print(f"\nProcessed {message_count} messages")
    print(f"Found {len(snapshots)} snapshots at market open")

    # Print the snapshots
    if snapshots:
        print("\nOrder Book State At Market Open:")
        print(f"Market opened at: 2024-01-03 14:00:00 UTC (9:00 AM EST)")
        print("(Order book initialized with midnight UTC synthetic snapshot)")
        print("-" * 60)
        
        for ts, symbol, best_bid, best_offer in snapshots:
            print(f"\n{symbol} Aggregated BBO | {ts}")
            print(f"    Best Offer: {best_offer}")
            print(f"    Best Bid: {best_bid}")
            print(f"    Time since market open: {(ts - market_open_time).total_seconds():.3f} seconds")
            if best_bid and best_offer:
                spread = (best_offer.price - best_bid.price) / FIXED_PRICE_SCALE
                spread_pct = (spread / (best_offer.price / FIXED_PRICE_SCALE)) * 100
                print(f"    Spread: ${spread:.2f} ({spread_pct:.3f}%)")
    else:
        print("\nNo snapshots found at market open. Available time range:")
        print(f"First message: {data[0].pretty_ts_recv}")
        print(f"Last message: {data[-1].pretty_ts_recv}") 