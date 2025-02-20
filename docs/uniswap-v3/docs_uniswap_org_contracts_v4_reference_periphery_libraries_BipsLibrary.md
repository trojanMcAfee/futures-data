[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/BipsLibrary#)

On this page

# BipsLibrary

[Git Source](https://github.com/uniswap/v4-periphery/blob/3f295d8435e4f776ea2daeb96ce1bc6d63f33fc7/src/libraries/BipsLibrary.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

## State Variables [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/BipsLibrary\#state-variables "Direct link to heading")

### BPS\_DENOMINATOR [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/BipsLibrary\#bps_denominator "Direct link to heading")

```codeBlockLines_mRuA
uint256 internal constant BPS_DENOMINATOR = 10_000;

```

Copy

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/BipsLibrary\#functions "Direct link to heading")

### calculatePortion [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/BipsLibrary\#calculateportion "Direct link to heading")

```codeBlockLines_mRuA
function calculatePortion(uint256 amount, uint256 bips) internal pure returns (uint256);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `amount` | `uint256` | The total amount to calculate a percentage of |
| `bips` | `uint256` | The percentage to calculate, in bips |

## Errors [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/BipsLibrary\#errors "Direct link to heading")

### InvalidBips [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/BipsLibrary\#invalidbips "Direct link to heading")

emitted when an invalid percentage is provided

```codeBlockLines_mRuA
error InvalidBips();

```

Copy

- [State Variables](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/BipsLibrary#state-variables)
  - [BPS\_DENOMINATOR](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/BipsLibrary#bps_denominator)
- [Functions](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/BipsLibrary#functions)
  - [calculatePortion](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/BipsLibrary#calculateportion)
- [Errors](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/BipsLibrary#errors)
  - [InvalidBips](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/BipsLibrary#invalidbips)