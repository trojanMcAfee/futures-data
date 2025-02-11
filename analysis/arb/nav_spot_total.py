from __future__ import annotations
import os
import json
from typing import Dict, Any

class SimulationTracker:
    def __init__(self):
        self.data_file = os.path.join(os.path.dirname(__file__), 'simulation_results.json')
        self.results = self._load_results()
        self.processed_dates = set(self.results.keys())

    def _load_results(self) -> Dict[str, Any]:
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                return json.load(f)
        return {}

    def _save_results(self):
        with open(self.data_file, 'w') as f:
            json.dump(self.results, f, indent=2)

    def add_simulation_result(self, date: str, profit: float, roi: float, num_trades: int):
        if date in self.processed_dates:
            print(f"Warning: Date {date} has already been processed. Skipping...")
            return

        self.results[date] = {
            'profit': profit,
            'roi': roi,
            'num_trades': num_trades
        }
        self.processed_dates.add(date)
        self._save_results()

    def get_cumulative_results(self):
        total_profit = sum(result['profit'] for result in self.results.values())
        total_trades = sum(result['num_trades'] for result in self.results.values())
        
        # Calculate weighted average ROI based on number of trades
        if total_trades > 0:
            weighted_roi = sum(
                result['roi'] * result['num_trades'] 
                for result in self.results.values()
            ) / total_trades
        else:
            weighted_roi = 0.0

        return {
            'total_profit': total_profit,
            'avg_roi': weighted_roi,
            'total_trades': total_trades
        }

    def print_summary(self):
        cumulative = self.get_cumulative_results()
        
        print("\n=== Cumulative NAV Arbitrage Results ===")
        print(f"Total Dates Processed: {len(self.processed_dates)}")
        print(f"Total Profit: ${cumulative['total_profit']:,.2f}")
        print(f"Average ROI: {cumulative['avg_roi']:.2f}%")
        print(f"Total Trades: {cumulative['total_trades']:,}")
        
        print("\nProcessed Dates:")
        for date, result in sorted(self.results.items()):
            print(f"  {date}: ${result['profit']:,.2f} profit, {result['roi']:.2f}% ROI, {result['num_trades']:,} trades") 