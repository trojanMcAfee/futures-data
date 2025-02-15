import os
import requests
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
ETHERSCAN_API_KEY = os.getenv('ETHERSCAN_API_KEY')

# Base URLs for APIs
ETHERSCAN_BASE_URL = "https://api.etherscan.io/api"
KRAKEN_BASE_URL = "https://api.kraken.com/0/public"

def get_block_by_timestamp(timestamp):
    """Get the Ethereum block number for a given Unix timestamp."""
    params = {
        'module': 'block',
        'action': 'getblocknobytime',
        'timestamp': str(int(timestamp)),
        'closest': 'before',
        'apikey': ETHERSCAN_API_KEY
    }
    
    response = requests.get(ETHERSCAN_BASE_URL, params=params)
    data = response.json()
    
    if data['status'] == '1':
        return int(data['result'])
    else:
        raise Exception(f"Error getting block number: {data['message']}")

def get_block_info(block_number):
    """Get block information using eth_getBlockByNumber."""
    params = {
        'module': 'proxy',
        'action': 'eth_getBlockByNumber',
        'tag': hex(block_number),
        'boolean': 'true',
        'apikey': ETHERSCAN_API_KEY
    }
    
    response = requests.get(ETHERSCAN_BASE_URL, params=params)
    data = response.json()
    
    if 'result' in data and data['result']:
        return data['result']
    else:
        raise Exception(f"Error getting block info: {data.get('error', {}).get('message', 'Unknown error')}")

def get_eth_historical_price(timestamp):
    """Get historical ETH price from Kraken at a specific timestamp."""
    params = {
        'pair': 'ETHUSD',
        'since': str(int(timestamp * 1000000000)),  # Convert to nanoseconds
        'count': 1
    }
    
    response = requests.get(f"{KRAKEN_BASE_URL}/Trades", params=params)
    
    if response.status_code != 200:
        print(f"API Response: {response.text}")
        raise Exception(f"API request failed with status code: {response.status_code}")
    
    data = response.json()
    
    if not data.get('error') and 'result' in data:
        # Get the first trade from the ETHUSD pair (XETHZUSD in Kraken's format)
        trades = data['result'].get('XETHZUSD', [])
        if trades:
            trade = trades[0]
            return {
                'timestamp': datetime.fromtimestamp(float(trade[2])),
                'price': float(trade[0])
            }
    
    print(f"API Response: {data}")
    raise Exception("Error getting historical price from Kraken")

def main():
    # Convert the timestamp string to Unix timestamp and datetime
    timestamp_str = "2024-01-03 14:00:00.083460495+00:00"
    dt = datetime.fromisoformat(timestamp_str.replace('Z', '+00:00'))
    unix_timestamp = dt.timestamp()
    
    # Get block number
    block_number = get_block_by_timestamp(unix_timestamp)
    print(f"\nBlock number for timestamp {timestamp_str}:")
    print(f"Block: {block_number}")
    
    # Get block information
    block_info = get_block_info(block_number)
    print(f"\nBlock information:")
    print(f"Timestamp: {datetime.fromtimestamp(int(block_info['timestamp'], 16))}")
    print(f"Gas Used: {int(block_info['gasUsed'], 16)}")
    print(f"Base Fee Per Gas: {int(block_info['baseFeePerGas'], 16) / 1e9} Gwei")
    
    # Get ETH historical price from Kraken
    try:
        price_data = get_eth_historical_price(unix_timestamp)
        print(f"\nETH historical price data from Kraken:")
        print(f"Timestamp: {price_data['timestamp']}")
        print(f"Price: ${price_data['price']:,.2f}")
    except Exception as e:
        print(f"\nFailed to get price data: {str(e)}")

if __name__ == "__main__":
    main() 