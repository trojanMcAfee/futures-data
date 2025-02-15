Endpoints with ![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2Fsg8e76TOnPYfHTGZoQl0%2Fblobs%2FnO0IqZUuuzhIJvlXPnTH%2Fpro.PNG&width=81&dpr=4&quality=100&sign=a2e7a29f&sv=2) are under the API Pro subscription. To upgrade your API plan, browse through the [**Etherscan APIs**](https://etherscan.io/apis) page.

## [Direct link to heading](https://docs.etherscan.io/etherscan-v2/api-endpoints/tokens\#get-erc20-token-totalsupply-by-contractaddress)    Get ERC20-Token TotalSupply by ContractAddress

Returns the current amount of an ERC-20 token in circulation.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=stats
   &action=tokensupply
   &contractaddress=0x57d90b64a1a57749b0f932f1a3395792e12e7055
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api.etherscan.io/v2/api?chainid=1&module=stats&action=tokensupply&contractaddress=0x57d90b64a1a57749b0f932f1a3395792e12e7055&apikey=YourApiKeyToken) 🔗

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
   "result":"21265524714464"
}
```

📈 **Tip** : The `result` is returned in the token's **smallest decimal representation.**

Eg. a token with a balance of `215.241526476136819398` and 18 decimal places will be returned as `215241526476136819398`

## [Direct link to heading](https://docs.etherscan.io/etherscan-v2/api-endpoints/tokens\#get-erc20-token-account-balance-for-tokencontractaddress)    Get ERC20-Token Account Balance for TokenContractAddress

Returns the current balance of an ERC-20 token of an address.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=account
   &action=tokenbalance
   &contractaddress=0x57d90b64a1a57749b0f932f1a3395792e12e7055
   &address=0xe04f27eb70e025b78871a2ad7eabe85e61212761
   &tag=latest&apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api.etherscan.io/v2/api?chainid=1&module=account&action=tokenbalance&contractaddress=0x57d90b64a1a57749b0f932f1a3395792e12e7055&address=0xe04f27eb70e025b78871a2ad7eabe85e61212761&tag=latest&apikey=YourApiKeyToken) 🔗

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
   "result":"135499"
}
```

📈 **Tip** : The `result` is returned in the token's **smallest decimal representation.**

Eg. a token with a balance of `215.241526476136819398` and 18 decimal places will be returned as `215241526476136819398`

## [Direct link to heading](https://docs.etherscan.io/etherscan-v2/api-endpoints/tokens\#get-historical-erc20-token-totalsupply-by-contractaddress-and-blockno)    Get Historical ERC20-Token TotalSupply by ContractAddress & BlockNo ![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2Fsg8e76TOnPYfHTGZoQl0%2Fblobs%2FUNUGdpodJYN3gil5sSsx%2Fpro_padding_latest.png&width=75&dpr=4&quality=100&sign=d0c300b8&sv=2)

Returns the amount of an ERC-20 token in circulation at a certain block height.

📝 **Note :** This endpoint is throttled to **2 calls/second** regardless of API Pro tier.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=stats
   &action=tokensupplyhistory
   &contractaddress=0x57d90b64a1a57749b0f932f1a3395792e12e7055
   &blockno=8000000
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api.etherscan.io/v2/api?chainid=1&module=stats&action=tokensupplyhistory&contractaddress=0x57d90b64a1a57749b0f932f1a3395792e12e7055&blockno=8000000&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

contractaddress

the `contract address` of the ERC-20 token

blockno

