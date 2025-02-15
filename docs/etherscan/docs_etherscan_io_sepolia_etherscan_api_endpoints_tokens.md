## [Direct link to heading](https://docs.etherscan.io/sepolia-etherscan/api-endpoints/tokens\#get-erc20-token-totalsupply-by-contractaddress)    Get ERC20-Token TotalSupply by ContractAddress

Returns the current amount of an ERC-20 token in circulation.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api-sepolia.etherscan.io/api
   ?module=stats
   &action=tokensupply
   &contractaddress=0x15f0ca26781c3852f8166ed2ebce5d18265cceb7
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api-sepolia.etherscan.io/api?module=stats&action=tokensupply&contractaddress=0x15f0ca26781c3852f8166ed2ebce5d18265cceb7&apikey=YourApiKeyToken) 🔗

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
   "result":"115792089237316195350517916280681741865800000000000204321000008482101313059520"
}
```

📈 **Tip** : The `result` is returned in the token's **smallest decimal representation.**

Eg. a token with a balance of `215.241526476136819398` and 18 decimal places will be returned as `215241526476136819398`

## [Direct link to heading](https://docs.etherscan.io/sepolia-etherscan/api-endpoints/tokens\#get-erc20-token-account-balance-for-tokencontractaddress)    Get ERC20-Token Account Balance for TokenContractAddress

Returns the current balance of an ERC-20 token of an address.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api-sepolia.etherscan.io/api
   ?module=account
   &action=tokenbalance
   &contractaddress=0x15f0ca26781c3852f8166ed2ebce5d18265cceb7
   &address=0x89c184f7c342b106f37c486a38453a1af7db10b6
   &tag=latest&apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api-sepolia.etherscan.io/api?module=account&action=tokenbalance&contractaddress=0x15f0ca26781c3852f8166ed2ebce5d18265cceb7&address=0x89c184f7c342b106f37c486a38453a1af7db10b6&tag=latest&apikey=YourApiKeyToken) 🔗

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
   "result":"13400000000000000000000"
}
```

📈 **Tip** : The `result` is returned in the token's **smallest decimal representation.**

Eg. a token with a balance of `215.241526476136819398` and 18 decimal places will be returned as `215241526476136819398`

[PreviousGeth/Parity Proxy](https://docs.etherscan.io/sepolia-etherscan/api-endpoints/geth-parity-proxy) [NextStats](https://docs.etherscan.io/sepolia-etherscan/api-endpoints/stats-1)

Last updated 2 years ago

This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject