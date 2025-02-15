## [Direct link to heading](https://docs.etherscan.io/etherscan-v2/api-endpoints/chain-specific\#polygon-137)    Polygon \[137\]

### [Direct link to heading](https://docs.etherscan.io/etherscan-v2/api-endpoints/chain-specific\#get-list-of-plasma-deposits-by-address)    Get list of Plasma Deposits by Address

Returns a list of Plasma Deposits received by an address.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/v2/api
   ?chainid=137
   &module=account
   &action=txnbridge
   &address=0x4880bd4695a8e59dc527d124085749744b6c988e
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api.etherscan.io/v2/api?chainid=137&module=account&action=txnbridge&address=0x4880bd4695a8e59dc527d124085749744b6c988e&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

address

the `string` representing the address to check for balance

blocktype

the `string` pre-defined block type, `blocks` for canonical blocks

page

the `integer` page number, if pagination is enabled

offset

the number of transactions displayed per page

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
    "status":"1",
    "message":"OK",
    "result":[\
        {\
            "blockNumber":"19569186",\
            "timeStamp":"1632738360",\
            "blockReward":"388632493476995398"\
        },\
        {\
            "blockNumber":"19569185",\
            "timeStamp":"1632738358",\
            "blockReward":"1021530830332446078"\
        },\
    ]
}
```

⏳ **Note :** The `timeStamp` is represented in [**Unix timestamp.**](https://www.unixtimestamp.com/)

[PreviousStats](https://docs.etherscan.io/etherscan-v2/api-endpoints/stats-1) [NextUsage](https://docs.etherscan.io/etherscan-v2/api-endpoints/blocks-1)

Last updated 5 months ago

This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject