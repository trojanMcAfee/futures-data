The Event Log API was designed to provide an alternative to the native [**eth\_getLogs**](https://eth.wiki/json-rpc/API).

Below are the list of supported filter parameters:

- fromBlock, toBlock, address

- topic0, topic1, topic2, topic3 (32 Bytes per topic)

- topic0\_1\_opr (and\|or between topic0 & topic1), topic1\_2\_opr (and\|or between topic1 & topic2), topic2\_3\_opr (and\|or between topic2 & topic3), topic0\_2\_opr (and\|or between topic0 & topic2), topic0\_3\_opr (and\|or between topic0 & topic3), topic1\_3\_opr (and\|or between topic1 & topic3)


**Some parameters to take note of** 📝

- FromBlock & ToBlock accepts the blocknumber (integer, NOT hex) or 'latest' (earliest & pending is NOT supported yet)

- Topic Operator (opr) choices are either ' **and**' or ' **or**' and are restricted to the above choices only

- FromBlock & ToBlock parameters are required

- An address and/or topic(X) parameters are required, when multiple topic(X) parameters are used the topicX\_X\_opr (and\|or operator) is also required


For performance & security considerations, only the first **1000 results** are return. So please narrow down the filter parameters.

## [Direct link to heading](https://docs.etherscan.io/sepolia-etherscan/api-endpoints/logs\#sample-log-api-queries)    Sample Log API Queries

#### [Direct link to heading](https://docs.etherscan.io/sepolia-etherscan/api-endpoints/logs\#get-event-logs-from-block-number-1092029-to-latest-where-log-address-0x639d4384b429ea4660f377b7a29da)    Get Event Logs from block number 1092029 to 'latest' , where log address = 0x639D4384b429ea4660f377B7A29dAe6d2255090f and topic\[0\] = 0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api-sepolia.etherscan.io/api
   ?module=logs
   &action=getLogs
   &fromBlock=1092029
   &toBlock=latest
   &address=0x639D4384b429ea4660f377B7A29dAe6d2255090f
   &topic0=0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api-sepolia.etherscan.io/api?module=logs&action=getLogs&fromBlock=1092029&toBlock=latest&address=0x639D4384b429ea4660f377B7A29dAe6d2255090f&topic0=0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef&apikey=YourApiKeyToken) 🔗

#### [Direct link to heading](https://docs.etherscan.io/sepolia-etherscan/api-endpoints/logs\#get-event-logs-from-block-number-9433622-to-block-latest-where-log-address-0x5592ec0cfb4dbc12d3ab100)    Get Event Logs from block number 9433622 to block 'latest', where log address = 0x5592ec0cfb4dbc12d3ab100b257153436a1f0fea, topic\[0\] = 0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef 'AND' topic\[1\] = 0x0000000000000000000000008e811410ce01e0244808af95bba906b8ab77a40b

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api-sepolia.etherscan.io/api
   ?module=logs
   &action=getLogs
   &fromBlock=1089604
   &toBlock=latest
   &address=0x64A736Aa55958a41bC1B18590AB7dfCb78444Dd1
   &topic0=0xc3d58168c5ae7397731d063d5bbf3d657854427343f4c083240f7aacaa2d0f62
   &topic0_1_opr=and
   &topic1=0x000000000000000000000000955866ee0bd3b8b0be4d4ea306670f34b90ef3ed
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api-sepolia.etherscan.io/api?module=logs&action=getLogs&fromBlock=1089604&toBlock=latest&address=0x64A736Aa55958a41bC1B18590AB7dfCb78444Dd1&topic0=0xc3d58168c5ae7397731d063d5bbf3d657854427343f4c083240f7aacaa2d0f62&topic0_1_opr=and&topic1=0x000000000000000000000000955866ee0bd3b8b0be4d4ea306670f34b90ef3ed&apikey=YourApiKeyToken) 🔗

[PreviousBlocks](https://docs.etherscan.io/sepolia-etherscan/api-endpoints/blocks) [NextGeth/Parity Proxy](https://docs.etherscan.io/sepolia-etherscan/api-endpoints/geth-parity-proxy)

Last updated 2 years ago

This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject