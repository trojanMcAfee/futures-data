[Skip to main content](https://docs.kraken.com/api/docs/rest-api/get-recent-trades/#__docusaurus_skipToContent_fallback)

# Get Recent Trades

```
GET https://api.kraken.com/0/public/Trades
```

Returns the last 1000 trades by default

## Request [​](https://docs.kraken.com/api/docs/rest-api/get-recent-trades/\#request "Direct link to Request")

### Query Parameters

**pair**stringrequired

Asset pair to get data for

**Example:** XBTUSD

**since**string

Return trade data since given timestamp

**Example:** 1616663618

**count**integer

**Possible values:** `>= 1` and `<= 1000`

**Default value:** `1000`

Return specific number of trades, up to 1000

**Example:** 2

## Responses [​](https://docs.kraken.com/api/docs/rest-api/get-recent-trades/\#responses "Direct link to Responses")

- 200

Trade data retrieved.

- application/json

- Schema
- Example (from schema)

**Schema**

**result** object

**last** string

ID to be used as since when polling for new trade data

**property name\*** TickData

Array of trade entries
`[<price>, <volume>, <time>, <buy/sell>, <market/limit>, <miscellaneous>, <trade_id>]`

Array \[\
\
**type**\
\
**items** object\
\
oneOf\
\
- string\
- number\
\
string\
\
number\
\
\]

**error** string\[\]

```codeBlockLines_e6Vv
{
  "error": [],
  "result": {
    "XXBTZUSD": [\
      [\
        "30243.40000",\
        "0.34507674",\
        1688669597.8277369,\
        "b",\
        "m",\
        "",\
        61044952\
      ],\
      [\
        "30243.30000",\
        "0.00376960",\
        1688669598.2804112,\
        "s",\
        "l",\
        "",\
        61044953\
      ],\
      [\
        "30243.30000",\
        "0.01235716",\
        1688669602.698379,\
        "s",\
        "m",\
        "",\
        61044956\
      ]\
    ],
    "last": "1688671969993150842"
  }
}

```

- curl
- python
- go
- nodejs

- CURL

```openapi-explorer__code-block-lines openapi-explorer__code-block-lines-numbering
curl -L 'https://api.kraken.com/0/public/Trades' \
-H 'Accept: application/json'

```

Request Collapse all

Base URL

Edit

https://api.kraken.com/0

Parameters

pair — queryrequired

Show optional parameters

since — query

count — query

Send API Request

ResponseClear

Click the `Send API Request` button above and see the response here!