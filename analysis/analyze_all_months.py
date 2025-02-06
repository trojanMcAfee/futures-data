#!/usr/bin/env python3

'''
This script is used to analyze the roll events for all months in 2024, in a monthly manner.
You can run this script by passing in the month you want to analyze as an argument.
'''

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main.roll_analysis_logic import analyze_month_rolls

def main():
    # Dictionary of months to analyze
    months = {
        "january": 1,
        "february": 2,
        "march": 3,
        "april": 4,
        "may": 5,
        "june": 6,
        "july": 7,
        "august": 8,
        "september": 9,
        "october": 10,
        "november": 11,
        "december": 12
    }
    
    if len(sys.argv) != 2:
        print("Usage: python analyze_all_months.py <month>")
        print("Example: python analyze_all_months.py june")
        sys.exit(1)
    
    # Get month from command line argument and convert to lowercase
    requested_month = sys.argv[1].lower()
    
    if requested_month not in months:
        print(f"Error: Invalid month '{sys.argv[1]}'")
        print(f"Valid months are: {', '.join(month.capitalize() for month in months.keys())}")
        sys.exit(1)
    
    # Get the month number and capitalize the month name
    month_num = months[requested_month]
    month_name = requested_month.capitalize()
    
    print(f"\n{'='*80}")
    print(f"Analyzing {month_name} 2024")
    print(f"{'='*80}")
    analyze_month_rolls(month_name, month_num)

if __name__ == "__main__":
    main() 