"""
Core logic for NAV spot arbitrage simulations. This module:
- Loads and processes order book data
- Manages market state and simulation parameters
- Executes trading logic and opportunity detection
- Generates simulation results and reports
"""

from __future__ import annotations
import os
import sys
from datetime import datetime, timezone
from dotenv import load_dotenv
import databento as db
from databento_dbn import FIXED_PRICE_SCALE

# Add the project root to the Python path
project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)

from main.construct_order_book import Market
from analysis.arb.core.nav_arb_simulation import NAVArbitrageSimulator
from analysis.arb.periphery.utils import load_nav_data
from analysis.arb.periphery.nav_report_generator import SimulationResults, generate_report

def get_data_quality(client: db.Historical, dataset: str, date: datetime) -> str:
    """Check the data quality for a specific date."""
    conditions = client.metadata.get_dataset_condition(
        dataset=dataset,
        start_date=date.strftime('%Y-%m-%d')
    )
    
    # Find condition for our specific date
    for condition in conditions:
        if condition['date'] == date.strftime('%Y-%m-%d'):
            return condition['condition']
    return 'available'  # Default to available if no condition found

def run_nav_spot_simulation(simulation_date: datetime, nav_price: float, delay_ms: int = 1) -> SimulationResults:
    """
    Run NAV spot arbitrage simulation for a specific date and NAV price.
    
    Args:
        simulation_date (datetime): The date to run the simulation for
        nav_price (float): The NAV price to use for arbitrage calculations
        delay_ms (int): Minimum delay between trades in milliseconds (default: 1)
        
    Returns:
        SimulationResults: The results of the simulation
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
        target_capital=7_500_000,
        delay_ms=delay_ms  # Pass the delay parameter
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
    print(f"Trade delay: {delay_ms}ms")
    
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
    return simulation_results

def run_daily_simulation(simulation_date: datetime, nav_index: int, delay_ms: int = 1) -> None:
    """
    Run a daily NAV arbitrage simulation and add results to the tracker.
    This function encapsulates the common logic used by all daily simulation scripts.
    
    Args:
        simulation_date (datetime): The date to run the simulation for
        nav_index (int): The index in the NAV data array to use for the simulation
        delay_ms (int): Minimum delay between trades in milliseconds (default: 1)
    """
    # Load NAV data and get price for the specified index
    nav_data = load_nav_data()
    nav_price = float(nav_data['January'][nav_index]['price'])
    
    # Run simulation with the specified date and NAV price
    results = run_nav_spot_simulation(simulation_date, nav_price, delay_ms=delay_ms)  # Pass the delay parameter
    
    # Add results to the total tracker
    from analysis.arb.periphery.nav_spot_total import get_tracker
    tracker = get_tracker(delay_ms=delay_ms)
    if tracker.add_simulation_results(simulation_date, results.total_profit, len(results.trades)):
        print("\nResults added to total tracker successfully.")
    else:
        print("\nResults already exist in total tracker for this date.")