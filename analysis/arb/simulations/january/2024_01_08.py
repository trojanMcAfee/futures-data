from __future__ import annotations
import os
import sys
from datetime import datetime
from dotenv import load_dotenv

# Add the project root to the Python path
project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..')
sys.path.append(project_root)

# Load environment variables from the root directory
dotenv_path = os.path.join(project_root, '.env')
load_dotenv(dotenv_path)

from analysis.arb.nav_spot_logic import run_daily_simulation

def run_simulation():
    # Set simulation date and NAV index
    simulation_date = datetime(2024, 1, 8)
    nav_index = 3  # Use January[3] price (NAV price from January 5th)
    
    # Run simulation using shared logic
    run_daily_simulation(simulation_date, nav_index)

if __name__ == "__main__":
    run_simulation() 