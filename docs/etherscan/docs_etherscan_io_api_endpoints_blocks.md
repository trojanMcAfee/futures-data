Endpoints with ![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F1052732906-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-McrExXKKJBLJqymbFhO%252Fuploads%252Fgit-blob-847813a741fd3ea768e70bdba58451fc9b87492e%252Fpro.PNG%3Falt%3Dmedia&width=81&dpr=4&quality=100&sign=8d112ea1&sv=2) are under the API Pro subscription. To upgrade your API plan, browse through the [**Etherscan APIs**](https://etherscan.io/apis) page.

## [Direct link to heading](https://docs.etherscan.io/api-endpoints/blocks\#get-block-and-uncle-rewards-by-blockno)    Get Block And Uncle Rewards by BlockNo

Returns the block reward and 'Uncle' block rewards.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/api
   ?module=block
   &action=getblockreward
   &blockno=2165403
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api.etherscan.io/api?module=block&action=getblockreward&blockno=2165403&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

blockno

the `integer` block number to check block rewards for eg. [`12697906`](https://etherscan.io/block/12697906)

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "status":"1",
   "message":"OK",
   "result":{
      "blockNumber":"2165403",
      "timeStamp":"1472533979",
      "blockMiner":"0x13a06d3dfe21e0db5c016c03ea7d2509f7f8d1e3",
      "blockReward":"5314181600000000000",
      "uncles":[\
         {\
            "miner":"0xbcdfc35b86bedf72f0cda046a3c16829a2ef41d1",\
            "unclePosition":"0",\
            "blockreward":"3750000000000000000"\
         },\
         {\
            "miner":"0x0d0c9855c722ff0c78f21e43aa275a5b8ea60dce",\
            "unclePosition":"1",\
            "blockreward":"3750000000000000000"\
         }\
      ],
      "uncleInclusionReward":"312500000000000000"
   }
}
```

​​ ⏳ **Tip :** The `timestamp` field is denoted in [**Unix timestamp.**](https://www.unixtimestamp.com/)

## [Direct link to heading](https://docs.etherscan.io/api-endpoints/blocks\#get-estimated-block-countdown-time-by-blockno)    Get Estimated Block Countdown Time by BlockNo

Returns the estimated time remaining, in seconds, until a certain block is mined.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/api
   ?module=block
   &action=getblockcountdown
   &blockno=16701588
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api.etherscan.io/api?module=block&action=getblockcountdown&blockno=16701588&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

blockno

the `integer` block number to estimate time remaining to be mined eg. [`12697906`](https://etherscan.io/block/12697906)

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "status":"1",
   "message":"OK",
   "result":{
      "CurrentBlock":"12715477",
      "CountdownBlock":"16701588",
      "RemainingBlock":"3986111",
      "EstimateTimeInSec":"52616680.2"
   }
}
```

## [Direct link to heading](https://docs.etherscan.io/api-endpoints/blocks\#get-block-number-by-timestamp)    Get Block Number by Timestamp

Returns the block number that was mined at a certain timestamp.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/api
   ?module=block
   &action=getblocknobytime
   &timestamp=1578638524
   &closest=before
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api.etherscan.io/api?module=block&action=getblocknobytime&timestamp=1578638524&closest=before&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

timestamp

the `integer` representing the Unix timestamp in **seconds**.

closest

the closest available block to the provided timestamp, either `before` or `after`

⏳ **Tip :** Convert a regular date-time to a [**Unix timestamp.**](https://www.unixtimestamp.com/)

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "status":"1",
   "message":"OK",
   "result":"12712551"
}
```

## [Direct link to heading](https://docs.etherscan.io/api-endpoints/blocks\#get-daily-average-block-size)    Get Daily Average Block Size ![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F1052732906-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-McrExXKKJBLJqymbFhO%252Fuploads%252Fgit-blob-80b86ca0904cf1db448758a969151e04dd7415dc%252Fpro_padding_latest.png%3Falt%3Dmedia&width=75&dpr=4&quality=100&sign=fe36a34c&sv=2)

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

## [Direct link to heading](https://docs.etherscan.io/api-endpoints/blocks\#get-daily-block-count-and-rewards)    Get Daily Block Count and Rewards ![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F1052732906-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-McrExXKKJBLJqymbFhO%252Fuploads%252Fgit-blob-80b86ca0904cf1db448758a969151e04dd7415dc%252Fpro_padding_latest.png%3Falt%3Dmedia&width=75&dpr=4&quality=100&sign=fe36a34c&sv=2)

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

## [Direct link to heading](https://docs.etherscan.io/api-endpoints/blocks\#get-daily-block-rewards)    Get Daily Block Rewards ![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F1052732906-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-McrExXKKJBLJqymbFhO%252Fuploads%252Fgit-blob-80b86ca0904cf1db448758a969151e04dd7415dc%252Fpro_padding_latest.png%3Falt%3Dmedia&width=75&dpr=4&quality=100&sign=fe36a34c&sv=2)

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

## [Direct link to heading](https://docs.etherscan.io/api-endpoints/blocks\#get-daily-average-time-for-a-block-to-be-included-in-the-ethereum-blockchain)    Get Daily Average Time for A Block to be Included in the Ethereum Blockchain ![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F1052732906-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-McrExXKKJBLJqymbFhO%252Fuploads%252Fgit-blob-80b86ca0904cf1db448758a969151e04dd7415dc%252Fpro_padding_latest.png%3Falt%3Dmedia&width=75&dpr=4&quality=100&sign=fe36a34c&sv=2)

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

## [Direct link to heading](https://docs.etherscan.io/api-endpoints/blocks\#get-daily-uncle-block-count-and-rewards)    Get Daily Uncle Block Count and Rewards ![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F1052732906-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-McrExXKKJBLJqymbFhO%252Fuploads%252Fgit-blob-80b86ca0904cf1db448758a969151e04dd7415dc%252Fpro_padding_latest.png%3Falt%3Dmedia&width=75&dpr=4&quality=100&sign=fe36a34c&sv=2)

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

[PreviousTransactions](https://docs.etherscan.io/api-endpoints/stats) [NextLogs](https://docs.etherscan.io/api-endpoints/logs)

Last updated 3 years ago

This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject