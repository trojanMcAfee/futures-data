import requests
import json
import urllib3
from contract_search import searchContract

# Disable SSL Warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def placeOrder(conid):
    base_url = "https://localhost:5000/v1/api/"
    endpoint = "iserver/account/DUH210440/orders"  # Using the account from the screenshot

    # Order parameters
    json_body = {
        "orders": [{
            "conid": int(conid),  # Convert to integer
            "orderType": "MKT",
            "side": "BUY",
            "tif": "DAY",
            "quantity": 1
        }]
    }

    request_url = base_url + endpoint
    print("\nStep 2: Submitting order...")
    print("Making request to URL:", request_url)
    print("With order details:", json.dumps(json_body, indent=2))
    
    order_req = requests.post(url=request_url, json=json_body, verify=False)
    print("\nOrder Response Status Code:", order_req.status_code)
    print("Order Response Text:", order_req.text)
    
    if order_req.text:
        try:
            response = order_req.json()
            # Check if we got an order reply message that needs confirmation
            if isinstance(response, list) and len(response) > 0 and 'id' in response[0]:
                return 'needs_confirmation', response[0]['id']
            # Check if we got a direct order confirmation
            elif isinstance(response, dict) and 'order_id' in response:
                return 'confirmed', response['order_id']
            else:
                return 'error', 'Unexpected response format'
        except json.JSONDecodeError as e:
            return 'error', f'Error parsing response: {e}'
    return 'error', 'No response received'

def confirmOrder(reply_id):
    base_url = "https://localhost:5000/v1/api/"
    endpoint = f"iserver/reply/{reply_id}"

    json_body = {"confirmed": True}

    request_url = base_url + endpoint
    print("\nStep 3: Confirming order...")
    print("Making request to URL:", request_url)
    
    reply_req = requests.post(url=request_url, json=json_body, verify=False)
    print("\nConfirmation Response Status Code:", reply_req.status_code)
    print("Confirmation Response Text:", reply_req.text)
    
    if reply_req.text:
        try:
            response = reply_req.json()
            if isinstance(response, dict) and 'order_status' in response:
                return True, response['order_status']
            else:
                return False, 'Unexpected confirmation response format'
        except json.JSONDecodeError as e:
            return False, f'Error parsing confirmation response: {e}'
    return False, 'No confirmation response received'

if __name__ == "__main__":
    print("Starting order submission sequence...")
    print("\nStep 1: Getting contract ID...")
    conid = searchContract()
    
    if not conid:
        print("\nError: Could not find contract ID for MCL March 2025")
        exit(1)
    
    print(f"\nFound contract ID: {conid}")
    status, result = placeOrder(conid)
    
    if status == 'needs_confirmation':
        print("\nOrder needs confirmation. Reply ID:", result)
        success, message = confirmOrder(result)
        if success:
            print(f"\nOrder successfully submitted and confirmed! Status: {message}")
        else:
            print(f"\nError confirming order: {message}")
    elif status == 'confirmed':
        print(f"\nOrder successfully submitted! Order ID: {result}")
    else:
        print(f"\nError placing order: {result}") 