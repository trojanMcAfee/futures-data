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
from analysis.arb.periphery.transaction_cost import SWAP_COST

@dataclass
class SimulationResults:
    start_time: datetime
    end_time: Optional[datetime]
    total_investment: float
    total_profit: float
    trades: List[dict]
    data_quality: str = 'available'  # Can be 'available', 'degraded', 'pending', 'missing', or 'intraday'

def generate_report(results: SimulationResults) -> None:
    print("\n=== NAV Arbitrage Trading Report ===")
    print(f"Simulation period: {results.start_time} to {results.end_time if results.end_time else 'No trades executed'}")
    print(f"Data Quality: {results.data_quality.upper()}")
    print(f"Gas Units per Trade (SWAP_COST): {SWAP_COST:,}")
    
    if results.data_quality != 'available':
        print("⚠️  Warning: Results may be affected by data quality issues")
    
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
        
        # Calculate total transaction costs
        total_costs = trades_df['total_cost'].sum()
        avg_cost_per_trade = total_costs / len(trades_df) if len(trades_df) > 0 else 0
        
        print(f"\nTransaction Costs Summary:")
        print(f"Total Transaction Costs: ${total_costs:,.2f}")
        print(f"Average Cost per Trade: ${avg_cost_per_trade:,.2f}")
        print(f"Transaction Costs as % of Gross Profit: {(total_costs / (results.total_profit + total_costs) * 100):.2f}%")

        print("\n=== Trade Summary ===")
        
        # Create multi-level column headers with adjusted spacing
        columns = pd.MultiIndex.from_tuples([
            ('', 'timestamp'),
            ('investment', 'shares'),
            ('investment', 'nav_price'),
            ('investment', 'bid_price'),
            ('investment', 'initial_investment'),
            ('costs', 'block'),
            ('costs', 'base_fee'),
            ('costs', 'eth_price'),
            ('costs', 'total_cost'),
            ('revenue/profits', 'gross_revenue'),
            ('revenue/profits', 'net_profit'),
            ('revenue/profits', 'roi_percent'),
            ('TOTALS', 'cumulative_investment'),
            ('TOTALS', 'cumulative_profit'),
            ('TOTALS', 'cumulative_roi')
        ])
        
        # Reorder columns and set multi-level headers
        trades_df = trades_df[[col[1] for col in columns]]
        trades_df.columns = columns
        
        # Format the output
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.expand_frame_repr', False)
        
        # Adjust column spacing
        with pd.option_context('display.max_colwidth', None):
            print(trades_df.to_string(index=False))