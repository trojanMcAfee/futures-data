#!/usr/bin/env python3

# Cross-analyzes a traditional roll strategy and an alternative roll strategy (which consists 
# of rolling subset of contracts daily on backwardeed markets) for a year.
# *** THIS GOES ***

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main.roll_analysis_logic import analyze_month_rolls

def main():
    # Position parameters
    INITIAL_CONTRACTS = 100
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
    print("\nMonth      Traditional Strategy              Alternative Strategy")
    print("          Position Value    Contracts      Position Value    Contracts")
    print("-" * 75)
    
    # Track the latest values
    traditional_latest_value = None
    alternative_latest_value = None
    traditional_contracts = INITIAL_CONTRACTS
    alternative_contracts = INITIAL_CONTRACTS
    
    # Analyze each month
    for month_num, month_name in months.items():
        results = analyze_month_rolls(month_name, month_num, verbose=False)
        
        # Get traditional strategy details
        if results['traditional_roll']:
            # Calculate how many contracts we can buy with the money from selling
            sell_value = traditional_contracts * BARRELS_PER_CONTRACT * results['traditional_roll']['sell_price']
            traditional_contracts = sell_value / (BARRELS_PER_CONTRACT * results['traditional_roll']['buy_price'])
            trad_value = traditional_contracts * BARRELS_PER_CONTRACT * results['traditional_roll']['buy_price']
            traditional_latest_value = trad_value
        else:
            trad_value = traditional_latest_value if traditional_latest_value else 0
        
        # Get alternative strategy details
        if month_num == 1:  # Special handling for January
            alt_value = trad_value  # In January, both strategies have same value
            alternative_latest_value = alt_value
            print(f"{month_name:<10} ${trad_value:>15,.2f}  {traditional_contracts:>8.4f}    ${alt_value:>15,.2f}  {alternative_contracts:>8.4f}")
            print("          (Month in backwardation - no alternative strategy applied)\n")
        else:
            if results['alternative_strategy']:
                # Calculate contracts for alternative strategy
                sell_value = alternative_contracts * BARRELS_PER_CONTRACT * results['alternative_strategy']['initial_price']
                alternative_contracts = sell_value / (BARRELS_PER_CONTRACT * results['alternative_strategy']['final_price'])
                alt_value = alternative_contracts * BARRELS_PER_CONTRACT * results['alternative_strategy']['final_price']
                alternative_latest_value = alt_value
            else:
                alt_value = alternative_latest_value
            
            print(f"{month_name:<10} ${trad_value:>15,.2f}  {traditional_contracts:>8.4f}    ${alt_value:>15,.2f}  {alternative_contracts:>8.4f}\n")
        
        monthly_comparison.append({
            'month': month_name,
            'traditional_value': trad_value,
            'traditional_contracts': traditional_contracts,
            'alternative_value': alt_value,
            'alternative_contracts': alternative_contracts
        })
    
    # Calculate final statistics
    initial_value = monthly_comparison[0]['traditional_value']  # January's value (same for both strategies)
    traditional_change = traditional_latest_value - initial_value
    alternative_change = alternative_latest_value - initial_value
    
    print("\nYearly Summary")
    print("==============")
    print(f"Initial Position Value (January): ${initial_value:,.2f}")
    print(f"Initial Contracts: {INITIAL_CONTRACTS:.4f}")
    
    print("\nTraditional Strategy:")
    print(f"Final Position Value: ${traditional_latest_value:,.2f}")
    print(f"Final Contracts: {traditional_contracts:.4f}")
    print(f"Contract Change: {traditional_contracts - INITIAL_CONTRACTS:.4f}")
    print(f"Total Value Change: ${traditional_change:,.2f} ({(traditional_change/initial_value * 100):.2f}%)")
    
    print("\nAlternative Strategy:")
    print(f"Final Position Value: ${alternative_latest_value:,.2f}")
    print(f"Final Contracts: {alternative_contracts:.4f}")
    print(f"Contract Change: {alternative_contracts - INITIAL_CONTRACTS:.4f}")
    print(f"Total Value Change: ${alternative_change:,.2f} ({(alternative_change/initial_value * 100):.2f}%)")
    
    print("\nComparison:")
    value_difference = alternative_latest_value - traditional_latest_value
    contract_difference = alternative_contracts - traditional_contracts
    print(f"Final Value Difference: ${value_difference:,.2f}")
    print(f"Final Contract Difference: {contract_difference:.4f}")
    print(f"Strategy Value Difference: {(value_difference/traditional_latest_value * 100):.2f}%")
    print(f"Strategy Contract Difference: {(contract_difference/traditional_contracts * 100):.2f}%")
    
    # Additional statistics
    best_month = max(monthly_comparison[1:], key=lambda x: x['alternative_value'] - x['traditional_value'])
    worst_month = min(monthly_comparison[1:], key=lambda x: x['alternative_value'] - x['traditional_value'])
    
    print("\nNotable Months")
    print("==============")
    print(f"Best Value Difference: {best_month['month']}")
    print(f"  Traditional: ${best_month['traditional_value']:,.2f} ({best_month['traditional_contracts']:.4f} contracts)")
    print(f"  Alternative: ${best_month['alternative_value']:,.2f} ({best_month['alternative_contracts']:.4f} contracts)")
    print(f"  Difference: ${best_month['alternative_value'] - best_month['traditional_value']:,.2f}")
    print(f"  Contract Difference: {best_month['alternative_contracts'] - best_month['traditional_contracts']:.4f}")
    
    print(f"\nWorst Value Difference: {worst_month['month']}")
    print(f"  Traditional: ${worst_month['traditional_value']:,.2f} ({worst_month['traditional_contracts']:.4f} contracts)")
    print(f"  Alternative: ${worst_month['alternative_value']:,.2f} ({worst_month['alternative_contracts']:.4f} contracts)")
    print(f"  Difference: ${worst_month['alternative_value'] - worst_month['traditional_value']:,.2f}")
    print(f"  Contract Difference: {worst_month['alternative_contracts'] - worst_month['traditional_contracts']:.4f}")

if __name__ == "__main__":
    main() 