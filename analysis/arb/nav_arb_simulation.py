from __future__ import annotations
import os
import sys
from datetime import datetime, timezone
from dataclasses import dataclass
from typing import List, Optional, Dict
import pandas as pd
import databento as db
from databento_dbn import FIXED_PRICE_SCALE

# Add the main directory to the Python path so we can import construct_order_book
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'main'))
from construct_order_book import Market

@dataclass
class Trade:
    timestamp: datetime
    shares: int
    nav_price: float
    bid_price: float
    initial_investment: float
    gross_revenue: float
    net_profit: float
    roi_percent: float

    def to_dict(self) -> Dict:
        return {
            'timestamp': self.timestamp,
            'shares': self.shares,
            'nav_price': self.nav_price,
            'bid_price': self.bid_price,
            'initial_investment': self.initial_investment,
            'gross_revenue': self.gross_revenue,
            'net_profit': self.net_profit,
            'roi_percent': self.roi_percent
        }

class NAVArbitrageSimulator:
    def __init__(self, initial_capital: float, target_capital: float):
        self.initial_capital = initial_capital
        self.target_capital = target_capital
        self.remaining_capital = target_capital
        self.trades: List[Trade] = []
        self.total_profit = 0
        self.total_investment = 0
        self.start_time: Optional[datetime] = None
        self.end_time: Optional[datetime] = None

    def process_opportunity(self, timestamp: datetime, shares: int, nav_price: float, bid_price: float) -> None:
        # Set start time if not set
        if not self.start_time:
            self.start_time = timestamp

        # If we're out of capital, don't process any more opportunities
        if self.remaining_capital <= 0:
            return

        # Skip if bid price is lower than NAV
        if bid_price <= nav_price:
            return

        # Calculate the investment needed for this trade
        investment = shares * nav_price

        # If this trade would exceed our remaining capital, adjust shares
        if investment > self.remaining_capital:
            shares = int(self.remaining_capital / nav_price)
            investment = shares * nav_price

        if shares == 0:
            return

        # Calculate trade metrics
        gross_revenue = shares * bid_price
        net_profit = gross_revenue - investment
        roi = (net_profit / investment) * 100

        # Record the trade
        self.trades.append(
            Trade(
                timestamp=timestamp,
                shares=shares,
                nav_price=nav_price,
                bid_price=bid_price,
                initial_investment=investment,
                gross_revenue=gross_revenue,
                net_profit=net_profit,
                roi_percent=roi
            )
        )

        # Update simulator state
        self.total_profit += net_profit
        self.total_investment += investment
        self.remaining_capital -= investment
        self.end_time = timestamp

    def get_results(self) -> Dict:
        return {
            'start_time': self.start_time,
            'end_time': self.end_time,
            'total_investment': self.total_investment,
            'total_profit': self.total_profit,
            'trades': [trade.to_dict() for trade in self.trades]
        } 