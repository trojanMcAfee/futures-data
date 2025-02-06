import json
import glob
from decimal import Decimal

# Read the main reth_prices.json file
with open('data/reth_prices.json', 'r') as f:
    reth_prices = json.load(f)

# Get all monthly Uniswap rate files
monthly_files = glob.glob('data/reth_uni_*.json')

# Process each monthly file
for monthly_file in monthly_files:
    # Extract month name from filename
    month = monthly_file.split('_')[-1].split('.')[0]
    
    # Read the monthly Uniswap rates
    with open(monthly_file, 'r') as f:
        uni_rates = json.load(f)
    
    # Create a mapping of block numbers to formatted uni rates
    block_to_rate = {}
    for rate_data in uni_rates:
        # Format uni_rate by dividing by 1e18 and keeping 4 decimals
        uni_rate = Decimal(rate_data['uni_rate']) / Decimal('1000000000000000000')
        formatted_rate = f"{uni_rate:.4f}"
        block_to_rate[rate_data['block']] = formatted_rate
    
    # Update the corresponding month in reth_prices
    if month in reth_prices:
        for entry in reth_prices[month]:
            block = entry['block']
            if block in block_to_rate:
                # Rename 'rate' to 'nav_rate'
                entry['nav_rate'] = entry.pop('rate')
                # Add the uni_rate
                entry['uni_rate'] = block_to_rate[block]

# Write the updated data back to reth_prices.json
with open('data/reth_prices.json', 'w') as f:
    json.dump(reth_prices, f, indent=2) 