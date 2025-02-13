"""
Report generator for NAV arbitrage simulations. This module provides:
- Data structures for organizing simulation results
- Detailed trade-by-trade reporting
- Performance metrics calculation and formatting
- Summary statistics for simulation runs

The report generator takes raw simulation results and produces formatted output
showing trade details, cumulative metrics, and overall performance statistics,
making it easy to analyze the effectiveness of the NAV arbitrage strategy.
"""

from __future__ import annotations
import pandas as pd
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

@dataclass
class SimulationResults:
    start_time: datetime
    end_time: Optional[datetime]
    total_investment: float
    total_profit: float
    trades: List[dict]

def generate_report(results: SimulationResults) -> None:
    print("\n=== NAV Arbitrage Trading Report ===")
    print(f"Simulation period: {results.start_time} to {results.end_time if results.end_time else 'No trades executed'}")
    if results.end_time:
        print(f"Duration: {results.end_time - results.start_time}")
    else:
        print("Duration: No trades executed")
    print(f"\nTotal Investment: ${results.total_investment:,.2f}")
    print(f"Total Profit: ${results.total_profit:,.2f}")
    
    # Calculate ROI only if there was investment
    if results.total_investment > 0:
        roi = (results.total_profit / results.total_investment * 100)
        print(f"Overall ROI: {roi:.2f}%")
    else:
        print("Overall ROI: N/A - No trades executed")
    
    print(f"Number of trades: {len(results.trades)}")
    
    # Convert trades to DataFrame for summary
    if results.trades:
        trades_df = pd.DataFrame(results.trades)
        trades_df['timestamp'] = pd.to_datetime(trades_df['timestamp'])
        
        # Calculate cumulative metrics
        trades_df['cumulative_investment'] = trades_df['initial_investment'].cumsum()
        trades_df['cumulative_profit'] = trades_df['net_profit'].cumsum()
        trades_df['cumulative_roi'] = (trades_df['cumulative_profit'] / trades_df['cumulative_investment']) * 100

        print("\n=== Trade Summary ===")
        print(trades_df.to_string(index=False)) 