import json
import glob
from decimal import Decimal

def format_rate(rate_str):
    # Convert the large number string to a decimal and divide by 10^18
    rate_decimal = Decimal(rate_str) / Decimal('1000000000000000000')
    # Format to 4 decimal places
    return f"{rate_decimal:.4f}"

def process_reth_files():
    # Read the main prices file
    with open('data/reth_prices.json', 'r') as f:
        prices_data = json.load(f)

    # Process each month's file
    months = ['january', 'february', 'march', 'april', 'may', 'june', 
             'july', 'august', 'september', 'october', 'november', 'december']

    for month in months:
        try:
            # Read the monthly file
            with open(f'data/reth_{month}.json', 'r') as f:
                month_data = json.load(f)

            # Update the main prices file for this month
            for i, daily_data in enumerate(month_data):
                if i < len(prices_data[month]):  # Ensure we don't go out of bounds
                    # Update block and rate, keeping timestamp and unix
                    prices_data[month][i]['block'] = daily_data['block']
                    # Format the rate to 4 decimal places
                    formatted_rate = format_rate(daily_data['rate'])
                    prices_data[month][i]['rate'] = formatted_rate

        except FileNotFoundError:
            print(f"Warning: Could not find data/reth_{month}.json")
            continue

    # Save the updated data back to reth_prices.json
    with open('data/reth_prices.json', 'w') as f:
        json.dump(prices_data, f, indent=2)

if __name__ == "__main__":
    process_reth_files() 