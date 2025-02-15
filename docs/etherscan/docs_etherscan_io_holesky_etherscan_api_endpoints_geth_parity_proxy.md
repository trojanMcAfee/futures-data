For the full documentation of available parameters and descriptions, please visit the official [**Ethereum JSON-RPC**](https://eth.wiki/json-rpc/API) docs.

For compatibility with **Parity**, please prefix all hex strings with " **0x** ".

## [Direct link to heading](https://docs.etherscan.io/holesky-etherscan/api-endpoints/geth-parity-proxy\#eth_blocknumber)    **eth\_blockNumber**

Returns the number of most recent block

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api-holesky.etherscan.io/api
   ?module=proxy
   &action=eth_blockNumber
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api-holesky.etherscan.io/api?module=proxy&action=eth_blockNumber&apikey=YourApiKeyToken) 🔗

RequestResponse

No parameters required.

Sample response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "jsonrpc":"2.0",
   "result":"0x10a79f",
   "id":83
}
```

## [Direct link to heading](https://docs.etherscan.io/holesky-etherscan/api-endpoints/geth-parity-proxy\#eth_getblockbynumber)    **eth\_getBlockByNumber**

Returns information about a block by block number.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api-holesky.etherscan.io/api
   ?module=proxy
   &action=eth_getBlockByNumber
   &tag=0x91b743
   &boolean=true
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api-holesky.etherscan.io/api?module=proxy&action=eth_getBlockByNumber&tag=0x91b743&boolean=true&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

tag

the block number, in hex eg. `0xC36B3C`

boolean

the `boolean` value to show full transaction objects.

when `true`, returns **full transaction objects** and their information, when `false` only returns a **list of transactions.**

Sample response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "jsonrpc":"2.0",
   "id":1,
   "result":{
      "baseFeePerGas":"0x7",
      "difficulty":"0x1348c54c4",
      "extraData":"0xd883010a11846765746888676f312e31372e37856c696e7578",
      "gasLimit":"0x7a1200",
      "gasUsed":"0x0",
      "hash":"0x2cb5abe6b662c8a676df0c55a8fb01c81fdad7c1e1b7b3e7f8900439fd626c37",
      "logsBloom":"0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
      "miner":"0x45ff5f8723dae09d008dae9462346fd806736390",
      "mixHash":"0x914dac73b89721483a62fb78b7fd1110b91d57752afc84e911c34eedef090519",
      "nonce":"0x6517543e5b8f467c",
      "number":"0x10a79f",
      "parentHash":"0xbccd65c8ad26b21413d4593161c7161ea612033d00dd6887673ab3eab283ff7b",
      "receiptsRoot":"0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
      "sha3Uncles":"0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
      "size":"0x21e",
      "stateRoot":"0xa01ded26f5c6b00bfff7b8e244ec361b521093d07d3ce3db9c7b05f918bc877d",
      "timestamp":"0x627e7d2c",
      "totalDifficulty":"0xbf255bf92df41",
      "transactions":[\
\
      ],
      "transactionsRoot":"0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
      "uncles":[\
\
      ]
   }
}
```

## [Direct link to heading](https://docs.etherscan.io/holesky-etherscan/api-endpoints/geth-parity-proxy\#eth_getunclebyblocknumberandindex)    **eth\_getUncleByBlockNumberAndIndex**

Returns information about a uncle by block number.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api-holesky.etherscan.io/api
   ?module=proxy
   &action=eth_getUncleByBlockNumberAndIndex
   &tag=0x10A7A6
   &index=0x0
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api-holesky.etherscan.io/api?module=proxy&action=eth_getUncleByBlockNumberAndIndex&tag=0x10A7A6&index=0x0&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

tag

the block number, in hex eg. `0xC36B3C`

index

the position of the uncle's index in the block, in hex eg. `0x5`

