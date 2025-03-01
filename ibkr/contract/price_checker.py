"""
This module retrieves the current trading price of the near-month MCL futures contract.
It uses the contractSearch function from details.py to identify the appropriate contract,
then queries the IBKR API for current market data.
"""

import requests
import json
import urllib3
from details import contractSearch

# Disable SSL Warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_market_data(conid):
    """
    Get current market data for a specific contract ID.
    
    Args:
        conid (int): The contract ID to fetch market data for
        
    Returns:
        dict: Market data information including price, if successful
        None: If there was an error
    """
    base_url = "https://localhost:5000/v1/api/"
    endpoint = f"iserver/marketdata/snapshot"
    
    # Request more fields to get comprehensive data
    # 31=Last Price, 84=Bid, 86=Ask, 6509=Market Data Availability, 7085=Put/Call Interest
    # 87=Volume, 70=High, 71=Low, 6004=Exchange
    params = {
        "conids": str(conid),
        "fields": "31,84,86,6509,87,70,71,6004,85"
    }
    
    request_url = f"{base_url}{endpoint}"
    print(f"\nRetrieving market data for contract ID {conid}...")
    print("Making request to URL:", request_url)
    print("With parameters:", params)
    
    try:
        market_req = requests.get(url=request_url, params=params, verify=False)
        print("\nMarket Data Response Status Code:", market_req.status_code)
        
        if market_req.status_code == 200:
            market_data = market_req.json()
            # Print the raw response for debugging
            print("\nRaw response:", json.dumps(market_data, indent=2))
            return market_data
        else:
            print(f"\nError: Received status code {market_req.status_code}")
            print("Response text:", market_req.text)
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"\nError making request: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"\nError parsing JSON response: {e}")
        return None

def check_market_data_availability(market_data):
    """
    Check the market data availability code to diagnose issues.
    
    Args:
        market_data (list/dict): Market data response from the IBKR API
        
    Returns:
        str: Market data availability status information
    """
    if not market_data or not isinstance(market_data, list) or len(market_data) == 0:
        return "No market data available"
    
    availability_code = market_data[0].get('6509', None)
    
    if not availability_code:
        return "Market data availability information not provided in response"
    
    availability_info = []
    
    if availability_code[0:1] == 'R':
        availability_info.append("RealTime data available")
    elif availability_code[0:1] == 'D':
        availability_info.append("Delayed data available (15-20 min delay)")
    elif availability_code[0:1] == 'Z':
        availability_info.append("Frozen data available (last recorded at market close)")
    elif availability_code[0:1] == 'Y':
        availability_info.append("Frozen delayed data available")
    elif availability_code[0:1] == 'N':
        availability_info.append("Not subscribed to required market data")
    
    if len(availability_code) > 1 and availability_code[1:2] == 'P':
        availability_info.append("Snapshot data available")
    elif len(availability_code) > 1 and availability_code[1:2] == 'p':
        availability_info.append("Consolidated data available")
    
    if len(availability_code) > 2 and availability_code[2:3] == 'B':
        availability_info.append("Book data available")
    
    if not availability_info:
        return f"Unknown availability code: {availability_code}"
    
    return ", ".join(availability_info)

