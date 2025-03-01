#!/usr/bin/env python
"""
This script calculates the sqrtPriceX96 value used in Uniswap V3-style liquidity pools
based on the current market price of a futures contract.

It imports the price_checker module to get the current price, then
applies the formula: sqrt((market_price * 10^6) / (10^18)) * 2^96
"""

import math
import sys
import os

# Add the contract directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'contract'))

# Import the price_checker module
from price_checker import get_last_price

def calculate_sqrtPriceX96(last_price):
    """
    Calculate sqrtPriceX96 value based on the formula:
    sqrt((market_price * 10^6) / (10^18)) * 2^96
    
    Args:
        last_price (float): The last price from IBKR
        
    Returns:
        int: The calculated sqrtPriceX96 value
    """
    # Convert the last price to market_price by dividing by 1e6
    market_price = last_price / 1e6
    
    # Apply the formula: sqrt((market_price * 10^6) / (10^18)) * 2^96
    # Simplifies to: sqrt(market_price / 10^12) * 2^96
    sqrt_value = math.sqrt((market_price * 10**6) / (10**18))
    sqrtPriceX96 = sqrt_value * (2**96)
    
    # Convert to integer as sqrtPriceX96 is typically represented as an integer
    return int(sqrtPriceX96)

def get_sqrtPriceX96():
    """
    Get the last price and calculate sqrtPriceX96.
    
    Returns:
        int/None: The calculated sqrtPriceX96 value or None if unable to get price
    """
    # Get the last price from IBKR
    last_price = get_last_price()
    
    if last_price is None:
        print("Error: Unable to get last price from IBKR")
        return None
    
    print(f"Retrieved last price: ${last_price}")
    
    # Calculate market_price (last_price / 1e6)
    market_price = last_price / 1e6
    print(f"Calculated market_price: ${market_price}")
    
    # Calculate sqrtPriceX96
    sqrtPriceX96 = calculate_sqrtPriceX96(last_price)
    print(f"Calculated sqrtPriceX96: {sqrtPriceX96}")
    
    return sqrtPriceX96

if __name__ == "__main__":
    sqrtPriceX96 = get_sqrtPriceX96()
    
    if sqrtPriceX96 is None:
        print("Failed to calculate sqrtPriceX96")
        sys.exit(1)
    
    # Print the final result
    print(f"\nFinal sqrtPriceX96: {sqrtPriceX96}")
    
    # Return the calculated value
    print(sqrtPriceX96)
    sys.exit(0) 