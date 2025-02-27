import requests
import json
import urllib3

# Disable SSL Warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def searchContract():
    base_url = "https://localhost:5000/v1/api/"
    
    # Step 1: Search for the base instrument
    search_endpoint = "iserver/secdef/search"
    search_body = {
        "symbol": "MCL",
        "secType": "FUT",
        "month": "APR25",
        "exchange": "NYMEX"
    }

    print("Step 1a: Searching for base contract...")
    search_req = requests.post(url=base_url+search_endpoint, json=search_body, verify=False)
    
    if not search_req.text:
        return None
        
    try:
        search_json = search_req.json()
        base_conid = None
        
        # Find the MCL instrument
        if isinstance(search_json, list):
            for contract in search_json:
                if (contract.get('symbol') == 'MCL' and 
                    any(section.get('secType') == 'FUT' and 
                        'APR25' in section.get('months', '') 
                        for section in contract.get('sections', []))):
                    base_conid = contract.get('conid')
                    break
        
        if not base_conid:
            return None
            
        # Step 2: Get the specific futures contract info
        info_endpoint = "iserver/secdef/info"
        params = {
            "conid": base_conid,
            "sectype": "FUT",
            "month": "APR25",
            "exchange": "NYMEX"
        }
        
        print("\nStep 1b: Getting specific futures contract...")
        info_req = requests.get(url=f"{base_url}{info_endpoint}", params=params, verify=False)
        
        if info_req.text:
            info_json = info_req.json()
            if isinstance(info_json, list) and len(info_json) > 0:
                futures_contract = info_json[0]
                if futures_contract.get('secType') == 'FUT':
                    return futures_contract.get('conid')
                    
    except json.JSONDecodeError as e:
        print("\nError parsing response:", e)
        
    return None

if __name__ == "__main__":
    conid = searchContract()
    if conid:
        print(f"\nFound futures contract ID: {conid}")
    else:
        print("\nCould not find futures contract") 