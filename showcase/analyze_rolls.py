#!/usr/bin/env python3

import json
import pandas as pd
from datetime import datetime

# Read the existing output.json
with open('output.json', 'r') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Convert timestamp to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Sort by timestamp
df = df.sort_values('timestamp')

# Create a sample window to show roll period
print("\nExample of a roll period:")
print("------------------------")

# Group by timestamp and show both contracts side by side
pivot_df = df.pivot(index='timestamp', columns='symbol', 
                    values=['volume', 'close'])

# Format for display
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.2f' % x)

# Display 5 days of data to show the roll
print(pivot_df.head(10))

# Show volume shift during roll
print("\nVolume comparison during roll period:")
print("------------------------------------")
print(pivot_df['volume'].head(10)) 