from __future__ import annotations
import os
from collections import defaultdict
from dataclasses import dataclass, field
from itertools import takewhile
import databento as db
from databento_dbn import FIXED_PRICE_SCALE, UNDEF_PRICE, BidAskPair, MBOMsg
from sortedcontainers import SortedDict

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
        order = self.orders_by_id[mbo.order_id]
        level = self._get_level(mbo.price, mbo.side)
        assert order.size >= mbo.size
        order.size -= mbo.size
        # If the full size is cancelled, remove the order from the book
        if order.size == 0:
            self.orders_by_id.pop(mbo.order_id)
            level.orders.remove(order)
            # If the level is now empty, remove it from the book
            if not level:
                self._remove_level(mbo.price, mbo.side)

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

    # Request MBO data for USO during regular trading hours
    data_path = "data/uso/order-book/arcx-pillar-20240102.mbo.dbn.zst"
    
    # Force a fresh download of the data, starting from UTC midnight to get the initial snapshot
    data = client.timeseries.get_range(
        dataset="ARCX.PILLAR",
        start="2024-01-02T00:00:00",  # Start from UTC midnight to get initial snapshot
        end="2024-01-02T21:00:00",    # 4:00 PM EST
        symbols=["USO"],
        schema="mbo",
        path=data_path,
    )

    # Parse the symbology
    instrument_map = db.common.symbology.InstrumentMap()
    instrument_map.insert_metadata(data.metadata)

    # Create a market instance and process the data
    market = Market()
    print_count = 0  # Counter to limit output to 5 snapshots
    trading_started = False  # Flag to track if we've reached regular trading hours
    last_print_time = None  # Track when we last printed a snapshot

    for mbo in data:
        # Only print snapshots during regular trading hours
        ts = mbo.pretty_ts_recv
        if ts.hour == 14 and ts.minute >= 30:  # 9:30 AM EST
            trading_started = True
        
        try:
            market.apply(mbo)
            # Print snapshots spread throughout the trading day
            if (trading_started and 
                mbo.flags & db.RecordFlags.F_LAST and 
                print_count < 5 and
                (last_print_time is None or (ts - last_print_time).total_seconds() > 3600)):  # At least 1 hour between snapshots
                
                symbol = (
                    instrument_map.resolve(mbo.instrument_id, ts.date())
                    or "USO"
                )
                print(f"\n{symbol} Aggregated BBO | {ts}")
                best_bid, best_offer = market.aggregated_bbo(mbo.instrument_id)
                print(f"    Best Offer: {best_offer}")
                print(f"    Best Bid: {best_bid}")
                print_count += 1
                last_print_time = ts
        except KeyError as e:
            # Skip orders that can't be found (this can happen with partial data)
            continue 