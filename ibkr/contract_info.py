import requests
import json
import urllib3

# Disable SSL Warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def searchContract():
    base_url = "https://localhost:5000/v1/api/"
    endpoint = "iserver/secdef/search"
    
    # Search for MCL (Micro WTI Crude Oil) futures
    json_body = {
        "symbol": "MCL",
        "secType": "FUT",
        "month": "MAR25",
        "exchange": "NYMEX"
    }
    
    search_req = requests.post(url=base_url+endpoint, verify=False, json=json_body)
    search_json = search_req.json()
    print("\nSearch Results:")
    print(json.dumps(search_json, indent=2))
    
    # Look for the specific futures contract
    if isinstance(search_json, list):
        for contract in search_json:
            sections = contract.get('sections', [])
            for section in sections:
                if (section.get('secType') == 'FUT' and 
                    section.get('exchange') == 'NYMEX' and 
                    'MAR25' in section.get('months', '')):
                    return contract.get('conid'), section
    return None, None

def getContractDetails(conid):
    base_url = "https://localhost:5000/v1/api/"
    endpoint = f"iserver/contract/{conid}/info"

    request_url = base_url + endpoint
    contract_req = requests.get(url=request_url, verify=False)
    contract_json = json.dumps(contract_req.json(), indent=2)

    print("\nRequest URL:", request_url)
    print("\nResponse Status:", contract_req)
    print("\nContract Information:")
    print(contract_json)

if __name__ == "__main__":
    print("Searching for MCL March 2025 contract...")
    conid, section = searchContract()
    if conid:
        print(f"\nFound contract ID: {conid}")
        print("\nFutures Section Information:")
        print(json.dumps(section, indent=2))
        getContractDetails(conid)
    else:
        print("\nNo matching contract found") 