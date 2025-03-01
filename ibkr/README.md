# IBKR API Gateway and Utilities

This directory contains the Interactive Brokers Client Portal Gateway and Python utilities for interacting with the IBKR API.

## Directory Structure

- `account/` - Contains scripts for account-related operations
- `contract/` - Contains scripts for contract-related operations and trading
- `clientportal.gw/` - The IBKR Client Portal Gateway

## Starting the Gateway

To use the IBKR API, you need to start the Client Portal Gateway:

1. Open a terminal and navigate to the clientportal.gw directory:
   ```bash
   cd clientportal.gw
   ```

2. Start the gateway by running the shell script with the configuration file:
   ```bash
   bin/run.sh root/conf.yaml
   ```
   
   For Windows users:
   ```cmd
   bin\run.bat root\conf.yaml
   ```

3. Once the gateway is running, you should see the message "Server listening on port 5000" in the console.

4. To authenticate, open your browser and go to:
   ```
   https://localhost:5000/
   ```

5. Log in with your Interactive Brokers credentials.

6. After successful authentication, you can close the browser window. The gateway will continue running.

7. The API endpoints will now be accessible at `https://localhost:5000/v1/api/`.

## Checking Gateway Status

You can check the authentication status of the gateway by running:

```bash
python account/auth_status.py
```

This script will make a request to the gateway's authentication status endpoint and display the response.

## Python Utilities

### Account Scripts

Located in the `account/` directory:

- `auth_status.py` - Check the authentication status of the gateway
- `acctSummary.py` - Retrieve account summary information. Output includes values with suffixes that indicate different account segments:
  - `-c`: Commodities segment (futures, options on futures)
  - `-s`: Securities segment (stocks, ETFs, options on stocks)
  
  Example output snippet:
  ```json
  {
    "availablefunds": {
      "amount": 828217.375,
      "currency": "USD"
    },
    "availablefunds-c": {
      "amount": 584364.625,
      "currency": "USD"
    },
    "availablefunds-s": {
      "amount": 243852.71875,
      "currency": "USD"
    }
  }
  ```

### Contract Scripts

Located in the `contract/` directory:

- `details.py` - Retrieves information about Micro WTI Crude Oil (MCL) futures contracts on NYMEX. It identifies the base contract (conid: 500567051) and dynamically determines the near-month futures contract for trading, filtering results to show only futures (FUT) contracts.
- `order.py` - Place orders for financial contracts
- `positions.py` - Retrieve position information for a specific contract
- `price_checker.py` - Queries and displays the current trading price of the near-month futures contract, showing last price, bid and ask prices

### Other Scripts

- `mixed.py` - Mixed API functionality examples
- `sqrtprice_calculator.py` - Calculates the `sqrtPriceX96` value based on the current market price of a futures contract

## sqrtPriceX96 Calculator

This utility calculates the `sqrtPriceX96` value based on the current market price of a futures contract from IBKR.

### Overview

The calculation follows these steps:

1. Retrieve the `last_price` from IBKR for a specific futures contract
2. Calculate `market_price` = `last_price` / 1,000,000
3. Apply the formula: `sqrtPriceX96` = sqrt((market_price * 10^6) / (10^18)) * 2^96

This value is commonly used in Uniswap V3-style liquidity pools for determining price ranges.

### Usage

1. Ensure the IBKR Gateway is running and you're authenticated
2. Activate your Python virtual environment:
   ```bash
   source venv/bin/activate
   ```
3. Run the script:
   ```bash
   python ibkr/sqrtprice_calculator.py
   ```

The script will:
- Connect to IBKR
- Identify the near-month futures contract
- Retrieve the current price
- Calculate and output the `sqrtPriceX96` value

### Programmatic Usage

You can also import and use this in your own Python code:

```python
from ibkr.sqrtprice_calculator import get_sqrtPriceX96

# Get the calculated sqrtPriceX96 value
sqrtPriceX96 = get_sqrtPriceX96()

if sqrtPriceX96 is not None:
    print(f"The sqrtPriceX96 value is: {sqrtPriceX96}")
else:
    print("Failed to calculate sqrtPriceX96")
```

## Prerequisites

- Python 3.x with the `requests` package installed
- Java 1.8 update 192 or higher (for the gateway)

## Additional Resources

For more detailed technical information about the Client Portal Gateway, refer to:
- `clientportal.gw/doc/GettingStarted.md`

For API documentation, visit:
- [IBKR Client Portal API Guide](https://interactivebrokers.github.io/cpwebapi)
- [API Specification](https://gdcdyn.interactivebrokers.com/portal.proxy/v1/portal/swagger/swagger?format=yaml)

## Note

The gateway requires re-authentication regularly (typically daily). If you experience authentication issues, restart the gateway and re-authenticate through the browser.