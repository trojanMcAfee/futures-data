import os
import requests
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
ETHERSCAN_API_KEY = os.getenv('ETHERSCAN_API_KEY')

# Base URL for Etherscan API
BASE_URL = "https://api.etherscan.io/api"

def get_block_by_timestamp(timestamp):
    """Get the Ethereum block number for a given Unix timestamp."""
    params = {
        'module': 'block',
        'action': 'getblocknobytime',
        'timestamp': str(int(timestamp)),
        'closest': 'before',
        'apikey': ETHERSCAN_API_KEY
    }
    
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    if data['status'] == '1':
        return int(data['result'])
    else:
        raise Exception(f"Error getting block number: {data['message']}")

def get_eth_price():
    """Get current ETH price."""
    params = {
        'module': 'stats',
        'action': 'ethprice',
        'apikey': ETHERSCAN_API_KEY
    }
    
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    if data['status'] == '1':
        return data['result']
    else:
        raise Exception(f"Error getting ETH price: {data['message']}")

def main():
    # Convert the timestamp string to Unix timestamp
    timestamp_str = "2024-01-03 14:00:00.083460495+00:00"
    dt = datetime.fromisoformat(timestamp_str.replace('Z', '+00:00'))
    unix_timestamp = dt.timestamp()
    
    # Get block number
    block_number = get_block_by_timestamp(unix_timestamp)
    print(f"\nBlock number for timestamp {timestamp_str}:")
    print(f"Block: {block_number}")
    
    # Get ETH price data
    eth_price_data = get_eth_price()
    print(f"\nETH price data:")
    for key, value in eth_price_data.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main() 