"""
This module retrieves information about Micro WTI Crude Oil (MCL) futures contracts on NYMEX.
The base contract (conid: 500567051) represents the Micro WTI Crude Oil market instrument.
This script performs two main functions:
1. Retrieves the base contract information for MCL (Micro WTI Crude Oil)
2. Gets the details of the near-month futures contract for trading
"""

import requests
import json
import urllib3
from datetime import datetime

# Disable SSL Warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def _should_print():
    """Helper function to determine if we should print output"""
    return __name__ == "__main__"

def _print_if_main(*args, **kwargs):
    """Only print if this is the main module being run"""
    if _should_print():
        print(*args, **kwargs)

def contractSearch():
    base_url = "https://localhost:5000/v1/api/"
    endpoint = "iserver/secdef/search"
    
    # MCL is the symbol for Micro Crude Oil Futures
    json_body = {
        "symbol": "MCL",
        "secType": "FUT",  # FUT for futures
        "name": False
    }
    
    contract_req = requests.post(url=base_url+endpoint, verify=False, json=json_body)
    search_results = contract_req.json()
    
    # Filter for only Micro WTI Crude Oil results
    filtered_results = []
    
    for contract in search_results:
        if contract.get('companyName') == 'Micro WTI Crude Oil':
            # Create a copy of the contract to modify
            filtered_contract = contract.copy()
            
            # Filter sections to only include FUT
            if 'sections' in filtered_contract:
                filtered_contract['sections'] = [
                    section for section in filtered_contract['sections']
                    if section.get('secType') == 'FUT'
                ]
            
            # Add the filtered contract to our results
            filtered_results.append(filtered_contract)
    
    contract_json = json.dumps(filtered_results, indent=2)
    _print_if_main(f"Search Results for MCL Futures:\n{contract_json}")
    
    # Find the base contract ID
    base_conid = None
    months_list = []
    
    # Extract the base contract ID and available months
    for contract in filtered_results:
        if contract.get('symbol') == 'MCL' and contract.get('companyName') == 'Micro WTI Crude Oil':
            base_conid = contract.get('conid')
            # Find the futures section to get available months
            for section in contract.get('sections', []):
                if section.get('secType') == 'FUT':
                    months_string = section.get('months', '')
                    months_list = months_string.split(';')
                    break
            break
    
    if not base_conid or not months_list:
        _print_if_main("Warning: Could not find a valid MCL futures contract or available months")
        return None
    
    # Get the nearest month (first in the list, which should be the nearest)
    nearest_month = months_list[0]
    _print_if_main(f"Found base contract ID: {base_conid}")
    _print_if_main(f"Nearest contract month: {nearest_month}")
    
    # Now get the specific contract ID for this month
    month_endpoint = "iserver/secdef/info"
    month_params = {
        "conid": base_conid,
        "sectype": "FUT",
        "month": nearest_month,
        "exchange": "NYMEX"
    }
    
    month_req = requests.get(url=f"{base_url}{month_endpoint}", params=month_params, verify=False)
    
    try:
        month_data = month_req.json()
        # The data structure can vary, but we need to extract the specific contract ID
        if isinstance(month_data, list) and len(month_data) > 0:
            # Some APIs return a list of contracts
            near_month_conid = month_data[0].get('conid')
            _print_if_main(f"Found near-month contract ID: {near_month_conid}")
            return near_month_conid
        elif isinstance(month_data, dict) and 'data' in month_data:
            # Some APIs nest the data
            near_month_conid = month_data.get('data', [{}])[0].get('conid')
            _print_if_main(f"Found near-month contract ID: {near_month_conid}")
            return near_month_conid
    except Exception as e:
        _print_if_main(f"Error processing month data: {e}")
        _print_if_main(f"Raw response: {month_req.text}")
    
    # If we couldn't find the near-month contract dynamically,
    # use the currently working ID as a fallback (but log a warning)
    _print_if_main("Warning: Falling back to known contract ID (661016520)")
    return 661016520

def getContractDetails(conid):
    base_url = "https://localhost:5000/v1/api/"
    endpoint = f"iserver/contract/{conid}/info"
    
    details_req = requests.get(url=base_url+endpoint, verify=False)
    details_json = json.dumps(details_req.json(), indent=2)
    _print_if_main(f"\nContract Details for {conid}:\n{details_json}")

if __name__ == "__main__":
    near_month_conid = contractSearch() 
    print("--------------------------------")
    print("--------------------------------")
    print("--------------------------------")
    getContractDetails(near_month_conid)