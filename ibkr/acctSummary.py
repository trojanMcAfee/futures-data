import requests
import json
import urllib3
from contract_details import contractSearch

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
            
            # Filter out elements with "amount: 0.0"
            filtered_data = {}
            for key, value in summary_data.items():
                if isinstance(value, dict) and 'amount' in value and value['amount'] != 0.0:
                    filtered_data[key] = value
            
            print("\nAccount Summary (filtered to exclude zero amounts):")
            print(json.dumps(filtered_data, indent=2))
            return summary_data  # Return the original data for further processing if needed
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
            positions_data = pos_req.json()
            
            # Filter out elements with "amount: 0.0" if they exist in the positions data
            filtered_positions = []
            for position in positions_data:
                # Check if position has nested dictionaries with 'amount' field
                include_position = True
                for key, value in position.items():
                    if isinstance(value, dict) and 'amount' in value and value['amount'] == 0.0:
                        include_position = False
                        break
                
                if include_position:
                    filtered_positions.append(position)
            
            print("\nPositions Data (filtered to exclude zero amounts):")
            print(json.dumps(filtered_positions, indent=2))
            return positions_data  # Return the original data for further processing if needed
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
    print("\n=== Account Summary ===")
    acctSum()
    # print("\n=== Account Positions ===")
    # acctPos()