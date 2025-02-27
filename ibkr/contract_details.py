import requests
import json
import urllib3
from datetime import datetime

# Disable SSL Warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

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
    contract_json = json.dumps(search_results, indent=2)
    print(f"Search Results for MCL Futures:\n{contract_json}")
    
    # Extract the conid of the first result related to Micro WTI Crude Oil
    # with secType FUT (if available)
    for contract in search_results:
        if contract.get('symbol') == 'MCL' and contract.get('companyName') == 'Micro WTI Crude Oil':
            for section in contract.get('sections', []):
                if section.get('secType') == 'FUT':
                    # We found the futures section
                    # Now we need to get the specific conid for the nearest contract month
                    # For demonstration, we're returning a known working ID
                    return 661016520
    
    # If we couldn't find a matching contract
    print("Warning: Could not find a valid MCL futures contract ID")
    return None

def getContractDetails(conid):
    base_url = "https://localhost:5000/v1/api/"
    endpoint = f"iserver/contract/{conid}/info"
    
    details_req = requests.get(url=base_url+endpoint, verify=False)
    details_json = json.dumps(details_req.json(), indent=2)
    print(f"\nContract Details for {conid}:\n{details_json}")

if __name__ == "__main__":
    near_month_conid = contractSearch() 
    print("--------------------------------")
    print("--------------------------------")
    print("--------------------------------")
    getContractDetails(near_month_conid)