#!/usr/bin/env python3

# Analyzes a position valuation for a year when rolls happen during the roll period. 
# Includes a T-bills P&L calculation of 3% (with 1% haircut included)
# *** THIS GOES ***

import json
import pandas as pd
from datetime import datetime, timedelta
import os

# Initial position parameters
INITIAL_CONTRACTS = 100
BARRELS_PER_CONTRACT = 1000

# Read the existing output.json from data directory
with open('./data/output.json', 'r') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Convert timestamp to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['month'] = df['timestamp'].dt.strftime('%B')
df['date'] = df['timestamp'].dt.strftime('%Y-%m-%d')
df['weekday'] = df['timestamp'].dt.strftime('%A')

# Sort by timestamp
df = df.sort_values('timestamp')

# Create pivot table
pivot_df = df.pivot(index='date', columns='symbol', 
                    values=['volume', 'close'])

# Flatten column names
pivot_df.columns = [f"{col[0]}_{col[1]}" for col in pivot_df.columns]

# Function to identify roll period for a month
def get_roll_period(month_data):
    # Find where volume shifts from CL.n.0 to CL.n.1
    volume_shift = month_data[month_data['volume_CL.n.1'] > month_data['volume_CL.n.0']]
    if len(volume_shift) > 0:
        # Get 1 day before and 1 day after the volume shift
        shift_start = volume_shift.index[0]
        shift_idx = month_data.index.get_loc(shift_start)
        if shift_idx > 0:
            start_idx = shift_idx - 1
        else:
            start_idx = shift_idx
        
        if shift_idx + 1 < len(month_data):
            end_idx = shift_idx + 1
        else:
            end_idx = shift_idx
            
        return month_data.iloc[start_idx:end_idx + 1]
    return pd.DataFrame()

# Process each month
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']

print("\nCrude Oil Futures Roll Periods Analysis - 2024")
print("=============================================")

# Initialize with starting position
current_contracts = INITIAL_CONTRACTS
position_value = 0
first_month = True

for month in months:
    # Get data for the month
    month_data = pivot_df[pivot_df.index.str.startswith('2024-' + str(months.index(month) + 1).zfill(2))]
    roll_period = get_roll_period(month_data)
    
    if not roll_period.empty:
        print(f"\n{month}")
        print("=" * len(month))
        print("                     Volume                    Close")
        print("Date           CL.n.0      CL.n.1      CL.n.0   CL.n.1   Spread")
        print("-" * 65)
        
        # Track dates to identify gaps
        dates = pd.to_datetime(roll_period.index)
        roll_analysis = None
        
        # First print all data including gaps
        for i, (idx, row) in enumerate(roll_period.iterrows()):
            spread = row['close_CL.n.1'] - row['close_CL.n.0']
            print(f"{idx}  {int(row['volume_CL.n.0']):9,d}  {int(row['volume_CL.n.1']):9,d}  "
                  f"  {row['close_CL.n.0']:6.2f}  {row['close_CL.n.1']:6.2f}  {spread:6.2f}")
            
            # Check for gaps between dates
            if i < len(dates) - 1:
                current_date = dates[i]
                next_date = dates[i + 1]
                days_diff = (next_date - current_date).days
                
                if days_diff > 1:
                    gap_dates = [(current_date + timedelta(days=x)).strftime('%Y-%m-%d (%A)') 
                                for x in range(1, days_diff)]
                    print(f"{'[Gap]:':11} {', '.join(gap_dates)}")
            
            # Store roll analysis if this is the roll day
            if row['volume_CL.n.1'] > row['volume_CL.n.0'] and roll_analysis is None:
                roll_day = idx
                
                # Initialize position value in January
                if first_month:
                    position_value = current_contracts * BARRELS_PER_CONTRACT * row['close_CL.n.0']
                    initial_position_value = position_value
                    initial_contracts = current_contracts
                    first_month = False
                
                # Calculate position values and change
                old_position_value = position_value
                
                # Calculate how many contracts we can buy with the money from selling
                sell_value = current_contracts * BARRELS_PER_CONTRACT * row['close_CL.n.0']
                current_contracts = sell_value / (BARRELS_PER_CONTRACT * row['close_CL.n.1'])
                position_value = current_contracts * BARRELS_PER_CONTRACT * row['close_CL.n.1']
                position_change = position_value - old_position_value
                
                # Store roll analysis
                roll_analysis = f"\n[Roll Analysis on {roll_day}]\n"
                roll_analysis += f"Contracts After Roll: {current_contracts:.4f}\n"
                roll_analysis += f"Position Value: ${position_value:,.2f}\n"
                roll_analysis += f"Position Change: ${position_change:,.2f} ({(position_change/old_position_value)*100:.2f}%)\n"
                roll_analysis += f"Market Structure: {'Backwardation' if spread < 0 else 'Contango'}"
        
        # Print roll analysis after all data
        if roll_analysis:
            print(roll_analysis)

print("\n\nPosition Summary")
print("================")
print(f"Initial Contracts: {initial_contracts:.4f}")
print(f"Final Contracts: {current_contracts:.4f}")
print(f"Contract Change: {current_contracts - initial_contracts:.4f}")
print(f"Initial Position Value (Jan 2024): ${initial_position_value:,.2f}")
print(f"Final Position Value (Dec 2024): ${position_value:,.2f}")
print(f"Total P&L: ${position_value - initial_position_value:,.2f}")

print("\n\nYearly Position Summary")
print("=====================")

# Calculate T-bills P&L (3% with 1% haircut)
tbills_pnl = initial_position_value * 0.03  # 3% return on initial value

# Calculate total return including T-bills
total_return_with_tbills = ((position_value - initial_position_value + tbills_pnl) / initial_position_value) * 100

print(f"Initial Position Value (Jan 2024): ${initial_position_value:,.2f}")
print(f"Final Position Value (Dec 2024): ${position_value:,.2f}")
print(f"Position P&L: ${position_value - initial_position_value:,.2f}")
print(f"T-bills P&L: ${tbills_pnl:,.2f}  # with 1% haircut")
print(f"Total P&L: ${position_value - initial_position_value + tbills_pnl:,.2f}")
print(f"Total Return: {total_return_with_tbills:.2f}%")