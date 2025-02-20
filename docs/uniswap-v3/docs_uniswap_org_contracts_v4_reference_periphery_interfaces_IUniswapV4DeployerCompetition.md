[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IUniswapV4DeployerCompetition#)

On this page

# IUniswapV4DeployerCompetition

[Git Source](https://github.com/uniswap/v4-periphery/blob/3f295d8435e4f776ea2daeb96ce1bc6d63f33fc7/src/interfaces/IUniswapV4DeployerCompetition.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

A competition to deploy the UniswapV4 contract with the best address

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IUniswapV4DeployerCompetition\#functions "Direct link to heading")

### updateBestAddress [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IUniswapV4DeployerCompetition\#updatebestaddress "Direct link to heading")

Updates the best address if the new address has a better vanity score

_The first 20 bytes of the salt must be either address(0) or msg.sender_

```codeBlockLines_mRuA
function updateBestAddress(bytes32 salt) external;

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `salt` | `bytes32` | The salt to use to compute the new address with CREATE2 |

### deploy [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IUniswapV4DeployerCompetition\#deploy "Direct link to heading")

deploys the Uniswap v4 PoolManager contract

_The bytecode must match the initCodeHash_

```codeBlockLines_mRuA
function deploy(bytes memory bytecode) external;

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `bytecode` | `bytes` | The bytecode of the Uniswap v4 PoolManager contract |

## Events [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IUniswapV4DeployerCompetition\#events "Direct link to heading")

### NewAddressFound [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IUniswapV4DeployerCompetition\#newaddressfound "Direct link to heading")

```codeBlockLines_mRuA
event NewAddressFound(address indexed bestAddress, address indexed submitter, uint256 score);

```

Copy

## Errors [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IUniswapV4DeployerCompetition\#errors "Direct link to heading")

### InvalidBytecode [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IUniswapV4DeployerCompetition\#invalidbytecode "Direct link to heading")

```codeBlockLines_mRuA
error InvalidBytecode();

```

Copy

### CompetitionNotOver [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IUniswapV4DeployerCompetition\#competitionnotover "Direct link to heading")

```codeBlockLines_mRuA
error CompetitionNotOver(uint256 currentTime, uint256 deadline);

```

Copy

### CompetitionOver [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IUniswapV4DeployerCompetition\#competitionover "Direct link to heading")

```codeBlockLines_mRuA
error CompetitionOver(uint256 currentTime, uint256 deadline);

```

Copy

### NotAllowedToDeploy [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IUniswapV4DeployerCompetition\#notallowedtodeploy "Direct link to heading")

```codeBlockLines_mRuA
error NotAllowedToDeploy(address sender, address deployer);

```

Copy

### WorseAddress [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IUniswapV4DeployerCompetition\#worseaddress "Direct link to heading")

```codeBlockLines_mRuA
error WorseAddress(address newAddress, address bestAddress, uint256 newScore, uint256 bestScore);

```

Copy

### InvalidSender [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IUniswapV4DeployerCompetition\#invalidsender "Direct link to heading")

```codeBlockLines_mRuA
error InvalidSender(bytes32 salt, address sender);

```

Copy

- [Functions](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IUniswapV4DeployerCompetition#functions)
  - [updateBestAddress](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IUniswapV4DeployerCompetition#updatebestaddress)
  - [deploy](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IUniswapV4DeployerCompetition#deploy)
- [Events](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IUniswapV4DeployerCompetition#events)
  - [NewAddressFound](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IUniswapV4DeployerCompetition#newaddressfound)
- [Errors](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IUniswapV4DeployerCompetition#errors)
  - [InvalidBytecode](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IUniswapV4DeployerCompetition#invalidbytecode)
  - [CompetitionNotOver](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IUniswapV4DeployerCompetition#competitionnotover)
  - [CompetitionOver](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IUniswapV4DeployerCompetition#competitionover)
  - [NotAllowedToDeploy](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IUniswapV4DeployerCompetition#notallowedtodeploy)
  - [WorseAddress](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IUniswapV4DeployerCompetition#worseaddress)
  - [InvalidSender](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IUniswapV4DeployerCompetition#invalidsender)