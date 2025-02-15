Write a whale watcher Discord bot, monitor for larger transfers 🔀 or keep tabs on Binance's exchange reserves with this recipe!

Endpoint used: " [**Get a list of 'ERC20 - Token Transfer Events' by Address**](https://docs.etherscan.io/api-endpoints/accounts#get-a-list-of-erc20-token-transfer-events-by-address)"

### [Direct link to heading](https://docs.etherscan.io/etherscan-v2/recipes/get-all-usdt-transfers-from-binance\#id-1.-determine-the-contract-address-of-the-usdt-token)    1\. Determine the contract address of the USDT token

Simply by going on [**Etherscan**](https://etherscan.io/address/0xdac17f958d2ee523a2206206994597c13d831ec7) and searching for "USDT", we're able to determine it as `0xdac17f958d2ee523a2206206994597c13d831ec7` which we'll set as the `contractaddress` parameter.

### [Direct link to heading](https://docs.etherscan.io/etherscan-v2/recipes/get-all-usdt-transfers-from-binance\#id-2.-filter-by-a-specific-address-to-watch-for)    2\. Filter by a specific address to watch for

In this case, we're looking to observe one of [**Binance's hot wallets**](https://etherscan.io/address/0xdfd5293d8e347dfe59e90efd55b2956a1343963d), also tagged and available on Etherscan.

We'll set the `address` parameter to `0xdfd5293d8e347dfe59e90efd55b2956a1343963d` , which indicates that we'll filter token transfers by this address.

### [Direct link to heading](https://docs.etherscan.io/etherscan-v2/recipes/get-all-usdt-transfers-from-binance\#id-3.-sort-by-the-latest-token-transfers-first)    3\. Sort by the latest token transfers first

As a preference, we'll set the `sort` parameter to `desc` to get the latest transactions first, though you can always get the oldest first by flipping it to `asc`.

### [Direct link to heading](https://docs.etherscan.io/etherscan-v2/recipes/get-all-usdt-transfers-from-binance\#id-4.-integrate-and-format-token-decimals)    4\. Integrate and format token decimals

One thing to note is the token `value` field is returned in the token's smallest representation, you would have to divide this by the token `decimal` to get the transfer amount.

An example value of `198000000000` would be represented as the transfer of `198000` USDT.

### [Direct link to heading](https://docs.etherscan.io/etherscan-v2/recipes/get-all-usdt-transfers-from-binance\#final-query)    Final Query

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=account
   &action=tokentx
   &contractaddress=0xdac17f958d2ee523a2206206994597c13d831ec7
   &address=0xdfd5293d8e347dfe59e90efd55b2956a1343963d
   &page=1
   &offset=100
   &startblock=0
   &endblock=99999999
   &sort=desc
   &apikey=YourApiKeyToken
```

> Try this endpoint in your \[ **browser**\](https://api.etherscan.io/v2/api?chainid=1 &module=account&action=tokentx&contractaddress=0xdac17f958d2ee523a2206206994597c13d831ec7&address=0xdfd5293d8e347dfe59e90efd55b2956a1343963d&page=1&offset=100&startblock=0&endblock=99999999&sort=desc&apikey=YourApiKeyToken) 🔗

Last updated 5 months ago

This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject