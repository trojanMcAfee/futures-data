import json
from datetime import datetime
import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pathlib import Path

def load_data(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def filter_wti_data(data):
    # Filter for WTI Crude Oil and Spot Price FOB
    wti_data = []
    for item in data['response']['data']:
        if (item.get('product-name') == 'WTI Crude Oil' and 
            item.get('process-name') == 'Spot Price FOB'):
            wti_data.append({
                'date': item['period'],
                'price': item['value']
            })
    
    return wti_data

def analyze_spot_prices(wti_data):
    # Convert to DataFrame
    df = pd.DataFrame(wti_data)
    
    # Convert date string to datetime and price to float
    df['date'] = pd.to_datetime(df['date'])
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    
    # Sort by date
    df = df.sort_values('date')
    
    # Calculate daily percentage changes
    df['daily_change'] = df['price'].pct_change() * 100
    
    # Format the data for display
    daily_data = []
    for _, row in df.iterrows():
        daily_data.append([
            row['date'],
            row['price'],
            f"{row['daily_change']:+.2f}%" if pd.notna(row['daily_change']) else "N/A"
        ])
    
    return daily_data

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
            pct_change = ((prices[i] - prices[i-1]) / prices[i-1]) * 100
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
    # Load the spot data
    data_path = Path("../../data/spot_data.json")
    if not data_path.exists():
        print("Error: spot_data.json not found. Please run fetch_eia_data.py first.")
        return
    
    data = load_data(data_path)
    
    # Filter WTI data
    wti_data = filter_wti_data(data)
    
    if not wti_data:
        print("No WTI spot price data found in the specified date range.")
        return
    
    # Analyze the data
    daily_data = analyze_spot_prices(wti_data)
    
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