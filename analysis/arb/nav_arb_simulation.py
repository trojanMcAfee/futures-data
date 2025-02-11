from __future__ import annotations
import os
import sys
from datetime import datetime, timezone
from typing import List, Optional, Dict

from analysis.arb.simulation_types import Trade, SimulationResults

class NAVArbitrageSimulator:
    def __init__(self, nav_price: float, initial_capital: float, target_capital: float):
        self.nav_price = nav_price
        self.initial_capital = initial_capital
        self.target_capital = target_capital
        self.remaining_capital = target_capital
        self.trades: List[Trade] = []
        self.total_profit = 0
        self.total_investment = 0
        self.start_time: Optional[datetime] = None
        self.end_time: Optional[datetime] = None

    def process_opportunity(self, msg) -> None:
        # Set start time if not set
        if not self.start_time:
            self.start_time = msg.ts

        # If we're out of capital, don't process any more opportunities
        if self.remaining_capital <= 0:
            return

        # Skip if bid price is lower than NAV
        if msg.bid_px <= self.nav_price:
            return

        # Calculate the investment needed for this trade
        investment = msg.bid_sz * self.nav_price

        # If this trade would exceed our remaining capital, adjust shares
        if investment > self.remaining_capital:
            shares = int(self.remaining_capital / self.nav_price)
            investment = shares * self.nav_price
        else:
            shares = msg.bid_sz

        if shares == 0:
            return

        # Calculate trade metrics
        gross_revenue = shares * msg.bid_px
        net_profit = gross_revenue - investment
        roi = (net_profit / investment) * 100

        # Record the trade
        self.trades.append(
            Trade(
                timestamp=msg.ts,
                shares=shares,
                nav_price=self.nav_price,
                bid_price=msg.bid_px,
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
        self.end_time = msg.ts

    def get_results(self) -> SimulationResults:
        return SimulationResults(
            start_time=self.start_time,
            end_time=self.end_time,
            total_investment=self.total_investment,
            total_profit=self.total_profit,
            trades=self.trades
        ) 