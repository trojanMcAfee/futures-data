#!/usr/bin/env python3

import os
from datetime import datetime, timezone
import databento as db
import pandas as pd
from dotenv import load_dotenv
import json

# Load environment variables from .env file
load_dotenv()

# Initialize client with API key from .env
client = db.Historical(os.getenv('DATABENTO_API_KEY'))

# Define parameters
dataset = "GLBX.MDP3"  # CME Globex MDP 3.0
symbols = ["CLG5"]  # Crude Oil Future March 2025
start = datetime(2024, 1, 1, tzinfo=timezone.utc)
end = datetime(2025, 1, 1, tzinfo=timezone.utc)

try:
    # Get OHLCV daily data
    data = client.timeseries.get_range(
        dataset=dataset,
        symbols=symbols,
        schema="ohlcv-1d",
        start=start,
        end=end
    )
    
    # Convert to pandas DataFrame first
    df = data.to_df()
    
    # Save to JSON
    output_file = "output.json"
    with open(output_file, 'w') as f:
        df.to_json(f, orient='records', date_format='iso')
    print(f"Data successfully saved to {output_file}")
    
    # Display first few rows
    print("\nFirst few rows of the data:")
    print(df.head())

except Exception as e:
    print(f"Error occurred: {str(e)}")