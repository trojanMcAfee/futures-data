import json
from datetime import datetime
import pandas as pd
from tabulate import tabulate

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
                date.strftime('%Y-%m-%d'),
                f"${price:.2f}",
                f"${row['volume_CL.n.0']:,.0f}",
                f"${row['volume_CL.n.1']:,.0f}",
                "ROLL" if roll_event else ""
            ])
    
    return daily_data

def main():
    data = load_data('../data/output.json')
    daily_data = analyze_continuous_futures(data)
    
    # Print table
    headers = ["Date", "Price", "Front Vol", "Next Vol", "Event"]
    print("\nContinuous Futures Price Evolution (2024)")
    print("========================================")
    print(tabulate(daily_data, headers=headers, tablefmt="simple"))
    
    # Print summary
    roll_days = [row for row in daily_data if row[4] == "ROLL"]
    print(f"\nTotal number of rolls: {len(roll_days)}")
    print("\nRoll dates:")
    for roll in roll_days:
        print(f"  {roll[0]}: {roll[1]} (Front Vol: {roll[2]}, Next Vol: {roll[3]})")

if __name__ == "__main__":
    main() 