import requests
import json
import urllib3
from details import contractSearch

# Disable SSL Warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def placeOrder(conid):
    base_url = "https://localhost:5000/v1/api/"
    endpoint = "iserver/account/DUH210440/orders" 

    # Order parameters 
    json_body = {
        "orders": [{
            "conid": int(conid),  
            "orderType": "MKT",
            "side": "SELL",
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
            if isinstance(response, list) and len(response) > 0:
                if 'id' in response[0]:
                    # This is a confirmation request
                    return 'needs_confirmation', response[0]['id']
                elif 'order_id' in response[0]:
                    # This is a pre-submitted order
                    return 'pre_submitted', {
                        'order_id': response[0]['order_id'],
                        'status': response[0].get('order_status', 'Unknown')
                    }
            # Check if we got a direct order confirmation
            elif isinstance(response, dict) and 'order_id' in response:
                return 'confirmed', response['order_id']
            
            return 'error', f'Unexpected response format: {response}'
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
            
            # Handle list response format (which seems to be what we get from IBKR)
            if isinstance(response, list) and len(response) > 0:
                order_info = response[0]
                if 'order_id' in order_info and 'order_status' in order_info:
                    status = order_info['order_status']
                    # PreSubmitted is a valid status for market orders
                    if status == "PreSubmitted":
                        return True, {
                            'order_id': order_info['order_id'],
                            'status': status
                        }
                elif 'message' in order_info:
                    return False, f'Received error message: {order_info.get("message")}'
            
            # Also handle direct dict response format (as shown in docs)
            elif isinstance(response, dict):
                if 'order_id' in response and 'order_status' in response:
                    status = response['order_status']
                    if status in ["Submitted", "PreSubmitted"]:
                        return True, {
                            'order_id': response['order_id'],
                            'status': status
                        }
            
            return False, f'Unexpected confirmation response format: {response}'
        except json.JSONDecodeError as e:
            return False, f'Error parsing confirmation response: {e}'
    return False, 'No confirmation response received'

if __name__ == "__main__":
    print("Starting order submission sequence...")
    print("\nStep 1: Getting contract ID...")
    conid = contractSearch()
    
    if not conid:
        print("\nError: Could not find contract ID")
        exit(1)
    
    print(f"\nFound contract ID: {conid}")
    status, result = placeOrder(conid)
    
    if status == 'needs_confirmation':
        print("\nOrder needs confirmation. Reply ID:", result)
        success, message = confirmOrder(result)
        if success:
            if isinstance(message, dict):
                print(f"\nOrder successfully submitted!")
                print(f"Order ID: {message['order_id']}")
                print(f"Status: {message['status']} (this is normal for market orders)")
            else:
                print(f"\nOrder successfully submitted! Status: {message}")
        else:
            print(f"\nError confirming order: {message}")
    elif status == 'pre_submitted':
        print(f"\nOrder successfully submitted!")
        print(f"Order ID: {result['order_id']}")
        print(f"Status: {result['status']} (this is normal for market orders)")
    elif status == 'confirmed':
        print(f"\nOrder successfully submitted! Order ID: {result}")
    else:
        print(f"\nError placing order: {result}") 