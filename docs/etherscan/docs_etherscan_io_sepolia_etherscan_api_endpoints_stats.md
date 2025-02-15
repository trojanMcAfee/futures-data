## [Direct link to heading](https://docs.etherscan.io/sepolia-etherscan/api-endpoints/stats\#check-contract-execution-status)    Check Contract Execution Status

Returns the status code of a contract execution.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api-sepolia.etherscan.io/api
   ?module=transaction
   &action=getstatus
   &txhash=0x8dac9d2429f2f73cab7db5d26986f77b96552188b1c969a50ce7bff563ffbb6c
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api-sepolia.etherscan.io/api?module=transaction&action=getstatus&txhash=0x8dac9d2429f2f73cab7db5d26986f77b96552188b1c969a50ce7bff563ffbb6c&apikey=YourApiKeyToken) 🔗

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
      "isError":"1",
      "errDescription":"execution reverted"
   }
}
```

📖 **Tip:** The `isError` field returns `0` for **successful transactions** and `1` for **failed transactions.**

## [Direct link to heading](https://docs.etherscan.io/sepolia-etherscan/api-endpoints/stats\#check-transaction-receipt-status)    Check Transaction Receipt Status

Returns the status code of a transaction execution.

📝 **Note:** Only applicable for post [**Byzantium Fork**](https://www.investopedia.com/news/what-byzantium-hard-fork-ethereum/) transactions.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api-sepolia.etherscan.io/api
   ?module=transaction
   &action=gettxreceiptstatus
   &txhash=0x57fe171a6bcf99669f4bb4a0947a59503f7a88059a9749e3d3ebecda53c08f55
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api-sepolia.etherscan.io/api?module=transaction&action=gettxreceiptstatus&txhash=0x57fe171a6bcf99669f4bb4a0947a59503f7a88059a9749e3d3ebecda53c08f55&apikey=YourApiKeyToken) 🔗

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
      "status":"0"
   }
}
```

📖 **Tip:** The `status` field returns `0` for **failed transactions** and `1` for **successful transactions.**

[PreviousContracts](https://docs.etherscan.io/sepolia-etherscan/api-endpoints/contracts) [NextBlocks](https://docs.etherscan.io/sepolia-etherscan/api-endpoints/blocks)

Last updated 2 years ago

This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject