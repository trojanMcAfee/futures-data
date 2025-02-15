The following is a complete list of additional API endpoints available under the API PRO subscription.

To upgrade your API plan, kindly visit [**Etherscan APIs**](https://etherscan.io/apis) **.**

## [Direct link to heading](https://docs.etherscan.io/api-pro/api-pro?fallback=true\#get-historical-ether-balance-for-a-single-address-by-blockno)    Get Historical Ether Balance for a Single Address By BlockNo ![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F1052732906-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-McrExXKKJBLJqymbFhO%252Fuploads%252Fgit-blob-80b86ca0904cf1db448758a969151e04dd7415dc%252Fpro_padding_latest.png%3Falt%3Dmedia&width=75&dpr=4&quality=100&sign=fe36a34c&sv=2)

Returns the balance of an address at a certain block height.

📝 **Note :** This API endpoint is throttled to 2 calls/second regardless of **API PRO tier.**

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/api
   ?module=account
   &action=balancehistory
   &address=0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae
   &blockno=8000000
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api.etherscan.io/api?module=account&action=balancehistory&address=0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae&blockno=8000000&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

address

the `string` representing the address to check for balance

blockno

the `integer` block number to check balance for eg. [`12697906`](https://etherscan.io/block/12697906)

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "status":"1",
   "message":"OK",
   "result":"610538078574759898951277"
}
```

📖 **Note:** The `result` field is denoted in **wei.**

## [Direct link to heading](https://docs.etherscan.io/api-pro/api-pro?fallback=true\#get-daily-average-block-size)    Get Daily Average Block Size ![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F1052732906-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-McrExXKKJBLJqymbFhO%252Fuploads%252Fgit-blob-80b86ca0904cf1db448758a969151e04dd7415dc%252Fpro_padding_latest.png%3Falt%3Dmedia&width=75&dpr=4&quality=100&sign=fe36a34c&sv=2)

Returns the daily average block size within a date range.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/api
   ?module=stats
   &action=dailyavgblocksize
   &startdate=2019-02-01
   &enddate=2019-02-28
   &sort=asc
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api.etherscan.io/api?module=stats&action=dailyavgblocksize&startdate=2019-02-01&enddate=2019-02-28&sort=asc&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

startdate

the starting date in `yyyy-MM-dd` format, eg. `2019-02-01`

enddate

the ending date in `yyyy-MM-dd` format, eg. `2019-02-28`

sort

the sorting preference, use `asc` to sort by ascending and `desc` to sort by descending

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "status":"1",
   "message":"OK",
   "result":[\
      {\
         "UTCDate":"2019-02-01",\
         "unixTimeStamp":"1548979200",\
         "blockSize_bytes":20373\
      },\
      {\
         "UTCDate":"2019-02-28",\
         "unixTimeStamp":"1551312000",\
         "blockSize_bytes":25117\
      }\
   ]
}
```

## [Direct link to heading](https://docs.etherscan.io/api-pro/api-pro?fallback=true\#get-daily-block-count-and-rewards)    Get Daily Block Count and Rewards ![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F1052732906-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-McrExXKKJBLJqymbFhO%252Fuploads%252Fgit-blob-80b86ca0904cf1db448758a969151e04dd7415dc%252Fpro_padding_latest.png%3Falt%3Dmedia&width=75&dpr=4&quality=100&sign=fe36a34c&sv=2)

Returns the number of blocks mined daily and the amount of block rewards.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/api
   ?module=stats
   &action=dailyblkcount
   &startdate=2019-02-01
   &enddate=2019-02-28
   &sort=asc
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api.etherscan.io/api?module=stats&action=dailyblkcount&startdate=2019-02-01&enddate=2019-02-28&sort=asc&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

startdate

the starting date in `yyyy-MM-dd` format, eg. `2019-02-01`

enddate

the ending date in `yyyy-MM-dd` format, eg. `2019-02-28`

sort

the sorting preference, use `asc` to sort by ascending and `desc` to sort by descending

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "status":"1",
   "message":"OK",
   "result":[\
      {\
         "UTCDate":"2019-02-01",\
         "unixTimeStamp":"1548979200",\
         "blockCount":4848,\
         "blockRewards_Eth":"14929.464690870590355682"\
      },\
      {\
         "UTCDate":"2019-02-28",\
         "unixTimeStamp":"1551312000",\
         "blockCount":4366,\
         "blockRewards_Eth":"12808.485512162356907132"\
      }\
   ]
}
```

## [Direct link to heading](https://docs.etherscan.io/api-pro/api-pro?fallback=true\#get-daily-block-rewards)    Get Daily Block Rewards ![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F1052732906-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-McrExXKKJBLJqymbFhO%252Fuploads%252Fgit-blob-80b86ca0904cf1db448758a969151e04dd7415dc%252Fpro_padding_latest.png%3Falt%3Dmedia&width=75&dpr=4&quality=100&sign=fe36a34c&sv=2)

Returns the amount of block rewards distributed to miners daily.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/api
   ?module=stats
   &action=dailyblockrewards
   &startdate=2019-02-01
   &enddate=2019-02-28
   &sort=asc
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api.etherscan.io/api?module=stats&action=dailyblockrewards&startdate=2019-02-01&enddate=2019-02-28&sort=asc&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

startdate

the starting date in `yyyy-MM-dd` format, eg. `2019-02-01`

enddate

the ending date in `yyyy-MM-dd` format, eg. `2019-02-28`

sort

the sorting preference, use `asc` to sort by ascending and `desc` to sort by descending

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "status":"1",
   "message":"OK",
   "result":[\
      {\
         "UTCDate":"2019-02-01",\
         "unixTimeStamp":"1548979200",\
         "blockRewards_Eth":"15300.65625"\
      },\
      {\
         "UTCDate":"2019-02-28",\
         "unixTimeStamp":"1551312000",\
         "blockRewards_Eth":"12954.84375"\
      }\
   ]
}
```

