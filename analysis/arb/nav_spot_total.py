"""
Tracks and accumulates results from multiple NAV arbitrage simulations. This module:
- Maintains a persistent record of simulation results in nav_spot_total.json
- Prevents duplicate processing of the same trading day
- Calculates aggregate statistics like total profits and average profit per trade
- Provides a summary report of all processed simulations

The results are stored persistently and can be accessed across different sessions,
making it easy to track the performance of the NAV arbitrage strategy over time.
"""

from __future__ import annotations
import os
import json
from datetime import datetime
from pathlib import Path

class NAVSpotTotal:
    def __init__(self):
        self.total_profits = 0.0
        self.total_trades = 0
        self.total_investment = 0.0  # Added to track total investment
        self.processed_dates = set()
        self.data_file = os.path.join(os.path.dirname(__file__), 'nav_spot_total.json')
        self.load_data()
    
    def load_data(self):
        """Load existing data from JSON file if it exists"""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                self.total_profits = data['total_profits']
                self.total_trades = data['total_trades']
                self.total_investment = data.get('total_investment', 0.0)  # Added with backward compatibility
                self.processed_dates = set(data['processed_dates'])
    
    def save_data(self):
        """Save current data to JSON file"""
        data = {
            'total_profits': self.total_profits,
            'total_trades': self.total_trades,
            'total_investment': self.total_investment,  # Added to save total investment
            'processed_dates': list(self.processed_dates)
        }
        with open(self.data_file, 'w') as f:
            json.dump(data, f)
    
    def add_simulation_results(self, date: datetime, profits: float, trades: int, investment: float = 7_500_000) -> bool:
        """
        Add simulation results if not already processed.
        Returns True if results were added, False if already processed.
        Args:
            date (datetime): The simulation date
            profits (float): Total profits from the simulation
            trades (int): Number of trades executed
            investment (float): Total investment used in simulation (defaults to 7.5M)
        """
        date_str = date.strftime('%Y-%m-%d')
        if date_str in self.processed_dates:
            return False
        
        self.total_profits += profits
        self.total_trades += trades
        self.total_investment += investment  # Track total investment across all simulations
        self.processed_dates.add(date_str)
        self.save_data()
        return True
    
    def print_summary(self):
        """Print summary of all accumulated results"""
        print("\n=== NAV Spot Total Results ===")
        print(f"Total Profits: ${self.total_profits:,.2f}")
        print(f"Total Investment: ${self.total_investment:,.2f}")
        print(f"Total Number of Trades: {self.total_trades:,}")
        print(f"Number of Days Processed: {len(self.processed_dates)}")
        
        if self.total_trades > 0:
            avg_profit_per_trade = self.total_profits / self.total_trades
            print(f"Average Profit per Trade: ${avg_profit_per_trade:,.2f}")
        
        if self.total_investment > 0:
            cumulative_roi = (self.total_profits / self.total_investment) * 100
            print(f"Cumulative ROI: {cumulative_roi:.2f}%")
            daily_avg_roi = cumulative_roi / len(self.processed_dates) if self.processed_dates else 0
            print(f"Average Daily ROI: {daily_avg_roi:.2f}%")

def get_tracker() -> NAVSpotTotal:
    """Get or create the NAV spot total tracker"""
    return NAVSpotTotal()

if __name__ == "__main__":
    tracker = get_tracker()
    tracker.print_summary() 