Create a live data feed of users bridging into a Layer 2 protocol by watching Arbitrum's bridge contract address!

Endpoint used: " [**Get a list of 'Normal' Transactions By Address**](https://docs.etherscan.io/api-endpoints/accounts#get-a-list-of-normal-transactions-by-address)"

### [Direct link to heading](https://docs.etherscan.io/etherscan-v2/recipes/list-eth-deposits-to-arbitrum-bridge\#id-1.-determine-the-contract-address-of-arbitrum-bridge)    1\. Determine the contract address of Arbitrum Bridge

Arbitrum's bridge user deposits are directed to the [**Arbitrum Delayed Inbox**](https://etherscan.io/address/0x4dbd4fc535ac27206064b68ffcf827b0a60bab3f), with the contract address of `0x4dbd4fc535ac27206064b68ffcf827b0a60bab3f`.

Setting this as the `address` parameter allows us to get the ETH transfers to this address.

### [Direct link to heading](https://docs.etherscan.io/etherscan-v2/recipes/list-eth-deposits-to-arbitrum-bridge\#id-2.-sort-by-the-latest-transactions-first)    2\. Sort by the latest transactions first

Set the `sort` parameter to `desc` to get the latest transactions first, you can also get the oldest first by flipping it to `asc`.

### [Direct link to heading](https://docs.etherscan.io/etherscan-v2/recipes/list-eth-deposits-to-arbitrum-bridge\#id-3.-filter-transaction-methods)    3\. Filter transaction methods

The method `depositEth` with method ID of `0x439370b1` can be used to determine an ETH deposit transaction to this contract address.

You may optionally filter by this using your favorite programming language such as JS to separate out other transaction methods.

### [Direct link to heading](https://docs.etherscan.io/etherscan-v2/recipes/list-eth-deposits-to-arbitrum-bridge\#final-query)    Final Query

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=account
   &action=txlist
   &address=0x4dbd4fc535ac27206064b68ffcf827b0a60bab3f
   &startblock=0
   &endblock=99999999
   &page=1
   &offset=1000
   &sort=desc
   &apikey=YourApiKeyToken
```

> Try this endpoint in your \[ **browser**\](https://api.etherscan.io/v2/api?chainid=1 &module=account&action=txlist&address=0x4dbd4fc535ac27206064b68ffcf827b0a60bab3f&startblock=0&endblock=99999999&page=1&offset=1000&sort=desc&apikey=YourApiKeyToken) 🔗

Last updated 5 months ago

This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject