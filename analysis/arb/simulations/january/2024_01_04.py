from __future__ import annotations
import os
import sys
from datetime import datetime
from dotenv import load_dotenv

# Add the project root to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))

from analysis.arb.utils import load_nav_data
from analysis.arb.nav_spot_logic import run_nav_spot_simulation
from analysis.arb.nav_spot_total import get_tracker

def run_simulation():
    # Load environment variables
    load_dotenv()

    # Set simulation date
    simulation_date = datetime(2024, 1, 4)
    
    # Load NAV data and get January[1] price
    nav_data = load_nav_data()
    nav_price = float(nav_data['January'][1]['price'])
    
    # Run simulation with the specified date and NAV price
    results = run_nav_spot_simulation(simulation_date, nav_price)
    
    # Add results to the total tracker
    tracker = get_tracker()
    if tracker.add_simulation_results(simulation_date, results.total_profit, len(results.trades)):
        print("\nResults added to total tracker successfully.")
    else:
        print("\nResults already exist in total tracker for this date.")

if __name__ == "__main__":
    run_simulation() 