## [Direct link to heading](https://docs.etherscan.io/api-pro/api-pro?fallback=true\#get-daily-average-time-for-a-block-to-be-included-in-the-ethereum-blockchain)    Get Daily Average Time for A Block to be Included in the Ethereum Blockchain ![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F1052732906-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-McrExXKKJBLJqymbFhO%252Fuploads%252Fgit-blob-80b86ca0904cf1db448758a969151e04dd7415dc%252Fpro_padding_latest.png%3Falt%3Dmedia&width=75&dpr=4&quality=100&sign=fe36a34c&sv=2)

Returns the daily average of time needed for a block to be successfully mined.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/api
   ?module=stats
   &action=dailyavgblocktime
   &startdate=2019-02-01
   &enddate=2019-02-28
   &sort=asc
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api.etherscan.io/api?module=stats&action=dailyavgblocktime&startdate=2019-02-01&enddate=2019-02-28&sort=asc&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

startdate

the starting date in `yyyy-MM-dd` format, eg. `2019-02-01`

enddate

the ending date in `yyyy-MM-dd` format, eg. `2019-02-28`

sort

the sorting preference, use `asc` to sort by ascending and `desc` to sort by descending

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "status":"1",
   "message":"OK",
   "result":[\
      {\
         "UTCDate":"2019-02-01",\
         "unixTimeStamp":"1548979200",\
         "blockTime_sec":"17.67"\
      },\
      {\
         "UTCDate":"2019-02-28",\
         "unixTimeStamp":"1551312000",\
         "blockTime_sec":"19.61"\
      }\
   ]
}
```

## [Direct link to heading](https://docs.etherscan.io/api-pro/api-pro?fallback=true\#get-daily-uncle-block-count-and-rewards)    Get Daily Uncle Block Count and Rewards ![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F1052732906-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-McrExXKKJBLJqymbFhO%252Fuploads%252Fgit-blob-80b86ca0904cf1db448758a969151e04dd7415dc%252Fpro_padding_latest.png%3Falt%3Dmedia&width=75&dpr=4&quality=100&sign=fe36a34c&sv=2)

Returns the number of 'Uncle' blocks mined daily and the amount of 'Uncle' block rewards.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/api
   ?module=stats
   &action=dailyuncleblkcount
   &startdate=2019-02-01
   &enddate=2019-02-28
   &sort=asc
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api.etherscan.io/api?module=stats&action=dailyuncleblkcount&startdate=2019-02-01&enddate=2019-02-28&sort=asc&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

startdate

the starting date in `yyyy-MM-dd` format, eg. `2019-02-01`

enddate

the ending date in `yyyy-MM-dd` format, eg. `2019-02-28`

sort

the sorting preference, use `asc` to sort by ascending and `desc` to sort by descending

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "status":"1",
   "message":"OK",
   "result":[\
      {\
         "UTCDate":"2019-02-01",\
         "unixTimeStamp":"1548979200",\
         "uncleBlockCount":287,\
         "uncleBlockRewards_Eth":"729.75"\
      },\
      {\
         "UTCDate":"2019-02-28",\
         "unixTimeStamp":"1551312000",\
         "uncleBlockCount":288,\
         "uncleBlockRewards_Eth":"691.5"\
      }\
   ]
}
```

