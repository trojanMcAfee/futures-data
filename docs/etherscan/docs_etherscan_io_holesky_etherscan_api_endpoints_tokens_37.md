## [Direct link to heading](https://docs.etherscan.io/holesky-etherscan/api-endpoints/tokens\#get-erc20-token-totalsupply-by-contractaddress)    Get ERC20-Token TotalSupply by ContractAddress

Returns the current amount of an ERC-20 token in circulation.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api-holesky.etherscan.io/api
   ?module=stats
   &action=tokensupply
   &contractaddress=0x639d4384b429ea4660f377b7a29dae6d2255090f
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api-holesky.etherscan.io/api?module=stats&action=tokensupply&contractaddress=0x639d4384b429ea4660f377b7a29dae6d2255090f&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

contractaddress

the `contract address` of the ERC-20 token

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "status":"1",
   "message":"OK",
   "result":"10000000000000000000000"
}
```

📈 **Tip** : The `result` is returned in the token's **smallest decimal representation.**

Eg. a token with a balance of `215.241526476136819398` and 18 decimal places will be returned as `215241526476136819398`

## [Direct link to heading](https://docs.etherscan.io/holesky-etherscan/api-endpoints/tokens\#get-erc20-token-account-balance-for-tokencontractaddress)    Get ERC20-Token Account Balance for TokenContractAddress

Returns the current balance of an ERC-20 token of an address.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api-holesky.etherscan.io/api
   ?module=account
   &action=tokenbalance
   &contractaddress=0x639d4384b429ea4660f377b7a29dae6d2255090f
   &address=0x955866ee0bd3b8b0be4d4ea306670f34b90ef3ed
   &tag=latest&apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api-holesky.etherscan.io/api?module=account&action=tokenbalance&contractaddress=0x639d4384b429ea4660f377b7a29dae6d2255090f&address=0x955866ee0bd3b8b0be4d4ea306670f34b90ef3ed&tag=latest&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

contractaddress

the `contract address` of the ERC-20 token

address

the `string` representing the address to check for token balance

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "status":"1",
   "message":"OK",
   "result":"10000000000000000000000"
}
```

📈 **Tip** : The `result` is returned in the token's **smallest decimal representation.**

Eg. a token with a balance of `215.241526476136819398` and 18 decimal places will be returned as `215241526476136819398`

[PreviousGeth/Parity Proxy](https://docs.etherscan.io/holesky-etherscan/api-endpoints/geth-parity-proxy) [NextStats](https://docs.etherscan.io/holesky-etherscan/api-endpoints/stats-1)

Last updated 10 months ago

This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject