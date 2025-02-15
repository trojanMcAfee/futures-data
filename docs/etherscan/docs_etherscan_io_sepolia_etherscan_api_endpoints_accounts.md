## [Direct link to heading](https://docs.etherscan.io/sepolia-etherscan/api-endpoints/accounts\#get-ether-balance-for-a-single-address)    Get Ether Balance for a Single Address

Returns the Ether balance of a given address.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api-sepolia.etherscan.io/api
   ?module=account
   &action=balance
   &address=0x382b4ca2c4a7cd28c1c400c69d81ec2b2637f7dd
   &tag=latest
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api-sepolia.etherscan.io/api?module=account&action=balance&address=0x382b4ca2c4a7cd28c1c400c69d81ec2b2637f7dd&tag=latest&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

address

the `string` representing the address to check for balance

tag

the `string` pre-defined block parameter, either `earliest`, `pending` or `latest`

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "status":"1",
   "message":"OK",
   "result":"206796937658929992503000"
}
```

📖 **Tip:** The `result` is returned in [**wei.**](https://sepolia.etherscan.io/unitconverter)

Convert Ethereum units using our [**Unit Converter.**](https://sepolia.etherscan.io/unitconverter)

## [Direct link to heading](https://docs.etherscan.io/sepolia-etherscan/api-endpoints/accounts\#get-ether-balance-for-multiple-addresses-in-a-single-call)    Get Ether Balance for Multiple Addresses in a Single Call

Returns the balance of the accounts from a list of addresses.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api-sepolia.etherscan.io/api
   ?module=account
   &action=balancemulti
   &address=https://api-sepolia.etherscan.io/api?module=account&action=balance&address=0x382b4ca2c4a7cd28c1c400c69d81ec2b2637f7dd,0x382b4ca2c4a7cd28c1c400c69d81ec2b2637f7dd,0x8a5847fd0e592b058c026c5fdc322aee834b87f5&tag=latest&apikey=YourApiKeyToken,0x63a9dbCe75413036B2B778E670aaBd4493aAF9F3,0xd82b6aB1f20A21484fA5E28221B95425dddC5E8E
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api-sepolia.etherscan.io/api?module=account&action=balancemulti&address=0x382b4ca2c4a7cd28c1c400c69d81ec2b2637f7dd,0x382b4ca2c4a7cd28c1c400c69d81ec2b2637f7dd,0x8a5847fd0e592b058c026c5fdc322aee834b87f5&tag=latest&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

address

the `strings` representing the addresses to check for balance, separated by `,` commas

up to **20 addresses** per call

tag

the `integer` pre-defined block parameter, either `earliest`, `pending` or `latest`

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "status":"1",
   "message":"OK",
   "result":[\
      {\
         "account":"0x382b4ca2c4a7cd28c1c400c69d81ec2b2637f7dd",\
         "balance":"206796937658929992503000"\
      },\
      {\
         "account":"0x382b4ca2c4a7cd28c1c400c69d81ec2b2637f7dd",\
         "balance":"206796937658929992503000"\
      },\
      {\
         "account":"0x8a5847fd0e592b058c026c5fdc322aee834b87f5",\
         "balance":"16288712393992050891"\
      }\
   ]
}
```

📖 **Tip:** The `result` is returned in [**wei.**](https://sepolia.etherscan.io/unitconverter)

Convert Ethereum units using our [**Unit Converter.**](https://sepolia.etherscan.io/unitconverter)

## [Direct link to heading](https://docs.etherscan.io/sepolia-etherscan/api-endpoints/accounts\#get-a-list-of-normal-transactions-by-address)    Get a list of 'Normal' Transactions By Address

Returns the list of transactions performed by an address, with optional pagination.

**​** ​ ​ 📝 **Note :** This API endpoint returns a maximum of **10000 records** only.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api-sepolia.etherscan.io/api
   ?module=account
   &action=txlist
   &address=0x382b4ca2c4a7cd28c1c400c69d81ec2b2637f7dd
   &startblock=0
   &endblock=99999999
   &page=1
   &offset=10
   &sort=asc
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api-sepolia.etherscan.io/api?module=account&action=txlist&address=0x382b4ca2c4a7cd28c1c400c69d81ec2b2637f7dd&startblock=0&endblock=99999999&page=1&offset=10&sort=asc&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

address

the `string` representing the addresses to check for balance

startblock

the `integer` block number to start searching for transactions

endblock

the `integer` block number to stop searching for transactions

page

the `integer` page number, if pagination is enabled

offset

the number of transactions displayed per page

sort

the sorting preference, use `asc` to sort by ascending and `desc` to sort by descending

💡 **Tip:** Specify a smaller `startblock` and `endblock` range for faster search results.

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "status":"1",
   "message":"OK-Missing/Invalid API Key, rate limit of 1/5sec applied",
   "result":[\
      {\
         "blockNumber":"1037571",\
         "timeStamp":"1651759857",\
         "hash":"0x710e53707c79dd438a8bc3db2a45a123af6dba0d4a653a134035306d11f415fd",\
         "nonce":"5",\
         "blockHash":"0x64201f8940cee65186f64adb68a99fe3da0450bc9490617aeedd08f80cb8e29b",\
         "transactionIndex":"0",\
         "from":"0x10f5d45854e038071485ac9e402308cf80d2d2fe",\
         "to":"0x382b4ca2c4a7cd28c1c400c69d81ec2b2637f7dd",\
         "value":"50000000000000000000000",\
         "gas":"21000",\
         "gasPrice":"1500000007",\
         "isError":"0",\
         "txreceipt_status":"1",\
         "input":"0x",\
         "contractAddress":"",\
         "cumulativeGasUsed":"21000",\
         "gasUsed":"21000",\
         "confirmations":"48476"\
      },\
      {\
         "blockNumber":"1061942",\
         "timeStamp":"1652077697",\
         "hash":"0x7734cae034c8a7198a5988c5ae927adf30cf77d2cbb25ed996278e402c0e0032",\
         "nonce":"0",\
         "blockHash":"0xedc7119adb34edf5480fe52f090dedbef647948ffc91806afe7d8b0182781b40",\
         "transactionIndex":"0",\
         "from":"0x382b4ca2c4a7cd28c1c400c69d81ec2b2637f7dd",\
         "to":"0x93e973436cd7757f21b1c947599f67082624a721",\
         "value":"1000000000000000",\
         "gas":"21000",\
         "gasPrice":"2000000007",\
         "isError":"0",\
         "txreceipt_status":"1",\
         "input":"0x",\
         "contractAddress":"",\
         "cumulativeGasUsed":"21000",\
         "gasUsed":"21000",\
         "confirmations":"24105"\
      }\
   ]
}
```

## [Direct link to heading](https://docs.etherscan.io/sepolia-etherscan/api-endpoints/accounts\#get-a-list-of-internal-transactions-by-address)    Get a list of 'Internal' Transactions by Address

Returns the list of internal transactions performed by an address, with optional pagination.

📝 **Note :** This API endpoint returns a maximum of **10000 records** only.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api-sepolia.etherscan.io/api
   ?module=account
   &action=txlistinternal
   &address=0xa4fadaa5e8577fee5799e2bd9615014013b45c5d
   &startblock=0
   &endblock=99999999
   &page=1
   &offset=10
   &sort=asc
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api-sepolia.etherscan.io/api?module=account&action=txlistinternal&address=0xa4fadaa5e8577fee5799e2bd9615014013b45c5d&startblock=0&endblock=99999999&page=1&offset=10&sort=asc&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

address

the `string` representing the addresses to check for balance

startblock

the `integer` block number to start searching for transactions

endblock

the `integer` block number to stop searching for transactions

page

the `integer` page number, if pagination is enabled

offset

the number of transactions displayed per page

sort

the sorting preference, use `asc` to sort by ascending and `desc` to sort by descending

💡 **Tip:** Specify a smaller `startblock` and `endblock` range for faster search results

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "status":"1",
   "message":"OK",
   "result":[\
      {\
         "blockNumber":"765371",\
         "timeStamp":"1648218619",\
         "hash":"0xcb6609b6f9133fc1bfd189fb52ed616968a5f7c56af8da3bd6724f7655fe5f78",\
         "from":"0x02f11eabf51d28bb0bae795e256ce52161d65c2b",\
         "to":"0xa4fadaa5e8577fee5799e2bd9615014013b45c5d",\
         "value":"10000000000000000",\
         "contractAddress":"",\
         "input":"",\
         "type":"call",\
         "gas":"2300",\
         "gasUsed":"0",\
         "traceId":"0_1",\
         "isError":"0",\
         "errCode":""\
      }\
   ]
}
```

## [Direct link to heading](https://docs.etherscan.io/sepolia-etherscan/api-endpoints/accounts\#get-internal-transactions-by-transaction-hash)    Get 'Internal Transactions' by Transaction Hash

Returns the list of internal transactions performed within a transaction.

**Note :** This API endpoint returns a maximum of **10000 records** only.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api-sepolia.etherscan.io/api
   ?module=account
   &action=txlistinternal
   &txhash=0xb730ee4dc8d0274be31d1e31ed7fe9749d7a67c0e35b297f3c2d10b06c1f6f1e
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api-sepolia.etherscan.io/api?module=account&action=txlistinternal&txhash=0xb730ee4dc8d0274be31d1e31ed7fe9749d7a67c0e35b297f3c2d10b06c1f6f1e&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

txhash

the `string` representing the transaction hash to check for internal transactions

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "status":"1",
   "message":"OK",
   "result":[\
      {\
         "blockNumber":"312070",\
         "timeStamp":"1639592011",\
         "from":"0xa234eead085ac80a4f7cc5220789e048373f0f1e",\
         "to":"",\
         "value":"0",\
         "contractAddress":"0x63a19c2868e469ffc2c8346c93f81ff6e140ffaf",\
         "input":"",\
         "type":"create",\
         "gas":"8504616",\
         "gasUsed":"134349",\
         "isError":"0",\
         "errCode":""\
      },\
\
      {\
         "blockNumber":"312070",\
         "timeStamp":"1639592011",\
         "from":"0xa234eead085ac80a4f7cc5220789e048373f0f1e",\
         "to":"",\
         "value":"0",\
         "contractAddress":"0xe05ba0186f4a5a5d0eb8a5394d8413411ffd321c",\
         "input":"",\
         "type":"create",\
         "gas":"1119086",\
         "gasUsed":"134349",\
         "isError":"0",\
         "errCode":""\
      },\
      {\
         "blockNumber":"312070",\
         "timeStamp":"1639592011",\
         "from":"0xa234eead085ac80a4f7cc5220789e048373f0f1e",\
         "to":"",\
         "value":"0",\
         "contractAddress":"0x7b99f4f6260c3cd12984e8d2b83eaf51d44e2254",\
         "input":"",\
         "type":"create",\
         "gas":"134349",\
         "gasUsed":"134349",\
         "isError":"0",\
         "errCode":""\
      }\
   ]
}
```

The `isError` field returns `0` for **successful transactions** and `1` for **rejected/cancelled transactions.**

## [Direct link to heading](https://docs.etherscan.io/sepolia-etherscan/api-endpoints/accounts\#get-internal-transactions-by-block-range)    Get "Internal Transactions" by Block Range

Returns the list of internal transactions performed within a block range, with optional pagination.

​​ 📝 **Note :** This API endpoint returns a maximum of **10000 records** only.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api-sepolia.etherscan.io/api
   ?module=account
   &action=txlistinternal
   &startblock=484887
   &endblock=765371
   &page=1
   &offset=10
   &sort=asc
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api-sepolia.etherscan.io/api?module=account&action=txlistinternal&startblock=484887&endblock=765371&page=1&offset=10&sort=asc&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

startblock

the `integer` block number to start searching for transactions

endblock

the `integer` block number to stop searching for transactions

page

the `integer` page number, if pagination is enabled

offset

the number of transactions displayed per page

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
         "blockNumber":"484887",\
         "timeStamp":"1644613109",\
         "hash":"0xc3ff81084b157b7d695f3df8636eebcacb6ca938c62c3102492978dbe8f5879b",\
         "from":"0x9bcdb32c4d0f0992bfb926a28ee2cb7b9d9750cc",\
         "to":"0x105083929bf9bb22c26cb1777ec92661170d4285",\
         "value":"3906875000000000000000",\
         "contractAddress":"",\
         "input":"",\
         "type":"call",\
         "gas":"2300",\
         "gasUsed":"0",\
         "traceId":"0_1",\
         "isError":"0",\
         "errCode":""\
      },\
      {\
         "blockNumber":"498080",\
         "timeStamp":"1644787132",\
         "hash":"0x1ab55087625084f2e1462a49f13a36d0996bff67da3cb4e7250e110e922274bd",\
         "from":"0x9bcdb32c4d0f0992bfb926a28ee2cb7b9d9750cc",\
         "to":"0x84e9304fa9aafc5e70090eadda9ac2c76d93ad51",\
         "value":"1491314746532500000000",\
         "contractAddress":"",\
         "input":"",\
         "type":"call",\
         "gas":"2300",\
         "gasUsed":"0",\
         "traceId":"0_1",\
         "isError":"0",\
         "errCode":""\
      },\
      {\
         "blockNumber":"518080",\
         "timeStamp":"1645046610",\
         "hash":"0x1b08041082471d96bbf5362db688f447ce8c775d242998a3b190211560911d86",\
         "from":"0x9bcdb32c4d0f0992bfb926a28ee2cb7b9d9750cc",\
         "to":"0x105083929bf9bb22c26cb1777ec92661170d4285",\
         "value":"4250625000000000000000",\
         "contractAddress":"",\
         "input":"",\
         "type":"call",\
         "gas":"2300",\
         "gasUsed":"0",\
         "traceId":"0_1",\
         "isError":"0",\
         "errCode":""\
      }\
   ]
}
```

The `isError` field returns `0` for **successful transactions** and `1` for **rejected/cancelled transactions.**

## [Direct link to heading](https://docs.etherscan.io/sepolia-etherscan/api-endpoints/accounts\#get-a-list-of-erc20-token-transfer-events-by-address)    Get a list of 'ERC20 - Token Transfer Events' by Address

Returns the list of ERC-20 tokens transferred by an address, with optional filtering by token contract.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api-sepolia.etherscan.io/api
   ?module=account
   &action=tokentx
   &contractaddress=0xa808b14492AC6E33419ac16112154D40D0A4AEBA
   &address=0x105083929bf9bb22c26cb1777ec92661170d4285
   &page=1
   &offset=100
   &startblock=0
   &endblock=99999999
   &sort=asc
   &apikey=YourApiKeyToken
```

Usage:

- ERC-20 transfers from an **address**, specify the `address` parameter

- ERC-20 transfers from a **contract address**, specify the `contract address` parameter

- ERC-20 transfers from an **address** filtered by a **token contract**, specify both `address` and `contract address` parameters.


> Try this endpoint in your [**browser**](https://api-sepolia.etherscan.io/api?module=account&action=tokentx&contractaddress=0xa808b14492AC6E33419ac16112154D40D0A4AEBA&address=0x105083929bf9bb22c26cb1777ec92661170d4285&page=1&offset=100&startblock=0&endblock=99999999&sort=asc&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

address

the `string` representing the address to check for balance

contractaddress

the `string` representing the token contract address to check for balance

page

the `integer` page number, if pagination is enabled

offset

the number of transactions displayed per page

startblock

the `integer` block number to start searching for transactions

endblock

the `integer` block number to stop searching for transactions

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
         "blockNumber":"496492",\
         "timeStamp":"1644767322",\
         "hash":"0x433994d50986d0c021098adadac4f4a89249c51fb4ea372e553af6ee6fc0965c",\
         "nonce":"20",\
         "blockHash":"0x29394a72a707d77a167a1eec53d33940b5a366a2c01cd10094c18a15517ff44b",\
         "from":"0x84e9304fa9aafc5e70090eadda9ac2c76d93ad51",\
         "contractAddress":"0xa808b14492ac6e33419ac16112154d40d0a4aeba",\
         "to":"0x105083929bf9bb22c26cb1777ec92661170d4285",\
         "value":"100000000000000000000000",\
         "tokenName":"Vitcoin",\
         "tokenSymbol":"VTC",\
         "tokenDecimal":"18",\
         "transactionIndex":"0",\
         "gas":"53517",\
         "gasPrice":"1000000007",\
         "gasUsed":"35678",\
         "cumulativeGasUsed":"35678",\
         "input":"deprecated",\
         "confirmations":"589603"\
      },\
      {\
         "blockNumber":"886779",\
         "timeStamp":"1649789803",\
         "hash":"0x1071238546873837a9b03736a8ca26ce379e66999f6e74748dd919890232e34a",\
         "nonce":"28",\
         "blockHash":"0xd1a3ad751eba89ac664e691844a5a44361d8c801ce6bbfe31c03f1d7970e28f7",\
         "from":"0x84e9304fa9aafc5e70090eadda9ac2c76d93ad51",\
         "contractAddress":"0xa808b14492ac6e33419ac16112154d40d0a4aeba",\
         "to":"0x105083929bf9bb22c26cb1777ec92661170d4285",\
         "value":"999900000000000000000000000",\
         "tokenName":"Vitcoin",\
         "tokenSymbol":"VTC",\
         "tokenDecimal":"18",\
         "transactionIndex":"0",\
         "gas":"53553",\
         "gasPrice":"1500000007",\
         "gasUsed":"30902",\
         "cumulativeGasUsed":"30902",\
         "input":"deprecated",\
         "confirmations":"199316"\
      }\
   ]
}
```

