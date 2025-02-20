[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/libraries/LiquidityMath#)

On this page

# LiquidityMath

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/libraries/LiquidityMath.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/LiquidityMath\#functions "Direct link to heading")

### addDelta [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/LiquidityMath\#adddelta "Direct link to heading")

Add a signed liquidity delta to liquidity and revert if it overflows or underflows

```codeBlockLines_mRuA
function addDelta(uint128 x, int128 y) internal pure returns (uint128 z);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `x` | `uint128` | The liquidity before change |
| `y` | `int128` | The delta by which liquidity should be changed |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `z` | `uint128` | The liquidity delta |

- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/libraries/LiquidityMath#functions)
  - [addDelta](https://docs.uniswap.org/contracts/v4/reference/core/libraries/LiquidityMath#adddelta)