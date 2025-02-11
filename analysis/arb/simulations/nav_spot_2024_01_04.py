from __future__ import annotations
import os
import sys
from datetime import datetime, timezone
from dotenv import load_dotenv
import databento as db
from databento_dbn import FIXED_PRICE_SCALE
import pandas as pd

# Add the project root to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from main.construct_order_book import Market
from analysis.arb.nav_arb_simulation import NAVArbitrageSimulator
from analysis.arb.utils import load_nav_data

class ModifiedNAVArbitrageSimulator(NAVArbitrageSimulator):
    def generate_report(self) -> None:
        print("\n=== NAV Arbitrage Trading Report ===")
        print(f"Simulation period: {self.start_time} to {self.end_time}")
        print(f"Duration: {self.end_time - self.start_time}")
        print(f"\nTotal Investment: ${self.total_investment:,.2f}")
        print(f"Total Profit: ${self.total_profit:,.2f}")
        print(f"Overall ROI: {(self.total_profit / self.total_investment * 100):.2f}%")
        print(f"Number of trades: {len(self.trades)}")
        
        # Convert trades to DataFrame for summary
        if self.trades:
            trades_df = pd.DataFrame([vars(t) for t in self.trades])
            trades_df['timestamp'] = pd.to_datetime(trades_df['timestamp'])
            
            # Calculate cumulative metrics
            trades_df['cumulative_investment'] = trades_df['initial_investment'].cumsum()
            trades_df['cumulative_profit'] = trades_df['net_profit'].cumsum()
            trades_df['cumulative_roi'] = (trades_df['cumulative_profit'] / trades_df['cumulative_investment']) * 100

            print("\n=== Trade Summary ===")
            print(trades_df.to_string(index=False))

        # Show skipped opportunities summary
        print("\n=== Skipped Opportunities ===")
        print(f"Number of skipped opportunities: {len(self.skipped_opportunities)}")
        
        if self.skipped_opportunities:
            print("\nFirst skipped trade:")
            first = self.skipped_opportunities[0]
            print(f"Timestamp: {first.timestamp}")
            print(f"Shares: {first.shares}")
            print(f"NAV Price: ${first.nav_price:.2f}")
            print(f"Bid Price: ${first.bid_price:.2f}")
            print(f"Price Difference: ${first.price_difference:.2f}")
            
            print("\nLast skipped trade:")
            last = self.skipped_opportunities[-1]
            print(f"Timestamp: {last.timestamp}")
            print(f"Shares: {last.shares}")
            print(f"NAV Price: ${last.nav_price:.2f}")
            print(f"Bid Price: ${last.bid_price:.2f}")
            print(f"Price Difference: ${last.price_difference:.2f}")

def run_simulation():
    # Load environment variables
    load_dotenv()

    # Set simulation date
    simulation_date = datetime(2024, 1, 4)
    
    # Load NAV data and get January[1] price (original behavior)
    nav_data = load_nav_data()
    nav_price = float(nav_data['January'][1]['price'])
    
    # Get order book data
    client = db.Historical(os.getenv('DATABENTO_API_KEY'))
    data_path = os.path.join(
        os.path.dirname(__file__), 
        '..', '..', '..', 
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
    simulator = ModifiedNAVArbitrageSimulator(
        initial_capital=7_500_000,
        target_capital=7_500_000
    )

    # Parse symbology
    instrument_map = db.common.symbology.InstrumentMap()
    instrument_map.insert_metadata(data.metadata)

    # Define market open time (9:00 AM EST / 14:00 UTC) - original behavior
    market_open = datetime(2024, 1, 4, 14, 0, 0, tzinfo=timezone.utc)
    
    print("\nProcessing order book and simulating NAV arbitrage...")
    print(f"Simulation date: {simulation_date.strftime('%Y-%m-%d')}")
    print(f"NAV Price: ${nav_price:.2f}")
    
    bid_count = 0
    total_messages = 0
    out_of_capital = False

    # Process the order book
    for mbo in data:
        total_messages += 1
        ts = mbo.pretty_ts_recv
        market.apply(mbo)

        # First check: Stop all processing if we're out of capital
        if simulator.remaining_capital <= 0:
            out_of_capital = True
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
    
    # Generate and print the report
    simulator.generate_report()

if __name__ == "__main__":
    run_simulation() 