## [Direct link to heading](https://docs.etherscan.io/holesky-etherscan/api-endpoints/blocks\#get-block-and-uncle-rewards-by-blockno)    Get Block And Uncle Rewards by BlockNo

Returns the block reward and 'Uncle' block rewards.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api-holesky.etherscan.io/api
   ?module=block
   &action=getblockreward
   &blockno=1090932
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api-holesky.etherscan.io/api?module=block&action=getblockreward&blockno=1090932&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

blockno

the `integer` block number to check block rewards for eg. `12697906`

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "status":"1",
   "message":"OK",
   "result":{
      "blockNumber":"1090932",
      "timeStamp":"1652449149",
      "blockMiner":"0xd87def8bbd2c4d59494611ab259a2005c154212a",
      "blockReward":"2000031500000000000",
      "uncles":[\
\
      ],
      "uncleInclusionReward":"0"
   }
}
```

​​ ⏳ **Tip :** The `timestamp` field is denoted in [**Unix timestamp.**](https://www.unixtimestamp.com/)

## [Direct link to heading](https://docs.etherscan.io/holesky-etherscan/api-endpoints/blocks\#get-estimated-block-countdown-time-by-blockno)    Get Estimated Block Countdown Time by BlockNo

Returns the estimated time remaining, in seconds, until a certain block is mined.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api-holesky.etherscan.io/api
   ?module=block
   &action=getblockcountdown
   &blockno=1090932
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api-holesky.etherscan.io/api?module=block&action=getblockcountdown&blockno=9588666&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

blockno

the `integer` block number to estimate time remaining to be mined eg. `12697906`

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "status":"1",
   "message":"OK",
   "result":{
      "CurrentBlock":"9548810",
      "CountdownBlock":"9588666",
      "RemainingBlock":"39856",
      "EstimateTimeInSec":"577927.0"
   }
}
```

## [Direct link to heading](https://docs.etherscan.io/holesky-etherscan/api-endpoints/blocks\#get-block-number-by-timestamp)    Get Block Number by Timestamp

Returns the block number that was mined at a certain timestamp.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api-holesky.etherscan.io/api
   ?module=block
   &action=getblocknobytime
   &timestamp=1652459409
   &closest=before
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api-holesky.etherscan.io/api?module=block&action=getblocknobytime&timestamp=1652459409&closest=before&apikey=YourApiKeyToken) 🔗

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
   "result":"1091685"
}
```

[PreviousTransactions](https://docs.etherscan.io/holesky-etherscan/api-endpoints/stats) [NextLogs](https://docs.etherscan.io/holesky-etherscan/api-endpoints/logs)

Last updated 10 months ago

This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject