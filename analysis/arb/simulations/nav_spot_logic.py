from __future__ import annotations
import os
import sys
from datetime import datetime, timezone
from dotenv import load_dotenv
import databento as db
from databento_dbn import FIXED_PRICE_SCALE

# Add the project root to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from main.construct_order_book import Market
from analysis.arb.nav_arb_simulation import NAVArbitrageSimulator
from analysis.arb.utils import load_nav_data
from analysis.arb.nav_report_generator import SimulationResults, generate_report

def run_nav_spot_simulation(simulation_date: datetime, nav_price: float) -> None:
    """
    Run NAV spot arbitrage simulation for a specific date and NAV price.
    
    Args:
        simulation_date (datetime): The date to run the simulation for
        nav_price (float): The NAV price to use for arbitrage calculations
    """
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
    simulator = NAVArbitrageSimulator(
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
    
    print("\nProcessing order book and simulating NAV arbitrage...")
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
    
    # Get simulation results and generate report
    results = simulator.get_results()
    simulation_results = SimulationResults(
        start_time=results['start_time'],
        end_time=results['end_time'],
        total_investment=results['total_investment'],
        total_profit=results['total_profit'],
        trades=results['trades']
    )
    generate_report(simulation_results) 