## [Direct link to heading](https://docs.etherscan.io/api-pro/api-pro?fallback=true\#get-historical-erc20-token-totalsupply-by-contractaddress-and-blockno)    Get Historical ERC20-Token TotalSupply by ContractAddress & BlockNo ![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F1052732906-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-McrExXKKJBLJqymbFhO%252Fuploads%252Fgit-blob-80b86ca0904cf1db448758a969151e04dd7415dc%252Fpro_padding_latest.png%3Falt%3Dmedia&width=75&dpr=4&quality=100&sign=fe36a34c&sv=2)

Returns the amount of an ERC-20 token in circulation at a certain block height.

📝 **Note :** This endpoint is throttled to **2 calls/second** regardless of API Pro tier.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/api
   ?module=stats
   &action=tokensupplyhistory
   &contractaddress=0x57d90b64a1a57749b0f932f1a3395792e12e7055
   &blockno=8000000
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api.etherscan.io/api?module=stats&action=tokensupplyhistory&contractaddress=0x57d90b64a1a57749b0f932f1a3395792e12e7055&blockno=8000000&apikey=YourApiKeyToken) 🔗

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

## [Direct link to heading](https://docs.etherscan.io/api-pro/api-pro?fallback=true\#get-historical-erc20-token-account-balance-for-tokencontractaddress-by-blockno)    Get Historical ERC20-Token Account Balance for TokenContractAddress by BlockNo ![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F1052732906-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-McrExXKKJBLJqymbFhO%252Fuploads%252Fgit-blob-80b86ca0904cf1db448758a969151e04dd7415dc%252Fpro_padding_latest.png%3Falt%3Dmedia&width=75&dpr=4&quality=100&sign=fe36a34c&sv=2)

Returns the balance of an ERC-20 token of an address at a certain block height.

📝 **Note :** This endpoint is throttled to **2 calls/second** regardless of API Pro tier.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/api
   ?module=account
   &action=tokenbalancehistory
   &contractaddress=0x57d90b64a1a57749b0f932f1a3395792e12e7055
   &address=0xe04f27eb70e025b78871a2ad7eabe85e61212761
   &blockno=8000000
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api.etherscan.io/api?module=account&action=tokenbalancehistory&contractaddress=0x57d90b64a1a57749b0f932f1a3395792e12e7055&address=0xe04f27eb70e025b78871a2ad7eabe85e61212761&blockno=8000000&apikey=YourApiKeyToken) 🔗

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

## [Direct link to heading](https://docs.etherscan.io/api-pro/api-pro?fallback=true\#get-token-info-by-contractaddress)    Get Token Info by ContractAddress ![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F1052732906-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-McrExXKKJBLJqymbFhO%252Fuploads%252Fgit-blob-80b86ca0904cf1db448758a969151e04dd7415dc%252Fpro_padding_latest.png%3Falt%3Dmedia&width=75&dpr=4&quality=100&sign=fe36a34c&sv=2)

Returns project information and social media links of an ERC-20/ERC-721 token.

📝 **Note :** This endpoint is throttled to **2 calls/second** regardless of API Pro tier.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/api
   ?module=token
   &action=tokeninfo
   &contractaddress=0x0e3a2a1f2146d86a604adc220b4967a898d7fe07
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api.etherscan.io/api?module=token&action=tokeninfo&contractaddress=0x0e3a2a1f2146d86a604adc220b4967a898d7fe07&apikey=YourApiKeyToken) 🔗

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

## [Direct link to heading](https://docs.etherscan.io/api-pro/api-pro?fallback=true\#get-daily-average-gas-limit)    Get Daily Average Gas Limit ![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F1052732906-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-McrExXKKJBLJqymbFhO%252Fuploads%252Fgit-blob-80b86ca0904cf1db448758a969151e04dd7415dc%252Fpro_padding_latest.png%3Falt%3Dmedia&width=75&dpr=4&quality=100&sign=fe36a34c&sv=2)

