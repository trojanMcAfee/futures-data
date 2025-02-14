from __future__ import annotations
import os
import sys
from datetime import datetime, timezone, timedelta
from dotenv import load_dotenv
import databento as db
from databento_dbn import FIXED_PRICE_SCALE
import json
from dataclasses import dataclass
from typing import List, Dict, Optional
import pandas as pd

# Add the project root to the Python path
project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)

# Load environment variables from the root directory
dotenv_path = os.path.join(project_root, '.env')
load_dotenv(dotenv_path)

# Add the main directory to the Python path
sys.path.append(os.path.join(project_root, 'main'))
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

class NAVArbitrageSimulator250ms:
    def __init__(self, initial_capital: float, target_capital: float):
        self.initial_capital = initial_capital
        self.target_capital = target_capital
        self.remaining_capital = target_capital
        self.trades: List[Trade] = []
        self.total_profit = 0
        self.total_investment = 0
        self.start_time: Optional[datetime] = None
        self.end_time: Optional[datetime] = None
        self.last_trade_time: Optional[datetime] = None
        self.min_time_between_trades = timedelta(milliseconds=250)

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
        self.last_trade_time = timestamp

def load_nav_price() -> float:
    """Load NAV price from nav_prices.json"""
    nav_file = os.path.join(project_root, 'data', 'uso', 'nav_prices.json')
    with open(nav_file, 'r') as f:
        nav_data = json.load(f)
        return float(nav_data['January'][0]['price'])

def print_simulation_report(simulator: NAVArbitrageSimulator250ms) -> None:
    """Print a report of the simulation results in the same format as nav_report_generator.py"""
    print("\n=== NAV Arbitrage Trading Report (250ms Experiment) ===")
    print(f"Simulation period: {simulator.start_time} to {simulator.end_time if simulator.end_time else 'No trades executed'}")
    print(f"Data Quality: available")
    
    if simulator.end_time:
        print(f"Duration: {simulator.end_time - simulator.start_time}")
    else:
        print("Duration: No trades executed")
    
    print(f"\nTotal Investment: ${simulator.total_investment:,.2f}")
    print(f"Total Profit: ${simulator.total_profit:,.2f}")
    
    # Calculate ROI only if there was investment
    if simulator.total_investment > 0:
        roi = (simulator.total_profit / simulator.total_investment * 100)
        print(f"Overall ROI: {roi:.2f}%")
    else:
        print("Overall ROI: N/A - No trades executed")
    
    print(f"Number of trades: {len(simulator.trades)}")
    
    # Convert trades to DataFrame for summary
    if simulator.trades:
        trades_df = pd.DataFrame([trade.to_dict() for trade in simulator.trades])
        trades_df['timestamp'] = pd.to_datetime(trades_df['timestamp'])
        
        # Calculate cumulative metrics
        trades_df['cumulative_investment'] = trades_df['initial_investment'].cumsum()
        trades_df['cumulative_profit'] = trades_df['net_profit'].cumsum()
        trades_df['cumulative_roi'] = (trades_df['cumulative_profit'] / trades_df['cumulative_investment']) * 100

        print("\n=== Trade Summary ===")
        # Format the DataFrame columns
        pd.set_option('display.float_format', lambda x: '%.6f' % x)
        print(trades_df[[
            'timestamp', 'shares', 'nav_price', 'bid_price', 
            'initial_investment', 'gross_revenue', 'net_profit', 'roi_percent',
            'cumulative_investment', 'cumulative_profit', 'cumulative_roi'
        ]].to_string(index=False))

def run_simulation():
    # Set simulation date and get NAV price
    simulation_date = datetime(2024, 1, 3)
    nav_price = load_nav_price()
    
    # Get order book data
    client = db.Historical(os.getenv('DATABENTO_API_KEY'))
    data_path = os.path.join(
        project_root,
        'data', 'uso', 'order-book',
        f"arcx-pillar-{simulation_date.strftime('%Y%m%d')}-full.mbo.dbn.zst"
    )
    
    if not os.path.exists(data_path):
        print(f"Downloading data to {data_path}...")
        data = client.timeseries.get_range(
            dataset="ARCX.PILLAR",
            schema="mbo",
            symbols=["USO"],
            start=f"{simulation_date.strftime('%Y-%m-%d')}T00:00:00",
            end=f"{simulation_date.strftime('%Y-%m-%d')}T21:00:00",
            path=data_path,
        )
    else:
        print(f"Using existing data from {data_path}")
        data = db.DBNStore.from_file(data_path)

    # Initialize market and simulator
    market = Market()
    simulator = NAVArbitrageSimulator250ms(
        initial_capital=7_500_000,
        target_capital=7_500_000
    )

    # Parse symbology
    instrument_map = db.common.symbology.InstrumentMap()
    instrument_map.insert_metadata(data.metadata)

    # Define market open time (9:00 AM EST / 14:00 UTC)
    market_open = datetime(
        simulation_date.year,
        simulation_date.month,
        simulation_date.day,
        14, 0, 0,
        tzinfo=timezone.utc
    )
    
    print("\nProcessing order book and simulating NAV arbitrage (250ms experiment)...")
    print(f"Simulation date: {simulation_date.strftime('%Y-%m-%d')}")
    print(f"NAV Price: ${nav_price:.2f}")
    
    bid_count = 0
    total_messages = 0

    # Process the order book
    for mbo in data:
        total_messages += 1
        ts = mbo.pretty_ts_recv
        market.apply(mbo)

        # First check: Stop all processing if we're out of capital
        if simulator.remaining_capital <= 0:
            print("\nSimulation stopped: Target capital fully utilized")
            break

        # Only look at opportunities after market open
        if ts >= market_open:
            if mbo.flags & db.RecordFlags.F_LAST:
                best_bid, _ = market.aggregated_bbo(mbo.instrument_id)
                
                if best_bid:
                    bid_count += 1
                    bid_price = best_bid.price / FIXED_PRICE_SCALE
                    simulator.process_opportunity(ts, best_bid.size, nav_price, bid_price)

    print(f"\nProcessed {total_messages:,} total messages")
    print(f"Evaluated {bid_count:,} bids after market open")
    
    # Print simulation results
    print_simulation_report(simulator)

if __name__ == "__main__":
    run_simulation() 