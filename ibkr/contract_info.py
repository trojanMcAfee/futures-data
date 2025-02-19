import requests
import json
import urllib3
from contract_search import searchContract

# Disable SSL Warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def getContractInfo(conid):
    base_url = "https://localhost:5000/v1/api/"
    endpoint = "iserver/secdef/info"

    # Parameters as specified in the documentation
    params = {
        "conid": conid,
        "sectype": "FUT",
        "month": "MAR25",
        "exchange": "NYMEX"
    }

    request_url = f"{base_url}{endpoint}"
    print("\nStep 2: Getting contract details...")
    print("Making request to URL:", request_url)
    print("With parameters:", json.dumps(params, indent=2))
    
    contract_req = requests.get(url=request_url, params=params, verify=False)
    print("\nInfo Response Status Code:", contract_req.status_code)
    print("\nRaw Response Text:")
    print(contract_req.text)
    
    if contract_req.text:
        try:
            contract_json = json.dumps(contract_req.json(), indent=2)
            print("\nParsed JSON Response:")
            print(contract_json)
        except json.JSONDecodeError as e:
            print("\nError parsing JSON response:", e)

if __name__ == "__main__":
    print("Starting contract information retrieval sequence...")
    print("\nStep 1: Searching for contract...")
    conid = searchContract()
    if conid:
        print(f"\nFound contract ID: {conid}")
        getContractInfo(conid)
    else:
        print("\nNo matching contract found") 