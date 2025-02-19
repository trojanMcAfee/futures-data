import requests
import json
import urllib3

# Disable SSL Warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def searchContract():
    base_url = "https://localhost:5000/v1/api/"
    endpoint = "iserver/secdef/search"

    # Search for MCL futures
    json_body = {
        "symbol": "MCL",
        "secType": "FUT",
        "month": "MAR25"
    }

    print("Making search request with body:", json.dumps(json_body, indent=2))
    search_req = requests.post(url=base_url+endpoint, verify=False, json=json_body)
    print("\nResponse Status Code:", search_req.status_code)
    print("\nRaw Response Text:")
    print(search_req.text)
    
    if search_req.text:
        try:
            search_json = search_req.json()
            print("\nParsed JSON Response:")
            print(json.dumps(search_json, indent=2))
            
            # Return the conid if we find a matching contract
            if isinstance(search_json, list):
                for contract in search_json:
                    if (contract.get('symbol') == 'MCL' and 
                        any(section.get('secType') == 'FUT' and 
                            'MAR25' in section.get('months', '') 
                            for section in contract.get('sections', []))):
                        return contract.get('conid')
        except json.JSONDecodeError as e:
            print("\nError parsing JSON response:", e)
    return None

if __name__ == "__main__":
    searchContract() 