Search SecDef information by conidCopy Location
Provides Contract Details of Futures, Options, Warrants, Cash and CFDs based on conid.

For all instruments, /iserver/secdef/search must be called first.

For derivatives such as Options, Warrants, and Futures Options, you will need to query /iserver/secdef/strikes as well.

GET /iserver/secdef/info

 

Request Object
Query Parameters
conid: String. Required
Contract identifier of the underlying. May also pass the final derivative conid directly.

sectype: String. Required
Security type of the requested contract of interest.

month: String. Required for Derivatives
Expiration month for the given derivative.

exchange: String. Optional
Designate the exchange you wish to receive information for in relation to the contract.

strike: String. Required for Options and Futures Options
Set the strike price for the requested contract details

right: String. Required for Options
Set the right for the given contract.
Value Format: “C” for Call or “P” for Put.

issuerId: String. Required for Bonds
Set the issuerId for the given bond issuer type.
Example Format: “e1234567”

Python
cURL
request_url = f"{baseUrl}/iserver/secdef/info?conid=265598&secType=OPT&month=JAN24&strike=195&right=P"
requests.get(url=request_url)
 

Response Object
conid: int.
Contract Identifier of the given contract

ticker: String
Ticker symbol for the given contract

secType: String.
Security type for the given contract.

listingExchange: String.
Primary listing exchange for the given contract.

exchange: String.
Exchange requesting data for.

companyName: String.
Name of the company for the given contract.

currency: String
Traded currency allowed for the given contract.

validExchanges: String*
Series of all valid exchanges the contract can be traded on in a single comma-separated string.
priceRendering: null.

maturityDate: String
Date of expiration for the given contract.

right: String.
Right (P or C) for the given contract.

strike: Float.
Returns the given strike value for the given contract.