## [Direct link to heading](https://docs.etherscan.io/sepolia-etherscan/api-endpoints/accounts\#get-a-list-of-erc721-token-transfer-events-by-address)    Get a list of 'ERC721 - Token Transfer Events' by Address

Returns the list of ERC-721 ( NFT ) tokens transferred by an address, with optional filtering by token contract

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api-sepolia.etherscan.io/api
   ?module=account
   &action=tokennfttx
   &contractaddress=0x03e73ef97303e11703864a5404d71351ef61d8f8
   &address=0xb541f07fd1ae0a0d0244982e847a072436ee67db
   &page=1
   &offset=100
   &startblock=0
   &endblock=99999999
   &sort=asc
   &apikey=YourApiKeyToken
```

Usage:

- ERC-721 transfers from an **address**, specify the `address` parameter

- ERC-721 transfers from a **contract address**, specify the `contract address` parameter

- ERC-721 transfers from an **address** filtered by a **token contract**, specify both `address` and `contract address` parameters.


> Try this endpoint in your [**browser**](https://api-sepolia.etherscan.io/api?module=account&action=tokennfttx&contractaddress=0x03e73ef97303e11703864a5404d71351ef61d8f8&address=0xb541f07fd1ae0a0d0244982e847a072436ee67db&page=1&offset=100&startblock=0&endblock=99999999&sort=asc&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

address

the `string` representing the address to check for balance

contractaddress

the `string` representing the token contract address to check for balance

page

the `integer` page number, if pagination is enabled

offset

the number of transactions displayed per page

startblock

the `integer` block number to start searching for transactions

endblock

the `integer` block number to stop searching for transactions

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
         "blockNumber":"8618316",\
         "timeStamp":"1621510305",\
         "hash":"0x9c10c45f47088060c9493e88361d7eedbc3b4dd2772e0b1deeb84d46a5c8e623",\
         "nonce":"338",\
         "blockHash":"0x2b690dd69f868351e179068befc3cd3f6d2621a8d425093d3980a24ac1347179",\
         "from":"0x0000000000000000000000000000000000000000",\
         "contractAddress":"0x03e73ef97303e11703864a5404d71351ef61d8f8",\
         "to":"0xb541f07fd1ae0a0d0244982e847a072436ee67db",\
         "tokenID":"10001",\
         "tokenName":"Artifex",\
         "tokenSymbol":"ARTIFEX",\
         "tokenDecimal":"0",\
         "transactionIndex":"0",\
         "gas":"5016425",\
         "gasPrice":"2051200000",\
         "gasUsed":"5016425",\
         "cumulativeGasUsed":"5016425",\
         "input":"deprecated",\
         "confirmations":"927169"\
      },\
      {\
         "blockNumber":"8618316",\
         "timeStamp":"1621510305",\
         "hash":"0x9c10c45f47088060c9493e88361d7eedbc3b4dd2772e0b1deeb84d46a5c8e623",\
         "nonce":"338",\
         "blockHash":"0x2b690dd69f868351e179068befc3cd3f6d2621a8d425093d3980a24ac1347179",\
         "from":"0x0000000000000000000000000000000000000000",\
         "contractAddress":"0x03e73ef97303e11703864a5404d71351ef61d8f8",\
         "to":"0xb541f07fd1ae0a0d0244982e847a072436ee67db",\
         "tokenID":"10002",\
         "tokenName":"Artifex",\
         "tokenSymbol":"ARTIFEX",\
         "tokenDecimal":"0",\
         "transactionIndex":"0",\
         "gas":"5016425",\
         "gasPrice":"2051200000",\
         "gasUsed":"5016425",\
         "cumulativeGasUsed":"5016425",\
         "input":"deprecated",\
         "confirmations":"927169"\
      }\
   ]
}
```

## [Direct link to heading](https://docs.etherscan.io/sepolia-etherscan/api-endpoints/accounts\#get-list-of-blocks-mined-by-address)    Get list of Blocks Mined by Address

Returns the list of blocks mined by an address.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api-sepolia.etherscan.io/api
   ?module=account
   &action=getminedblocks
   &address=0x3d080421c9DD5fB387d6e3124f7E1C241ADE9568
   &blocktype=blocks
   &page=1
   &offset=10
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api-sepolia.etherscan.io/api?module=account&action=getminedblocks&address=0x3d080421c9DD5fB387d6e3124f7E1C241ADE9568&blocktype=blocks&page=1&offset=10&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

address

the `string` representing the address to check for balance

blocktype

the `string` pre-defined block type, either `blocks` for canonical blocks or `uncles` for uncle blocks only

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
         "blockNumber":"1088398",\
         "timeStamp":"1652415312",\
         "blockReward":"2000000000000000000"\
      },\
      {\
         "blockNumber":"1088395",\
         "timeStamp":"1652415289",\
         "blockReward":"2000000000000000000"\
      },\
      {\
         "blockNumber":"1088361",\
         "timeStamp":"1652414946",\
         "blockReward":"2000000000000000000"\
      }\
   ]
}
```

⏳ **Note :** The `timeStamp` is represented in [**Unix timestamp.**](https://www.unixtimestamp.com/)

[PreviousSepolia Testnet](https://docs.etherscan.io/sepolia-etherscan) [NextContracts](https://docs.etherscan.io/sepolia-etherscan/api-endpoints/contracts)

Last updated 2 years ago

This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject