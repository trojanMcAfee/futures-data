import json
from datetime import datetime
import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os

def load_data(file_path):
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct absolute path to the data file
    abs_file_path = os.path.join(script_dir, '..', '..', 'data', 'output.json')
    with open(abs_file_path, 'r') as f:
        return json.load(f)

def analyze_continuous_futures(data):
    # Convert to DataFrame
    df = pd.DataFrame(data)
    
    # Convert timestamp to datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['month'] = df['timestamp'].dt.strftime('%B')
    df['date'] = df['timestamp'].dt.strftime('%Y-%m-%d')
    
    # Create pivot table for volumes and prices
    pivot_df = df.pivot(index='date', columns='symbol', 
                       values=['volume', 'close'])
    
    # Flatten column names
    pivot_df.columns = [f"{col[0]}_{col[1]}" for col in pivot_df.columns]
    
    # Sort by date
    pivot_df = pivot_df.sort_index()
    pivot_df.index = pd.to_datetime(pivot_df.index)
    
    # Group by month
    monthly_groups = pivot_df.groupby(pivot_df.index.strftime('%Y-%m'))
    
    # Track continuous price and rolls
    daily_data = []
    current_contract = 'front'  # Start with front month
    
    for month, month_data in monthly_groups:
        # Reset contract to front at the start of each month
        current_contract = 'front'
        roll_happened = False
        
        for date, row in month_data.iterrows():
            # Skip if we don't have both volume values
            if pd.isna(row['volume_CL.n.0']) or pd.isna(row['volume_CL.n.1']):
                continue
                
            # Check for roll condition
            roll_event = False
            if not roll_happened and current_contract == 'front':
                # Check if next month volume is higher
                if row['volume_CL.n.1'] > row['volume_CL.n.0']:
                    roll_event = True
                    roll_happened = True
                    current_contract = 'next'
            
            # Get price from the current contract
            price = row['close_CL.n.0'] if current_contract == 'front' else row['close_CL.n.1']
            
            # Store the data
            daily_data.append([
                date,  # Keep as datetime for plotting
                price,  # Keep as float for plotting
                f"${row['volume_CL.n.0']:,.0f}",
                f"${row['volume_CL.n.1']:,.0f}",
                roll_event
            ])
    
    return daily_data

def plot_continuous_futures(daily_data):
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    plot_path = os.path.join(script_dir, 'continuous_futures_plot.png')
    
    # Check if plot already exists
    if os.path.exists(plot_path):
        print("\nPlot already exists at:", plot_path)
        return
    
    # Convert data for plotting
    dates = [row[0] for row in daily_data]
    prices = [row[1] for row in daily_data]
    roll_dates = [row[0] for row in daily_data if row[4]]
    roll_prices = [row[1] for row in daily_data if row[4]]
    
    # Calculate daily changes for plotting
    daily_changes = []
    for i in range(len(prices)):
        if i == 0:
            daily_changes.append(0)  # First day has no change
        else:
            pct_change = ((prices[i] - prices[i-1]) / prices[i-1]) * 100
            daily_changes.append(pct_change)
    
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
    
    # Save the plot in the futures directory
    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
    print("\nPlot has been saved at:", plot_path)
    plt.close()

def format_for_table(daily_data):
    # Convert data for table display
    formatted_data = []
    
    for i, (date, price, vol1, vol2, roll) in enumerate(daily_data):
        # Calculate daily percentage change
        if i > 0:
            prev_price = daily_data[i-1][1]  # Get previous day's price
            pct_change = ((price - prev_price) / prev_price) * 100
            pct_change_str = f"{pct_change:+.2f}%"  # + sign for positive changes
        else:
            pct_change_str = "N/A"  # First day has no previous price
            
        formatted_data.append([
            date.strftime('%Y-%m-%d'),
            f"${price:.2f}",
            vol1,
            vol2,
            "ROLL" if roll else "",
            pct_change_str
        ])
    
    return formatted_data

def main():
    data = load_data('output.json')
    daily_data = analyze_continuous_futures(data)
    
    # Create the plot
    plot_continuous_futures(daily_data)
    
    # Format data for table display
    table_data = format_for_table(daily_data)
    
    # Print table
    headers = ["Date", "Price", "Front Vol", "Next Vol", "Event", "Daily Change"]
    print("\nContinuous Futures Price Evolution (2024)")
    print("========================================")
    print(tabulate(table_data, headers=headers, tablefmt="simple"))
    
    # Print summary
    roll_days = [row for row in table_data if row[4] == "ROLL"]
    print(f"\nTotal number of rolls: {len(roll_days)}")
    print("\nRoll dates:")
    for roll in roll_days:
        print(f"  {roll[0]}: {roll[1]} (Front Vol: {roll[2]}, Next Vol: {roll[3]})")

if __name__ == "__main__":
    main() 