Endpoints with ![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2Fsg8e76TOnPYfHTGZoQl0%2Fblobs%2FnO0IqZUuuzhIJvlXPnTH%2Fpro.PNG&width=81&dpr=4&quality=100&sign=a2e7a29f&sv=2) are under the API Pro subscription. To upgrade your API plan, browse through the [**Etherscan APIs**](https://etherscan.io/apis) page.

## [Direct link to heading](https://docs.etherscan.io/etherscan-v2/api-endpoints/gas-tracker\#get-estimation-of-confirmation-time)    Get Estimation of Confirmation Time

Returns the estimated time, in seconds, for a transaction to be confirmed on the blockchain.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=gastracker
   &action=gasestimate
   &gasprice=2000000000
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api.etherscan.io/v2/api?chainid=1&module=gastracker&action=gasestimate&gasprice=2000000000&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

gasprice

the price paid per unit of gas, in `wei`

📖 **Tip:** Easily convert Ethereum units using our [**unit converter.**](https://etherscan.io/unitconverter)

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "status":"1",
   "message":"OK",
   "result":"9227"
}
```

📝 **Note:** The `result` is returned in **seconds.**

## [Direct link to heading](https://docs.etherscan.io/etherscan-v2/api-endpoints/gas-tracker\#get-gas-oracle)    Get Gas Oracle

Returns the current Safe, Proposed and Fast gas prices.

Post **EIP-1559** 🔥 changes :

- Safe/Proposed/Fast gas price recommendations are now modeled as Priority Fees.

- New field `suggestBaseFee` , the baseFee of the next pending block

- New field `gasUsedRatio`, to estimate how busy the network is


Learn more about the [**gas changes in EIP-1559.**](https://metamask.io/1559)

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=gastracker
   &action=gasoracle
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api.etherscan.io/v2/api?chainid=1&module=gastracker&action=gasoracle&apikey=YourApiKeyToken) 🔗

RequestResponse

No parameters required.

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "status":"1",
   "message":"OK",
   "result":{
      "LastBlock":"13053741",
      "SafeGasPrice":"20",
      "ProposeGasPrice":"22",
      "FastGasPrice":"24",
      "suggestBaseFee":"19.230609716",
      "gasUsedRatio":"0.370119078777807,0.8954731,0.550911766666667,0.212457033333333,0.552463633333333"
   }
}
```

⛽ **Note:** The gas prices are returned in **Gwei.**

## [Direct link to heading](https://docs.etherscan.io/etherscan-v2/api-endpoints/gas-tracker\#get-daily-average-gas-limit)    Get Daily Average Gas Limit ![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2Fsg8e76TOnPYfHTGZoQl0%2Fblobs%2FUNUGdpodJYN3gil5sSsx%2Fpro_padding_latest.png&width=75&dpr=4&quality=100&sign=d0c300b8&sv=2)

Returns the historical daily average gas limit of the Ethereum network.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
 https://api.etherscan.io/v2/api
    ?chainid=1
   &module=stats
    &action=dailyavggaslimit
    &startdate=2019-02-01
    &enddate=2019-02-28
    &sort=asc
    &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api.etherscan.io/v2/api?chainid=1&module=stats&action=dailyavggaslimit&startdate=2019-02-01&enddate=2019-02-28&sort=asc&apikey=YourApiKeyToken) 🔗

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

## [Direct link to heading](https://docs.etherscan.io/etherscan-v2/api-endpoints/gas-tracker\#get-ethereum-daily-total-gas-used)    Get Ethereum Daily Total Gas Used![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2Fsg8e76TOnPYfHTGZoQl0%2Fblobs%2FUNUGdpodJYN3gil5sSsx%2Fpro_padding_latest.png&width=75&dpr=4&quality=100&sign=d0c300b8&sv=2)

Returns the total amount of gas used daily for transctions on the Ethereum network.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
 https://api.etherscan.io/v2/api
    ?chainid=1
   &module=stats
    &action=dailygasused
    &startdate=2019-02-01
    &enddate=2019-02-28
    &sort=asc
    &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api.etherscan.io/v2/api?chainid=1&module=stats&action=dailygasused&startdate=2019-02-01&enddate=2019-02-28&sort=asc&apikey=YourApiKeyToken) 🔗

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

## [Direct link to heading](https://docs.etherscan.io/etherscan-v2/api-endpoints/gas-tracker\#get-daily-average-gas-price)    Get Daily Average Gas Price![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2Fsg8e76TOnPYfHTGZoQl0%2Fblobs%2FUNUGdpodJYN3gil5sSsx%2Fpro_padding_latest.png&width=75&dpr=4&quality=100&sign=d0c300b8&sv=2)

Returns the daily average gas price used on the Ethereum network.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
 https://api.etherscan.io/v2/api
    ?chainid=1
   &module=stats
    &action=dailyavggasprice
    &startdate=2019-02-01
    &enddate=2019-02-28
    &sort=asc
    &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api.etherscan.io/v2/api?chainid=1&module=stats&action=dailyavggasprice&startdate=2019-02-01&enddate=2019-02-28&sort=asc&apikey=YourApiKeyToken) 🔗

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

[PreviousTokens](https://docs.etherscan.io/etherscan-v2/api-endpoints/tokens) [NextStats](https://docs.etherscan.io/etherscan-v2/api-endpoints/stats-1)

Last updated 5 months ago

This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject