#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main.roll_analysis_logic import analyze_month_rolls

def main():
    # Dictionary of months to analyze (excluding January and February)
    months = {
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    
    # Run analysis for each month
    for month_num, month_name in months.items():
        print(f"\n{'='*80}")
        print(f"Analyzing {month_name} 2024")
        print(f"{'='*80}")
        analyze_month_rolls(month_name, month_num)

if __name__ == "__main__":
    main() 