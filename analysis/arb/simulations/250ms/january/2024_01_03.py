from __future__ import annotations
import os
import sys
from datetime import datetime
from dotenv import load_dotenv

# Add the project root to the Python path
project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', '..')
sys.path.append(project_root)

# Load environment variables from the root directory
dotenv_path = os.path.join(project_root, '.env')
load_dotenv(dotenv_path)

from analysis.arb.nav_spot_logic import run_daily_simulation
from analysis.arb.nav_spot_total import get_tracker

def run_simulation():
    # Set simulation date and NAV index
    simulation_date = datetime(2024, 1, 3)
    nav_index = 0  # Use January[0] price (NAV price from January 2nd)
    delay_ms = 250
    
    # Run simulation using shared logic with 250ms delay
    run_daily_simulation(simulation_date, nav_index, delay_ms=delay_ms)
    
    # Print summary after simulation
    tracker = get_tracker(delay_ms=delay_ms)
    tracker.print_summary()

if __name__ == "__main__":
    run_simulation() 