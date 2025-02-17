"""
Tracks and accumulates results from multiple NAV arbitrage simulations. This module:
- Maintains a persistent record of simulation results in nav_spot_total.json
- Prevents duplicate processing of the same trading day
- Calculates aggregate statistics like total profits and average profit per trade
- Provides monthly and total summaries of all processed simulations

The results are stored persistently and can be accessed across different sessions,
making it easy to track the performance of the NAV arbitrage strategy over time.
"""

from __future__ import annotations
import os
import json
from datetime import datetime
from pathlib import Path
import pandas as pd
from typing import Dict, List, Optional
from collections import defaultdict

class NAVSpotTotal:
    DAILY_INVESTMENT = 7_500_000  # Constant investment amount that gets recycled each day
    DATA_FILE = os.path.join(os.path.dirname(__file__), 'nav_spot_total.json')
    
    def __init__(self, delay_ms: int = 250):
        self.delay_ms = delay_ms
        self.total_profits = 0.0
        self.total_trades = 0
        self.processed_dates = set()
        self.degraded_data_days: Dict[str, dict] = {}  # Store details of degraded data days
        self.zero_profit_days: Dict[str, dict] = {}  # Store details of zero profit days
        self.monthly_data: Dict[str, List[dict]] = defaultdict(list)  # Store daily results by month
        self.load_data()
    
    def load_data(self):
        """Load existing data from JSON file if it exists"""
        if os.path.exists(self.DATA_FILE):
            with open(self.DATA_FILE, 'r') as f:
                all_data = json.load(f)
                delay_key = str(self.delay_ms)
                if delay_key in all_data:
                    data = all_data[delay_key]
                    self.total_profits = data['total_profits']
                    self.total_trades = data['total_trades']
                    self.processed_dates = set(data['processed_dates'])
                    self.degraded_data_days = data.get('degraded_data_days', {})
                    self.zero_profit_days = data.get('zero_profit_days', {})
                    self.monthly_data = defaultdict(list, data.get('monthly_data', {}))
    
    def save_data(self):
        """Save current data to JSON file"""
        # Load existing data first to preserve other delays' data
        all_data = {}
        if os.path.exists(self.DATA_FILE):
            with open(self.DATA_FILE, 'r') as f:
                all_data = json.load(f)
        
        # Update data for current delay
        all_data[str(self.delay_ms)] = {
            'total_profits': self.total_profits,
            'total_trades': self.total_trades,
            'processed_dates': list(self.processed_dates),
            'degraded_data_days': self.degraded_data_days,
            'zero_profit_days': self.zero_profit_days,
            'monthly_data': dict(self.monthly_data)
        }
        
        # Save all data back
        with open(self.DATA_FILE, 'w') as f:
            json.dump(all_data, f)
    
    def add_simulation_results(self, date: datetime, profits: float, trades: int, data_quality: str = 'available') -> bool:
        """
        Add simulation results if not already processed for this specific delay.
        Returns True if results were added, False if already processed.
        Args:
            date (datetime): The simulation date
            profits (float): Total profits from the simulation
            trades (int): Number of trades executed
            data_quality (str): Quality of the data used in simulation
        """
        date_str = date.strftime('%Y-%m-%d')
        month_key = date.strftime('%Y-%m')
        
        # Check if this date is already processed for this specific delay
        if date_str in self.processed_dates:
            print(f"\nDate {date_str} already processed for {self.delay_ms}ms delay")
            return False
        
        self.total_profits += profits
        self.total_trades += trades
        self.processed_dates.add(date_str)
        
        # Calculate daily ROI
        daily_roi = (profits / self.DAILY_INVESTMENT) * 100
        
        # Store daily results in monthly data
        daily_result = {
            'date': date_str,
            'profits': profits,
            'trades': trades,
            'roi': daily_roi,
            'data_quality': data_quality
        }
        self.monthly_data[month_key].append(daily_result)
        
        # Track degraded data days
        if data_quality != 'available':
            self.degraded_data_days[date_str] = daily_result
        
        # Track zero profit days
        if profits == 0:
            self.zero_profit_days[date_str] = daily_result
        
        self.save_data()
        return True
    
    def get_monthly_summary(self, month_key: str) -> Optional[pd.DataFrame]:
        """Generate a summary DataFrame for a specific month"""
        if month_key not in self.monthly_data:
            return None
            
        df = pd.DataFrame(self.monthly_data[month_key])
        df = df.sort_values('date')
        df['profits'] = df['profits'].map('${:,.2f}'.format)
        df['roi'] = df['roi'].map('{:.2f}%'.format)
        return df
    
    def print_summary(self):
        """Print summary of all accumulated results"""
        print(f"\n=== NAV Spot Total Results ({self.delay_ms}ms delay) ===")
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
        
        # Print monthly summaries
        print("\n=== Monthly Summaries ===")
        for month_key in sorted(self.monthly_data.keys()):
            month_name = datetime.strptime(month_key, '%Y-%m').strftime('%B %Y')
            print(f"\n{month_name} Results:")
            df = self.get_monthly_summary(month_key)
            if df is not None:
                print(df.to_string(index=False))
                
                # Calculate monthly totals
                monthly_profits = sum(float(p.strip('$').replace(',', '')) for p in df['profits'])
                monthly_trades = df['trades'].sum()
                print(f"\nMonthly Totals:")
                print(f"Total Profits: ${monthly_profits:,.2f}")
                print(f"Total Trades: {monthly_trades:,}")
                monthly_roi = (monthly_profits / self.DAILY_INVESTMENT) * 100
                print(f"Monthly ROI: {monthly_roi:.2f}%")
        
        # Print zero profit days
        if self.zero_profit_days:
            print(f"\n=== Days with Zero Profits ({self.delay_ms}ms delay) ===")
            df = pd.DataFrame(self.zero_profit_days.values())
            df = df.sort_values('date')
            df['profits'] = df['profits'].map('${:,.2f}'.format)
            df['roi'] = df['roi'].map('{:.2f}%'.format)
            print(df.to_string(index=False))
        
        # Print degraded data days
        if self.degraded_data_days:
            print(f"\n=== Days with Data Quality Issues ({self.delay_ms}ms delay) ===")
            df = pd.DataFrame(self.degraded_data_days.values())
            df = df.sort_values('date')
            df['profits'] = df['profits'].map('${:,.2f}'.format)
            df['roi'] = df['roi'].map('{:.2f}%'.format)
            print(df.to_string(index=False))
            
            # Calculate impact of degraded data days
            degraded_profits = sum(float(day['profits'].strip('$').replace(',', '')) for day in self.degraded_data_days.values())
            degraded_trades = sum(day['trades'] for day in self.degraded_data_days.values())
            print(f"\nImpact of Degraded Data Days:")
            print(f"Total Profits from Degraded Days: ${degraded_profits:,.2f}")
            print(f"Total Trades on Degraded Days: {degraded_trades:,}")
            if self.total_profits != 0:
                print(f"Percentage of Total Profits: {(degraded_profits/self.total_profits)*100:.2f}%")

def get_tracker(delay_ms: int = 250) -> NAVSpotTotal:
    """Get or create the NAV spot total tracker"""
    return NAVSpotTotal(delay_ms=delay_ms)

def print_all_summaries():
    """Print summaries for all delay values"""
    # Print 250ms delay results first
    tracker_250ms = get_tracker(delay_ms=250)
    tracker_250ms.print_summary()
    print("\n")  # Add extra spacing between summaries
    
    # Print 12s delay results
    tracker_12s = get_tracker(delay_ms=12000)
    tracker_12s.print_summary()

if __name__ == "__main__":
    print_all_summaries() 