def display_price_info(market_data):
    """
    Display formatted price information from the market data response.
    
    Args:
        market_data (list/dict): Market data response from the IBKR API
        
    Returns:
        float: The last price if available, or 70.415 if 'N/A'
    """
    if not market_data:
        print("No market data available to display.")
        print("Using default price value: 70.415")
        return 70.415
    
    # First check market data availability
    availability_info = check_market_data_availability(market_data)
    print(f"\nMarket Data Availability: {availability_info}")
        
    print("\n=== Contract Price Information ===")
    
    # The API usually returns a list with a single item containing the snapshot data
    if isinstance(market_data, list) and len(market_data) > 0:
        contract_data = market_data[0]
        
        # Extract price information
        last_price = contract_data.get('31', 'N/A')  # Last price
        bid_price = contract_data.get('84', 'N/A')   # Bid
        ask_price = contract_data.get('86', 'N/A')   # Ask
        high_price = contract_data.get('70', 'N/A')  # High
        low_price = contract_data.get('71', 'N/A')   # Low
        volume = contract_data.get('87', 'N/A')      # Volume
        exchange = contract_data.get('6004', 'N/A')  # Exchange
        ask_size = contract_data.get('85', 'N/A')    # Ask Size
        
        # Display formatted information
        print(f"Symbol: {contract_data.get('symbol', 'Unknown')}")
        print(f"Contract ID: {contract_data.get('conid', 'Unknown')}")
        print(f"Description: {contract_data.get('company_name', 'Unknown Contract')}")
        print(f"Exchange: {exchange}")
        print(f"Last Price: ${last_price}")
        print(f"Bid Price: ${bid_price}")
        print(f"Ask Price: ${ask_price}")
        print(f"Ask Size: {ask_size}")
        print(f"High: ${high_price}")
        print(f"Low: ${low_price}")
        print(f"Volume: {volume}")
        
        # Check if we have valid price data
        has_price_data = (
            last_price != 'N/A' or
            bid_price != 'N/A' or
            ask_price != 'N/A'
        )
        
        if not has_price_data:
            print("\nNo price data available. Possible reasons:")
            print("1. You may not have the required market data subscription")
            print("2. The market for this contract may be closed")
            print("3. The contract ID may be outdated or no longer active")
            print("4. IBKR Gateway may need to be restarted")
            print("\nSuggested actions:")
            print("1. Check your market data subscriptions in IBKR Trader Workstation")
            print("2. Verify the contract is still active")
            print("3. Try restarting the IBKR Gateway")
            print("\nUsing default price value: 70.415")
            return 70.415
        
        # Convert last_price to float if it's not 'N/A'
        if last_price != 'N/A':
            try:
                return float(last_price)
            except (ValueError, TypeError):
                print(f"Warning: Could not convert last_price '{last_price}' to float")
                print("Using default price value: 70.415")
                return 70.415
        else:
            print("Last price value is 'N/A'")
            print("Using default price value: 70.415")
            return 70.415
    else:
        print("Market data format unexpected:", json.dumps(market_data, indent=2))
        print("Using default price value: 70.415")
        return 70.415

def get_gateway_status():
    """
    Check the status of the IBKR Gateway.
    
    Returns:
        dict: Status information from the gateway
    """
    base_url = "https://localhost:5000/v1/api/"
    endpoint = "iserver/auth/status"
    
    print("\nChecking IBKR Gateway status...")
    
    try:
        status_req = requests.get(url=f"{base_url}{endpoint}", verify=False)
        
        if status_req.status_code == 200:
            status_data = status_req.json()
            return status_data
        else:
            print(f"Error checking gateway status: {status_req.status_code}")
            return None
    except Exception as e:
        print(f"Error checking gateway status: {e}")
        return None

def get_last_price():
    """
    Get the last price of the near-month futures contract.
    
    Returns:
        float: The last price if available, or 70.415 as default value
    """
    print("Starting price check for near-month futures contract...")
    
    # First check the gateway status
    gateway_status = get_gateway_status()
    if gateway_status:
        print("\nIBKR Gateway Status:")
        print(f"Authenticated: {gateway_status.get('authenticated', False)}")
        print(f"Connected: {gateway_status.get('connected', False)}")
        
        if not gateway_status.get('authenticated', False):
            print("\nERROR: Not authenticated with IBKR Gateway. Please log in to IBKR Trader Workstation or IBKR Gateway.")
            print("\nUsing default price value: 70.415")
            return 70.415
        
        if not gateway_status.get('connected', False):
            print("\nERROR: Not connected to IBKR Gateway. Please ensure IBKR Trader Workstation or IBKR Gateway is running.")
            print("\nUsing default price value: 70.415")
            return 70.415
    
    # Get the near-month contract ID
    print("\nStep 1: Identifying near-month futures contract...")
    conid = contractSearch()
    
    if not conid:
        print("\nError: Could not find contract ID")
        print("Using default price value: 70.415")
        return 70.415
    
    print(f"\nFound near-month contract ID: {conid}")
    
    # Get market data for the contract
    print("\nStep 2: Retrieving current price information...")
    market_data = get_market_data(conid)
    
    # Display the price information and get the last price
    last_price = display_price_info(market_data)
    
    # Since display_price_info now always returns a value (either actual price or 70.415),
    # we don't need to check for None anymore
    print(f"\nUsing price: ${last_price}")
    
    return last_price

if __name__ == "__main__":
    last_price = get_last_price()
    print(f"Final last price: ${last_price}")
    exit(0)  # Success 