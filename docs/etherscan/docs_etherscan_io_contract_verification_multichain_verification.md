For repeated or multichain contract verification, it's best to use the [**Verify Contract endpoint**](https://docs.etherscan.io/api-endpoints/contracts#verify-source-code) to automate source code submission 🐇.

> You may specify a `chainId` along with an [**Etherscan API key**](https://docs.etherscan.io/getting-started/viewing-api-usage-statistics) to submit verification for any Etherscan-like explorer

## [Direct link to heading](https://docs.etherscan.io/contract-verification/multichain-verification\#id-1.-using-the-verify-contract-endpoint)    1\. Using the Verify Contract Endpoint

In Postman, set your request method to **HTTP POST** and your URL to `https://api.etherscan.io/api` .

Under the Body tab and using `form-data`, specify the "module" to `contract` and "action" to `verifysourcecode.`

All API based verification must be authenticated, include your [**Etherscan API key**](https://docs.etherscan.io/getting-started/viewing-api-usage-statistics) under the "apikey" field.

![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F1052732906-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-McrExXKKJBLJqymbFhO%252Fuploads%252FzhH98WU0nkaqlYxZkuMS%252Fimage.png%3Falt%3Dmedia%26token%3D56c608a7-d077-4a28-82c9-cd5337c59e56&width=768&dpr=4&quality=100&sign=3362c82d&sv=2)

## [Direct link to heading](https://docs.etherscan.io/contract-verification/multichain-verification\#id-2.-specify-your-chainid)    2\. Specify Your chainId

Select the chain you've deployed your contract, which is supported by an Etherscan-like explorer.

Specify it under the "chainId" parameter, such as `1` for Ethereum and `8453` for Base.

![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F1052732906-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-McrExXKKJBLJqymbFhO%252Fuploads%252Fz6CbWH0JYs2vwSFyH4Yq%252Fimage.png%3Falt%3Dmedia%26token%3D8ea621e1-31b6-49e8-943f-abde221fb9fb&width=768&dpr=4&quality=100&sign=c1d2daa1&sv=2)

## [Direct link to heading](https://docs.etherscan.io/contract-verification/multichain-verification\#id-3.-add-contract-source-code)    3\. Add Contract Source Code

We support 2 formats, `solidity-single-file` or `solidity-standard-json-input.`

Using JSON is the gold standard ✨ for verification, as you can [**include compiler settings and multiple files**](https://gist.github.com/0xV4L3NT1N3/974d6bfb58070e0fe4e38d626cdf1c44) ( if you use imports such as from [**OpenZeppelin**](https://www.openzeppelin.com/contracts) ).

Paste your source code under "sourceCode" and the code format under the "codeformat" parameter.

![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F1052732906-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-McrExXKKJBLJqymbFhO%252Fuploads%252FP9uQLccIb2xaFvvDxKRo%252Fimage.png%3Falt%3Dmedia%26token%3D87c17e56-2627-4b41-99ca-d3e5dcccd9c3&width=768&dpr=4&quality=100&sign=5cb10465&sv=2)

Optionally if your contract uses [**constructor arguments**](https://info.etherscan.com/contract-verification-constructor-arguments/), you may specify them too under the "constructorArguments" parameter in [**ABI encoded**](https://abi.hashex.org/) format.

![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F1052732906-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-McrExXKKJBLJqymbFhO%252Fuploads%252Fmru5Xx3qH94a6qdffuIQ%252Fimage.png%3Falt%3Dmedia%26token%3D8fe9f723-6ca1-4928-a137-ac78b9dffbd4&width=768&dpr=4&quality=100&sign=f2873ec2&sv=2)

## [Direct link to heading](https://docs.etherscan.io/contract-verification/multichain-verification\#id-4.-add-contract-metadata)    4\. Add Contract Metadata

Include the contract address as "contractaddress", beginning with "0x".

Specify your contract file path and contract name **separated by a colon** as "contractname", such as "contracts/Verified.sol:Verified".

Select the compiler version used from [**this list**](https://etherscan.io/solcversions) as your "compilerversion".

![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F1052732906-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-McrExXKKJBLJqymbFhO%252Fuploads%252FkKL2HBUhNnNb7fE99Yby%252Fimage.png%3Falt%3Dmedia%26token%3D3555f9a0-41b9-4f5b-9d0f-263a8e8fb987&width=768&dpr=4&quality=100&sign=6dfe22b5&sv=2)

## [Direct link to heading](https://docs.etherscan.io/contract-verification/multichain-verification\#id-5.-submitting-verification)    5\. Submitting Verification

Click Send and you'll receive a `guid` which you can then [**check on your verification status**](https://docs.etherscan.io/api-endpoints/contracts#check-source-code-verification-submission-status).

![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F1052732906-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-McrExXKKJBLJqymbFhO%252Fuploads%252FCyOerxywXafujtyIkADi%252Fimage.png%3Falt%3Dmedia%26token%3Dde329c92-8e26-4165-a03e-35e7c2edb501&width=768&dpr=4&quality=100&sign=7bdff8c7&sv=2)

Alternatively if everything went well, you'll see the happy green checkmark on your [**contract code**](https://basescan.org/address/0x539a277b12a3f6723f4c1769edb11b0be7c214da#code) ✅

![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F1052732906-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-McrExXKKJBLJqymbFhO%252Fuploads%252Fo9hC2gjarJCDNET9u4i7%252Fimage.png%3Falt%3Dmedia%26token%3D9b0c9755-b076-455a-8084-46c3db70e475&width=768&dpr=4&quality=100&sign=ca929b4a&sv=2)

[PreviousWhat's Contract Verification](https://docs.etherscan.io/contract-verification/whats-contract-verification) [NextSupported Chains](https://docs.etherscan.io/contract-verification/supported-chains)

Last updated 9 months ago

This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject