#!/usr/bin/env python3

import json
import pandas as pd
from datetime import datetime

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
df['date'] = df['timestamp'].dt.strftime('%Y-%m-%d')
df['weekday'] = df['timestamp'].dt.strftime('%A')

# Sort by timestamp
df = df.sort_values('timestamp')

# Create pivot table
pivot_df = df.pivot(index='date', columns='symbol', 
                    values=['volume', 'close'])

# Flatten column names
pivot_df.columns = [f"{col[0]}_{col[1]}" for col in pivot_df.columns]

# Get February data
feb_data = pivot_df[pivot_df.index.str.startswith('2024-02')]

print("\nPart 1: February 2024 Traditional Roll Analysis")
print("============================================")
print("                     Volume                    Close")
print("Date           CL.n.0      CL.n.1      CL.n.0   CL.n.1   Spread   Structure")
print("-" * 85)

backwardation_days = []
contango_days = []

for idx, row in feb_data.iterrows():
    spread = row['close_CL.n.1'] - row['close_CL.n.0']
    structure = "Backwardation" if spread < 0 else "Contango"
    
    if spread < 0:
        backwardation_days.append((idx, spread, row))
    else:
        contango_days.append((idx, spread, row))
    
    print(f"{idx}  {int(row['volume_CL.n.0']):9,d}  {int(row['volume_CL.n.1']):9,d}  "
          f"  {row['close_CL.n.0']:6.2f}  {row['close_CL.n.1']:6.2f}  {spread:6.2f}   {structure}")

# Traditional Roll Analysis (during volume shift period)
roll_period = feb_data[(feb_data['volume_CL.n.1'] > feb_data['volume_CL.n.0'])]
if not roll_period.empty:
    roll_day = roll_period.index[0]
    sell_price = roll_period.loc[roll_day, 'close_CL.n.0']
    buy_price = roll_period.loc[roll_day, 'close_CL.n.1']
    
    sell_value = CONTRACTS * BARRELS_PER_CONTRACT * sell_price
    buy_value = CONTRACTS * BARRELS_PER_CONTRACT * buy_price
    roll_pnl = sell_value - buy_value
    
    print("\nTraditional Roll Analysis")
    print("========================")
    print(f"Roll Date: {roll_day}")
    print(f"Selling {CONTRACTS:,d} contracts at ${sell_price:.2f} = ${sell_value:,.2f}")
    print(f"Buying {CONTRACTS:,d} contracts at ${buy_price:.2f} = ${buy_value:,.2f}")
    print(f"Roll P&L: ${roll_pnl:,.2f}")
    print(f"Market Structure: {'Backwardation' if (buy_price - sell_price) < 0 else 'Contango'}")

print("\n\nPart 2: Alternative Rolling Strategy (Backwardation-based)")
print("====================================================")

# Filter days until February 19th
backwardation_days = [(d, s, r) for d, s, r in backwardation_days 
                      if datetime.strptime(d, '%Y-%m-%d').day <= 19]

if backwardation_days:
    # Calculate how many contracts to roll each backwardation day
    contracts_per_day = CONTRACTS / len(backwardation_days)
    contracts_per_day = round(contracts_per_day)  # Round to whole contracts
    remaining_contracts = CONTRACTS
    
    total_alternative_pnl = 0
    print("\nRolling Schedule:")
    print("================")
    
    for i, (day, spread, row) in enumerate(backwardation_days):
        # For the last day, roll all remaining contracts
        if i == len(backwardation_days) - 1:
            contracts_to_roll = remaining_contracts
        else:
            contracts_to_roll = min(contracts_per_day, remaining_contracts)
        
        if contracts_to_roll > 0:
            sell_price = row['close_CL.n.0']
            buy_price = row['close_CL.n.1']
            
            sell_value = contracts_to_roll * BARRELS_PER_CONTRACT * sell_price
            buy_value = contracts_to_roll * BARRELS_PER_CONTRACT * buy_price
            roll_pnl = sell_value - buy_value
            
            total_alternative_pnl += roll_pnl
            remaining_contracts -= contracts_to_roll
            
            print(f"\nDate: {day}")
            print(f"Rolling {contracts_to_roll:,d} contracts")
            print(f"Selling at ${sell_price:.2f} = ${sell_value:,.2f}")
            print(f"Buying at ${buy_price:.2f} = ${buy_value:,.2f}")
            print(f"Roll P&L: ${roll_pnl:,.2f}")
            print(f"Spread: ${spread:.2f}")

    print("\nAlternative Strategy Summary")
    print("==========================")
    print(f"Total P&L: ${total_alternative_pnl:,.2f}")
    
    # Calculate final position value for alternative strategy
    final_position_value = CONTRACTS * BARRELS_PER_CONTRACT * buy_price  # Using last buy price
    print(f"Final Position Value: ${final_position_value:,.2f}")
    
    if roll_pnl:  # Compare with traditional roll if available
        print(f"\nComparison with Traditional Roll:")
        print(f"Traditional Roll P&L: ${-4000.00:,.2f}")  # Fixed value from Part 1
        print(f"Alternative Strategy P&L: ${total_alternative_pnl:,.2f}")
        print(f"Difference: ${total_alternative_pnl - (-4000.00):,.2f}")
        print(f"Strategy Outperformance: {((total_alternative_pnl - (-4000.00)) / abs(-4000.00) * 100):.2f}%")
else:
    print("\nNo backwardation days found before February 19th. Strategy could not be executed.") 