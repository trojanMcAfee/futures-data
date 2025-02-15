## [Direct link to heading](https://docs.etherscan.io/etherscan-v2/api-endpoints/logs\#get-event-logs-by-address)    Get Event Logs by Address

Returns the event logs from an address, with optional filtering by block range.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=logs
   &action=getLogs
   &address=0xbd3531da5cf5857e7cfaa92426877b022e612cf8
   &fromBlock=12878196
   &toBlock=12878196
   &page=1
   &offset=1000
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api.etherscan.io/v2/api?chainid=1&module=logs&action=getLogs&address=0xbd3531da5cf5857e7cfaa92426877b022e612cf8&fromBlock=12878196&toBlock=12878196&page=1&offset=1000&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

address

the `string` representing the address to check for logs

fromBlock

the `integer` block number to start searching for logs eg. `12878196`

toBlock

the `integer` block number to stop searching for logs eg. `12879196`

page

the `integer` page number, if pagination is enabled

offset

the number of transactions displayed per page

limited to **1000 records** per query, use the `page` parameter for subsequent records

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "status":"1",
   "message":"OK",
   "result":[\
      {\
         "address":"0xbd3531da5cf5857e7cfaa92426877b022e612cf8",\
         "topics":[\
            "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef",\
            "0x0000000000000000000000000000000000000000000000000000000000000000",\
            "0x000000000000000000000000c45a4b3b698f21f88687548e7f5a80df8b99d93d",\
            "0x00000000000000000000000000000000000000000000000000000000000000b5"\
         ],\
         "data":"0x",\
         "blockNumber":"0xc48174",\
         "timeStamp":"0x60f9ce56",\
         "gasPrice":"0x2e90edd000",\
         "gasUsed":"0x247205",\
         "logIndex":"0x",\
         "transactionHash":"0x4ffd22d986913d33927a392fe4319bcd2b62f3afe1c15a2c59f77fc2cc4c20a9",\
         "transactionIndex":"0x"\
      },\
      {\
         "address":"0xbd3531da5cf5857e7cfaa92426877b022e612cf8",\
         "topics":[\
            "0x645f26e653c951cec836533f8fe0616d301c20a17153debc17d7c3dbe4f32b28",\
            "0x00000000000000000000000000000000000000000000000000000000000000b5"\
         ],\
         "data":"0x",\
         "blockNumber":"0xc48174",\
         "timeStamp":"0x60f9ce56",\
         "gasPrice":"0x2e90edd000",\
         "gasUsed":"0x247205",\
         "logIndex":"0x1",\
         "transactionHash":"0x4ffd22d986913d33927a392fe4319bcd2b62f3afe1c15a2c59f77fc2cc4c20a9",\
         "transactionIndex":"0x"\
      }\
   ]
}
```

## [Direct link to heading](https://docs.etherscan.io/etherscan-v2/api-endpoints/logs\#get-event-logs-by-topics)    Get Event Logs by Topics

Returns the events log in a block range, filtered by topics.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=logs
   &action=getLogs
   &fromBlock=12878196
   &toBlock=12879196
   &topic0=0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef
   &topic0_1_opr=and
   &topic1=0x0000000000000000000000000000000000000000000000000000000000000000
   &page=1
   &offset=1000
   &apikey=YourApiKeyToken
```

Usage:

- For a single topic, specify the topic number such as `topic0`, `topic1`, `topic2`, `topic3`

- For multiple topics, specify the topic numbers **and** topic operator either `and` or `or` such as below

topic0\_1\_opr (and\|or between topic0 & topic1), topic1\_2\_opr (and\|or between topic1 & topic2) topic2\_3\_opr (and\|or between topic2 & topic3), topic0\_2\_opr (and\|or between topic0 & topic2) topic0\_3\_opr (and\|or between topic0 & topic3), topic1\_3\_opr (and\|or between topic1 & topic3)


> Try this endpoint in your [**browser**](https://api.etherscan.io/v2/api?chainid=1&module=logs&action=getLogs&fromBlock=12878196&toBlock=12879196&topic0=0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef&topic0_1_opr=and&topic1=0x0000000000000000000000000000000000000000000000000000000000000000&page=1&offset=1000&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

fromBlock

the `integer` block number to start searching for logs eg. `12878196`

toBlock

the `integer` block number to stop searching for logs eg. `12879196`

topic

the topic numbers to search for

limited to `topic0`, `topic1`, `topic2`, `topic3`

topicOperator

the topic operator when multiple topic combinations are used

limited to `and` or `or`

page

the `integer` page number, if pagination is enabled

offset

the number of transactions displayed per page

limited to **1000 records** per query, use the `page` parameter for subsequent records

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "status":"1",
   "message":"OK",
   "result":[\
      {\
         "address":"0xbd3531da5cf5857e7cfaa92426877b022e612cf8",\
         "topics":[\
            "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef",\
            "0x0000000000000000000000000000000000000000000000000000000000000000",\
            "0x000000000000000000000000c45a4b3b698f21f88687548e7f5a80df8b99d93d",\
            "0x00000000000000000000000000000000000000000000000000000000000000b5"\
         ],\
         "data":"0x",\
         "blockNumber":"0xc48174",\
         "timeStamp":"0x60f9ce56",\
         "gasPrice":"0x2e90edd000",\
         "gasUsed":"0x247205",\
         "logIndex":"0x",\
         "transactionHash":"0x4ffd22d986913d33927a392fe4319bcd2b62f3afe1c15a2c59f77fc2cc4c20a9",\
         "transactionIndex":"0x"\
      },\
      {\
         "address":"0xbd3531da5cf5857e7cfaa92426877b022e612cf8",\
         "topics":[\
            "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef",\
            "0x0000000000000000000000000000000000000000000000000000000000000000",\
            "0x000000000000000000000000c45a4b3b698f21f88687548e7f5a80df8b99d93d",\
            "0x00000000000000000000000000000000000000000000000000000000000000b6"\
         ],\
         "data":"0x",\
         "blockNumber":"0xc48174",\
         "timeStamp":"0x60f9ce56",\
         "gasPrice":"0x2e90edd000",\
         "gasUsed":"0x247205",\
         "logIndex":"0x2",\
         "transactionHash":"0x4ffd22d986913d33927a392fe4319bcd2b62f3afe1c15a2c59f77fc2cc4c20a9",\
         "transactionIndex":"0x"\
      }\
   ]
}
```

## [Direct link to heading](https://docs.etherscan.io/etherscan-v2/api-endpoints/logs\#get-event-logs-by-address-filtered-by-topics)    Get Event Logs by Address filtered by Topics

Returns the event logs from an address, filtered by topics and block range.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=logs
   &action=getLogs
   &fromBlock=15073139
   &toBlock=15074139
   &address=0x59728544b08ab483533076417fbbb2fd0b17ce3a
   &topic0=0x27c4f0403323142b599832f26acd21c74a9e5b809f2215726e244a4ac588cd7d
   &topic0_1_opr=and
   &topic1=0x00000000000000000000000023581767a106ae21c074b2276d25e5c3e136a68b
   &page=1
   &offset=1000
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api.etherscan.io/v2/api?chainid=1&module=logs&action=getLogs&fromBlock=15073139&toBlock=15074139&address=0x59728544b08ab483533076417fbbb2fd0b17ce3a&topic0=0x27c4f0403323142b599832f26acd21c74a9e5b809f2215726e244a4ac588cd7d&topic0_1_opr=and&topic1=0x00000000000000000000000023581767a106ae21c074b2276d25e5c3e136a68b&page=1&offset=1000&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

fromBlock

the `integer` block number to start searching for logs eg. `12878196`

toBlock

the `integer` block number to stop searching for logs eg. `12879196`

address

the `string` representing the address to check for logs

topic

the topic numbers to search for

limited to `topic0`, `topic1`, `topic2`, `topic3`

topicOperator

the topic operator when multiple topic combinations are used

limited to `and` or `or`

page

the `integer` page number, if pagination is enabled

offset

the number of transactions displayed per page

limited to **1000 records** per query, use the `page` parameter for subsequent records

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "status":"1",
   "message":"OK",
   "result":[\
      {\
         "address":"0x59728544b08ab483533076417fbbb2fd0b17ce3a",\
         "topics":[\
            "0x27c4f0403323142b599832f26acd21c74a9e5b809f2215726e244a4ac588cd7d",\
            "0x00000000000000000000000023581767a106ae21c074b2276d25e5c3e136a68b",\
            "0x000000000000000000000000000000000000000000000000000000000000236d",\
            "0x000000000000000000000000c8a5592031f93debea5d9e67a396944ee01bb2ca"\
         ],\
         "data":"0x000000000000000000000000c02aaa39b223fe8d0a0e5c4f27ead9083c756cc20000000000000000000000000000000000000000000000000f207539952d0000",\
         "blockNumber":"0xe60262",\
         "timeStamp":"0x62c26caf",\
         "gasPrice":"0x5e2d742c9",\
         "gasUsed":"0xfb7f8",\
         "logIndex":"0x4b",\
         "transactionHash":"0x26fe1a0a403fd44ef11ee72f3b4ceff590b6ea533684cb279cb4242be463304c",\
         "transactionIndex":"0x39"\
      },\
      {\
         "address":"0x59728544b08ab483533076417fbbb2fd0b17ce3a",\
         "topics":[\
            "0x27c4f0403323142b599832f26acd21c74a9e5b809f2215726e244a4ac588cd7d",\
            "0x00000000000000000000000023581767a106ae21c074b2276d25e5c3e136a68b",\
            "0x0000000000000000000000000000000000000000000000000000000000002261",\
            "0x000000000000000000000000c8a5592031f93debea5d9e67a396944ee01bb2ca"\
         ],\
         "data":"0x000000000000000000000000c02aaa39b223fe8d0a0e5c4f27ead9083c756cc20000000000000000000000000000000000000000000000000de0b6b3a7640000",\
         "blockNumber":"0xe6035b",\
         "timeStamp":"0x62c27ab1",\
         "gasPrice":"0x27e523173",\
         "gasUsed":"0x3b86e",\
         "logIndex":"0x1d7",\
         "transactionHash":"0x3a299413cf2c91e376e542efcf3fc308c562da79af6e992401217cc6208c7f74",\
         "transactionIndex":"0x92"\
      }\
   ]
}
```

[PreviousBlocks](https://docs.etherscan.io/etherscan-v2/api-endpoints/blocks) [NextGeth/Parity Proxy](https://docs.etherscan.io/etherscan-v2/api-endpoints/geth-parity-proxy)

Last updated 5 months ago

This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject