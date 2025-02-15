### [Direct link to heading](https://docs.etherscan.io/etherscan-v2/getting-started/v2-quickstart\#if-youre-coming-from-v1)    If you're coming from V1

Your base url looks like this

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/api
```

Just append V2 to the base url, and a `chainId` parameter

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/v2/api?chainid=1
```

### [Direct link to heading](https://docs.etherscan.io/etherscan-v2/getting-started/v2-quickstart\#if-youre-coming-from-another-explorer-basescan-arbiscan-polygonscan-etc)    If you're coming from another explorer, Basescan/Arbiscan/Polygonscan etc

Your query looks something like one of these

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.basescan.org/api
https://api.polygonscan.com/api
https://api.bscscan.com/api
https://api.apescan.io/api
```

Change your base URL to Etherscan, and point the chainId to `8453` or any chain you want

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
https://api.etherscan.io/v2/api?chainid=8453
```

### [Direct link to heading](https://docs.etherscan.io/etherscan-v2/getting-started/v2-quickstart\#if-youre-starting-with-v2)    If you're starting with V2

Run this complete script with Node JS, `node script.js`

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
async function main() {

    // query ETH balances on Arbitrum, Base and Optimism

    const chains = [42161, 8453, 10]

    for (const chain of chains) {

        // endpoint accepts one chain at a time, loop for all your chains

        const query = await fetch(`https://api.etherscan.io/v2/api
           ?chainid=${chain}
           &module=account
           &action=balance
           &address=0xb5d85cbf7cb3ee0d56b3bb207d5fc4b82f43f511
           &tag=latest&apikey=YourApiKeyToken`)

        const response = await query.json()

        const balance = response.result
        console.log(balance)

    }
}

main()
```

[PreviousV2 FAQ](https://docs.etherscan.io/etherscan-v2/v2-faq) [NextCreating an Account](https://docs.etherscan.io/etherscan-v2/getting-started/creating-an-account)

Last updated 3 months ago

This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject