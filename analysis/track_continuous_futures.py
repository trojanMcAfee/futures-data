import json
from datetime import datetime
import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def load_data(file_path):
    with open(file_path, 'r') as f:
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
    # Convert data for plotting
    dates = [row[0] for row in daily_data]
    prices = [row[1] for row in daily_data]
    roll_dates = [row[0] for row in daily_data if row[4]]
    roll_prices = [row[1] for row in daily_data if row[4]]
    
    # Create the plot
    plt.figure(figsize=(15, 8))
    
    # Plot continuous price
    plt.plot(dates, prices, label='Continuous Future Price', color='blue', linewidth=1)
    
    # Plot roll events
    plt.scatter(roll_dates, roll_prices, color='red', marker='o', 
                label='Roll Events', zorder=5, s=100)
    
    # Customize the plot
    plt.title('Crude Oil Continuous Futures Price (2024)', fontsize=14, pad=20)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Price ($)', fontsize=12)
    
    # Format x-axis
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    plt.xticks(rotation=45)
    
    # Add grid
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Add legend
    plt.legend(loc='upper left')
    
    # Adjust layout
    plt.tight_layout()
    
    # Save the plot
    plt.savefig('continuous_futures_plot.png', dpi=300, bbox_inches='tight')
    plt.close()

def format_for_table(daily_data):
    # Convert data for table display
    return [[date.strftime('%Y-%m-%d'), f"${price:.2f}", vol1, vol2, "ROLL" if roll else ""]
            for date, price, vol1, vol2, roll in daily_data]

def main():
    data = load_data('../data/output.json')
    daily_data = analyze_continuous_futures(data)
    
    # Create the plot
    plot_continuous_futures(daily_data)
    
    # Format data for table display
    table_data = format_for_table(daily_data)
    
    # Print table
    headers = ["Date", "Price", "Front Vol", "Next Vol", "Event"]
    print("\nContinuous Futures Price Evolution (2024)")
    print("========================================")
    print(tabulate(table_data, headers=headers, tablefmt="simple"))
    
    # Print summary
    roll_days = [row for row in table_data if row[4] == "ROLL"]
    print(f"\nTotal number of rolls: {len(roll_days)}")
    print("\nRoll dates:")
    for roll in roll_days:
        print(f"  {roll[0]}: {roll[1]} (Front Vol: {roll[2]}, Next Vol: {roll[3]})")
    
    print("\nPlot has been saved as 'continuous_futures_plot.png'")

if __name__ == "__main__":
    main() 