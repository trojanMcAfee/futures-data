import json
import time
from datetime import datetime
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Constants
ETHERSCAN_API_KEY = os.getenv('ETHERSCAN_API_KEY')
ETHERSCAN_API_URL = 'https://api.etherscan.io/api'

def convert_to_unix_timestamp(date_str):
    """Convert date string to Unix timestamp at 00:00:00"""
    dt = datetime.strptime(date_str, '%Y-%m-%d')
    return int(dt.timestamp())

def get_block_number_by_timestamp(timestamp):
    """Get the closest block number for a given timestamp using Etherscan API"""
    params = {
        'module': 'block',
        'action': 'getblocknobytime',
        'timestamp': timestamp,
        'closest': 'after',  # Get the block after this timestamp
        'apikey': ETHERSCAN_API_KEY
    }
    
    response = requests.get(ETHERSCAN_API_URL, params=params)
    data = response.json()
    
    if data['status'] == '1' and data['message'] == 'OK':
        return data['result']
    else:
        raise Exception(f"Error getting block number: {data}")

def main():
    # Read the JSON file
    with open('data/reth_prices.json', 'r') as f:
        data = json.load(f)
    
    # Process only January data
    for entry in data['january']:
        # Add Unix timestamp
        entry['unix'] = str(convert_to_unix_timestamp(entry['timestamp']))
        
        # Get correct block number
        try:
            correct_block = get_block_number_by_timestamp(entry['unix'])
            entry['block'] = correct_block
            # Add small delay to avoid hitting rate limits
            time.sleep(0.2)
        except Exception as e:
            print(f"Error processing {entry['timestamp']}: {e}")
    
    # Write updated data back to file
    with open('data/reth_prices.json', 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    main() 