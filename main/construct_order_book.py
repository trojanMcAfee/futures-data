from __future__ import annotations
import os
import json
from datetime import datetime
from collections import defaultdict
from dataclasses import dataclass, field
from itertools import takewhile
from enum import Flag, auto

# Import necessary classes and constants.
# (These are assumed to be available from your Databento-related package.)
from databento_dbn import FIXED_PRICE_SCALE, UNDEF_PRICE, BidAskPair, MBOMsg
from sortedcontainers import SortedDict

# Define RecordFlags since it's not available in the current version
class RecordFlags(Flag):
    NONE = 0
    F_LAST = auto()  # Last message in batch
    F_TOB = auto()   # Top of book update

# -------------------------------
# Data Structures for the Order Book
# -------------------------------

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
            count=sum(1 for o in self.orders if not o.flags & RecordFlags.F_TOB),
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
            # For bids, the highest prices come last in the SortedDict.
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
        # Trade, Fill, or None messages do not affect the book.
        if mbo.action in ("T", "F", "N"):
            return
        # A Clear ("R") action removes all resting orders.
        if mbo.action == "R":
            self._clear()
            return
        # For non-clear actions, side must be "A" (ask) or "B" (bid).
        assert mbo.side in ("A", "B")
        # If a top-of-book update is received (price == UNDEF_PRICE), clear the side.
        if mbo.price == UNDEF_PRICE and mbo.flags & RecordFlags.F_TOB:
            self._side_levels(mbo.side).clear()
            return
        # Add, Cancel, or Modify actions.
        if mbo.action == "A":
            self._add(mbo)
        elif mbo.action == "C":
            self._cancel(mbo)
        elif mbo.action == "M":
            self._modify(mbo)
        else:
            raise ValueError(f"Unknown action={mbo.action}")

    def _clear(self) -> None:
        self.orders_by_id.clear()
        self.offers.clear()
        self.bids.clear()

    def _add(self, mbo: MBOMsg) -> None:
        if mbo.flags & RecordFlags.F_TOB:
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
        # Remove the order if its entire size is cancelled.
        if order.size == 0:
            self.orders_by_id.pop(mbo.order_id)
            level.orders.remove(order)
            if not level:
                self._remove_level(mbo.price, mbo.side)

    def _modify(self, mbo: MBOMsg) -> None:
        order = self.orders_by_id.get(mbo.order_id)
        if order is None:
            # If the order doesn't exist, treat this as an add.
            self._add(mbo)
            return
        assert order.side == mbo.side, f"Order {order} changed side to {mbo.side}"
        level = self._get_level(order.price, order.side)
        if order.price != mbo.price:
            # Changing the price means losing priority.
            level.orders.remove(order)
            if not level:
                self._remove_level(order.price, mbo.side)
            level = self._get_or_insert_level(mbo.price, mbo.side)
            level.orders.append(mbo)
        elif order.size < mbo.size:
            # Increasing the size loses priority.
            level.orders.remove(order)
            level.orders.append(mbo)
        else:
            # Update the order in place.
            level.orders[level.orders.index(order)] = mbo
        self.orders_by_id[mbo.order_id] = mbo

    def _side_levels(self, side: str) -> SortedDict:
        if side == "A":
            return self.offers
        if side == "B":
            return self.bids
        raise ValueError(f"Invalid side: {side}")

    def _get_level(self, price: int, side: str) -> LevelOrders:
        levels = self._side_levels(side)
        if price not in levels:
            raise KeyError(f"No price level found for price={price} and side={side}")
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
        default_factory=lambda: defaultdict(lambda: defaultdict(Book))
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
        # For bids, we take the maximum price; for asks, the minimum.
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

# -------------------------------
# JSON Data Conversion Helpers
# -------------------------------

def parse_timestamp(ts_str: str) -> datetime:
    """
    Convert an ISO 8601 string (with a trailing "Z" for UTC) to a datetime object.
    """
    return datetime.fromisoformat(ts_str.replace("Z", "+00:00"))

def json_to_mbo(raw: dict) -> MBOMsg:
    """
    Convert a JSON dictionary (following the given convention) to an MBOMsg.
    Adjust conversions as necessary.
    """
    # Convert price from string to integer (multiplied by FIXED_PRICE_SCALE)
    price = None if raw["price"] is None else int(float(raw["price"]) * FIXED_PRICE_SCALE)
    
    # Generate a unique order ID based on timestamp and other fields if not provided
    # This is a workaround since our data doesn't include order IDs
    order_id = hash(f"{raw['ts_recv']}{raw['action']}{raw['side']}{raw['price']}{raw['size']}")
    
    return MBOMsg(
        ts_event = parse_timestamp(raw["hd"]["ts_event"]),
        ts_recv = parse_timestamp(raw["ts_recv"]),
        action = raw["action"],
        side = raw["side"],
        price = price if price is not None else UNDEF_PRICE,
        size = raw["size"],
        order_id = order_id,
        flags = RecordFlags.F_LAST if raw["hd"]["rtype"] == 160 else RecordFlags.NONE,
        instrument_id = raw["hd"]["instrument_id"],
        publisher_id = raw["hd"]["publisher_id"],
    )

# -------------------------------
# Main Routine: Load JSON Data and Build the Book
# -------------------------------

if __name__ == "__main__":
    # Instead of fetching data from Databento, we load it from a JSON file.
    data_path = "data/uso/order-book/2024-01-02.json"
    if os.path.exists(data_path):
        with open(data_path, "r") as f:
            # Option 1: If the file contains one JSON object per line (JSON Lines)
            json_data = [json.loads(line) for line in f if line.strip()]
            # Option 2: If the file is a JSON array, uncomment the following line:
            # json_data = json.load(f)
    else:
        raise FileNotFoundError(f"JSON file '{data_path}' not found.")

    # Create a Market instance to manage the order books.
    market = Market()

    # Process each JSON record and update the order book.
    for raw_msg in json_data:
        mbo = json_to_mbo(raw_msg)
        market.apply(mbo)
        # If this message is flagged as the last in an update batch (F_LAST), print an aggregated snapshot.
        if mbo.flags & RecordFlags.F_LAST:
            # Use the symbol from the JSON (if available) for printing.
            symbol = raw_msg.get("symbol", "")
            print(f"{symbol} Aggregated BBO | {mbo.ts_recv}")
            best_bid, best_offer = market.aggregated_bbo(mbo.instrument_id)
            print(f"    Best Offer: {best_offer}")
            print(f"    Best Bid: {best_bid}")
