This V2 update is aimed at a single goal, of unifying EVM data across [**50+ chains**](https://docs.etherscan.io/etherscan-v2/getting-started/supported-chains). 🤝

### [Direct link to heading](https://docs.etherscan.io/etherscan-v2\#why-v2)    Why V2

With the rise of multichain apps, many projects' GitHub repositories resemble a ( shortened ) version of this.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
ETHERSCAN_API_KEY=VZFDUWB3YGQ1YCDKTCU1D6DDSS
BSCSCAN_API_KEY=ZM8ACMJB67C2IXKKBF8URFUNSY
SNOWSCAN_API_KEY=ATJQERBKV1CI3GVKNSE3Q7RGEJ
ARBISCAN_API_KEY=B6SVGA7K3YBJEQ69AFKJF4YHVX
OPTIMISM_API_KEY=66N5FRNV1ZD4I87S7MAHCJVXFJ

ETHERSCAN_API_URL=https://api.etherscan.io/api
BSCSCAN_API_KEY=https://api.bscscan.com/api
SNOWSCAN_API_KEY=https://api.snowscan.xyz/api
ARBISCAN_API_KEY=https://api.arbiscan.io/api
OPTIMISM_API_KEY=https://api-optimistic.etherscan.io/api
```

As support for Etherscan explorers across multiple chains grew, so did the fragmentation of the developer experience.

### [Direct link to heading](https://docs.etherscan.io/etherscan-v2\#single-api-key)    Single API Key

You can now query data from any of our [**50+ supported chains**](https://docs.etherscan.io/etherscan-v2/getting-started/supported-chains) with a single API key.

This includes features like contract verification ✅, fetching transactions across chains 🔵 and more.

To add support for a new chain, simply append its **chain ID** to your array, like this JavaScript ( intern can't get Python installed on Windows )

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
const chains = [42161, 8453, 10, 534352, 81457]

for (const chain of chains) {

  // endpoint accepts one chain at a time, loop for all your chains
  const balance = fetch(`https://api.etherscan.io/v2/api?
     chainid=${chain}
     &module=account
     &action=balance
     &address=0xb5d85cbf7cb3ee0d56b3bb207d5fc4b82f43f511
     &tag=latest&apikey=YourApiKeyToken`)

}

```

We don't currently support [**all endpoints**](https://docs.etherscan.io/etherscan-v2/getting-started/supported-endpoints) on all chains. Please feel free to [**reach out**](mailto:apisupport@etherscan.io) if you need something specific!

[NextV2 FAQ](https://docs.etherscan.io/etherscan-v2/v2-faq)

Last updated 1 month ago

This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject