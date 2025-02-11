from __future__ import annotations
import os
import sys
from datetime import datetime
from dotenv import load_dotenv

# Add the project root to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

from analysis.arb.utils import load_nav_data
from nav_spot_logic import run_nav_spot_simulation

def run_simulation():
    # Load environment variables
    load_dotenv()

    # Set simulation date
    simulation_date = datetime(2024, 1, 4)
    
    # Load NAV data and get January[1] price
    nav_data = load_nav_data()
    nav_price = float(nav_data['January'][1]['price'])
    
    # Run simulation with the specified date and NAV price
    run_nav_spot_simulation(simulation_date, nav_price)

if __name__ == "__main__":
    run_simulation() 