Returns the historical daily average gas limit of the Ethereum network.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
 https://api.etherscan.io/api
    ?module=stats
    &action=dailyavggaslimit
    &startdate=2019-02-01
    &enddate=2019-02-28
    &sort=asc
    &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api.etherscan.io/api?module=stats&action=dailyavggaslimit&startdate=2019-02-01&enddate=2019-02-28&sort=asc&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

startdate

the starting date in `yyyy-MM-dd` format, eg. `2019-01-31`

enddate

the ending date in `yyyy-MM-dd` format, eg. `2019-02-28`

sort

the sorting preference, use `asc` to sort by ascending and `desc` to sort by descending

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "status":"1",
   "message":"OK",
   "result":[\
      {\
         "UTCDate":"2019-02-01",\
         "unixTimeStamp":"1548979200",\
         "gasLimit":"8001360"\
      },\
      {\
         "UTCDate":"2019-02-27",\
         "unixTimeStamp":"1551225600",\
         "gasLimit":"8001071"\
      },\
      {\
         "UTCDate":"2019-02-28",\
         "unixTimeStamp":"1551312000",\
         "gasLimit":"8001137"\
      }\
   ]
}
```

## [Direct link to heading](https://docs.etherscan.io/api-pro/api-pro?fallback=true\#get-ethereum-daily-total-gas-used)    Get Ethereum Daily Total Gas Used![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F1052732906-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-McrExXKKJBLJqymbFhO%252Fuploads%252Fgit-blob-80b86ca0904cf1db448758a969151e04dd7415dc%252Fpro_padding_latest.png%3Falt%3Dmedia&width=75&dpr=4&quality=100&sign=fe36a34c&sv=2)

Returns the total amount of gas used daily for transctions on the Ethereum network.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
 https://api.etherscan.io/api
    ?module=stats
    &action=dailygasused
    &startdate=2019-02-01
    &enddate=2019-02-28
    &sort=asc
    &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api.etherscan.io/api?module=stats&action=dailygasused&startdate=2019-02-01&enddate=2019-02-28&sort=asc&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

startdate

the starting date in `yyyy-MM-dd` format, eg. `2019-01-31`

enddate

the ending date in `yyyy-MM-dd` format, eg. `2019-02-28`

sort

the sorting preference, use `asc` to sort by ascending and `desc` to sort by descending

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "status":"1",
   "message":"OK",
   "result":[\
      {\
         "UTCDate":"2019-02-01",\
         "unixTimeStamp":"1548979200",\
         "gasUsed":"32761450415"\
      },\
      {\
         "UTCDate":"2019-02-27",\
         "unixTimeStamp":"1551225600",\
         "gasUsed":"32657440136"\
      },\
      {\
         "UTCDate":"2019-02-28",\
         "unixTimeStamp":"1551312000",\
         "gasUsed":"33081119561"\
      }\
   ]
}
```

## [Direct link to heading](https://docs.etherscan.io/api-pro/api-pro?fallback=true\#get-daily-average-gas-price)    Get Daily Average Gas Price![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F1052732906-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-McrExXKKJBLJqymbFhO%252Fuploads%252Fgit-blob-80b86ca0904cf1db448758a969151e04dd7415dc%252Fpro_padding_latest.png%3Falt%3Dmedia&width=75&dpr=4&quality=100&sign=fe36a34c&sv=2)

Returns the daily average gas price used on the Ethereum network.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
 https://api.etherscan.io/api
    ?module=stats
    &action=dailyavggasprice
    &startdate=2019-02-01
    &enddate=2019-02-28
    &sort=asc
    &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api.etherscan.io/api?module=stats&action=dailyavggasprice&startdate=2019-02-01&enddate=2019-02-28&sort=asc&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

startdate

the starting date in `yyyy-MM-dd` format, eg. `2019-01-31`

enddate

the ending date in `yyyy-MM-dd` format, eg. `2019-02-28`

sort

the sorting preference, use `asc` to sort by ascending and `desc` to sort by descending

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "status":"1",
   "message":"OK",
   "result":[\
      {\
         "UTCDate":"2019-02-01",\
         "unixTimeStamp":"1548979200",\
         "maxGasPrice_Wei":"60814303896257",\
         "minGasPrice_Wei":"432495",\
         "avgGasPrice_Wei":"13234562600"\
      },\
      {\
         "UTCDate":"2019-02-27",\
         "unixTimeStamp":"1551225600",\
         "maxGasPrice_Wei":"42000000000000",\
         "minGasPrice_Wei":"1000000",\
         "avgGasPrice_Wei":"16334617513"\
      },\
      {\
         "UTCDate":"2019-02-28",\
         "unixTimeStamp":"1551312000",\
         "maxGasPrice_Wei":"237222222222257",\
         "minGasPrice_Wei":"100000000",\
         "avgGasPrice_Wei":"18834674068"\
      }\
   ]
}
```

## [Direct link to heading](https://docs.etherscan.io/api-pro/api-pro?fallback=true\#get-daily-network-transaction-fee)    Get Daily Network Transaction Fee ![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F1052732906-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-McrExXKKJBLJqymbFhO%252Fuploads%252Fgit-blob-80b86ca0904cf1db448758a969151e04dd7415dc%252Fpro_padding_latest.png%3Falt%3Dmedia&width=75&dpr=4&quality=100&sign=fe36a34c&sv=2)

Returns the amount of transaction fees paid to miners per day.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/api
   ?module=stats
   &action=dailytxnfee
   &startdate=2019-02-01
   &enddate=2019-02-28
   &sort=asc
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api.etherscan.io/api?module=stats&action=dailytxnfee&startdate=2019-02-01&enddate=2019-02-28&sort=asc&apikey=YourApiKeyToken) 🔗

RequestResponse

No parameters required.

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "status":"1",
   "message":"OK",
   "result":[\
      {\
         "UTCDate":"2019-02-01",\
         "unixTimeStamp":"1548979200",\
         "transactionFee_Eth":"358.558440870590355682"\
      }\
      {\
         "UTCDate":"2019-02-28",\
         "unixTimeStamp":"1551312000",\
         "transactionFee_Eth":"545.141762162356907132"\
      }\
   ]
}
```

## [Direct link to heading](https://docs.etherscan.io/api-pro/api-pro?fallback=true\#get-daily-new-address-count)    Get Daily New Address Count ![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F1052732906-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-McrExXKKJBLJqymbFhO%252Fuploads%252Fgit-blob-80b86ca0904cf1db448758a969151e04dd7415dc%252Fpro_padding_latest.png%3Falt%3Dmedia&width=75&dpr=4&quality=100&sign=fe36a34c&sv=2)

Returns the number of new Ethereum addresses created per day.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/api
   ?module=stats
   &action=dailynewaddress
   &startdate=2019-02-01
   &enddate=2019-02-28
   &sort=asc
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api.etherscan.io/api?module=stats&action=dailynewaddress&startdate=2019-02-01&enddate=2019-02-28&sort=asc&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

startdate

the starting date in `yyyy-MM-dd` format, eg. `2019-02-01`

enddate

the ending date in `yyyy-MM-dd` format, eg. `2019-02-28`

sort

the sorting preference, use `asc` to sort by ascending and `desc` to sort by descending

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "status":"1",
   "message":"OK",
   "result":[\
      {\
         "UTCDate":"2019-02-01",\
         "unixTimeStamp":"1548979200",\
         "newAddressCount":54081\
      },\
      {\
         "UTCDate":"2019-02-28",\
         "unixTimeStamp":"1551312000",\
         "newAddressCount":53117\
      }\
   ]
}
```

## [Direct link to heading](https://docs.etherscan.io/api-pro/api-pro?fallback=true\#get-daily-network-utilization)    Get Daily Network Utilization ![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F1052732906-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-McrExXKKJBLJqymbFhO%252Fuploads%252Fgit-blob-80b86ca0904cf1db448758a969151e04dd7415dc%252Fpro_padding_latest.png%3Falt%3Dmedia&width=75&dpr=4&quality=100&sign=fe36a34c&sv=2)

Returns the daily average gas used over gas limit, in percentage.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/api
   ?module=stats
   &action=dailynetutilization
   &startdate=2019-02-01
   &enddate=2019-02-28
   &sort=asc
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api.etherscan.io/api?module=stats&action=dailynetutilization&startdate=2019-02-01&enddate=2019-02-28&sort=asc&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

startdate

the starting date in `yyyy-MM-dd` format, eg. `2019-02-01`

enddate

the ending date in `yyyy-MM-dd` format, eg. `2019-02-28`

sort

the sorting preference, use `asc` to sort by ascending and `desc` to sort by descending

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "status":"1",
   "message":"OK",
   "result":[\
      {\
         "UTCDate":"2019-02-01",\
         "unixTimeStamp":"1548979200",\
         "networkUtilization":"0.8464"\
      },\
      {\
         "UTCDate":"2019-02-28",\
         "unixTimeStamp":"1551312000",\
         "networkUtilization":"0.9472"\
      }\
   ]
}
```

## [Direct link to heading](https://docs.etherscan.io/api-pro/api-pro?fallback=true\#get-daily-average-network-hash-rate)    Get Daily Average Network Hash Rate ![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F1052732906-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-McrExXKKJBLJqymbFhO%252Fuploads%252Fgit-blob-80b86ca0904cf1db448758a969151e04dd7415dc%252Fpro_padding_latest.png%3Falt%3Dmedia&width=75&dpr=4&quality=100&sign=fe36a34c&sv=2)

Returns the historical measure of processing power of the Ethereum network.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/api
   ?module=stats
   &action=dailyavghashrate
   &startdate=2019-02-01
   &enddate=2019-02-28
   &sort=asc
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api.etherscan.io/api?module=stats&action=dailyavghashrate&startdate=2019-02-01&enddate=2019-02-28&sort=asc&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

startdate

the starting date in `yyyy-MM-dd` format, eg. `2019-02-01`

enddate

the ending date in `yyyy-MM-dd` format, eg. `2019-02-28`

sort

the sorting preference, use `asc` to sort by ascending and `desc` to sort by descending

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "status":"1",
   "message":"OK",
   "result":[\
      {\
         "UTCDate":"2019-02-01",\
         "unixTimeStamp":"1548979200",\
         "networkHashRate":"143116.0140"\
      },\
      {\
         "UTCDate":"2019-02-28",\
         "unixTimeStamp":"1551312000",\
         "networkHashRate":"157689.3983"\
      }\
   ]
}
```

🔥 **Tip :** The `networkHashRate` is represented in [**GigaHashes ( GH/s )**](https://coinguides.org/hashpower-converter-calculator/) **.**

## [Direct link to heading](https://docs.etherscan.io/api-pro/api-pro?fallback=true\#get-daily-transaction-count)    Get Daily Transaction Count ![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F1052732906-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-McrExXKKJBLJqymbFhO%252Fuploads%252Fgit-blob-80b86ca0904cf1db448758a969151e04dd7415dc%252Fpro_padding_latest.png%3Falt%3Dmedia&width=75&dpr=4&quality=100&sign=fe36a34c&sv=2)

Returns the number of transactions performed on the Ethereum blockchain per day.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/api
   ?module=stats
   &action=dailytx
   &startdate=2019-02-01
   &enddate=2019-02-28
   &sort=asc
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api.etherscan.io/api?module=stats&action=dailytx&startdate=2019-02-01&enddate=2019-02-28&sort=asc&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

startdate

the starting date in `yyyy-MM-dd` format, eg. `2019-02-01`

enddate

the ending date in `yyyy-MM-dd` format, eg. `2019-02-28`

sort

the sorting preference, use `asc` to sort by ascending and `desc` to sort by descending

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "status":"1",
   "message":"OK",
   "result":[\
      {\
         "UTCDate":"2019-02-01",\
         "unixTimeStamp":"1548979200",\
         "transactionCount":498856\
      },\
      {\
         "UTCDate":"2019-02-28",\
         "unixTimeStamp":"1551312000",\
         "transactionCount":541458\
      }\
   ]
}
```

## [Direct link to heading](https://docs.etherscan.io/api-pro/api-pro?fallback=true\#get-daily-average-network-difficulty)    Get Daily Average Network Difficulty ![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F1052732906-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-McrExXKKJBLJqymbFhO%252Fuploads%252Fgit-blob-80b86ca0904cf1db448758a969151e04dd7415dc%252Fpro_padding_latest.png%3Falt%3Dmedia&width=75&dpr=4&quality=100&sign=fe36a34c&sv=2)

Returns the historical mining difficulty of the Ethereum network.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/api
   ?module=stats
   &action=dailyavgnetdifficulty
   &startdate=2019-02-01
   &enddate=2019-02-28
   &sort=asc
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api.etherscan.io/api?module=stats&action=dailyavgnetdifficulty&startdate=2019-02-01&enddate=2019-02-28&sort=asc&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

