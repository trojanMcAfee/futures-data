
GET BLOCK NUMBER BY TIMESTAMP

To get the block number by timestamp using the Etherscan API, you can call the following endpoint:

https://api.etherscan.io/api?module=block&action=getblocknobytime&timestamp=YOUR_TIMESTAMP&closest=before&apikey=YourApiKeyToken

Replace YOUR_TIMESTAMP with the Unix timestamp (in seconds) for which you wish to find the closest block. The closest parameter can be set to either before or after depending on whether you want the block mined immediately before or after the given timestamp.


GET HISTORICAL PRICE OF ETH AT A SPECIFIC UNIX TIMESTAMP

You can use the Get Ether Historical Price endpoint from Etherscan to retrieve the historical price of ETH. However, note that this endpoint accepts dates (in yyyy-MM-dd format) as parameters, not a Unix timestamp directly. To get the historical price at a specific Unix timestamp, you would first convert the Unix timestamp into a date. Then, using that date as both the startdate and enddate in the API call, you can retrieve the price data for that day. For example:

https://api.etherscan.io/api?module=stats&action=ethdailyprice&startdate=YYYY-MM-DD&enddate=YYYY-MM-DD&sort=asc&apikey=YourApiKeyToken

Replace YYYY-MM-DD with the date corresponding to your Unix timestamp.

This approach returns an array of objects, each containing a unixTimeStamp field and the value (price in USD) for that date. Pick the record having the matching or nearest Unix timestamp.


