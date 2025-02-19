import requests
import json
import urllib3
from acctSummary import acctSum
from contract_order import placeOrder, confirmOrder
from contract_search import searchContract

# Disable SSL Warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def main():
    print("\n=== Initial Account Summary ===")
    initial_summary = acctSum()
    
    print("\n=== Placing Order ===")
    print("Step 1: Getting contract ID...")
    conid = searchContract()
    
    if not conid:
        print("\nError: Could not find contract ID")
        return
    
    print(f"\nFound contract ID: {conid}")
    status, result = placeOrder(conid)
    
    if status == 'needs_confirmation':
        print("\nOrder needs confirmation. Reply ID:", result)
        success, message = confirmOrder(result)
        if success:
            if isinstance(message, dict):
                print(f"\nOrder successfully submitted!")
                print(f"Order ID: {message['order_id']}")
                print(f"Status: {message['status']}")
            else:
                print(f"\nOrder successfully submitted! Status: {message}")
        else:
            print(f"\nError confirming order: {message}")
            return
    elif status == 'pre_submitted':
        print(f"\nOrder successfully submitted!")
        print(f"Order ID: {result['order_id']}")
        print(f"Status: {result['status']}")
    elif status == 'confirmed':
        print(f"\nOrder successfully submitted! Order ID: {result}")
    else:
        print(f"\nError placing order: {result}")
        return
    
    print("\n=== Final Account Summary ===")
    final_summary = acctSum()

if __name__ == "__main__":
    main() 