## [Direct link to heading](https://docs.etherscan.io/holesky-etherscan/api-endpoints/stats\#check-contract-execution-status)    Check Contract Execution Status

Returns the status code of a contract execution.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api-holesky.etherscan.io/api
   ?module=transaction
   &action=getstatus
   &txhash=0x5d329954fae7d19b2fb9abf0e6862735243b1079c58e0ea307d7e933657ac083
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api-holesky.etherscan.io/api?module=transaction&action=getstatus&txhash=0x5d329954fae7d19b2fb9abf0e6862735243b1079c58e0ea307d7e933657ac083&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

txhash

the `string` representing the transaction hash to check the execution status

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "status":"1",
   "message":"OK",
   "result":{
      "isError":"0",
      "errDescription":""
   }
}
```

📖 **Tip:** The `isError` field returns `0` for **successful transactions** and `1` for **failed transactions.**

## [Direct link to heading](https://docs.etherscan.io/holesky-etherscan/api-endpoints/stats\#check-transaction-receipt-status)    Check Transaction Receipt Status

Returns the status code of a transaction execution.

📝 **Note:** Only applicable for post [**Byzantium Fork**](https://www.investopedia.com/news/what-byzantium-hard-fork-ethereum/) transactions.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api-holesky.etherscan.io/api
   ?module=transaction
   &action=gettxreceiptstatus
   &txhash=0x13d297c02c1dd4ada29fa88e5d3dfa040c2f1d0d45802fb6b02ed95debdf2290
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api-holesky.etherscan.io/api?module=transaction&action=gettxreceiptstatus&txhash=0x13d297c02c1dd4ada29fa88e5d3dfa040c2f1d0d45802fb6b02ed95debdf2290&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

txhash

the `string` representing the transaction hash to check the execution status

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "status":"1",
   "message":"OK",
   "result":{
      "status":"1"
   }
}
```

📖 **Tip:** The `status` field returns `0` for **failed transactions** and `1` for **successful transactions.**

[PreviousContracts](https://docs.etherscan.io/holesky-etherscan/api-endpoints/contracts) [NextBlocks](https://docs.etherscan.io/holesky-etherscan/api-endpoints/blocks)

Last updated 10 months ago

This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject