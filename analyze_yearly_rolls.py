#!/usr/bin/env python3

import json
import pandas as pd
from datetime import datetime, timedelta
import os

# Position parameters
CONTRACTS = 100
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

total_roll_pnl = 0
current_position_value = 0
previous_roll_price = None

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
                
                # Calculate position values and P&L
                sell_price = row['close_CL.n.0']
                buy_price = row['close_CL.n.1']
                
                sell_value = CONTRACTS * BARRELS_PER_CONTRACT * sell_price
                buy_value = CONTRACTS * BARRELS_PER_CONTRACT * buy_price
                roll_pnl = sell_value - buy_value
                
                if previous_roll_price is None:
                    previous_roll_price = sell_price
                
                # Update running totals
                total_roll_pnl += roll_pnl
                current_position_value = buy_value
                previous_roll_price = buy_price
                
                # Store roll analysis
                roll_analysis = f"\n[Roll Analysis on {roll_day}]\n"
                roll_analysis += f"Selling {CONTRACTS:,d} contracts at ${sell_price:.2f} = ${sell_value:,.2f}\n"
                roll_analysis += f"Buying {CONTRACTS:,d} contracts at ${buy_price:.2f} = ${buy_value:,.2f}\n"
                roll_analysis += f"Roll P&L: ${roll_pnl:,.2f}\n"
                roll_analysis += f"Market Structure: {'Backwardation' if spread < 0 else 'Contango'}"
        
        # Print roll analysis after all data
        if roll_analysis:
            print(roll_analysis)

print("\n\nPosition Summary")
print("================")
print(f"Total Roll P&L: ${total_roll_pnl:,.2f}")
print(f"Final Position Value: ${current_position_value:,.2f}") 

print("\n\nYearly Position Summary")
print("=====================")

# Calculate initial and final values
initial_value = CONTRACTS * BARRELS_PER_CONTRACT * 71.32  # First roll price in January
final_value = current_position_value

# Calculate total return
total_pnl = final_value - initial_value + total_roll_pnl
total_return_pct = (total_pnl / initial_value) * 100

# Calculate average roll cost
avg_roll_cost = total_roll_pnl / 12

print(f"Initial Position Value (Jan 2024): ${initial_value:,.2f}")
print(f"Final Position Value (Dec 2024): ${final_value:,.2f}")
print(f"Total Roll P&L: ${total_roll_pnl:,.2f}")
print(f"Average Monthly Roll Cost: ${avg_roll_cost:,.2f}")
print(f"Total P&L: ${total_pnl:,.2f}")
print(f"Total Return: {total_return_pct:.2f}%")
print(f"Average Roll Cost per Barrel per Month: ${abs(total_roll_pnl/(CONTRACTS * BARRELS_PER_CONTRACT * 12)):.2f}") 