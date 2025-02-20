[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/periphery/UniswapV4DeployerCompetition#)

On this page

# UniswapV4DeployerCompetition

[Git Source](https://github.com/uniswap/v4-periphery/blob/3f295d8435e4f776ea2daeb96ce1bc6d63f33fc7/src/UniswapV4DeployerCompetition.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:** [IUniswapV4DeployerCompetition](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IUniswapV4DeployerCompetition)

A contract to crowdsource a salt for the best Uniswap V4 address

## State Variables [​](https://docs.uniswap.org/contracts/v4/reference/periphery/UniswapV4DeployerCompetition\#state-variables "Direct link to heading")

### bestAddressSalt [​](https://docs.uniswap.org/contracts/v4/reference/periphery/UniswapV4DeployerCompetition\#bestaddresssalt "Direct link to heading")

_The salt for the best address found so far_

```codeBlockLines_mRuA
bytes32 public bestAddressSalt;

```

Copy

### bestAddressSubmitter [​](https://docs.uniswap.org/contracts/v4/reference/periphery/UniswapV4DeployerCompetition\#bestaddresssubmitter "Direct link to heading")

_The submitter of the best address found so far_

```codeBlockLines_mRuA
address public bestAddressSubmitter;

```

Copy

### competitionDeadline [​](https://docs.uniswap.org/contracts/v4/reference/periphery/UniswapV4DeployerCompetition\#competitiondeadline "Direct link to heading")

_The deadline for the competition_

```codeBlockLines_mRuA
uint256 public immutable competitionDeadline;

```

Copy

### initCodeHash [​](https://docs.uniswap.org/contracts/v4/reference/periphery/UniswapV4DeployerCompetition\#initcodehash "Direct link to heading")

_The init code hash of the V4 contract_

```codeBlockLines_mRuA
bytes32 public immutable initCodeHash;

```

Copy

### deployer [​](https://docs.uniswap.org/contracts/v4/reference/periphery/UniswapV4DeployerCompetition\#deployer "Direct link to heading")

_The deployer who can initiate the deployment of the v4 PoolManager, until the exclusive deploy deadline._

_After this deadline anyone can deploy._

```codeBlockLines_mRuA
address public immutable deployer;

```

Copy

### exclusiveDeployDeadline [​](https://docs.uniswap.org/contracts/v4/reference/periphery/UniswapV4DeployerCompetition\#exclusivedeploydeadline "Direct link to heading")

_The deadline for exclusive deployment by deployer after deadline_

```codeBlockLines_mRuA
uint256 public immutable exclusiveDeployDeadline;

```

Copy

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/periphery/UniswapV4DeployerCompetition\#functions "Direct link to heading")

### constructor [​](https://docs.uniswap.org/contracts/v4/reference/periphery/UniswapV4DeployerCompetition\#constructor "Direct link to heading")

```codeBlockLines_mRuA
constructor(
    bytes32 _initCodeHash,
    uint256 _competitionDeadline,
    address _exclusiveDeployer,
    uint256 _exclusiveDeployLength
);

```

Copy

### updateBestAddress [​](https://docs.uniswap.org/contracts/v4/reference/periphery/UniswapV4DeployerCompetition\#updatebestaddress "Direct link to heading")

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

### deploy [​](https://docs.uniswap.org/contracts/v4/reference/periphery/UniswapV4DeployerCompetition\#deploy "Direct link to heading")

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

### bestAddress [​](https://docs.uniswap.org/contracts/v4/reference/periphery/UniswapV4DeployerCompetition\#bestaddress "Direct link to heading")

_returns the best address found so far_

```codeBlockLines_mRuA
function bestAddress() public view returns (address);

```

Copy

- [State Variables](https://docs.uniswap.org/contracts/v4/reference/periphery/UniswapV4DeployerCompetition#state-variables)
  - [bestAddressSalt](https://docs.uniswap.org/contracts/v4/reference/periphery/UniswapV4DeployerCompetition#bestaddresssalt)
  - [bestAddressSubmitter](https://docs.uniswap.org/contracts/v4/reference/periphery/UniswapV4DeployerCompetition#bestaddresssubmitter)
  - [competitionDeadline](https://docs.uniswap.org/contracts/v4/reference/periphery/UniswapV4DeployerCompetition#competitiondeadline)
  - [initCodeHash](https://docs.uniswap.org/contracts/v4/reference/periphery/UniswapV4DeployerCompetition#initcodehash)
  - [deployer](https://docs.uniswap.org/contracts/v4/reference/periphery/UniswapV4DeployerCompetition#deployer)
  - [exclusiveDeployDeadline](https://docs.uniswap.org/contracts/v4/reference/periphery/UniswapV4DeployerCompetition#exclusivedeploydeadline)
- [Functions](https://docs.uniswap.org/contracts/v4/reference/periphery/UniswapV4DeployerCompetition#functions)
  - [constructor](https://docs.uniswap.org/contracts/v4/reference/periphery/UniswapV4DeployerCompetition#constructor)
  - [updateBestAddress](https://docs.uniswap.org/contracts/v4/reference/periphery/UniswapV4DeployerCompetition#updatebestaddress)
  - [deploy](https://docs.uniswap.org/contracts/v4/reference/periphery/UniswapV4DeployerCompetition#deploy)
  - [bestAddress](https://docs.uniswap.org/contracts/v4/reference/periphery/UniswapV4DeployerCompetition#bestaddress)