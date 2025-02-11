from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import List, Dict, Any

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

    def to_dict(self) -> Dict[str, Any]:
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

@dataclass
class SimulationResults:
    start_time: datetime
    end_time: datetime
    total_investment: float
    total_profit: float
    trades: List[Trade]

    def to_dict(self) -> Dict[str, Any]:
        return {
            'start_time': self.start_time,
            'end_time': self.end_time,
            'total_investment': self.total_investment,
            'total_profit': self.total_profit,
            'trades': [trade.to_dict() for trade in self.trades]
        } 