For repeated or multichain contract verification, it's best to use the [**Verify Contract endpoint**](https://docs.etherscan.io/etherscan-v2/api-endpoints/contracts#verify-source-code) to automate source code submission 🐇.

> You may specify a `chainId` along with an [**Etherscan API key**](https://docs.etherscan.io/etherscan-v2/getting-started/viewing-api-usage-statistics) to submit verification for any Etherscan-like explorer

## [Direct link to heading](https://docs.etherscan.io/etherscan-v2/contract-verification/multichain-verification\#id-1.-using-the-verify-contract-endpoint)    1\. Using the Verify Contract Endpoint

In Postman, set your request method to **HTTP POST** and your URL to `https://api.etherscan.io/v2/api` .

Specify the verification endpoint under the **query parameters**, with the module set to `contract` and action to `verifysourcecode`.

All API based verification must be authenticated, include your [**Etherscan API key**](https://docs.etherscan.io/etherscan-v2/getting-started/viewing-api-usage-statistics) under the "apikey" field.

![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F2695072255-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fsg8e76TOnPYfHTGZoQl0%252Fuploads%252FGADU9w70J0j2ZvSrczFH%252Fimage.png%3Falt%3Dmedia%26token%3Ddf039dc3-115a-405d-9975-d24e35a50676&width=768&dpr=4&quality=100&sign=ac784a7&sv=2)

## [Direct link to heading](https://docs.etherscan.io/etherscan-v2/contract-verification/multichain-verification\#id-2.-specify-your-chainid)    2\. Specify Your chainId

Specify it under the "chainId" where you've deployed your contract, such as `1` for Ethereum and `8453` for Base.

![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F2695072255-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fsg8e76TOnPYfHTGZoQl0%252Fuploads%252Fpy5oGUgL6orLD8VRQVbJ%252Fimage.png%3Falt%3Dmedia%26token%3D5d9f6f08-8a04-46cb-a317-36670e8ce567&width=768&dpr=4&quality=100&sign=5f012cb&sv=2)

## [Direct link to heading](https://docs.etherscan.io/etherscan-v2/contract-verification/multichain-verification\#id-3.-add-contract-source-code)    3\. Add Contract Source Code

We support 2 formats, `solidity-single-file` or `solidity-standard-json-input.`

Using JSON is the gold standard ✨ for verification, as you can [**include compiler settings and multiple files**](https://gist.github.com/0xV4L3NT1N3/974d6bfb58070e0fe4e38d626cdf1c44) ( if you use imports such as from [**OpenZeppelin**](https://www.openzeppelin.com/contracts) ).

Under the **request body, p** aste your source code under "sourceCode" and the code format under the "codeformat" parameter.

![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F2695072255-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fsg8e76TOnPYfHTGZoQl0%252Fuploads%252FBBt2dykp2TxyK4Vkaypv%252Fimage.png%3Falt%3Dmedia%26token%3D1d1e4d7d-afcb-466d-a62e-2269543d8e3d&width=768&dpr=4&quality=100&sign=9e9fbc78&sv=2)

Optionally if your contract uses [**constructor arguments**](https://info.etherscan.com/contract-verification-constructor-arguments/), you may specify them too under the "constructorArguments" parameter in [**ABI encoded**](https://abi.hashex.org/) format.

![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F2695072255-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fsg8e76TOnPYfHTGZoQl0%252Fuploads%252F6JSPmUWqQzXnXEIdl0lx%252Fimage.png%3Falt%3Dmedia%26token%3D056c4181-85b2-435a-ba51-9bca1157328a&width=768&dpr=4&quality=100&sign=83349db0&sv=2)

## [Direct link to heading](https://docs.etherscan.io/etherscan-v2/contract-verification/multichain-verification\#id-4.-add-contract-metadata)    4\. Add Contract Metadata

Include the contract address as "contractaddress", beginning with "0x".

Specify your contract file path and contract name **separated by a colon** as "contractname", such as "contracts/Verified.sol:Verified".

Select the compiler version used from [**this list**](https://etherscan.io/solcversions) as your "compilerversion".

![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F2695072255-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fsg8e76TOnPYfHTGZoQl0%252Fuploads%252FfRvzt7H3yZafWB9Viazu%252Fimage.png%3Falt%3Dmedia%26token%3D1c392b11-dfbf-42de-b881-77b659b97d71&width=768&dpr=4&quality=100&sign=673eba7f&sv=2)

## [Direct link to heading](https://docs.etherscan.io/etherscan-v2/contract-verification/multichain-verification\#id-5.-submitting-verification)    5\. Submitting Verification

Click Send and you'll receive a `guid` which you can then [**check on your verification status**](https://docs.etherscan.io/etherscan-v2/api-endpoints/contracts#check-source-code-verification-submission-status).

![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F2695072255-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fsg8e76TOnPYfHTGZoQl0%252Fuploads%252F78y7DE3v5BYXVn0aCIkW%252Fimage.png%3Falt%3Dmedia%26token%3D4fe2a5aa-7ecd-4431-a2c5-553e402cc490&width=768&dpr=4&quality=100&sign=5cf9eb6a&sv=2)

Alternatively if everything went well, you'll see the happy green checkmark on your [**contract code**](https://basescan.org/address/0x2358f143ecc1802631dd0e86aec0786a7cbdd19d) ✅

![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F2695072255-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fsg8e76TOnPYfHTGZoQl0%252Fuploads%252FCoiQU3wP9T2bO9SEuGLL%252Fimage.png%3Falt%3Dmedia%26token%3D70f1a990-774f-47d0-a8d4-1c9ffad9ffe0&width=768&dpr=4&quality=100&sign=a1ecab31&sv=2)

Last updated 5 months ago

This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject