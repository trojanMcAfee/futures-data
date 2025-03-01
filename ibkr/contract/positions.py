import requests
import json
import urllib3
from details import contractSearch

# Disable SSL Warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def acctPosSingle():
    conid = contractSearch()
    
    base_url = "https://localhost:5000/v1/api/"
    endpoint = f"portfolio/DUH210440/position/{conid}"
    
    request_url = f"{base_url}{endpoint}"
    print(f"\nQuerying position details for conid {conid}...")
    print("Making request to URL:", request_url)

    print("--------------------------------")
    print("--------------------------------")
    print("--------------------------------")
    
    try:
        pos_req = requests.get(url=request_url, verify=False)
        print("\nPosition Details Response Status Code:", pos_req.status_code)
        
        if pos_req.status_code == 200:
            position_data = pos_req.json()
            
            # Check if position_data is a list
            if isinstance(position_data, list):
                print("\nPosition Details (list format):")
                filtered_positions = []
                
                for position in position_data:
                    # Check if we should include this position (if it has non-zero amounts)
                    include_position = True
                    for key, value in position.items():
                        if isinstance(value, dict) and 'amount' in value and value['amount'] == 0.0:
                            include_position = False
                            break
                    
                    if include_position:
                        filtered_positions.append(position)
                
                print(json.dumps(filtered_positions, indent=2))
                return position_data
            
            # If it's not a list, try processing as a dictionary
            elif isinstance(position_data, dict):
                # Filter out elements with "amount: 0.0" if they exist in the position data
                filtered_data = {}
                for key, value in position_data.items():
                    if isinstance(value, dict) and 'amount' in value and value['amount'] != 0.0:
                        filtered_data[key] = value
                    elif not isinstance(value, dict) or 'amount' not in value:
                        filtered_data[key] = value
                
                print("\nPosition Details (filtered to exclude zero amounts):")
                print(json.dumps(filtered_data, indent=2))
                return position_data
            
            # If it's neither a list nor a dictionary, just print the raw data
            else:
                print("\nPosition Details (raw format):")
                print(json.dumps(position_data, indent=2))
                return position_data
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
    print("Starting single position information retrieval...")
    acctPosSingle() 