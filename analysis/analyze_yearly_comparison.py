#!/usr/bin/env python3

# Cross-analyzes a traditional roll strategy and an alternative roll strategy (which consists 
# of rolling subset of contracts daily on backwardeed markets) for a year.

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main.roll_analysis_logic import analyze_month_rolls

def main():
    # Position parameters
    CONTRACTS = 100
    BARRELS_PER_CONTRACT = 1000
    
    # Dictionary of all months
    months = {
        1: "January",
        2: "February",
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
    
    # Initialize tracking variables
    monthly_comparison = []
    
    print("\nMonthly Position Valuation Comparison - 2024")
    print("=========================================")
    print("\nMonth      Traditional Strategy    Alternative Strategy")
    print("          Position Value         Position Value")
    print("-" * 55)
    
    # Track the latest position values
    traditional_latest_value = None
    alternative_latest_value = None
    
    # Analyze each month
    for month_num, month_name in months.items():
        results = analyze_month_rolls(month_name, month_num, verbose=False)
        
        # Get traditional strategy details
        if results['traditional_roll']:
            trad_value = CONTRACTS * BARRELS_PER_CONTRACT * results['traditional_roll']['buy_price']
            traditional_latest_value = trad_value
        else:
            trad_value = traditional_latest_value if traditional_latest_value else 0
        
        # Get alternative strategy details
        if month_num == 1:  # Special handling for January
            alt_value = trad_value  # In January, both strategies have same value
            alternative_latest_value = alt_value
            print(f"{month_name:<10} ${trad_value:>15,.2f}    ${alt_value:>15,.2f}")
            print("          (Month in backwardation - no alternative strategy applied)\n")
        else:
            alt_value = results['alternative_strategy']['final_position_value'] if results['alternative_strategy'] else alternative_latest_value
            if results['alternative_strategy']:
                alternative_latest_value = alt_value
            print(f"{month_name:<10} ${trad_value:>15,.2f}    ${alt_value:>15,.2f}\n")
        
        monthly_comparison.append({
            'month': month_name,
            'traditional_value': trad_value,
            'alternative_value': alt_value
        })
    
    # Calculate final statistics
    initial_value = monthly_comparison[0]['traditional_value']  # January's value (same for both strategies)
    traditional_change = traditional_latest_value - initial_value
    alternative_change = alternative_latest_value - initial_value
    
    print("\nYearly Summary")
    print("==============")
    print(f"Initial Position Value (January): ${initial_value:,.2f}")
    print("\nTraditional Strategy:")
    print(f"Final Position Value: ${traditional_latest_value:,.2f}")
    print(f"Total Change: ${traditional_change:,.2f} ({(traditional_change/initial_value * 100):.2f}%)")
    
    print("\nAlternative Strategy:")
    print(f"Final Position Value: ${alternative_latest_value:,.2f}")
    print(f"Total Change: ${alternative_change:,.2f} ({(alternative_change/initial_value * 100):.2f}%)")
    
    print("\nComparison:")
    value_difference = alternative_latest_value - traditional_latest_value
    print(f"Final Value Difference: ${value_difference:,.2f}")
    print(f"Strategy Difference: {(value_difference/traditional_latest_value * 100):.2f}%")
    
    # Additional statistics
    best_month = max(monthly_comparison[1:], key=lambda x: x['alternative_value'] - x['traditional_value'])
    worst_month = min(monthly_comparison[1:], key=lambda x: x['alternative_value'] - x['traditional_value'])
    
    print("\nNotable Months")
    print("==============")
    print(f"Best Value Difference: {best_month['month']}")
    print(f"  Traditional: ${best_month['traditional_value']:,.2f}")
    print(f"  Alternative: ${best_month['alternative_value']:,.2f}")
    print(f"  Difference: ${best_month['alternative_value'] - best_month['traditional_value']:,.2f}")
    
    print(f"\nWorst Value Difference: {worst_month['month']}")
    print(f"  Traditional: ${worst_month['traditional_value']:,.2f}")
    print(f"  Alternative: ${worst_month['alternative_value']:,.2f}")
    print(f"  Difference: ${worst_month['alternative_value'] - worst_month['traditional_value']:,.2f}")

if __name__ == "__main__":
    main() 