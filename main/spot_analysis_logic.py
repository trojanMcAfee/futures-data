"""
Spot Oil Analysis Logic

This module provides utility functions for processing and analyzing spot oil price data.
It loads data from spot_oil_prices.json, filters specifically for WTI Crude Oil prices,
and prepares the data for analysis and visualization.

Key functions:
- load_data: Loads JSON data from a specified file path
- filter_wti_data: Extracts only WTI Crude Oil spot price data
- get_spot_data: Main function that processes the data into a pandas DataFrame,
                calculates daily price changes, and prepares it for analysis

This module is used by various analysis scripts to provide consistent data processing
for spot oil price analysis throughout the project.
"""

import json
import pandas as pd
from pathlib import Path

def load_data(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def filter_wti_data(data):
    # Filter for WTI Crude Oil and Spot Price FOB
    wti_data = []
    for item in data['response']['data']:
        if (item.get('product-name') == 'WTI Crude Oil' and 
            item.get('process-name') == 'Spot Price FOB'):
            wti_data.append({
                'date': item['period'],
                'price': item['value']
            })
    
    return wti_data

def get_spot_data(data_path=None):
    if data_path is None:
        # Get the path relative to this script's location
        script_dir = Path(__file__).resolve().parent.parent
        spot_data_path = script_dir / "data" / "spot_oil_prices.json"
    else:
        spot_data_path = Path(data_path)
    
    if not spot_data_path.exists():
        print("Error: spot_oil_prices.json not found.")
        return None
    
    data = load_data(spot_data_path)
    wti_data = filter_wti_data(data)
    
    if not wti_data:
        print("No WTI spot price data found in the specified date range.")
        return None
    
    df_spot = pd.DataFrame(wti_data)
    
    # Convert date string to datetime and price to float
    df_spot['date'] = pd.to_datetime(df_spot['date'])
    df_spot['price'] = pd.to_numeric(df_spot['price'], errors='coerce')
    
    # Sort by date
    df_spot = df_spot.sort_values('date')
    
    # Calculate daily percentage changes
    df_spot['daily_change'] = df_spot['price'].pct_change() * 100
    
    return df_spot 