startdate

the starting date in `yyyy-MM-dd` format, eg. `2019-02-01`

enddate

the ending date in `yyyy-MM-dd` format, eg. `2019-02-28`

sort

the sorting preference, use `asc` to sort by ascending and `desc` to sort by descending

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "status":"1",
   "message":"OK",
   "result":[\
      {\
         "UTCDate":"2019-02-01",\
         "unixTimeStamp":"1548979200",\
         "networkDifficulty":"2,408.028"\
      },\
      {\
         "UTCDate":"2019-02-28",\
         "unixTimeStamp":"1551312000",\
         "networkDifficulty":"2,927.453"\
      }\
   ]
}
```

**​** ​ 🔥 **Tip :** The `networkDifficulty` is represented in [**TeraHashes ( TH/s )**](https://coinguides.org/hashpower-converter-calculator/) **.**

## [Direct link to heading](https://docs.etherscan.io/api-pro/api-pro?fallback=true\#get-ether-historical-daily-market-cap)    Get Ether Historical Daily Market Cap ![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F1052732906-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-McrExXKKJBLJqymbFhO%252Fuploads%252Fgit-blob-80b86ca0904cf1db448758a969151e04dd7415dc%252Fpro_padding_latest.png%3Falt%3Dmedia&width=75&dpr=4&quality=100&sign=fe36a34c&sv=2)

Returns the historical Ether daily market capitalization.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/api
   ?module=stats
   &action=ethdailymarketcap
   &startdate=2019-02-01
   &enddate=2019-02-28
   &sort=asc
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api.etherscan.io/api?module=stats&action=ethdailymarketcap&startdate=2019-02-01&enddate=2019-02-28&sort=asc&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

startdate

the starting date in `yyyy-MM-dd` format, eg. `2019-02-01`

enddate

the ending date in `yyyy-MM-dd` format, eg. `2019-02-28`

sort

the sorting preference, use `asc` to sort by ascending and `desc` to sort by descending

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "status":"1",
   "message":"OK",
   "result":[\
      {\
         "UTCDate":"2019-02-01",\
         "unixTimeStamp":"1548979200",\
         "supply":"104672819.281250",\
         "marketCap":"11203.1318476721875",\
         "price":"107.03"\
      },\
      {\
         "UTCDate":"2019-02-28",\
         "unixTimeStamp":"1551312000",\
         "supply":"105048576.406250",\
         "marketCap":"14317.0704784078125",\
         "price":"136.29"\
      }\
   ]
}
```

**​** ​ 💰 **Tip :** The `marketCap` is represented in **million US Dollars ( USD ).**

## [Direct link to heading](https://docs.etherscan.io/api-pro/api-pro?fallback=true\#get-ether-historical-price)    Get Ether Historical Price ![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F1052732906-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-McrExXKKJBLJqymbFhO%252Fuploads%252Fgit-blob-80b86ca0904cf1db448758a969151e04dd7415dc%252Fpro_padding_latest.png%3Falt%3Dmedia&width=75&dpr=4&quality=100&sign=fe36a34c&sv=2)

Returns the historical price of 1 ETH.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/api
   ?module=stats
   &action=ethdailyprice
   &startdate=2019-02-01
   &enddate=2019-02-28
   &sort=asc
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api.etherscan.io/api?module=stats&action=ethdailyprice&startdate=2019-02-01&enddate=2019-02-28&sort=asc&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

startdate

the starting date in `yyyy-MM-dd` format, eg. `2019-02-01`

enddate

the ending date in `yyyy-MM-dd` format, eg. `2019-02-28`

sort

the sorting preference, use `asc` to sort by ascending and `desc` to sort by descending

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "status":"1",
   "message":"OK",
   "result":[\
      {\
         "UTCDate":"2019-02-01",\
         "unixTimeStamp":"1548979200",\
         "value":"107.03"\
      },\
      {\
         "UTCDate":"2019-02-28",\
         "unixTimeStamp":"1551312000",\
         "value":"136.29"\
      }\
   ]
}
```

**​** ​ 💰 **Tip :** The `value` is represented in **US Dollars ( USD ).**

[PreviousEtherscan API PRO](https://docs.etherscan.io/api-pro/etherscan-api-pro) [NextGet All USDT Transfers from Binance](https://docs.etherscan.io/recipes/get-all-usdt-transfers-from-binance)

Last updated 3 years ago

This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject