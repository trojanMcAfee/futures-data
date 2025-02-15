Endpoints with ![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F1052732906-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-McrExXKKJBLJqymbFhO%252Fuploads%252Fgit-blob-847813a741fd3ea768e70bdba58451fc9b87492e%252Fpro.PNG%3Falt%3Dmedia&width=81&dpr=4&quality=100&sign=8d112ea1&sv=2) are under the API Pro subscription. To upgrade your API plan, kindly visit [**Etherscan API Pro**](https://etherscan.io/apis) **.**

## [Direct link to heading](https://docs.etherscan.io/api-endpoints/stats-1\#get-total-supply-of-ether)    Get Total Supply of Ether

Returns the current amount of Ether in circulation excluding ETH2 Staking rewards and EIP1559 burnt fees.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/api
   ?module=stats
   &action=ethsupply
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api.etherscan.io/api?module=stats&action=ethsupply&apikey=YourApiKeyToken) 🔗

RequestResponse

No parameters required.

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "status":"1",
   "message":"OK",
   "result":"116487067186500000000000000"
}
```

📖 **Tip :** Easily convert Ethereum units using our [**unit converter.**](https://etherscan.io/unitconverter)

## [Direct link to heading](https://docs.etherscan.io/api-endpoints/stats-1\#get-total-supply-of-ether-2)    Get Total Supply of Ether 2

Returns the current amount of Ether in circulation, ETH2 Staking rewards, EIP1559 burnt fees, and total withdrawn ETH from the beacon chain.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/api
   ?module=stats
   &action=ethsupply2
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api.etherscan.io/api?module=stats&action=ethsupply2&apikey=YourApiKeyToken) 🔗

RequestResponse

No parameters required.

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "status":"1",
   "message":"OK",
   "result":{
      "EthSupply":"122373866217800000000000000",
      "Eth2Staking":"1157529105115885000000000",
      "BurntFees":"3102505506455601519229842",
      "WithdrawnTotal":"1170200333006131000000000"
   }
}
```

📝 **Note:** The `EthSupply` is calculated **before** adding ETH minted as `Eth2Staking` rewards and subtracting `BurntFees` from EIP-1559.

For more information, check out our [**Ether Total Supply Dashboard.**](https://etherscan.io/stat/supply)

## [Direct link to heading](https://docs.etherscan.io/api-endpoints/stats-1\#get-ether-last-price)    Get Ether Last Price

Returns the latest price of 1 ETH.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/api
   ?module=stats
   &action=ethprice
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api.etherscan.io/api?module=stats&action=ethprice&apikey=YourApiKeyToken) 🔗

RequestResponse

No parameters required.

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "status":"1",
   "message":"OK",
   "result":{
      "ethbtc":"0.06116",
      "ethbtc_timestamp":"1624961308",
      "ethusd":"2149.18",
      "ethusd_timestamp":"1624961308"
   }
}
```

⏳ **Tip :** The `timestamps` are represented in [**Unix timestamp.**](https://www.unixtimestamp.com/)

## [Direct link to heading](https://docs.etherscan.io/api-endpoints/stats-1\#get-ethereum-nodes-size)    Get Ethereum Nodes Size

Returns the size of the Ethereum blockchain, in bytes, over a date range.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/api
   ?module=stats
   &action=chainsize
   &startdate=2019-02-01
   &enddate=2019-02-28
   &clienttype=geth
   &syncmode=default
   &sort=asc
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api.etherscan.io/api?module=stats&action=chainsize&startdate=2019-02-01&enddate=2019-02-28&clienttype=geth&syncmode=default&sort=asc&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

startdate

the starting date in `yyyy-MM-dd` format, eg. `2019-02-01`

enddate

the ending date in `yyyy-MM-dd` format, eg. `2019-02-28`

clienttype

the Ethereum [node client](https://ethereum.org/en/developers/docs/nodes-and-clients/) to use, either `geth` or `parity`

syncmode

the [type of node](https://ethereum.org/en/developers/docs/nodes-and-clients/) to run, either `default` or `archive`

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
         "blockNumber":"7156164",\
         "chainTimeStamp":"2019-02-01",\
         "chainSize":"184726421279",\
         "clientType":"Geth",\
         "syncMode":"Default"\
      }\
      {\
         "blockNumber":"7276521",\
         "chainTimeStamp":"2019-02-28",\
         "chainSize":"197073145113",\
         "clientType":"Geth",\
         "syncMode":"Default"\
      }\
   ]
}
```

⛓️ **Tip :** The `chainSize` is represented in **bytes.**

## [Direct link to heading](https://docs.etherscan.io/api-endpoints/stats-1\#get-total-nodes-count)    Get Total Nodes Count

Returns the total number of discoverable Ethereum nodes.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/api
   ?module=stats
   &action=nodecount
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api.etherscan.io/api?module=stats&action=nodecount&apikey=YourApiKeyToken) 🔗

RequestResponse

No parameters required.

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "status":"1",
   "message":"OK",
   "result":{
      "UTCDate":"2021-06-29",
      "TotalNodeCount":"6413"
   }
}
```

## [Direct link to heading](https://docs.etherscan.io/api-endpoints/stats-1\#get-daily-network-transaction-fee)    Get Daily Network Transaction Fee ![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F1052732906-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-McrExXKKJBLJqymbFhO%252Fuploads%252Fgit-blob-80b86ca0904cf1db448758a969151e04dd7415dc%252Fpro_padding_latest.png%3Falt%3Dmedia&width=75&dpr=4&quality=100&sign=fe36a34c&sv=2)

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

## [Direct link to heading](https://docs.etherscan.io/api-endpoints/stats-1\#get-daily-new-address-count)    Get Daily New Address Count ![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F1052732906-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-McrExXKKJBLJqymbFhO%252Fuploads%252Fgit-blob-80b86ca0904cf1db448758a969151e04dd7415dc%252Fpro_padding_latest.png%3Falt%3Dmedia&width=75&dpr=4&quality=100&sign=fe36a34c&sv=2)

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

## [Direct link to heading](https://docs.etherscan.io/api-endpoints/stats-1\#get-daily-network-utilization)    Get Daily Network Utilization ![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F1052732906-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-McrExXKKJBLJqymbFhO%252Fuploads%252Fgit-blob-80b86ca0904cf1db448758a969151e04dd7415dc%252Fpro_padding_latest.png%3Falt%3Dmedia&width=75&dpr=4&quality=100&sign=fe36a34c&sv=2)

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

## [Direct link to heading](https://docs.etherscan.io/api-endpoints/stats-1\#get-daily-average-network-hash-rate)    Get Daily Average Network Hash Rate ![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F1052732906-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-McrExXKKJBLJqymbFhO%252Fuploads%252Fgit-blob-80b86ca0904cf1db448758a969151e04dd7415dc%252Fpro_padding_latest.png%3Falt%3Dmedia&width=75&dpr=4&quality=100&sign=fe36a34c&sv=2)

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

## [Direct link to heading](https://docs.etherscan.io/api-endpoints/stats-1\#get-daily-transaction-count)    Get Daily Transaction Count ![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F1052732906-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-McrExXKKJBLJqymbFhO%252Fuploads%252Fgit-blob-80b86ca0904cf1db448758a969151e04dd7415dc%252Fpro_padding_latest.png%3Falt%3Dmedia&width=75&dpr=4&quality=100&sign=fe36a34c&sv=2)

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

## [Direct link to heading](https://docs.etherscan.io/api-endpoints/stats-1\#get-daily-average-network-difficulty)    Get Daily Average Network Difficulty ![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F1052732906-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-McrExXKKJBLJqymbFhO%252Fuploads%252Fgit-blob-80b86ca0904cf1db448758a969151e04dd7415dc%252Fpro_padding_latest.png%3Falt%3Dmedia&width=75&dpr=4&quality=100&sign=fe36a34c&sv=2)

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

## [Direct link to heading](https://docs.etherscan.io/api-endpoints/stats-1\#get-ether-historical-price)    Get Ether Historical Price ![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F1052732906-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-McrExXKKJBLJqymbFhO%252Fuploads%252Fgit-blob-80b86ca0904cf1db448758a969151e04dd7415dc%252Fpro_padding_latest.png%3Falt%3Dmedia&width=75&dpr=4&quality=100&sign=fe36a34c&sv=2)

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

[PreviousGas Tracker](https://docs.etherscan.io/api-endpoints/gas-tracker) [NextEtherscan API PRO](https://docs.etherscan.io/api-pro/etherscan-api-pro)

Last updated 10 days ago

This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject