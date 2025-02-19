import requests
import json
import urllib3

# Disable SSL Warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def acctSum():
    base_url = "https://localhost:5000/v1/api/"
    endpoint = "portfolio/DUH210440/summary"
    
    request_url = f"{base_url}{endpoint}"
    print("\nQuerying account summary...")
    print("Making request to URL:", request_url)
    
    try:
        summary_req = requests.get(url=request_url, verify=False)
        print("\nSummary Response Status Code:", summary_req.status_code)
        
        if summary_req.status_code == 200:
            summary_data = summary_req.json()
            print("\nAccount Summary:")
            print(json.dumps(summary_data, indent=2))
            return summary_data
        else:
            print(f"\nError: Received status code {summary_req.status_code}")
            print("Response text:", summary_req.text)
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"\nError making request: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"\nError parsing JSON response: {e}")
        return None

def acctPos():
    base_url = "https://localhost:5000/v1/api/"
    endpoint = "portfolio/DUH210440/positions/0"
    
    request_url = f"{base_url}{endpoint}"
    print("\nQuerying positions information...")
    print("Making request to URL:", request_url)
    
    try:
        pos_req = requests.get(url=request_url, verify=False)
        print("\nPositions Response Status Code:", pos_req.status_code)
        
        if pos_req.status_code == 200:
            pos_json = json.dumps(pos_req.json(), indent=2)
            print("\nPositions Data:")
            print(pos_json)
            return pos_req.json()
        else:
            print(f"\nError: Received status code {pos_req.status_code}")
            print("Response text:", pos_req.text)
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"\nError making request: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"\nError parsing JSON response: {e}")
        return None

def acctPosSingle(conid=661016571):
    base_url = "https://localhost:5000/v1/api/"
    endpoint = f"portfolio/DUH210440/position/{conid}"
    
    request_url = f"{base_url}{endpoint}"
    print(f"\nQuerying position details for conid {conid}...")
    print("Making request to URL:", request_url)
    
    try:
        pos_req = requests.get(url=request_url, verify=False)
        print("\nPosition Details Response Status Code:", pos_req.status_code)
        
        if pos_req.status_code == 200:
            pos_json = json.dumps(pos_req.json(), indent=2)
            print("\nPosition Details:")
            print(pos_json)
            return pos_req.json()
        else:
            print(f"\nError: Received status code {pos_req.status_code}")
            print("Response text:", pos_req.text)
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"\nError making request: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"\nError parsing JSON response: {e}")
        return None

if __name__ == "__main__":
    print("Starting account information retrieval...")
    # print("\n=== Account Summary ===")
    # acctSum()
    # print("\n=== Account Positions ===")
    # acctPos()
    print("\n=== Single Position Details ===")
    acctPosSingle() 