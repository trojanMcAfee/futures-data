The closest real world example of a raw transaction — probably a bank cheque 💸

Some ways we can utilize raw transactions include signing a transaction offline on a secure machine and then broadcasting it separately or to send a transaction at a later point of time.

> You will need [**Node.js**](https://nodejs.org/en/)![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2Fsg8e76TOnPYfHTGZoQl0%2Fblobs%2FgjpVSkZq6CJyKfXKkXAd%2FBiXDFDDp_400x400.jpg&width=40&dpr=4&quality=100&sign=cf301d2b&sv=2) installed and a valid [**Etherscan API Key**](https://docs.etherscan.io/etherscan-v2/getting-started/viewing-api-usage-statistics) **.**

### [Direct link to heading](https://docs.etherscan.io/etherscan-v2/tutorials/signing-raw-transactions\#id-1.-setting-up-a-node.js-project)    **1\. Setting up a Node.js project**

In a new folder, initiate a new Node.js project with the command `npm init -y` to accept all default project parameters.

A `package.json` file will be created for you, which contains all your packages and project information.

![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2Fsg8e76TOnPYfHTGZoQl0%2Fblobs%2FgpxGj1VD3kaspEJvja3Z%2Fimage.png&width=768&dpr=4&quality=100&sign=d95cec8&sv=2)

### [Direct link to heading](https://docs.etherscan.io/etherscan-v2/tutorials/signing-raw-transactions\#id-2.-integrating-ethers.js)    2\. Integrating Ethers.js

We'll need to integrate a helpful JavaScript library known as [**Ethers.js**](https://www.npmjs.com/package/ethers) that will help with interacting with the Ethereum blockchain.

We can do so using the command `npm i ethers` from a terminal within this project, which will add `ethers` as a dependency.

![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2Fsg8e76TOnPYfHTGZoQl0%2Fblobs%2F2XSs4ZvlBCXVEsWflf9F%2Fimage.png&width=768&dpr=4&quality=100&sign=f3f79687&sv=2)

We'll then create a new file named `transaction.js` where we'll write the rest of the code in JavaScript and import `ethers` at the top of the file.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
const ethers = require('ethers');

async function main() {

  // rest of code goes here

}

main();
```

### [Direct link to heading](https://docs.etherscan.io/etherscan-v2/tutorials/signing-raw-transactions\#id-3.-creating-a-wallet)    3\. Creating a wallet

One of the useful classes that [**Ethers.js**](https://www.npmjs.com/package/ethers) provides is a `Wallet`, which represents a regular Ethereum address that you can use to store and send Ether.

We can initiate a new `Wallet` by specifying a private key which we can [**generate**](https://www.myetherwallet.com/wallet/create) or grab one from an existing wallet like [**MetaMask.**](https://metamask.io/)

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
const ethers = require('ethers');

async function main() {

  // defining the wallet private key
  let privatekey = 'CE75F1A875F2DB7FB064F5DBD302B0C77FFEAA18CC4C314167A5111A04F79AFA';
  let wallet = new ethers.Wallet(privatekey);

  // print the wallet address
  console.log('Using wallet address ' + wallet.address);

}

main();
```

### [Direct link to heading](https://docs.etherscan.io/etherscan-v2/tutorials/signing-raw-transactions\#id-4.-crafting-the-transaction)    4\. Crafting the transaction

A transactions is made up of several parameters that have to be defined, for this example we'll be making a simple ETH transfer.

If you are following this article on a [**testnet**](https://ethereum.org/en/developers/docs/networks/#testnets), feel free to get some [**testnet Ether**](https://ethereum.org/en/developers/docs/networks/#testnet-faucets) ![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2Fsg8e76TOnPYfHTGZoQl0%2Fblobs%2FRw3lIchVYIgfFA8T83EX%2F1200px-Ethereum-icon-purple.svg.png&width=40&dpr=4&quality=100&sign=b9ab6ddf&sv=2)to fund your address.

Parameter

Description

to

the `address` to send Ether to

value

the amount of Ether to send

gasLimit

the maximum [**units of gas**](https://ethereum.org/en/developers/docs/gas/) to consume in this transaction, set to `21000` for basic Ether transfers

maxPriorityFeePerGas

the tip paid to miners, introduced in [**EIP-1559**](https://metamask.io/1559)

maxFeePerGas

the maximum price paid per unit of gas, introduced in [**EIP-1559**](https://metamask.io/1559)

nonce

the [**number of transactions**](https://kb.myetherwallet.com/en/transactions/what-is-nonce/) sent from the address

type

set to `0x2`, to denote EIP-1559 type transactions

chainId

the [**chain ID**](https://chainlist.org/) to send the transaction, for example `3` for Ropsten

The sample code to send `1 Ether` to address `0xEeee7341f206302f2216e39D715B96D8C6901A1C` on the [**Ropsteh testnet**](https://ropsten.etherscan.io/) will be as follows.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
const ethers = require('ethers');

async function main() {

  let privatekey = 'CE75F1A875F2DB7FB064F5DBD302B0C77FFEAA18CC4C314167A5111A04F79AFA';
  let wallet = new ethers.Wallet(privatekey);

  console.log('Using wallet address ' + wallet.address);

  let transaction = {
    to: '0xa238b6008Bc2FBd9E386A5d4784511980cE504Cd',
    value: ethers.utils.parseEther('1'),
    gasLimit: '21000',
    maxPriorityFeePerGas: ethers.utils.parseUnits('5', 'gwei'),
    maxFeePerGas: ethers.utils.parseUnits('20', 'gwei'),
    nonce: 1,
    type: 2,
    chainId: 3
  };

}

main();
```

### [Direct link to heading](https://docs.etherscan.io/etherscan-v2/tutorials/signing-raw-transactions\#id-5.-sign-and-serialize)    5\. Sign & serialize

After detailing the contents of the transaction, we'll need to sign it — using the wallet's private key we created in Step 3 to prove we are allowed to spend funds in the wallet address.

With the transaction signed, we have just one more step to _serialize_, or simply converting our transaction into a hexadecimal format.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
const ethers = require('ethers');

async function main() {

  let privatekey = 'CE75F1A875F2DB7FB064F5DBD302B0C77FFEAA18CC4C314167A5111A04F79AFA';
  let wallet = new ethers.Wallet(privatekey);

  console.log('Using wallet address ' + wallet.address);

  let transaction = {
    to: '0xa238b6008Bc2FBd9E386A5d4784511980cE504Cd',
    value: ethers.utils.parseEther('1'),
    gasLimit: '21000',
    maxPriorityFeePerGas: ethers.utils.parseUnits('5', 'gwei'),
    maxFeePerGas: ethers.utils.parseUnits('20', 'gwei'),
    nonce: 1,
    type: 2,
    chainId: 3
  };

  // sign and serialize the transaction
  let rawTransaction = await wallet.signTransaction(transaction).then(ethers.utils.serializeTransaction(transaction));

  // print the raw transaction hash
  console.log('Raw txhash string ' + rawTransaction);

}

main();
```

### [Direct link to heading](https://docs.etherscan.io/etherscan-v2/tutorials/signing-raw-transactions\#id-6.-send-via-api)    6\. Send via API

With the signed raw transaction, we can now pass it to the " [**eth\_sendRawTransaction**](https://docs.etherscan.io/etherscan-v2/api-endpoints/geth-parity-proxy#eth_sendrawtransaction)" endpoint to be broadcasted to the Ethereum network.

A successfully broadcasted transaction will return a transaction hash, which you can use the " [**eth\_getTransactionbyHash**](https://docs.etherscan.io/etherscan-v2/api-endpoints/geth-parity-proxy#eth_gettransactionbyhash)" endpoint or look it up on Etherscan!

You can run this code using the command `node transaction.js`

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
const ethers = require('ethers');
const fetch = require('node-fetch');

async function main() {

  let privatekey = 'CE75F1A875F2DB7FB064F5DBD302B0C77FFEAA18CC4C314167A5111A04F79AFA';
  let wallet = new ethers.Wallet(privatekey);

  console.log('Using wallet address ' + wallet.address);

  let transaction = {
    to: '0xa238b6008Bc2FBd9E386A5d4784511980cE504Cd',
    value: ethers.utils.parseEther('1'),
    gasLimit: '21000',
    maxPriorityFeePerGas: ethers.utils.parseUnits('5', 'gwei'),
    maxFeePerGas: ethers.utils.parseUnits('20', 'gwei'),
    nonce: 1,
    type: 2,
    chainId: 3
  };

  let rawTransaction = await wallet.signTransaction(transaction).then(ethers.utils.serializeTransaction(transaction));
  console.log('Raw txhash string ' + rawTransaction);

  // pass the raw transaction hash to the "eth_sendRawTransaction" endpoint
  let gethProxy = await fetch(`https://api-ropsten.etherscan.io/api?chainid=1
   &module=proxy&action=eth_sendRawTransaction&hex=${rawTransaction}&apikey=YourApiKeyToken`);
  let response = await gethProxy.json();

  // print the API response
  console.log(response);

}

main();
```

## [Direct link to heading](https://docs.etherscan.io/etherscan-v2/tutorials/signing-raw-transactions\#wrapping-up)    Wrapping Up

The full sample code for this tutorial is on [**Github**](https://github.com/0xV4L3NT1N3/ethereum-raw-transactions), feel free to fork and extend the functionality of it ! 🤖

Last updated 5 months ago

This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject