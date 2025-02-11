from __future__ import annotations
import pandas as pd
from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass
class SimulationResults:
    start_time: datetime
    end_time: datetime
    total_investment: float
    total_profit: float
    trades: List[dict]
    skipped_opportunities: List[dict]

def generate_report(results: SimulationResults) -> None:
    print("\n=== NAV Arbitrage Trading Report ===")
    print(f"Simulation period: {results.start_time} to {results.end_time}")
    print(f"Duration: {results.end_time - results.start_time}")
    print(f"\nTotal Investment: ${results.total_investment:,.2f}")
    print(f"Total Profit: ${results.total_profit:,.2f}")
    print(f"Overall ROI: {(results.total_profit / results.total_investment * 100):.2f}%")
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

    # Show skipped opportunities summary
    print("\n=== Skipped Opportunities ===")
    print(f"Number of skipped opportunities: {len(results.skipped_opportunities)}")
    
    if results.skipped_opportunities:
        print("\nFirst skipped trade:")
        first = results.skipped_opportunities[0]
        print(f"Timestamp: {first['timestamp']}")
        print(f"Shares: {first['shares']}")
        print(f"NAV Price: ${first['nav_price']:.2f}")
        print(f"Bid Price: ${first['bid_price']:.2f}")
        print(f"Price Difference: ${first['price_difference']:.2f}")
        
        print("\nLast skipped trade:")
        last = results.skipped_opportunities[-1]
        print(f"Timestamp: {last['timestamp']}")
        print(f"Shares: {last['shares']}")
        print(f"NAV Price: ${last['nav_price']:.2f}")
        print(f"Bid Price: ${last['bid_price']:.2f}")
        print(f"Price Difference: ${last['price_difference']:.2f}") 