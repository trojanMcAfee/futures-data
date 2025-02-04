import json
import time
from datetime import datetime, timezone
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Constants
ETHERSCAN_API_KEY = os.getenv('ETHERSCAN_API_KEY')
ETHERSCAN_API_URL = 'https://api.etherscan.io/api'

# Configure retry strategy
retry_strategy = Retry(
    total=3,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504],
)
adapter = HTTPAdapter(max_retries=retry_strategy)
session = requests.Session()
session.mount("https://", adapter)

def convert_to_unix_timestamp(date_str):
    """Convert date string to Unix timestamp at 00:00:00 UTC"""
    # Parse the date and make it timezone-aware with UTC
    dt = datetime.strptime(date_str, '%Y-%m-%d').replace(tzinfo=timezone.utc)
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
    
    response = session.get(ETHERSCAN_API_URL, params=params)
    data = response.json()
    
    if data['status'] == '1' and data['message'] == 'OK':
        return data['result']
    else:
        raise Exception(f"Error getting block number: {data}")

def needs_processing(entry):
    """Check if an entry needs processing"""
    return 'unix' not in entry or entry.get('block') is None

def save_progress(data, filename='data/reth_prices.json'):
    """Save current progress to file with error handling"""
    try:
        # First save to a temporary file
        temp_file = filename + '.tmp'
        with open(temp_file, 'w') as f:
            json.dump(data, f, indent=2)
        
        # Then rename it to the actual file (atomic operation)
        os.replace(temp_file, filename)
        return True
    except Exception as e:
        print(f"Error saving progress: {e}")
        return False

def main():
    # Read the JSON file
    with open('data/reth_prices.json', 'r') as f:
        data = json.load(f)
    
    # List of all months
    months = [
        'january', 'february', 'march', 'april', 'may', 'june',
        'july', 'august', 'september', 'october', 'november', 'december'
    ]
    
    # Process all months
    for month in months:
        print(f"Processing {month}...")
        month_modified = False
        
        for entry in data[month]:
            if needs_processing(entry):
                month_modified = True
                # Add Unix timestamp
                entry['unix'] = str(convert_to_unix_timestamp(entry['timestamp']))
                
                # Get correct block number with retries
                max_retries = 3
                for attempt in range(max_retries):
                    try:
                        correct_block = get_block_number_by_timestamp(entry['unix'])
                        entry['block'] = correct_block
                        # Add small delay to avoid hitting rate limits
                        time.sleep(0.2)
                        break
                    except Exception as e:
                        if attempt == max_retries - 1:  # Last attempt
                            print(f"Error processing {entry['timestamp']} after {max_retries} attempts: {e}")
                        else:
                            print(f"Attempt {attempt + 1} failed for {entry['timestamp']}, retrying...")
                            time.sleep(1)  # Wait longer between retries
        
        # Save after each month if any modifications were made
        if month_modified:
            if save_progress(data):
                print(f"Completed and saved {month}")
            else:
                print(f"Warning: Failed to save progress after {month}")

if __name__ == "__main__":
    main() 