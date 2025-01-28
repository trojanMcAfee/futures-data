import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import sys
from pathlib import Path

# Add main directory to Python path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from main.spot_analysis_logic import get_spot_data
from main.futures_analysis_logic import get_futures_data

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
    # Get plot path relative to the script location
    script_dir = Path(__file__).resolve().parent
    plot_path = script_dir / 'daily_deltas_analysis.png'
    
    # Check if plot already exists
    if plot_path.exists():
        print("\nPlot already exists at:", plot_path)
        return
    
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
    
    # Save the plot
    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
    print("\nPlot has been saved at:", plot_path)
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