import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import sys
from pathlib import Path

# Add main directory to Python path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from main.spot_analysis_logic import get_spot_data

def plot_spot_prices(daily_data):
    # Convert data for plotting
    dates = [row[0] for row in daily_data]
    prices = [row[1] for row in daily_data]
    
    # Calculate daily changes for plotting
    daily_changes = []
    for i in range(len(prices)):
        if i == 0:
            daily_changes.append(0)  # First day has no change
        else:
            pct_change = ((prices[i] - prices[i-1]) / prices[i-1]) * 100 if prices[i-1] != 0 else 0
            daily_changes.append(pct_change)
    
    # Create figure with two subplots sharing x-axis
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 12), height_ratios=[2, 1], sharex=True)
    
    # Top subplot - Price evolution
    ax1.plot(dates, prices, label='WTI Spot Price', color='blue', linewidth=1)
    
    # Customize top subplot
    ax1.set_title('WTI Crude Oil Spot Price (2024)', fontsize=14, pad=20)
    ax1.set_ylabel('Price ($)', fontsize=12)
    ax1.grid(True, linestyle='--', alpha=0.7)
    ax1.legend(loc='upper left')
    
    # Bottom subplot - Daily changes
    bars = ax2.bar(dates, daily_changes, width=1, alpha=0.7)
    
    # Color the bars based on positive/negative values
    for bar, change in zip(bars, daily_changes):
        if change >= 0:
            bar.set_color('green')
        else:
            bar.set_color('red')
    
    # Customize bottom subplot
    ax2.set_xlabel('Date', fontsize=12)
    ax2.set_ylabel('Daily Change (%)', fontsize=12)
    ax2.grid(True, linestyle='--', alpha=0.7)
    ax2.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
    
    # Format x-axis for both subplots
    ax2.xaxis.set_major_locator(mdates.MonthLocator())
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    plt.xticks(rotation=45)
    
    # Adjust layout
    plt.tight_layout()
    
    # Save the plot
    plt.savefig('spot_prices_plot.png', dpi=300, bbox_inches='tight')
    plt.close()

def format_for_table(daily_data):
    return [[
        date.strftime('%Y-%m-%d'),
        f"${price:.2f}",
        change
    ] for date, price, change in daily_data]

def main():
    # Get spot data using the new module
    df_spot = get_spot_data()
    
    if df_spot is None:
        return
    
    # Format data for display
    daily_data = []
    for _, row in df_spot.iterrows():
        daily_data.append([
            row['date'],
            row['price'],
            f"{row['daily_change']:+.2f}%" if pd.notna(row['daily_change']) else "N/A"
        ])
    
    # Create the plot
    plot_spot_prices(daily_data)
    
    # Format data for table display
    table_data = format_for_table(daily_data)
    
    # Print table
    headers = ["Date", "Price", "Daily Change"]
    print("\nWTI Crude Oil Spot Price Evolution (2024)")
    print("=========================================")
    print(tabulate(table_data, headers=headers, tablefmt="simple"))
    
    print("\nPlot has been saved as 'spot_prices_plot.png'")

if __name__ == "__main__":
    main() 