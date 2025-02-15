## [Direct link to heading](https://docs.etherscan.io/api-endpoints/stats\#check-contract-execution-status)    Check Contract Execution Status

Returns the status code of a contract execution.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/api
   ?module=transaction
   &action=getstatus
   &txhash=0x15f8e5ea1079d9a0bb04a4c58ae5fe7654b5b2b4463375ff7ffb490aa0032f3a
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api.etherscan.io/api?module=transaction&action=getstatus&txhash=0x15f8e5ea1079d9a0bb04a4c58ae5fe7654b5b2b4463375ff7ffb490aa0032f3a&apikey=YourApiKeyToken) 🔗

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
      "errDescription":"Bad jump destination"
   }
}
```

📖 **Tip:** The `isError` field returns `0` for **successful transactions** and `1` for **failed transactions.**

## [Direct link to heading](https://docs.etherscan.io/api-endpoints/stats\#check-transaction-receipt-status)    Check Transaction Receipt Status

Returns the status code of a transaction execution.

📝 **Note:** Only applicable for post [**Byzantium Fork**](https://www.investopedia.com/news/what-byzantium-hard-fork-ethereum/) transactions.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/api
   ?module=transaction
   &action=gettxreceiptstatus
   &txhash=0x513c1ba0bebf66436b5fed86ab668452b7805593c05073eb2d51d3a52f480a76
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api.etherscan.io/api?module=transaction&action=gettxreceiptstatus&txhash=0x513c1ba0bebf66436b5fed86ab668452b7805593c05073eb2d51d3a52f480a76&apikey=YourApiKeyToken) 🔗

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

[PreviousContracts](https://docs.etherscan.io/api-endpoints/contracts) [NextBlocks](https://docs.etherscan.io/api-endpoints/blocks)

Last updated 3 years ago

This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject