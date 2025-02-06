#!/usr/bin/env python3

# Cross-analyzes a traditional roll strategy and an alternative roll strategy (which consists 
# of rolling subset of contracts daily on backwardeed markets) for a year.

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main.roll_analysis_logic import analyze_month_rolls
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

def plot_strategy_comparison(monthly_comparison):
    # Create comparison-charts directory if it doesn't exist
    charts_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'comparison-charts')
    os.makedirs(charts_dir, exist_ok=True)
    
    strategy_chart_path = os.path.join(charts_dir, 'strategy_comparison.png')
    performance_chart_path = os.path.join(charts_dir, 'relative_performance.png')
    
    # Check if both charts already exist
    if os.path.exists(strategy_chart_path) and os.path.exists(performance_chart_path):
        print("\nCharts already exist in 'comparison-charts' directory.")
        return

    # Create the charts only if they don't exist
    dates = [datetime.strptime(f"2024-{month}-01", "%Y-%m-%d") for month in range(1, 13)]
    traditional_values = [data['traditional']['position_value'] for data in monthly_comparison]
    alternative_values = [data['alternative']['position_value'] for data in monthly_comparison]
    traditional_contracts = [data['traditional']['contracts'] for data in monthly_comparison]
    alternative_contracts = [data['alternative']['contracts'] for data in monthly_comparison]

    # First figure: Position Values and Contract Counts
    plt.figure(figsize=(15, 10))
    
    # Position Values subplot
    plt.subplot(2, 1, 1)
    plt.plot(dates, traditional_values, 'b-', label='Traditional Strategy')
    plt.plot(dates, alternative_values, 'r-', label='Alternative Strategy')
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b'))
    plt.title('Strategy Comparison - 2024')
    plt.ylabel('Position Value ($)')
    plt.legend()
    plt.grid(True)
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))
    
    # Contract Counts subplot
    plt.subplot(2, 1, 2)
    plt.plot(dates, traditional_contracts, 'b-', label='Traditional Strategy')
    plt.plot(dates, alternative_contracts, 'r-', label='Alternative Strategy')
    plt.axhline(y=100, color='g', linestyle='--', label='Initial Contracts')
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b'))
    plt.title('Number of Contracts Over Time')
    plt.ylabel('Number of Contracts')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.savefig(strategy_chart_path)
    plt.close()
    
    # Second figure: Relative Performance
    plt.figure(figsize=(12, 6))
    initial_value = traditional_values[0]
    traditional_relative = [(v - initial_value) / initial_value * 100 for v in traditional_values]
    alternative_relative = [(v - initial_value) / initial_value * 100 for v in alternative_values]
    
    plt.plot(dates, traditional_relative, 'b-', label='Traditional Strategy')
    plt.plot(dates, alternative_relative, 'r-', label='Alternative Strategy')
    plt.axhline(y=0, color='g', linestyle='--', label='Initial Value')
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b'))
    plt.title('Relative Performance - 2024')
    plt.ylabel('Percentage Change from Initial Value (%)')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.savefig(performance_chart_path)
    plt.close()
    
    print(f"\nCharts have been saved in the 'comparison-charts' directory")

def main():
    # Position parameters
    INITIAL_CONTRACTS = 100
    BARRELS_PER_CONTRACT = 1000
    
    # Dictionary of all months
    global months
    months = ['January', 'February', 'March', 'April', 'May', 'June', 
             'July', 'August', 'September', 'October', 'November', 'December']
    
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
    for month_num, month_name in enumerate(months, 1):
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
    
    # Generate visualization charts
    plot_strategy_comparison(monthly_comparison)

if __name__ == "__main__":
    main() 