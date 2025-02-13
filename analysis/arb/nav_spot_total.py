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
import pandas as pd
from typing import Dict, List

class NAVSpotTotal:
    DAILY_INVESTMENT = 7_500_000  # Constant investment amount that gets recycled each day
    
    def __init__(self):
        self.total_profits = 0.0
        self.total_trades = 0
        self.processed_dates = set()
        self.degraded_data_days: Dict[str, dict] = {}  # Store details of degraded data days
        self.data_file = os.path.join(os.path.dirname(__file__), 'nav_spot_total.json')
        self.load_data()
    
    def load_data(self):
        """Load existing data from JSON file if it exists"""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                self.total_profits = data['total_profits']
                self.total_trades = data['total_trades']
                self.processed_dates = set(data['processed_dates'])
                self.degraded_data_days = data.get('degraded_data_days', {})
    
    def save_data(self):
        """Save current data to JSON file"""
        data = {
            'total_profits': self.total_profits,
            'total_trades': self.total_trades,
            'processed_dates': list(self.processed_dates),
            'degraded_data_days': self.degraded_data_days
        }
        with open(self.data_file, 'w') as f:
            json.dump(data, f)
    
    def add_simulation_results(self, date: datetime, profits: float, trades: int, data_quality: str = 'available') -> bool:
        """
        Add simulation results if not already processed.
        Returns True if results were added, False if already processed.
        Args:
            date (datetime): The simulation date
            profits (float): Total profits from the simulation
            trades (int): Number of trades executed
            data_quality (str): Quality of the data used in simulation
        """
        date_str = date.strftime('%Y-%m-%d')
        if date_str in self.processed_dates:
            return False
        
        self.total_profits += profits
        self.total_trades += trades
        self.processed_dates.add(date_str)
        
        # Track degraded data days
        if data_quality != 'available':
            self.degraded_data_days[date_str] = {
                'date': date_str,
                'profits': profits,
                'trades': trades,
                'data_quality': data_quality
            }
        
        self.save_data()
        return True
    
    def print_summary(self):
        """Print summary of all accumulated results"""
        print("\n=== NAV Spot Total Results ===")
        print(f"Total Profits: ${self.total_profits:,.2f}")
        print(f"Base Investment (recycled daily): ${self.DAILY_INVESTMENT:,.2f}")
        print(f"Total Number of Trades: {self.total_trades:,}")
        print(f"Number of Days Processed: {len(self.processed_dates)}")
        
        if self.total_trades > 0:
            avg_profit_per_trade = self.total_profits / self.total_trades
            print(f"Average Profit per Trade: ${avg_profit_per_trade:,.2f}")
        
        # Calculate ROI based on the constant investment amount
        cumulative_roi = (self.total_profits / self.DAILY_INVESTMENT) * 100
        print(f"Cumulative ROI: {cumulative_roi:.2f}%")
        daily_avg_roi = cumulative_roi / len(self.processed_dates) if self.processed_dates else 0
        print(f"Average Daily ROI: {daily_avg_roi:.2f}%")
        
        # Print degraded data days summary if any exist
        if self.degraded_data_days:
            print("\n=== Days with Data Quality Issues ===")
            df = pd.DataFrame(self.degraded_data_days.values())
            df = df.sort_values('date')
            df.columns = ['Date', 'Profits ($)', 'Trades', 'Data Quality']
            df['Profits ($)'] = df['Profits ($)'].map('${:,.2f}'.format)
            print(df.to_string(index=False))
            
            # Calculate impact of degraded data days
            degraded_profits = sum(float(day['profits']) for day in self.degraded_data_days.values())
            degraded_trades = sum(day['trades'] for day in self.degraded_data_days.values())
            print(f"\nImpact of Degraded Data Days:")
            print(f"Total Profits from Degraded Days: ${degraded_profits:,.2f}")
            print(f"Total Trades on Degraded Days: {degraded_trades:,}")
            if self.total_profits != 0:
                print(f"Percentage of Total Profits: {(degraded_profits/self.total_profits)*100:.2f}%")

def get_tracker() -> NAVSpotTotal:
    """Get or create the NAV spot total tracker"""
    return NAVSpotTotal()

if __name__ == "__main__":
    tracker = get_tracker()
    tracker.print_summary() 