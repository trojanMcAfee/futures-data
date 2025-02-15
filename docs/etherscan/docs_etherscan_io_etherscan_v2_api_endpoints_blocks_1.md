## [Direct link to heading](https://docs.etherscan.io/etherscan-v2/api-endpoints/blocks-1\#check-etherscan-credit-usage)    Check Etherscan credit usage

Returns the amount of API credits available, and reset countdown.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/v2/api
   ?&module=getapilimit
   &action=getapilimit
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api.etherscan.io/v2/api?&module=getapilimit&action=getapilimit&apikey=YourApiKeyToken) 🔗

RequestResponse

No parameters required.

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "status":"1",
   "message":"OK",
   "result":{
      "creditsUsed":207,
      "creditsAvailable":499793,
      "creditLimit":500000,
      "limitInterval":"daily",
      "intervalExpiryTimespan":"07:20:05"
   }
}
```

## [Direct link to heading](https://docs.etherscan.io/etherscan-v2/api-endpoints/blocks-1\#list-supported-chains)    List supported chains

Returns a list of supported Etherscan explorer APIs, with web explorer links.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/v2/chainlist
```

> Try this endpoint in your [**browser**](https://api.etherscan.io/v2/chainlist) 🔗

RequestResponse

No parameters required.

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "totalcount":50,
   "result":[\
      {\
         "chainname":"Ethereum Mainnet",\
         "chainid":"1",\
         "blockexplorer":"https://etherscan.io",\
         "apiurl":"https://api.etherscan.io/v2/api?chainid=1",\
         "status":1\
      },\
      {\
         "chainname":"Sepolia Testnet",\
         "chainid":"11155111",\
         "blockexplorer":"https://sepolia.etherscan.io",\
         "apiurl":"https://api.etherscan.io/v2/api?chainid=11155111",\
         "status":1\
      }\
   ]
}
```

[PreviousChain Specific](https://docs.etherscan.io/etherscan-v2/api-endpoints/chain-specific) [NextEtherscan API PRO](https://docs.etherscan.io/etherscan-v2/api-pro/etherscan-api-pro)

Last updated 3 months ago

This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject