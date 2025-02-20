[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/test/Fuzzers#)

On this page

# Fuzzers

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/test/Fuzzers.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:**
StdUtils

## State Variables [​](https://docs.uniswap.org/contracts/v4/reference/core/test/Fuzzers\#state-variables "Direct link to heading")

### \_vm [​](https://docs.uniswap.org/contracts/v4/reference/core/test/Fuzzers\#_vm "Direct link to heading")

```codeBlockLines_mRuA
Vm internal constant _vm = Vm(address(uint160(uint256(keccak256("hevm cheat code")))));

```

Copy

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/test/Fuzzers\#functions "Direct link to heading")

### boundLiquidityDelta [​](https://docs.uniswap.org/contracts/v4/reference/core/test/Fuzzers\#boundliquiditydelta "Direct link to heading")

```codeBlockLines_mRuA
function boundLiquidityDelta(PoolKey memory key, int256 liquidityDeltaUnbounded, int256 liquidityMaxByAmount)
    internal
    pure
    returns (int256);

```

Copy

### boundLiquidityDeltaTightly [​](https://docs.uniswap.org/contracts/v4/reference/core/test/Fuzzers\#boundliquiditydeltatightly "Direct link to heading")

```codeBlockLines_mRuA
function boundLiquidityDeltaTightly(
    PoolKey memory key,
    int256 liquidityDeltaUnbounded,
    int256 liquidityMaxByAmount,
    uint256 maxPositions
) internal pure returns (int256);

```

Copy

### getLiquidityDeltaFromAmounts [​](https://docs.uniswap.org/contracts/v4/reference/core/test/Fuzzers\#getliquiditydeltafromamounts "Direct link to heading")

```codeBlockLines_mRuA
function getLiquidityDeltaFromAmounts(int24 tickLower, int24 tickUpper, uint160 sqrtPriceX96)
    internal
    pure
    returns (int256);

```

Copy

### boundTicks [​](https://docs.uniswap.org/contracts/v4/reference/core/test/Fuzzers\#boundticks "Direct link to heading")

```codeBlockLines_mRuA
function boundTicks(int24 tickLower, int24 tickUpper, int24 tickSpacing) internal pure returns (int24, int24);

```

Copy

### boundTicks [​](https://docs.uniswap.org/contracts/v4/reference/core/test/Fuzzers\#boundticks-1 "Direct link to heading")

```codeBlockLines_mRuA
function boundTicks(PoolKey memory key, int24 tickLower, int24 tickUpper) internal pure returns (int24, int24);

```

Copy

### createRandomSqrtPriceX96 [​](https://docs.uniswap.org/contracts/v4/reference/core/test/Fuzzers\#createrandomsqrtpricex96 "Direct link to heading")

```codeBlockLines_mRuA
function createRandomSqrtPriceX96(int24 tickSpacing, int256 seed) internal pure returns (uint160);

```

Copy

### createFuzzyLiquidityParams [​](https://docs.uniswap.org/contracts/v4/reference/core/test/Fuzzers\#createfuzzyliquidityparams "Direct link to heading")

_Obtain fuzzed and bounded parameters for creating liquidity_

```codeBlockLines_mRuA
function createFuzzyLiquidityParams(
    PoolKey memory key,
    IPoolManager.ModifyLiquidityParams memory params,
    uint160 sqrtPriceX96
) internal pure returns (IPoolManager.ModifyLiquidityParams memory result);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `key` | `PoolKey` | The pool key |
| `params` | `IPoolManager.ModifyLiquidityParams` | IPoolManager.ModifyLiquidityParams Note that these parameters are unbounded |
| `sqrtPriceX96` | `uint160` | The current sqrt price |

### createFuzzyLiquidityParamsWithTightBound [​](https://docs.uniswap.org/contracts/v4/reference/core/test/Fuzzers\#createfuzzyliquidityparamswithtightbound "Direct link to heading")

```codeBlockLines_mRuA
function createFuzzyLiquidityParamsWithTightBound(
    PoolKey memory key,
    IPoolManager.ModifyLiquidityParams memory params,
    uint160 sqrtPriceX96,
    uint256 maxPositions
) internal pure returns (IPoolManager.ModifyLiquidityParams memory result);

```

Copy

### createFuzzyLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/core/test/Fuzzers\#createfuzzyliquidity "Direct link to heading")

```codeBlockLines_mRuA
function createFuzzyLiquidity(
    PoolModifyLiquidityTest modifyLiquidityRouter,
    PoolKey memory key,
    IPoolManager.ModifyLiquidityParams memory params,
    uint160 sqrtPriceX96,
    bytes memory hookData
) internal returns (IPoolManager.ModifyLiquidityParams memory result, BalanceDelta delta);

```

Copy

### createFuzzyLiquidityWithTightBound [​](https://docs.uniswap.org/contracts/v4/reference/core/test/Fuzzers\#createfuzzyliquiditywithtightbound "Direct link to heading")

```codeBlockLines_mRuA
function createFuzzyLiquidityWithTightBound(
    PoolModifyLiquidityTest modifyLiquidityRouter,
    PoolKey memory key,
    IPoolManager.ModifyLiquidityParams memory params,
    uint160 sqrtPriceX96,
    bytes memory hookData,
    uint256 maxPositions
) internal returns (IPoolManager.ModifyLiquidityParams memory result, BalanceDelta delta);

```

Copy

- [State Variables](https://docs.uniswap.org/contracts/v4/reference/core/test/Fuzzers#state-variables)
  - [\_vm](https://docs.uniswap.org/contracts/v4/reference/core/test/Fuzzers#_vm)
- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/test/Fuzzers#functions)
  - [boundLiquidityDelta](https://docs.uniswap.org/contracts/v4/reference/core/test/Fuzzers#boundliquiditydelta)
  - [boundLiquidityDeltaTightly](https://docs.uniswap.org/contracts/v4/reference/core/test/Fuzzers#boundliquiditydeltatightly)
  - [getLiquidityDeltaFromAmounts](https://docs.uniswap.org/contracts/v4/reference/core/test/Fuzzers#getliquiditydeltafromamounts)
  - [boundTicks](https://docs.uniswap.org/contracts/v4/reference/core/test/Fuzzers#boundticks)
  - [boundTicks](https://docs.uniswap.org/contracts/v4/reference/core/test/Fuzzers#boundticks-1)
  - [createRandomSqrtPriceX96](https://docs.uniswap.org/contracts/v4/reference/core/test/Fuzzers#createrandomsqrtpricex96)
  - [createFuzzyLiquidityParams](https://docs.uniswap.org/contracts/v4/reference/core/test/Fuzzers#createfuzzyliquidityparams)
  - [createFuzzyLiquidityParamsWithTightBound](https://docs.uniswap.org/contracts/v4/reference/core/test/Fuzzers#createfuzzyliquidityparamswithtightbound)
  - [createFuzzyLiquidity](https://docs.uniswap.org/contracts/v4/reference/core/test/Fuzzers#createfuzzyliquidity)
  - [createFuzzyLiquidityWithTightBound](https://docs.uniswap.org/contracts/v4/reference/core/test/Fuzzers#createfuzzyliquiditywithtightbound)