the `integer` block number to check total supply for eg. [`12697906`](https://etherscan.io/block/12697906)

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "status":"1",
   "message":"OK",
   "result":"21265524714464"
}
```

📈 **Tip** : The `result` is returned in the token's **smallest decimal representation.**

Eg. a token with a balance of `215.241526476136819398` and 18 decimal places will be returned as `215241526476136819398`

## [Direct link to heading](https://docs.etherscan.io/etherscan-v2/api-endpoints/tokens\#get-historical-erc20-token-account-balance-for-tokencontractaddress-by-blockno)    Get Historical ERC20-Token Account Balance for TokenContractAddress by BlockNo ![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2Fsg8e76TOnPYfHTGZoQl0%2Fblobs%2FUNUGdpodJYN3gil5sSsx%2Fpro_padding_latest.png&width=75&dpr=4&quality=100&sign=d0c300b8&sv=2)

Returns the balance of an ERC-20 token of an address at a certain block height.

📝 **Note :** This endpoint is throttled to **2 calls/second** regardless of API Pro tier.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=account
   &action=tokenbalancehistory
   &contractaddress=0x57d90b64a1a57749b0f932f1a3395792e12e7055
   &address=0xe04f27eb70e025b78871a2ad7eabe85e61212761
   &blockno=8000000
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api.etherscan.io/v2/api?chainid=1&module=account&action=tokenbalancehistory&contractaddress=0x57d90b64a1a57749b0f932f1a3395792e12e7055&address=0xe04f27eb70e025b78871a2ad7eabe85e61212761&blockno=8000000&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

contractaddress

the `contract address` of the ERC-20 token

address

the `string` representing the address to check for balance

blockno

the `integer` block number to check total supply for eg. [`12697906`](https://etherscan.io/block/12697906)

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "status":"1",
   "message":"OK",
   "result":"135499"
}
```

📈 **Tip** : The `result` is returned in the token's **smallest decimal representation.**

Eg. a token with a balance of `215.241526476136819398` and 18 decimal places will be returned as `215241526476136819398`

## [Direct link to heading](https://docs.etherscan.io/etherscan-v2/api-endpoints/tokens\#get-token-holder-list-by-contract-address)    Get Token Holder List by Contract Address ![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2Fsg8e76TOnPYfHTGZoQl0%2Fblobs%2FUNUGdpodJYN3gil5sSsx%2Fpro_padding_latest.png&width=75&dpr=4&quality=100&sign=d0c300b8&sv=2)

Return the current ERC20 token holders and number of tokens held.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=token
   &action=tokenholderlist
   &contractaddress=0xaaaebe6fe48e54f431b0c390cfaf0b017d09d42d
   &page=1
   &offset=10
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api.etherscan.io/v2/api?chainid=1&module=token&action=tokenholderlist&contractaddress=0xaaaebe6fe48e54f431b0c390cfaf0b017d09d42d&page=1&offset=10&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

contractaddress

the `contract address` of the ERC-20 token

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
         "TokenHolderAddress":"0x0000000000000000000000000000000000000000",\
         "TokenHolderQuantity":"34956"\
      },\
      {\
         "TokenHolderAddress":"0x000000000000084e91743124a982076c59f10084",\
         "TokenHolderQuantity":"1"\
      },\
      {\
         "TokenHolderAddress":"0x0000000000000d9054f605ca65a2647c2b521422",\
         "TokenHolderQuantity":"10000000"\
      },\
      {\
         "TokenHolderAddress":"0x0000000000002d534ff79e9c69e7fcc742f0be83",\
         "TokenHolderQuantity":"5"\
      },\
      {\
         "TokenHolderAddress":"0x0000000000003f5e74c1ba8a66b48e6f3d71ae82",\
         "TokenHolderQuantity":"1"\
      }\
   ]
}
```

### [Direct link to heading](https://docs.etherscan.io/etherscan-v2/api-endpoints/tokens\#get-token-holder-count-by-contract-address)    Get Token Holder Count by Contract Address ![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F1052732906-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-McrExXKKJBLJqymbFhO%252Fuploads%252Fgit-blob-80b86ca0904cf1db448758a969151e04dd7415dc%252Fpro_padding_latest.png%3Falt%3Dmedia&width=75&dpr=4&quality=100&sign=fe36a34c&sv=2)

Return a simple count of the number of ERC20 token holders.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=token
   &action=tokenholdercount
   &contractaddress=0xaaaebe6fe48e54f431b0c390cfaf0b017d09d42d
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api.etherscan.io/v2/api?chainid=1&module=token&action=tokenholdercount&contractaddress=0xaaaebe6fe48e54f431b0c390cfaf0b017d09d42d&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

contractaddress

the `contract address` of the ERC20 token

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "status":"1",
   "message":"OK",
   "result":"30484"
}
```

## [Direct link to heading](https://docs.etherscan.io/etherscan-v2/api-endpoints/tokens\#get-token-info-by-contractaddress)    Get Token Info by ContractAddress ![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2Fsg8e76TOnPYfHTGZoQl0%2Fblobs%2FUNUGdpodJYN3gil5sSsx%2Fpro_padding_latest.png&width=75&dpr=4&quality=100&sign=d0c300b8&sv=2)

