import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import sys
from pathlib import Path

# Add main directory to Python path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from main.futures_analysis_logic import get_futures_data

def plot_continuous_futures(df_futures):
    # Get plot path relative to the script location
    script_dir = Path(__file__).resolve().parent
    plot_path = script_dir / 'continuous_futures_plot.png'
    
    # Check if plot already exists
    if plot_path.exists():
        print("\nPlot already exists at:", plot_path)
        return
    
    # Get data for plotting
    dates = df_futures['date']
    prices = df_futures['price']
    roll_dates = df_futures[df_futures['roll_event']]['date']
    roll_prices = df_futures[df_futures['roll_event']]['price']
    daily_changes = df_futures['daily_change']
    
    # Create figure with two subplots sharing x-axis
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 12), height_ratios=[2, 1], sharex=True)
    
    # Top subplot - Price and roll events
    ax1.plot(dates, prices, label='Continuous Future Price', color='blue', linewidth=1)
    ax1.scatter(roll_dates, roll_prices, color='red', marker='o', 
               label='Roll Events', zorder=5, s=100)
    
    # Customize top subplot
    ax1.set_title('Crude Oil Continuous Futures Price (2024)', fontsize=14, pad=20)
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
    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
    print("\nPlot has been saved at:", plot_path)
    plt.close()

def format_for_table(df_futures):
    table_data = []
    for _, row in df_futures.iterrows():
        table_data.append([
            row['date'].strftime('%Y-%m-%d'),
            f"${row['price']:.2f}",
            f"${row['volume_front']:,.0f}",
            f"${row['volume_next']:,.0f}",
            "ROLL" if row['roll_event'] else "",
            f"{row['daily_change']:+.2f}%" if pd.notna(row['daily_change']) else "N/A"
        ])
    return table_data

def main():
    # Get futures data using the new module
    df_futures = get_futures_data()
    
    if df_futures is None:
        return
    
    # Create the plot
    plot_continuous_futures(df_futures)
    
    # Format data for table display
    table_data = format_for_table(df_futures)
    
    # Print table
    headers = ["Date", "Price", "Front Vol", "Next Vol", "Event", "Daily Change"]
    print("\nContinuous Futures Price Evolution (2024)")
    print("========================================")
    print(tabulate(table_data, headers=headers, tablefmt="simple"))
    
    # Print summary
    roll_events = df_futures[df_futures['roll_event']]
    print(f"\nTotal number of rolls: {len(roll_events)}")
    print("\nRoll dates:")
    for _, row in roll_events.iterrows():
        print(f"  {row['date'].strftime('%Y-%m-%d')}: ${row['price']:.2f} "
              f"(Front Vol: ${row['volume_front']:,.0f}, Next Vol: ${row['volume_next']:,.0f})")

if __name__ == "__main__":
    main() 