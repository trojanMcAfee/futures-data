from __future__ import annotations
import os
import sys
from datetime import datetime, timezone
from dotenv import load_dotenv
import databento as db
from databento_dbn import FIXED_PRICE_SCALE

# Add the main directory to the Python path so we can import construct_order_book
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'main'))
from construct_order_book import Market

def analyze_order_book_jan_3():
    # Load environment variables
    load_dotenv()
    
    # Create a historical client with API key from environment
    client = db.Historical(os.getenv('DATABENTO_API_KEY'))

    # Request MBO data for USO during regular market hours, starting from midnight for synthetic snapshot
    data_path = "data/uso/order-book/arcx-pillar-20240103-full.mbo.dbn.zst"
    
    # Only download if the file doesn't exist
    if not os.path.exists(data_path):
        print(f"Downloading data to {data_path}...")
        data = client.timeseries.get_range(
            dataset="ARCX.PILLAR",
            schema="mbo",
            symbols=["USO"],
            start="2024-01-03T00:00:00",    # Start from midnight UTC to get synthetic snapshot
            end="2024-01-03T21:00:00",      # 4:00 PM EST
            path=data_path,
        )
    else:
        print(f"Using existing data from {data_path}")
        data = db.DBNStore.from_file(data_path)

    # Parse the symbology
    instrument_map = db.common.symbology.InstrumentMap()
    instrument_map.insert_metadata(data.metadata)

    # Create a market instance and process the data
    market = Market()
    snapshots = []  # Store snapshots after market open
    message_count = 0  # Debug counter
    last_print_time = None  # Track time between snapshots
    # Define market open time (9:00 AM EST / 14:00 UTC)
    market_open_time = datetime(2024, 1, 3, 14, 0, 0, tzinfo=timezone.utc)

    print("\nProcessing data and building order book...")
    print("(Including synthetic snapshot from midnight UTC for complete book state)")

    for mbo in data:
        ts = mbo.pretty_ts_recv
        message_count += 1
        market.apply(mbo)

        # Only start collecting snapshots after market open
        if ts >= market_open_time:
            # Store snapshots in the first few seconds after market open
            # Only store if at least 1 second has passed since last snapshot
            if (mbo.flags & db.RecordFlags.F_LAST and 
                len(snapshots) < 20 and  # Increased to 20 snapshots
                (last_print_time is None or (ts - last_print_time).total_seconds() >= 1.0)):  # Changed to 1 second
                
                symbol = instrument_map.resolve(mbo.instrument_id, ts.date()) or "USO"
                best_bid, best_offer = market.aggregated_bbo(mbo.instrument_id)
                snapshots.append((ts, symbol, best_bid, best_offer))
                last_print_time = ts

    print(f"\nProcessed {message_count} messages")
    print(f"Found {len(snapshots)} snapshots at market open")

    # Print the snapshots
    if snapshots:
        print("\nOrder Book State At Market Open:")
        print(f"Market opened at: 2024-01-03 14:00:00 UTC (9:00 AM EST)")
        print("(Order book initialized with midnight UTC synthetic snapshot)")
        print("-" * 60)
        
        for ts, symbol, best_bid, best_offer in snapshots:
            print(f"\n{symbol} Aggregated BBO | {ts}")
            print(f"    Best Offer: {best_offer}")
            print(f"    Best Bid: {best_bid}")
            print(f"    Time since market open: {(ts - market_open_time).total_seconds():.1f} seconds")  # Changed to 1 decimal place
            if best_bid and best_offer:
                spread = (best_offer.price - best_bid.price) / FIXED_PRICE_SCALE
                spread_pct = (spread / (best_offer.price / FIXED_PRICE_SCALE)) * 100
                print(f"    Spread: ${spread:.2f} ({spread_pct:.3f}%)")
    else:
        print("\nNo snapshots found at market open. Available time range:")
        print(f"First message: {data[0].pretty_ts_recv}")
        print(f"Last message: {data[-1].pretty_ts_recv}")

if __name__ == "__main__":
    # Change to the workspace root directory
    os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
    analyze_order_book_jan_3() 