Sample response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "jsonrpc":"2.0",
   "id":1,
   "result":{
      "baseFeePerGas":"0x7",
      "difficulty":"0x133cb6ea4",
      "extraData":"0xd883010a10846765746888676f312e31372e37856c696e7578",
      "gasLimit":"0x7a1200",
      "gasUsed":"0x0",
      "hash":"0xd5aabf16a6cd972bf33b7656143d1305f24273ca44a47908e2c36d8eb69a2d80",
      "logsBloom":"0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
      "miner":"0xd87def8bbd2c4d59494611ab259a2005c154212a",
      "mixHash":"0x4c2d04e4f691306fcca2f2623cdac968bc1dc90170a1c7104815cebe424c6411",
      "nonce":"0x4c0da4978732561b",
      "number":"0x10a7a5",
      "parentHash":"0xa92a3d6c31cdbed8d40067930f364291063e01946ca40db7cf4e95866bfcd7f1",
      "receiptsRoot":"0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
      "sha3Uncles":"0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
      "size":"0x21e",
      "stateRoot":"0x5c5ca1001e5f6b383a0bcab31823097146aa364158b12888de02bbff707da299",
      "timestamp":"0x627e7da6",
      "transactionsRoot":"0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
      "uncles":[\
\
      ]
   }
}
```

## [Direct link to heading](https://docs.etherscan.io/holesky-etherscan/api-endpoints/geth-parity-proxy\#eth_getblocktransactioncountbynumber)    **eth\_getBlockTransactionCountByNumber**

Returns the number of transactions in a block.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api-holesky.etherscan.io/api
   ?module=proxy
   &action=eth_getBlockTransactionCountByNumber
   &tag=0x10A70A
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api-holesky.etherscan.io/api?module=proxy&action=eth_getBlockTransactionCountByNumber&tag=0x10A70A&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

tag

the block number, in hex eg. `0x10FB78`

Sample response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "jsonrpc":"2.0",
   "id":1,
   "result":"0x1"
}
```

## [Direct link to heading](https://docs.etherscan.io/holesky-etherscan/api-endpoints/geth-parity-proxy\#eth_gettransactionbyhash)    **eth\_getTransactionByHash**

Returns the information about a transaction requested by transaction hash.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api-holesky.etherscan.io/api
   ?module=proxy
   &action=eth_getTransactionByHash
   &txhash=0x57be61afdf095899d160003f58e429d3f9b0851fd90db217fc0aa474761f9f34
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api-holesky.etherscan.io/api?module=proxy&action=eth_getTransactionByHash&txhash=0x57be61afdf095899d160003f58e429d3f9b0851fd90db217fc0aa474761f9f34&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

txhash

the `string` representing the hash of the transaction

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "jsonrpc":"2.0",
   "id":1,
   "result":{
      "blockHash":"0x9329b3b236fb6a60ddec501d9264e587593f7b810fff31c9a2cf1f2deb58ebe2",
      "blockNumber":"0x10a70a",
      "from":"0x382b4ca2c4a7cd28c1c400c69d81ec2b2637f7dd",
      "gas":"0x5208",
      "gasPrice":"0x77359407",
      "maxFeePerGas":"0x77359407",
      "maxPriorityFeePerGas":"0x77359400",
      "hash":"0x57be61afdf095899d160003f58e429d3f9b0851fd90db217fc0aa474761f9f34",
      "input":"0x",
      "nonce":"0x6e",
      "to":"0x97664026bf28d95330dd80174630c287a9c8e2e3",
      "transactionIndex":"0x0",
      "value":"0x35c007914225000",
      "type":"0x2",
      "accessList":[\
\
      ],
      "chainId":"0xaa36a7",
      "v":"0x1",
      "r":"0x9c358c4e6ef291967775d0c50e34dbb3a0c602a3d8e616dffb5a513e4ac2018e",
      "s":"0x28dd29246d37f57a35026d315c352042f04afc0709c541a9e0d39df571aa7c67"
   }
}
```

## [Direct link to heading](https://docs.etherscan.io/holesky-etherscan/api-endpoints/geth-parity-proxy\#eth_gettransactionbyblocknumberandindex)    **eth\_getTransactionByBlockNumberAndIndex**

Returns information about a transaction by block number and transaction index position.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api-holesky.etherscan.io/api
   ?module=proxy
   &action=eth_getTransactionByBlockNumberAndIndex
   &tag=0x10A70A
   &index=0x0
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api-holesky.etherscan.io/api?module=proxy&action=eth_getTransactionByBlockNumberAndIndex&tag=0x10A70A&index=0x0&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

tag

the block number, in hex eg. `0x10FB78`

index

the position of the uncle's index in the block, in hex eg. `0x0`

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "jsonrpc":"2.0",
   "id":1,
   "result":{
      "blockHash":"0x9329b3b236fb6a60ddec501d9264e587593f7b810fff31c9a2cf1f2deb58ebe2",
      "blockNumber":"0x10a70a",
      "from":"0x382b4ca2c4a7cd28c1c400c69d81ec2b2637f7dd",
      "gas":"0x5208",
      "gasPrice":"0x77359407",
      "maxFeePerGas":"0x77359407",
      "maxPriorityFeePerGas":"0x77359400",
      "hash":"0x57be61afdf095899d160003f58e429d3f9b0851fd90db217fc0aa474761f9f34",
      "input":"0x",
      "nonce":"0x6e",
      "to":"0x97664026bf28d95330dd80174630c287a9c8e2e3",
      "transactionIndex":"0x0",
      "value":"0x35c007914225000",
      "type":"0x2",
      "accessList":[\
\
      ],
      "chainId":"0xaa36a7",
      "v":"0x1",
      "r":"0x9c358c4e6ef291967775d0c50e34dbb3a0c602a3d8e616dffb5a513e4ac2018e",
      "s":"0x28dd29246d37f57a35026d315c352042f04afc0709c541a9e0d39df571aa7c67"
   }
}
```

## [Direct link to heading](https://docs.etherscan.io/holesky-etherscan/api-endpoints/geth-parity-proxy\#eth_gettransactioncount)    **eth\_getTransactionCount**

Returns the number of transactions performed by an address.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api-holesky.etherscan.io/api
   ?module=proxy
   &action=eth_getTransactionCount
   &address=0x1d41D6B1091C1a8A334096771bd1776019243d5e
   &tag=latest
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api-holesky.etherscan.io/api?module=proxy&action=eth_getTransactionCount&address=0x382b4ca2c4a7cd28c1c400c69d81ec2b2637f7dd&tag=latest&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

address

the `string` representing the address to get transaction count

tag

the `string` pre-defined block parameter, either `earliest`, `pending` or `latest`

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "jsonrpc":"2.0",
   "id":1,
   "result":"0x6f"
}
```

## [Direct link to heading](https://docs.etherscan.io/holesky-etherscan/api-endpoints/geth-parity-proxy\#eth_sendrawtransaction)    **eth\_sendRawTransaction**

Submits a pre-signed transaction for broadcast to the Ethereum network.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api-holesky.etherscan.io/api
   ?module=proxy
   &action=eth_sendRawTransaction
   &hex=0x02f874030185012a05f200852e90edd00082520894eeee7341f206302f2216e39d715b96d8c6901a1c880de0b6b3a764000080c001a0bf61ea5419c7856be4ea2221b721b849d50fec738d10a714e7aaa809d9ad8838a01e59353aa8e567cc0661fb58b047361998df234df6593bf424839bc5ea214a2c
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api-holesky.etherscan.io/api?module=proxy&action=eth_sendRawTransaction&hex=0x02f874030185012a05f200852e90edd00082520894eeee7341f206302f2216e39d715b96d8c6901a1c880de0b6b3a764000080c001a0bf61ea5419c7856be4ea2221b721b849d50fec738d10a714e7aaa809d9ad8838a01e59353aa8e567cc0661fb58b047361998df234df6593bf424839bc5ea214a2c&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

hex

the `string` representing the signed raw transaction data to broadcast.

💡 **Tip:** Send a **POST** request if your hex string is particularly long.

🖋️ For more information on creating a **signed raw transaction**, visit this [**page.**](https://github.com/BlockSolutions/etherscan-api-docs/blob/sepolia-etherscan/tutorials/signing-raw-transactions.md)

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
  "id":1,
  "jsonrpc": "2.0",
  "result": "0x84c81fc1e23474e13be0114f94f99b43696830f33292fd1d642f37e87e95acd6"
}
```

⛏️ **Note:** The `result` represents the **transaction hash** of the submitted raw transaction.

Use **eth\_getTransactionReceipt** to retrieve full details.

## [Direct link to heading](https://docs.etherscan.io/holesky-etherscan/api-endpoints/geth-parity-proxy\#eth_gettransactionreceipt)    **eth\_getTransactionReceipt**

Returns the receipt of a transaction by transaction hash.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api-holesky.etherscan.io/api
   ?module=proxy
   &action=eth_getTransactionReceipt
   &txhash=0x50b43f829e0b7044decbac0dc9216de1c7bf9a271999ed978300da1f5dc90c51
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api-holesky.etherscan.io/api?module=proxy&action=eth_getTransactionReceipt&txhash=0x50b43f829e0b7044decbac0dc9216de1c7bf9a271999ed978300da1f5dc90c51&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

txhash

the `string` representing the hash of the transaction

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "jsonrpc":"2.0",
   "id":1,
   "result":{
      "blockHash":"0xd201810e935bed977bdb63ac5e8e7328acaefe3ec5447597f8b2493728a6c1e3",
      "blockNumber":"0x10a574",
      "contractAddress":null,
      "cumulativeGasUsed":"0x5208",
      "effectiveGasPrice":"0x59682f07",
      "from":"0x9907dd452706a9783e241d7b16e6ad0759ae051e",
      "gasUsed":"0x5208",
      "logs":[\
\
      ],
      "logsBloom":"0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
      "status":"0x1",
      "to":"0x105083929bf9bb22c26cb1777ec92661170d4285",
      "transactionHash":"0x50b43f829e0b7044decbac0dc9216de1c7bf9a271999ed978300da1f5dc90c51",
      "transactionIndex":"0x0",
      "type":"0x2"
   }
}
```

## [Direct link to heading](https://docs.etherscan.io/holesky-etherscan/api-endpoints/geth-parity-proxy\#eth_call)    **eth\_call**

Executes a new message call immediately without creating a transaction on the block chain.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api-holesky.etherscan.io/api
   ?module=proxy
   &action=eth_call
   &to=0x272c31fc25e4e609cbcc9e7a9e6171b4b39feaca
   &data=0x60fe47b10000000000000000000000000000000000000000000000000000000000010f2c
   &tag=latest
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api-holesky.etherscan.io/api?module=proxy&action=eth_call&to=0x272c31fc25e4e609cbcc9e7a9e6171b4b39feaca&data=0x60fe47b10000000000000000000000000000000000000000000000000000000000010f2c&tag=latest&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

to

the `string` representing the address to interact with

data

the hash of the method signature and encoded parameters

tag

the `string` pre-defined block parameter, either `earliest`, `pending` or `latest`

⛽ **Note:** The `gas` parameter is capped at **2x** the current block gas limit.

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "jsonrpc":"2.0",
   "id":1,
   "result":"0x"
}
```

## [Direct link to heading](https://docs.etherscan.io/holesky-etherscan/api-endpoints/geth-parity-proxy\#eth_getcode)    **eth\_getCode**

Returns code at a given address.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api-holesky.etherscan.io/api
   ?module=proxy
   &action=eth_getCode
   &address=0x272c31fc25e4e609cbcc9e7a9e6171b4b39feaca
   &tag=latest
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api-holesky.etherscan.io/api?module=proxy&action=eth_getCode&address=0x272c31fc25e4e609cbcc9e7a9e6171b4b39feaca&tag=latest&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

address

the `string` representing the address to get code

tag

the `string` pre-defined block parameter, either `earliest`, `pending` or `latest`

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "jsonrpc":"2.0",
   "id":1,
   "result":"0x608060405234801561001057600080fd5b50600436106100365760003560e01c806360fe47b11461003b5780636d4ce63c14610057575b600080fd5b6100556004803603810190610050919061009d565b610075565b005b61005f61007f565b60405161006c91906100d9565b60405180910390f35b8060008190555050565b60008054905090565b60008135905061009781610103565b92915050565b6000602082840312156100b3576100b26100fe565b5b60006100c184828501610088565b91505092915050565b6100d3816100f4565b82525050565b60006020820190506100ee60008301846100ca565b92915050565b6000819050919050565b600080fd5b61010c816100f4565b811461011757600080fd5b5056fea2646970667358221220d7dae2ccb3d6437f2a190839abef6ef723207c70463c87c2b1257d40c938e42564736f6c63430008070033"
}
```

## [Direct link to heading](https://docs.etherscan.io/holesky-etherscan/api-endpoints/geth-parity-proxy\#eth_getstorageat)    **eth\_getStorageAt**

Returns the value from a storage position at a given address.

This endpoint is still **experimental** and may have potential issues

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api-holesky.etherscan.io/api
   ?module=proxy
   &action=eth_getStorageAt
   &address=0x272c31fc25e4e609cbcc9e7a9e6171b4b39feaca
   &position=0x0
   &tag=latest
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api-holesky.etherscan.io/api?module=proxy&action=eth_getStorageAt&address=0x272c31fc25e4e609cbcc9e7a9e6171b4b39feaca&position=0x0&tag=latest&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

address

the `string` representing the address to get code

position

the hex code of the position in storage, eg `0x0`

tag

the `string` pre-defined block parameter, either `earliest`, `pending` or `latest`

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "jsonrpc":"2.0",
   "id":1,
   "result":"0x000000000000x0000000000000000000000000000000000000000000000000000000000010f2c00000000000000000000000000000000000000000000000000000"
}
```

## [Direct link to heading](https://docs.etherscan.io/holesky-etherscan/api-endpoints/geth-parity-proxy\#eth_gasprice)    **eth\_gasPrice**

Returns the current price per gas in wei.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api-holesky.etherscan.io/api
   ?module=proxy
   &action=eth_gasPrice
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api-holesky.etherscan.io/api?module=proxy&action=eth_gasPrice&apikey=YourApiKeyToken) 🔗

RequestResponse

No parameters required.

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "jsonrpc":"2.0",
   "id":73,
   "result":"0x3b9aca07"
}
```

📖 **Tip:** The `result` is returned in **wei**.

Easily convert Ethereum units using our [**unit converter.**](https://holesky.etherscan.io/unitconverter)

## [Direct link to heading](https://docs.etherscan.io/holesky-etherscan/api-endpoints/geth-parity-proxy\#eth_estimategas)    **eth\_estimateGas**

Makes a call or transaction, which won't be added to the blockchain and returns the used gas.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api-holesky.etherscan.io/api
   ?module=proxy
   &action=eth_estimateGas
   &data=0x60fe47b10000000000000000000000000000000000000000000000000000000000000004
   &to=0x272c31fC25E4e609CbCC9E7a9e6171b4B39feAca
   &value=0x0
   &gasPrice=0x51da038cc
   &gas=0x186A0
   &apikey=YourApiKeyToken
```

> Try this endpoint in your [**browser**](https://api-holesky.etherscan.io/api?module=proxy&action=eth_estimateGas&data=0x60fe47b10000000000000000000000000000000000000000000000000000000000000004&to=0x272c31fC25E4e609CbCC9E7a9e6171b4B39feAca&value=0x0&gasPrice=0x51da038cc&gas=0x186A0&apikey=YourApiKeyToken) 🔗

RequestResponse

Query Parameters

Parameter

Description

data

the hash of the method signature and encoded parameters

to

the `string` representing the address to interact with

value

the value sent in this transaction, in hex eg. `0xff22`

gas

the amount of gas provided for the transaction, in hex eg. `0x5f5e0ff`

gasPrice

the gas price paid for each unit of gas, in wei

post **EIP-1559**, the `gasPrice` has to be higher than the block's `baseFeePerGas`

⛽ **Note:** The `gas` parameter is capped at **2x** the current block gas limit.

Sample Response

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "jsonrpc":"2.0",
   "id":1,
   "result":"0x67ea"
}
```

[PreviousLogs](https://docs.etherscan.io/holesky-etherscan/api-endpoints/logs) [NextTokens](https://docs.etherscan.io/holesky-etherscan/api-endpoints/tokens)

Last updated 10 months ago

This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject