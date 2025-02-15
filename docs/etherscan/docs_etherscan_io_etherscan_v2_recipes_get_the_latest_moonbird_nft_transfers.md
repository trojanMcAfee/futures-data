Track the latest NFT token transfers 🖼️ of a specific collection, inclusive of token ID and addresses involved!

Endpoint used: " [**Get a list of 'ERC721 - Token Transfer Events' by Address**](https://docs.etherscan.io/api-endpoints/accounts#get-a-list-of-erc721-token-transfer-events-by-address)"

### [Direct link to heading](https://docs.etherscan.io/etherscan-v2/recipes/get-the-latest-moonbird-nft-transfers\#id-1.-determine-the-contract-address-of-the-moonbird-token)    1\. Determine the contract address of the Moonbird token

Searching "Moonbird" on [**Etherscan**](https://etherscan.io/token/0x23581767a106ae21c074b2276D25e5C3e136a68b) or referencing their official docs, we can determine the token address to be `0x23581767a106ae21c074b2276D25e5C3e136a68b`.

Set this as the `contractaddress` to filter by token transfers from a specific collection, and omit the `address` parameter to return transfers from any address.

### [Direct link to heading](https://docs.etherscan.io/etherscan-v2/recipes/get-the-latest-moonbird-nft-transfers\#id-2.-sort-by-the-latest-token-transfers-first)    2\. Sort by the latest token transfers first

Set the `sort` parameter to `desc` to get the latest transactions first, you can also get the oldest first by flipping it to `asc`.

### [Direct link to heading](https://docs.etherscan.io/etherscan-v2/recipes/get-the-latest-moonbird-nft-transfers\#id-3.-integrate-the-token-ids-and-addresses)    3\. Integrate the token IDs and addresses

Use the `to` field representing the address the NFT was sent to, and `from` being the sender of the NFT.

### [Direct link to heading](https://docs.etherscan.io/etherscan-v2/recipes/get-the-latest-moonbird-nft-transfers\#final-query)    Final Query

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/v2/api
   ?chainid=1
   &module=account
   &action=
   &contractaddress=0x23581767a106ae21c074b2276D25e5C3e136a68b
   &page=1
   &offset=100
   &startblock=0
   &endblock=99999999
   &sort=desc
   &apikey=YourApiKeyToken
```

> Try this endpoint in your \[ **browser**\](https://api.etherscan.io/v2/api?chainid=1 &module=account&action=tokennfttx&contractaddress=0x23581767a106ae21c074b2276D25e5C3e136a68b&page=1&offset=100&startblock=0&endblock=99999999&sort=desc&apikey=YourApiKeyToken) 🔗

Last updated 5 months ago

This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject