"""
Core simulator for NAV arbitrage trading strategy. This module implements:
- Trade execution logic with capital management
- Real-time tracking of profits, investments, and ROI
- Trade record keeping with detailed metrics
- Capital allocation and position sizing

The simulator maintains state throughout a trading session, tracking available capital,
executed trades, and cumulative performance metrics. It implements safety checks to
prevent over-allocation of capital and ensures trades are only executed when
profitable opportunities exist (bid price > NAV price).
"""

from __future__ import annotations
import os
import sys
from datetime import datetime, timezone, timedelta
from dataclasses import dataclass
from typing import List, Optional, Dict
import pandas as pd
import databento as db
from databento_dbn import FIXED_PRICE_SCALE

# Add the main directory to the Python path so we can import construct_order_book
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'main'))
from construct_order_book import Market
from analysis.arb.transaction_cost import calculate_transaction_cost, SWAP_COST

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
    block: int
    base_fee: float
    total_cost: float

    def to_dict(self) -> Dict:
        return {
            'timestamp': self.timestamp,
            'shares': self.shares,
            'nav_price': self.nav_price,
            'bid_price': self.bid_price,
            'initial_investment': self.initial_investment,
            'gross_revenue': self.gross_revenue,
            'net_profit': self.net_profit,
            'roi_percent': self.roi_percent,
            'block': self.block,
            'base_fee': self.base_fee,
            'total_cost': self.total_cost
        }

class NAVArbitrageSimulator:
    def __init__(self, initial_capital: float, target_capital: float, delay_ms: int = 1):
        self.initial_capital = initial_capital
        self.target_capital = target_capital
        self.remaining_capital = target_capital
        self.trades: List[Trade] = []
        self.total_profit = 0
        self.total_investment = 0
        self.start_time: Optional[datetime] = None
        self.end_time: Optional[datetime] = None
        self.last_trade_time: Optional[datetime] = None
        self.min_time_between_trades = timedelta(milliseconds=delay_ms)

    def can_trade(self, current_time: datetime) -> bool:
        if self.last_trade_time is None:
            return True
        return (current_time - self.last_trade_time) >= self.min_time_between_trades

    def process_opportunity(self, timestamp: datetime, shares: int, nav_price: float, bid_price: float) -> None:
        # Set start time if not set
        if not self.start_time:
            self.start_time = timestamp

        # Check if enough time has passed since last trade
        if not self.can_trade(timestamp):
            return

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

        # Calculate trade metrics before transaction costs
        gross_revenue = shares * bid_price
        net_profit_before_costs = gross_revenue - investment

        try:
            # Calculate transaction costs
            tx_cost = calculate_transaction_cost(timestamp)
            total_cost_usd = tx_cost['total_cost_usd']

            # Only proceed if the trade is still profitable after costs
            if net_profit_before_costs <= total_cost_usd:
                return

            # Calculate final trade metrics including transaction costs
            net_profit = net_profit_before_costs - total_cost_usd
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
                    roi_percent=roi,
                    block=tx_cost['block'],
                    base_fee=tx_cost['base_fee_gwei'],
                    total_cost=total_cost_usd
                )
            )

            # Update simulator state
            self.total_profit += net_profit
            self.total_investment += investment
            self.remaining_capital -= investment
            self.end_time = timestamp
            self.last_trade_time = timestamp

        except Exception as e:
            print(f"Error calculating transaction costs: {str(e)}")
            return

    def get_results(self) -> Dict:
        return {
            'start_time': self.start_time,
            'end_time': self.end_time,
            'total_investment': self.total_investment,
            'total_profit': self.total_profit,
            'trades': [trade.to_dict() for trade in self.trades]
        } 