Returns project information and social media links of an ERC20/ERC721/ERC1155 token.

📝 **Note :** This endpoint is throttled to **2 calls/second** regardless of API Pro tier.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=token
   &action=tokeninfo
   &contractaddress=0x0e3a2a1f2146d86a604adc220b4967a898d7fe07
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api.etherscan.io/v2/api?chainid=1&module=token&action=tokeninfo&contractaddress=0x0e3a2a1f2146d86a604adc220b4967a898d7fe07&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

contractaddress

the `contract address` of the ERC-20/ERC-721 token to retrieve token info

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "status":"1",
   "message":"OK",
   "result":[\
      {\
         "contractAddress":"0x0e3a2a1f2146d86a604adc220b4967a898d7fe07",\
         "tokenName":"Gods Unchained Cards",\
         "symbol":"CARD",\
         "divisor":"0",\
         "tokenType":"ERC721",\
         "totalSupply":"6962498",\
         "blueCheckmark":"true",\
         "description":"A TCG on the Ethereum blockchain that uses NFT's to bring real ownership to in-game assets.",\
         "website":"https://godsunchained.com/",\
         "email":"",\
         "blog":"https://medium.com/@fuelgames",\
         "reddit":"https://www.reddit.com/r/GodsUnchained/",\
         "slack":"",\
         "facebook":"https://www.facebook.com/godsunchained/",\
         "twitter":"https://twitter.com/godsunchained",\
         "bitcointalk":"",\
         "github":"",\
         "telegram":"",\
         "wechat":"",\
         "linkedin":"",\
         "discord":"https://discordapp.com/invite/DKGr2pW",\
         "whitepaper":"",\
         "tokenPriceUSD":"0.000000000000000000"\
      }\
   ]
}
```

## [Direct link to heading](https://docs.etherscan.io/etherscan-v2/api-endpoints/tokens\#get-address-erc20-token-holding)    Get Address ERC20 Token Holding ![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2Fsg8e76TOnPYfHTGZoQl0%2Fblobs%2FUNUGdpodJYN3gil5sSsx%2Fpro_padding_latest.png&width=75&dpr=4&quality=100&sign=d0c300b8&sv=2)

Returns the ERC-20 tokens and amount held by an address.

**Note :** This endpoint is throttled to **2 calls/second** regardless of API Pro tier.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=account
   &action=addresstokenbalance
   &address=0x983e3660c0bE01991785F80f266A84B911ab59b0
   &page=1
   &offset=100
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api.etherscan.io/v2/api?chainid=1&module=account&action=addresstokenbalance&address=0x983e3660c0bE01991785F80f266A84B911ab59b0&page=1&offset=100&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

address

the `string` representing the address to check for balance

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
         "TokenAddress":"0xffffffff2ba8f66d4e51811c5190992176930278",\
         "TokenName":"Furucombo",\
         "TokenSymbol":"COMBO",\
         "TokenQuantity":"1861606940000000000",\
         "TokenDivisor":"18"\
      },\
      {\
         "TokenAddress":"0x53a1e9912323b8016424d6287286e3b6de263f76",\
         "TokenName":"PUTIN Token",\
         "TokenSymbol":"PTT",\
         "TokenQuantity":"3500000000000000000000",\
         "TokenDivisor":"18"\
      },\
      {\
         "TokenAddress":"0xb753428af26e81097e7fd17f40c88aaa3e04902c",\
         "TokenName":"Spice",\
         "TokenSymbol":"SFI",\
         "TokenQuantity":"7",\
         "TokenDivisor":"18"\
      },\
      {\
         "TokenAddress":"0x1b40183efb4dd766f11bda7a7c3ad8982e998421",\
         "TokenName":"VesperToken",\
         "TokenSymbol":"VSP",\
         "TokenQuantity":"962",\
         "TokenDivisor":"18"\
      },\
      {\
         "TokenAddress":"0x37e83a94c6b1bdb816b59ac71dd02cf154d8111f",\
         "TokenName":"PhotoChromic",\
         "TokenSymbol":"PHCR",\
         "TokenQuantity":"4608452961264910063288",\
         "TokenDivisor":"18"\
      }\
   ]
}
```

