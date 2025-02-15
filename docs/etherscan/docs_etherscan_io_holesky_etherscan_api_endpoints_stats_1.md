## [Direct link to heading](https://docs.etherscan.io/holesky-etherscan/api-endpoints/stats-1\#get-total-supply-of-ether)    Get Total Supply of Ether

Returns the current amount of Ether in circulation.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api-holesky.etherscan.io/api
   ?module=stats
   &action=ethsupply
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api-holesky.etherscan.io/api?module=stats&action=ethsupply&apikey=YourApiKeyToken) 🔗

RequestResponse

No parameters required.

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "status":"1",
   "message":"OK",
   "result":"77523186686500000000000000"
}
```

📖 **Tip** : Easily convert Ethereum units using our [**unit converter.**](https://holesky.etherscan.io/unitconverter)

## [Direct link to heading](https://docs.etherscan.io/holesky-etherscan/api-endpoints/stats-1\#get-ether-last-price)    Get Ether Last Price

Returns the latest price of 1 ETH.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api-holesky.etherscan.io/api
   ?module=stats
   &action=ethprice
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api-holesky.etherscan.io/api?module=stats&action=ethprice&apikey=YourApiKeyToken) 🔗

RequestResponse

No parameters required.

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "status":"1",
   "message":"OK",
   "result":{
      "ethbtc":"0.06906",
      "ethbtc_timestamp":"1652444393",
      "ethusd":"2110.63",
      "ethusd_timestamp":"1652444395"
   }
}
```

⏳ **Tip :** The `timestamps` are represented in [**Unix timestamp.**](https://www.unixtimestamp.com/)

[PreviousTokens](https://docs.etherscan.io/holesky-etherscan/api-endpoints/tokens)

Last updated 10 months ago

This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject