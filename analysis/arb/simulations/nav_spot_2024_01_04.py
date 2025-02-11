from __future__ import annotations
import os
import sys
from datetime import datetime

# Add the project root to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

from analysis.arb.utils import load_nav_data
from analysis.arb.nav_report_generator import generate_report
from analysis.arb.nav_spot_logic import NAVSpotSimulation
from analysis.arb.nav_spot_total import SimulationTracker

def run_simulation():
    # Set simulation date
    simulation_date = datetime(2024, 1, 4)
    
    # Load NAV data and get January[1] price
    nav_data = load_nav_data()
    nav_price = float(nav_data['January'][1]['price'])
    
    # Run simulation
    simulator = NAVSpotSimulation(simulation_date, nav_price)
    results = simulator.run_simulation()
    
    # Generate report
    generate_report(results)
    
    # Track results
    tracker = SimulationTracker()
    date_str = simulation_date.strftime('%Y-%m-%d')
    roi = (results.total_profit / results.total_investment * 100)
    tracker.add_simulation_result(date_str, results.total_profit, roi, len(results.trades))
    tracker.print_summary()

if __name__ == "__main__":
    run_simulation() 