## [Direct link to heading](https://docs.etherscan.io/etherscan-v2/api-endpoints/tokens\#get-address-erc721-token-holding)    Get Address ERC721 Token Holding ![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2Fsg8e76TOnPYfHTGZoQl0%2Fblobs%2FUNUGdpodJYN3gil5sSsx%2Fpro_padding_latest.png&width=75&dpr=4&quality=100&sign=d0c300b8&sv=2)

Returns the ERC-721 tokens and amount held by an address.

**Note :** This endpoint is throttled to **2 calls/second** regardless of API Pro tier.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=account
   &action=addresstokennftbalance
   &address=0x6b52e83941eb10f9c613c395a834457559a80114
   &page=1
   &offset=100
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api.etherscan.io/v2/api?chainid=1&module=account&action=addresstokennftbalance&address=0x6b52e83941eb10f9c613c395a834457559a80114&page=1&offset=100&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

address

the `string` representing the address to check for balance

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
         "TokenAddress":"0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b",\
         "TokenName":"CloneX",\
         "TokenSymbol":"CloneX",\
         "TokenQuantity":"52"\
      },\
      {\
         "TokenAddress":"0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d",\
         "TokenName":"BoredApeYachtClub",\
         "TokenSymbol":"BAYC",\
         "TokenQuantity":"1"\
      },\
      {\
         "TokenAddress":"0x60e4d786628fea6478f785a6d7e704777c86a7c6",\
         "TokenName":"MutantApeYachtClub",\
         "TokenSymbol":"MAYC",\
         "TokenQuantity":"1"\
      },\
      {\
         "TokenAddress":"0xed5af388653567af2f388e6224dc7c4b3241c544",\
         "TokenName":"Azuki",\
         "TokenSymbol":"AZUKI",\
         "TokenQuantity":"1"\
      },\
      {\
         "TokenAddress":"0x7bd29408f11d2bfc23c34f18275bbf23bb716bc7",\
         "TokenName":"Meebits",\
         "TokenSymbol":"⚇",\
         "TokenQuantity":"1"\
      }\
   ]
}
```

## [Direct link to heading](https://docs.etherscan.io/etherscan-v2/api-endpoints/tokens\#get-address-erc721-token-inventory-by-contract-address)    Get Address ERC721 Token Inventory By Contract Address ![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2Fsg8e76TOnPYfHTGZoQl0%2Fblobs%2FUNUGdpodJYN3gil5sSsx%2Fpro_padding_latest.png&width=75&dpr=4&quality=100&sign=d0c300b8&sv=2)

Returns the ERC-721 token inventory of an address, filtered by contract address.

📝 **Note :** This endpoint is throttled to **2 calls/second** regardless of API Pro tier.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=account
   &action=addresstokennftinventory
   &address=0x123432244443b54409430979df8333f9308a6040
   &contractaddress=0xed5af388653567af2f388e6224dc7c4b3241c544
   &page=1
   &offset=100
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api.etherscan.io/v2/api?chainid=1&module=account&action=addresstokennftinventory&address=0x123432244443b54409430979df8333f9308a6040&contractaddress=0xed5af388653567af2f388e6224dc7c4b3241c544&page=1&offset=100&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

address

the `string` representing the address to check for inventory

contractaddress

the `string` representing the ERC-721 token contractaddress to check for inventory

page

the `integer` page number, if pagination is enabled

offset

the number of records displayed per page

limited to **1000 records** per query, use the `page` parameter for subsequent records

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "status":"1",
   "message":"OK",
   "result":[\
      {\
         "TokenAddress":"0xed5af388653567af2f388e6224dc7c4b3241c544",\
         "TokenId":"5401"\
      },\
      {\
         "TokenAddress":"0xed5af388653567af2f388e6224dc7c4b3241c544",\
         "TokenId":"7411"\
      },\
      {\
         "TokenAddress":"0xed5af388653567af2f388e6224dc7c4b3241c544",\
         "TokenId":"453"\
      },\
      {\
         "TokenAddress":"0xed5af388653567af2f388e6224dc7c4b3241c544",\
         "TokenId":"8080"\
      },\
      {\
         "TokenAddress":"0xed5af388653567af2f388e6224dc7c4b3241c544",\
         "TokenId":"4255"\
      }\
   ]
}
```

[PreviousGeth/Parity Proxy](https://docs.etherscan.io/etherscan-v2/api-endpoints/geth-parity-proxy) [NextGas Tracker](https://docs.etherscan.io/etherscan-v2/api-endpoints/gas-tracker)

Last updated 1 month ago

This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject