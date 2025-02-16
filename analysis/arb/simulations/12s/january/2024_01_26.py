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

def run_simulation():
    # Set simulation date and NAV index
    simulation_date = datetime(2024, 1, 26)
    nav_index = 16  # Use January[16] price (NAV price from January 25th)
    delay_ms = 12000  # 12 seconds delay
    
    # Run simulation using shared logic with 12s delay
    run_daily_simulation(simulation_date, nav_index, delay_ms=delay_ms)

if __name__ == "__main__":
    run_simulation() 