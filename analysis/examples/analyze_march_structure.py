#!/usr/bin/env python3

import json
import pandas as pd
from datetime import datetime

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

# Get March data
march_data = pivot_df[pivot_df.index.str.startswith('2024-03')]

print("\nMarch 2024 Market Structure Analysis")
print("=================================")
print("                     Volume                    Close")
print("Date           CL.n.0      CL.n.1      CL.n.0   CL.n.1   Spread   Structure")
print("-" * 85)

backwardation_days = []
contango_days = []

for idx, row in march_data.iterrows():
    spread = row['close_CL.n.1'] - row['close_CL.n.0']
    structure = "Backwardation" if spread < 0 else "Contango"
    
    if spread < 0:
        backwardation_days.append(idx)
    else:
        contango_days.append(idx)
    
    print(f"{idx}  {int(row['volume_CL.n.0']):9,d}  {int(row['volume_CL.n.1']):9,d}  "
          f"  {row['close_CL.n.0']:6.2f}  {row['close_CL.n.1']:6.2f}  {spread:6.2f}   {structure}")

print("\nMarket Structure Summary")
print("=====================")
if backwardation_days:
    print("\nBackwardation Days:")
    for day in backwardation_days:
        spread = march_data.loc[day, 'close_CL.n.1'] - march_data.loc[day, 'close_CL.n.0']
        print(f"{day}: Spread = ${spread:.2f}")
else:
    print("\nNo days in Backwardation found. The market was in Contango throughout March 2024.") 