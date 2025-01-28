import json
from datetime import datetime
import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pathlib import Path
import numpy as np

def load_data(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def get_spot_data():
    # Load and process spot data
    spot_data_path = Path("../../data/spot_data.json")
    if not spot_data_path.exists():
        print("Error: spot_data.json not found. Please run fetch_eia_data.py first.")
        return None
    
    data = load_data(spot_data_path)
    spot_data = []
    
    for item in data['response']['data']:
        if (item.get('product-name') == 'WTI Crude Oil' and 
            item.get('process-name') == 'Spot Price FOB'):
            spot_data.append({
                'date': pd.to_datetime(item['period']),
                'price': float(item['value'])
            })
    
    df_spot = pd.DataFrame(spot_data)
    if not df_spot.empty:
        df_spot = df_spot.sort_values('date')
        df_spot['daily_change'] = df_spot['price'].pct_change() * 100
    
    return df_spot

def get_futures_data():
    # Load and process futures data
    futures_data_path = Path("../../data/output.json")
    if not futures_data_path.exists():
        print("Error: output.json not found.")
        return None
    
    data = load_data(futures_data_path)
    
    # Convert to DataFrame
    df = pd.DataFrame(data)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['date'] = df['timestamp'].dt.strftime('%Y-%m-%d')
    
    # Create pivot table for volumes and prices
    pivot_df = df.pivot(index='date', columns='symbol', 
                       values=['volume', 'close'])
    
    # Flatten column names
    pivot_df.columns = [f"{col[0]}_{col[1]}" for col in pivot_df.columns]
    
    # Sort by date
    pivot_df = pivot_df.sort_index()
    pivot_df.index = pd.to_datetime(pivot_df.index)
    
    # Track continuous price
    futures_data = []
    current_contract = 'front'  # Start with front month
    
    for date, row in pivot_df.iterrows():
        if pd.isna(row['volume_CL.n.0']) or pd.isna(row['volume_CL.n.1']):
            continue
        
        # Check for roll condition
        if current_contract == 'front' and row['volume_CL.n.1'] > row['volume_CL.n.0']:
            current_contract = 'next'
        
        # Get price from the current contract
        price = row['close_CL.n.0'] if current_contract == 'front' else row['close_CL.n.1']
        
        futures_data.append({
            'date': date,
            'price': price
        })
    
    df_futures = pd.DataFrame(futures_data)
    if not df_futures.empty:
        df_futures['daily_change'] = df_futures['price'].pct_change() * 100
    
    return df_futures

def plot_comparison(df_spot, df_futures):
    # Create figure with two subplots sharing x-axis
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 12), height_ratios=[2, 1], sharex=True)
    
    # Top subplot - Price evolution
    ax1.plot(df_spot['date'], df_spot['price'], 
            label='WTI Spot Price', color='#1f77b4', linewidth=1.5)
    ax1.plot(df_futures['date'], df_futures['price'], 
            label='Futures Price', color='#ff7f0e', linewidth=1.5)
    
    # Customize top subplot
    ax1.set_title('WTI Crude Oil Spot vs Futures Prices (2024)', fontsize=14, pad=20)
    ax1.set_ylabel('Price ($)', fontsize=12)
    ax1.grid(True, linestyle='--', alpha=0.7)
    ax1.legend(loc='upper left')
    
    # Bottom subplot - Daily changes
    # Calculate bar width to avoid overlap
    width = 0.35
    
    # Create bars for spot prices (left position)
    spot_bars = ax2.bar(df_spot['date'] - pd.Timedelta(days=width), 
                       df_spot['daily_change'], 
                       width=width, alpha=0.7, label='Spot Daily Change')
    
    # Create bars for futures prices (right position)
    futures_bars = ax2.bar(df_futures['date'] + pd.Timedelta(days=width), 
                          df_futures['daily_change'], 
                          width=width, alpha=0.7, label='Futures Daily Change')
    
    # Color the bars based on positive/negative values
    for bars, color_pos, color_neg in [(spot_bars, '#2ecc71', '#e74c3c'), 
                                      (futures_bars, '#3498db', '#9b59b6')]:
        for bar in bars:
            if bar.get_height() >= 0:
                bar.set_color(color_pos)
            else:
                bar.set_color(color_neg)
    
    # Customize bottom subplot
    ax2.set_xlabel('Date', fontsize=12)
    ax2.set_ylabel('Daily Change (%)', fontsize=12)
    ax2.grid(True, linestyle='--', alpha=0.7)
    ax2.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
    ax2.legend(loc='upper left')
    
    # Format x-axis for both subplots
    ax2.xaxis.set_major_locator(mdates.MonthLocator())
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    plt.xticks(rotation=45)
    
    # Adjust layout
    plt.tight_layout()
    
    # Save the plot
    plt.savefig('spot_futures_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()

def main():
    # Get spot data
    df_spot = get_spot_data()
    if df_spot is None:
        return
    
    # Get futures data
    df_futures = get_futures_data()
    if df_futures is None:
        return
    
    # Create the comparison plot
    plot_comparison(df_spot, df_futures)
    print("\nComparison plot has been saved as 'spot_futures_comparison.png'")
    
    # Calculate and display some statistics
    print("\nSummary Statistics:")
    print("==================")
    print("\nSpot Prices:")
    print(f"Average: ${df_spot['price'].mean():.2f}")
    print(f"Min: ${df_spot['price'].min():.2f}")
    print(f"Max: ${df_spot['price'].max():.2f}")
    print(f"Volatility (std): {df_spot['daily_change'].std():.2f}%")
    
    print("\nFutures Prices:")
    print(f"Average: ${df_futures['price'].mean():.2f}")
    print(f"Min: ${df_futures['price'].min():.2f}")
    print(f"Max: ${df_futures['price'].max():.2f}")
    print(f"Volatility (std): {df_futures['daily_change'].std():.2f}%")

if __name__ == "__main__":
    main() 