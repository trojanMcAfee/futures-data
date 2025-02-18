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
    contract_json = json.dumps(contract_req.json(), indent=2)
    print(f"Search Results for MCL Futures:\n{contract_json}")

def getContractDetails(conid):
    base_url = "https://localhost:5000/v1/api/"
    endpoint = f"iserver/contract/{conid}/info"
    
    details_req = requests.get(url=base_url+endpoint, verify=False)
    details_json = json.dumps(details_req.json(), indent=2)
    print(f"\nContract Details for {conid}:\n{details_json}")

if __name__ == "__main__":
    contractSearch() 