import json
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pathlib import Path
import numpy as np

def load_data(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def get_spot_data():
    spot_data_path = Path("../../data/spot_data.json")
    if not spot_data_path.exists():
        print("Error: spot_data.json not found.")
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
    futures_data_path = Path("../../data/output.json")
    if not futures_data_path.exists():
        print("Error: output.json not found.")
        return None
    
    data = load_data(futures_data_path)
    df = pd.DataFrame(data)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['date'] = df['timestamp'].dt.strftime('%Y-%m-%d')
    
    pivot_df = df.pivot(index='date', columns='symbol', 
                       values=['volume', 'close'])
    pivot_df.columns = [f"{col[0]}_{col[1]}" for col in pivot_df.columns]
    pivot_df = pivot_df.sort_index()
    pivot_df.index = pd.to_datetime(pivot_df.index)
    
    futures_data = []
    current_contract = 'front'
    
    for date, row in pivot_df.iterrows():
        if pd.isna(row['volume_CL.n.0']) or pd.isna(row['volume_CL.n.1']):
            continue
        
        if current_contract == 'front' and row['volume_CL.n.1'] > row['volume_CL.n.0']:
            current_contract = 'next'
        
        price = row['close_CL.n.0'] if current_contract == 'front' else row['close_CL.n.1']
        futures_data.append({
            'date': date,
            'price': price
        })
    
    df_futures = pd.DataFrame(futures_data)
    if not df_futures.empty:
        df_futures['daily_change'] = df_futures['price'].pct_change() * 100
    
    return df_futures

def analyze_deltas(df_spot, df_futures):
    # Merge spot and futures data on date
    df_merged = pd.merge(
        df_spot[['date', 'daily_change']].rename(columns={'daily_change': 'spot_change'}),
        df_futures[['date', 'daily_change']].rename(columns={'daily_change': 'futures_change'}),
        on='date', how='inner'
    )
    
    # Calculate the delta between futures and spot changes
    df_merged['delta'] = df_merged['futures_change'] - df_merged['spot_change']
    
    return df_merged

def plot_deltas(df_merged):
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 12), height_ratios=[2, 1])
    
    # Top subplot: Delta evolution over time with zero line
    ax1.plot(df_merged['date'], df_merged['delta'], 
             color='blue', linewidth=1.5, label='Daily Delta')
    ax1.axhline(y=0, color='red', linestyle='--', alpha=0.7)
    
    # Add bands for standard deviation
    std_dev = df_merged['delta'].std()
    mean = df_merged['delta'].mean()
    ax1.axhline(y=mean + std_dev, color='gray', linestyle=':', alpha=0.5, 
                label='±1 Std Dev')
    ax1.axhline(y=mean - std_dev, color='gray', linestyle=':', alpha=0.5)
    ax1.fill_between(df_merged['date'], 
                     mean - std_dev, mean + std_dev, 
                     color='gray', alpha=0.1)
    
    ax1.set_title('Delta Between Futures and Spot Daily Changes (2024)', 
                  fontsize=14, pad=20)
    ax1.set_ylabel('Delta (%)', fontsize=12)
    ax1.grid(True, linestyle='--', alpha=0.7)
    ax1.legend(loc='upper left')
    
    # Bottom subplot: Histogram of deltas
    n, bins, patches = ax2.hist(df_merged['delta'], bins=30, 
                               color='blue', alpha=0.7)
    
    # Add vertical lines for mean and std dev
    ax2.axvline(x=mean, color='red', linestyle='--', 
                label=f'Mean: {mean:.2f}%')
    ax2.axvline(x=mean + std_dev, color='gray', linestyle=':', 
                label=f'Std Dev: ±{std_dev:.2f}%')
    ax2.axvline(x=mean - std_dev, color='gray', linestyle=':', alpha=0.7)
    
    ax2.set_xlabel('Delta (%)', fontsize=12)
    ax2.set_ylabel('Frequency', fontsize=12)
    ax2.grid(True, linestyle='--', alpha=0.7)
    ax2.legend(loc='upper left')
    
    # Format x-axis for top subplot
    ax1.xaxis.set_major_locator(mdates.MonthLocator())
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    plt.setp(ax1.get_xticklabels(), rotation=45)
    
    plt.tight_layout()
    plt.savefig('daily_deltas_analysis.png', dpi=300, bbox_inches='tight')
    plt.close()

def main():
    # Get spot and futures data
    df_spot = get_spot_data()
    df_futures = get_futures_data()
    
    if df_spot is None or df_futures is None:
        return
    
    # Analyze deltas
    df_merged = analyze_deltas(df_spot, df_futures)
    
    # Create visualization
    plot_deltas(df_merged)
    
    # Print summary statistics
    print("\nDelta Analysis Summary:")
    print("=====================")
    print(f"Mean Delta: {df_merged['delta'].mean():.2f}%")
    print(f"Median Delta: {df_merged['delta'].median():.2f}%")
    print(f"Standard Deviation: {df_merged['delta'].std():.2f}%")
    print(f"Max Delta: {df_merged['delta'].max():.2f}%")
    print(f"Min Delta: {df_merged['delta'].min():.2f}%")
    
    # Print the dates with largest absolute deltas
    print("\nDates with Largest Absolute Deltas:")
    df_merged['abs_delta'] = df_merged['delta'].abs()
    top_deltas = df_merged.nlargest(5, 'abs_delta')
    for _, row in top_deltas.iterrows():
        print(f"\nDate: {row['date'].strftime('%Y-%m-%d')}")
        print(f"Spot Change: {row['spot_change']:.2f}%")
        print(f"Futures Change: {row['futures_change']:.2f}%")
        print(f"Delta: {row['delta']:.2f}%")

if __name__ == "__main__":
    main() 