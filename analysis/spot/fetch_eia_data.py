import requests
import json
import os
from pathlib import Path

def fetch_eia_data():
    # API configuration
    api_key = "yetkLTFHXJKifjhsgRlSRfGQmGnsKiBRV7vvD5Vp"
    base_url = "https://api.eia.gov/v2/petroleum/pri/spt/data/"
    
    # Parameters for the API request
    params = {
        "frequency": "daily",
        "data[0]": "value",
        "start": "2024-01-01",
        "end": "2024-12-31",
        "sort[0][column]": "period",
        "sort[0][direction]": "desc",
        "offset": 0,
        "length": 5000,
        "api_key": api_key
    }
    
    try:
        # Make the API request
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Parse the JSON response
        data = response.json()
        
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from EIA API: {e}")
        return None

def save_data(data, output_path):
    try:
        with open(output_path, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"Data successfully saved to {output_path}")
    except Exception as e:
        print(f"Error saving data to file: {e}")

def main():
    # Get the absolute path to the script's directory
    script_dir = Path(__file__).resolve().parent
    
    # Navigate up two levels to the project root and create data directory
    data_dir = script_dir.parent.parent / 'data'
    data_dir.mkdir(exist_ok=True)
    
    # Define the output path
    output_path = data_dir / 'spot_data.json'
    
    # Check if file already exists
    if output_path.exists():
        print("spot_data.json already exists. Skipping data fetch.")
        return
    
    # Fetch data from EIA API
    print("Fetching data from EIA API...")
    data = fetch_eia_data()
    
    if data:
        # Save the data
        save_data(data, output_path)
    else:
        print("Failed to fetch data from EIA API")

if __name__ == "__main__":
    main() 