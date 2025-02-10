from __future__ import annotations
import os
import sys
import json
from datetime import datetime, timezone
from dataclasses import dataclass
from typing import List, Optional
import pandas as pd
from dotenv import load_dotenv
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

@dataclass
class SkippedOpportunity:
    timestamp: datetime
    shares: int
    nav_price: float
    bid_price: float
    price_difference: float

class NAVArbitrageSimulator:
    def __init__(self, initial_capital: float, target_capital: float):
        self.initial_capital = initial_capital
        self.target_capital = target_capital
        self.remaining_capital = target_capital
        self.trades: List[Trade] = []
        self.skipped_opportunities: List[SkippedOpportunity] = []
        self.total_profit = 0
        self.total_investment = 0
        self.start_time: Optional[datetime] = None
        self.end_time: Optional[datetime] = None

    def process_opportunity(self, timestamp: datetime, shares: int, nav_price: float, bid_price: float) -> None:
        if not self.start_time:
            self.start_time = timestamp

        # Skip if bid price is lower than NAV
        if bid_price <= nav_price:
            price_diff = nav_price - bid_price
            self.skipped_opportunities.append(
                SkippedOpportunity(timestamp, shares, nav_price, bid_price, price_diff)
            )
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

    def generate_report(self) -> None:
        print("\n=== NAV Arbitrage Trading Report ===")
        print(f"Simulation period: {self.start_time} to {self.end_time}")
        print(f"Duration: {self.end_time - self.start_time}")
        print(f"\nTotal Investment: ${self.total_investment:,.2f}")
        print(f"Total Profit: ${self.total_profit:,.2f}")
        print(f"Overall ROI: {(self.total_profit / self.total_investment * 100):.2f}%")
        print(f"Number of trades: {len(self.trades)}")
        
        # Convert trades to DataFrame
        if self.trades:
            trades_df = pd.DataFrame([vars(t) for t in self.trades])
            trades_df['timestamp'] = pd.to_datetime(trades_df['timestamp'])
            
            # Calculate cumulative metrics
            trades_df['cumulative_investment'] = trades_df['initial_investment'].cumsum()
            trades_df['cumulative_profit'] = trades_df['net_profit'].cumsum()
            trades_df['cumulative_roi'] = (trades_df['cumulative_profit'] / trades_df['cumulative_investment']) * 100

            print("\n=== Trade Summary ===")
            print(trades_df.to_string(index=False))

        # Always print skipped opportunities section
        print("\n=== Skipped Opportunities ===")
        print(f"Number of skipped opportunities: {len(self.skipped_opportunities)}")
        
        if self.skipped_opportunities:
            skipped_df = pd.DataFrame([vars(s) for s in self.skipped_opportunities])
            skipped_df['timestamp'] = pd.to_datetime(skipped_df['timestamp'])
            print("\nSkipped Trades Detail:")
            print(skipped_df.to_string(index=False))
        else:
            print("No opportunities were skipped (all bids were above NAV price)")

def run_simulation():
    # Change to the workspace root directory
    os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
    
    # Load environment variables
    load_dotenv()

    # Load NAV price from JSON
    with open('data/uso/nav_prices.json', 'r') as f:
        nav_data = json.load(f)
        nav_price = float(nav_data['January'][0]['price'])  # First January price

    # Create historical client and load order book data
    client = db.Historical(os.getenv('DATABENTO_API_KEY'))
    data_path = "data/uso/order-book/arcx-pillar-20240103-full.mbo.dbn.zst"
    
    if not os.path.exists(data_path):
        print(f"Downloading data to {data_path}...")
        data = client.timeseries.get_range(
            dataset="ARCX.PILLAR",
            schema="mbo",
            symbols=["USO"],
            start="2024-01-03T00:00:00",
            end="2024-01-03T21:00:00",
            path=data_path,
        )
    else:
        print(f"Using existing data from {data_path}")
        data = db.DBNStore.from_file(data_path)

    # Initialize market and simulator
    market = Market()
    simulator = NAVArbitrageSimulator(
        initial_capital=7_500_000,
        target_capital=7_500_000
    )

    # Parse symbology
    instrument_map = db.common.symbology.InstrumentMap()
    instrument_map.insert_metadata(data.metadata)

    # Define market open time (9:00 AM EST / 14:00 UTC)
    market_open_time = datetime(2024, 1, 3, 14, 0, 0, tzinfo=timezone.utc)
    
    print("\nProcessing order book and simulating NAV arbitrage...")
    print(f"NAV Price: ${nav_price:.2f}")
    
    bid_count = 0
    total_messages = 0

    # Process the order book
    for mbo in data:
        total_messages += 1
        ts = mbo.pretty_ts_recv
        market.apply(mbo)

        # Only look at opportunities after market open
        if ts >= market_open_time:
            if mbo.flags & db.RecordFlags.F_LAST:
                best_bid, _ = market.aggregated_bbo(mbo.instrument_id)
                
                if best_bid:
                    bid_count += 1
                    bid_price = best_bid.price / FIXED_PRICE_SCALE
                    simulator.process_opportunity(ts, best_bid.size, nav_price, bid_price)

        # Stop if we've used all our capital
        if simulator.remaining_capital <= 0:
            break

    print(f"\nProcessed {total_messages:,} total messages")
    print(f"Evaluated {bid_count:,} bids after market open")
    
    # Generate and print the report
    simulator.generate_report()

if __name__ == "__main__":
    run_simulation() 