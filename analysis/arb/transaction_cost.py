"""
Transaction cost calculator for NAV arbitrage trades. This module:
- Calculates Ethereum transaction costs for potential trades
- Retrieves block information and gas prices
- Converts gas costs to USD using real-time ETH prices
- Caches block information for 12-second windows to improve performance
"""

from __future__ import annotations
import os
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv
from typing import Optional, Dict

# Load environment variables
load_dotenv()
ETHERSCAN_API_KEY = os.getenv('ETHERSCAN_API_KEY')

# Constants
ETHERSCAN_BASE_URL = "https://api.etherscan.io/api"
KRAKEN_BASE_URL = "https://api.kraken.com/0/public"
SWAP_COST = 150_000  # Gas units for a swap transaction
CACHE_WINDOW_SECONDS = 12  # Cache block info for 12 seconds

class BlockInfoCache:
    def __init__(self):
        self.last_fetch_time: Optional[datetime] = None
        self.cached_block: Optional[int] = None
        self.cached_base_fee: Optional[float] = None
        self.cached_eth_price: Optional[float] = None
        self.cache_window = timedelta(seconds=CACHE_WINDOW_SECONDS)

    def should_update_cache(self, timestamp: datetime) -> bool:
        """Check if we need to update the cache based on timestamp."""
        if self.last_fetch_time is None:
            return True
        return (timestamp - self.last_fetch_time) >= self.cache_window

    def update_cache(self, timestamp: datetime) -> None:
        """Update the cache with new block information."""
        unix_timestamp = timestamp.timestamp()
        
        # Get block number for timestamp
        self.cached_block = get_block_by_timestamp(unix_timestamp)
        
        # Get block information
        block_info = get_block_info(self.cached_block)
        self.cached_base_fee = int(block_info['baseFeePerGas'], 16) / 1e9
        
        # Get ETH price
        self.cached_eth_price = get_eth_price(unix_timestamp)
        
        # Update last fetch time
        self.last_fetch_time = timestamp

    def get_cached_info(self) -> Dict:
        """Get the currently cached information."""
        if any(x is None for x in [self.cached_block, self.cached_base_fee, self.cached_eth_price]):
            raise ValueError("Cache not initialized")
        
        return {
            'block': self.cached_block,
            'base_fee_gwei': self.cached_base_fee,
            'eth_price': self.cached_eth_price
        }

# Global cache instance
block_cache = BlockInfoCache()

def get_block_by_timestamp(timestamp: float) -> int:
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

def get_block_info(block_number: int) -> dict:
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

def get_eth_price(timestamp: float) -> float:
    """Get ETH price from Kraken at a specific timestamp."""
    params = {
        'pair': 'ETHUSD',
        'since': str(int(timestamp * 1000000000)),  # Convert to nanoseconds
        'count': 1
    }
    
    response = requests.get(f"{KRAKEN_BASE_URL}/Trades", params=params)
    
    if response.status_code != 200:
        raise Exception(f"API request failed with status code: {response.status_code}")
    
    data = response.json()
    
    if not data.get('error') and 'result' in data:
        trades = data['result'].get('XETHZUSD', [])
        if trades:
            return float(trades[0][0])  # Return the price
    
    raise Exception("Error getting ETH price from Kraken")

def calculate_transaction_cost(timestamp: datetime) -> dict:
    """
    Calculate the transaction cost in USD for a trade at the given timestamp.
    Uses cached block information for 12-second windows to improve performance.
    
    Returns:
        dict: Contains block number, base fee, and total cost in USD
    """
    global block_cache
    
    # Check if we need to update the cache
    if block_cache.should_update_cache(timestamp):
        block_cache.update_cache(timestamp)
    
    # Get cached information
    cached_info = block_cache.get_cached_info()
    
    # Calculate total gas cost in ETH
    gas_cost_eth = (cached_info['base_fee_gwei'] * SWAP_COST) / 1e9
    
    # Calculate total cost in USD
    total_cost_usd = gas_cost_eth * cached_info['eth_price']
    
    return {
        'block': cached_info['block'],
        'base_fee_gwei': cached_info['base_fee_gwei'],
        'total_cost_usd': total_cost_usd
    } 