# IBKR API Gateway and Utilities

This directory contains the Interactive Brokers Client Portal Gateway and Python utilities for interacting with the IBKR API.

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
python auth_status.py
```

This script will make a request to the gateway's authentication status endpoint and display the response.

## Python Utilities

This directory contains several Python scripts for interacting with the IBKR API:

- `auth_status.py` - Check the authentication status of the gateway
- `acctSummary.py` - Retrieve account summary information
- `contract_details.py` - Get details about financial contracts
- `contract_info.py` - Get information about financial contracts
- `contract_order.py` - Place orders for financial contracts
- `contract_search.py` - Search for financial contracts
- `mixed.py` - Mixed API functionality examples

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