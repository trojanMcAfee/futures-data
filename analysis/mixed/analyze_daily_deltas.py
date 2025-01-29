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
    
    # Mark deltas where futures change was the dominant factor
    df_merged['futures_driven'] = (
        # Futures move must be significant (>1%)
        (abs(df_merged['futures_change']) > 1.0) & 
        # Futures move must be larger than spot move
        (abs(df_merged['futures_change']) > abs(df_merged['spot_change'])) &
        # The difference must be meaningful (>0.5%)
        (abs(df_merged['futures_change'] - df_merged['spot_change']) > 0.5)
    )
    
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
    # Increase figure width for better x-axis spacing
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(20, 12), height_ratios=[2, 1])
    
    # Filter for futures-driven events
    futures_driven_data = df_merged[df_merged['futures_driven']]
    
    # Top subplot: Futures deviation from spot
    ax1.plot(df_merged['date'], df_merged['futures_change'], 
             color='blue', linewidth=1.5, label='Futures Daily Change')
    ax1.plot(df_merged['date'], df_merged['spot_change'], 
             color='red', linewidth=1.5, label='Spot Daily Change')
    
    # Highlight futures-driven divergences
    ax1.scatter(futures_driven_data['date'], futures_driven_data['futures_change'],
                color='yellow', s=100, zorder=5, alpha=0.5,
                label='Futures-Driven Divergence')
    
    # Add bands for standard deviation of futures-driven events
    std_dev = futures_driven_data['futures_change'].std()
    mean = futures_driven_data['futures_change'].mean()
    ax1.axhline(y=mean + std_dev, color='gray', linestyle=':', alpha=0.5, 
                label='±1 Std Dev (Futures)')
    ax1.axhline(y=mean - std_dev, color='gray', linestyle=':', alpha=0.5)
    
    ax1.set_title('Futures vs Spot Daily Changes (2024)\nHighlighting Futures-Driven Divergences', 
                  fontsize=14, pad=20)
    ax1.set_ylabel('Daily Change (%)', fontsize=12)
    ax1.grid(True, which='major', linestyle='--', alpha=0.7)
    ax1.legend(loc='upper left')
    
    # Customize x-axis for better spacing
    # Use WeekdayLocator for major ticks (Mondays) and format with date
    ax1.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.MO))
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    
    # Bottom subplot: Histogram of futures-driven divergences
    n, bins, patches = ax2.hist(futures_driven_data['futures_change'], bins=30, 
                               color='blue', alpha=0.7)
    
    # Add vertical lines for mean and std dev of futures-driven events
    ax2.axvline(x=mean, color='red', linestyle='--', 
                label=f'Mean: {mean:.2f}%')
    ax2.axvline(x=mean + std_dev, color='gray', linestyle=':', 
                label=f'Std Dev: ±{std_dev:.2f}%')
    ax2.axvline(x=mean - std_dev, color='gray', linestyle=':', alpha=0.7)
    
    ax2.set_xlabel('Futures Daily Change (%)', fontsize=12)
    ax2.set_ylabel('Frequency', fontsize=12)
    ax2.grid(True, linestyle='--', alpha=0.7)
    ax2.legend(loc='upper left')
    
    # Format x-axis labels for readability
    plt.setp(ax1.get_xticklabels(), rotation=45, ha='right')
    
    # Adjust layout with more space for x-axis labels
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
    
    # Get futures-driven events
    futures_driven = df_merged[df_merged['futures_driven']].sort_values('delta', ascending=False)
    
    # Print summary statistics for futures-driven events
    print("\nFutures-Driven Divergence Analysis:")
    print("=================================")
    print(f"Number of significant futures-driven events: {len(futures_driven)}")
    print(f"Mean Futures Change: {futures_driven['futures_change'].mean():.2f}%")
    print(f"Std Dev of Futures Changes: {futures_driven['futures_change'].std():.2f}%")
    print(f"Max Futures Change: {futures_driven['futures_change'].max():.2f}%")
    print(f"Min Futures Change: {futures_driven['futures_change'].min():.2f}%")
    
    # Print the dates with largest futures-driven divergences
    print("\nLargest Futures-Driven Divergences:")
    for _, row in futures_driven.head().iterrows():
        print(f"\nDate: {row['date'].strftime('%Y-%m-%d')}")
        print(f"Futures Change: {row['futures_change']:.2f}%")
        print(f"Spot Change: {row['spot_change']:.2f}%")
        print(f"Net Delta: {row['delta']:.2f}%")

if __name__ == "__main__":
    main() 