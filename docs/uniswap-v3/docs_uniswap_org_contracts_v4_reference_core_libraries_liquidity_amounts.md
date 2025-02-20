[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/libraries/liquidity-amounts#)

On this page

The `LiquidityAmounts` library provides functions for computing liquidity amounts from token amounts and prices in Uniswap V4.

# Key Concept: sqrtPriceX96

`sqrtPriceX96` represents the square root of the price ratio of token1 to token0, multiplied by 2^96. This representation allows for precise price calculations across a wide range of values while using fixed-point arithmetic. It's more efficient than using ticks for intermediate calculations, as it avoids frequent conversions between prices and ticks.

# Functions

## getLiquidityForAmount0 [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/liquidity-amounts\#getliquidityforamount0 "Direct link to heading")

```codeBlockLines_mRuA
function getLiquidityForAmount0(uint160 sqrtPriceAX96, uint160 sqrtPriceBX96, uint256 amount0)
internal
pure
returns (uint128 liquidity)

```

Copy

Computes the amount of liquidity received for a given amount of token0 and price range.

| Param Name | Type | Description |
| --- | --- | --- |
| sqrtPriceAX96 | uint160 | Square root of price at first tick boundary |
| sqrtPriceBX96 | uint160 | Square root of price at second tick boundary |
| amount0 | uint256 | The amount of token0 being sent in |

Returns the amount of liquidity received.

## getLiquidityForAmount1 [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/liquidity-amounts\#getliquidityforamount1 "Direct link to heading")

```codeBlockLines_mRuA
function getLiquidityForAmount1(uint160 sqrtPriceAX96, uint160 sqrtPriceBX96, uint256 amount1)
internal
pure
returns (uint128 liquidity)

```

Copy

Computes the amount of liquidity received for a given amount of token1 and price range.

| Param Name | Type | Description |
| --- | --- | --- |
| sqrtPriceAX96 | uint160 | Square root of price at first tick boundary |
| sqrtPriceBX96 | uint160 | Square root of price at second tick boundary |
| amount1 | uint256 | The amount of token1 being sent in |

Returns the amount of liquidity received.

## getLiquidityForAmounts [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/liquidity-amounts\#getliquidityforamounts "Direct link to heading")

```codeBlockLines_mRuA
function getLiquidityForAmounts(
uint160 sqrtPriceX96,
uint160 sqrtPriceAX96,
uint160 sqrtPriceBX96,
uint256 amount0,
uint256 amount1
) internal pure returns (uint128 liquidity)

```

Copy

Computes the maximum amount of liquidity received for given amounts of token0 and token1, the current pool prices, and the prices at the tick boundaries.

| Param Name | Type | Description |
| --- | --- | --- |
| sqrtPriceX96 | uint160 | Current square root price of the pool |
| sqrtPriceAX96 | uint160 | Square root of price at first tick boundary |
| sqrtPriceBX96 | uint160 | Square root of price at second tick boundary |
| amount0 | uint256 | The amount of token0 being sent in |
| amount1 | uint256 | The amount of token1 being sent in |

Returns the maximum amount of liquidity received.

## getAmount0ForLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/liquidity-amounts\#getamount0forliquidity "Direct link to heading")

```codeBlockLines_mRuA
function getAmount0ForLiquidity(uint160 sqrtPriceAX96, uint160 sqrtPriceBX96, uint128 liquidity)
internal
pure
returns (uint256 amount0)

```

Copy

Computes the amount of token0 for a given amount of liquidity and a price range.

| Param Name | Type | Description |
| --- | --- | --- |
| sqrtPriceAX96 | uint160 | Square root of price at first tick boundary |
| sqrtPriceBX96 | uint160 | Square root of price at second tick boundary |
| liquidity | uint128 | The liquidity being valued |

Returns the amount of token0.

## getAmount1ForLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/liquidity-amounts\#getamount1forliquidity "Direct link to heading")

```codeBlockLines_mRuA
function getAmount1ForLiquidity(uint160 sqrtPriceAX96, uint160 sqrtPriceBX96, uint128 liquidity)
internal
pure
returns (uint256 amount1)

```

Copy

Computes the amount of token1 for a given amount of liquidity and a price range.

| Param Name | Type | Description |
| --- | --- | --- |
| sqrtPriceAX96 | uint160 | Square root of price at first tick boundary |
| sqrtPriceBX96 | uint160 | Square root of price at second tick boundary |
| liquidity | uint128 | The liquidity being valued |

Returns the amount of token1.

## getAmountsForLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/liquidity-amounts\#getamountsforliquidity "Direct link to heading")

```codeBlockLines_mRuA
function getAmountsForLiquidity(
uint160 sqrtPriceX96,
uint160 sqrtPriceAX96,
uint160 sqrtPriceBX96,
uint128 liquidity
) internal pure returns (uint256 amount0, uint256 amount1)

```

Copy

Computes the token0 and token1 value for a given amount of liquidity, the current pool prices, and the prices at the tick boundaries.

| Param Name | Type | Description |
| --- | --- | --- |
| sqrtPriceX96 | uint160 | Current square root price of the pool |
| sqrtPriceAX96 | uint160 | Square root of price at first tick boundary |
| sqrtPriceBX96 | uint160 | Square root of price at second tick boundary |
| liquidity | uint128 | The liquidity being valued |

Returns the amount of token0 and token1.

- [getLiquidityForAmount0](https://docs.uniswap.org/contracts/v4/reference/core/libraries/liquidity-amounts#getliquidityforamount0)
- [getLiquidityForAmount1](https://docs.uniswap.org/contracts/v4/reference/core/libraries/liquidity-amounts#getliquidityforamount1)
- [getLiquidityForAmounts](https://docs.uniswap.org/contracts/v4/reference/core/libraries/liquidity-amounts#getliquidityforamounts)
- [getAmount0ForLiquidity](https://docs.uniswap.org/contracts/v4/reference/core/libraries/liquidity-amounts#getamount0forliquidity)
- [getAmount1ForLiquidity](https://docs.uniswap.org/contracts/v4/reference/core/libraries/liquidity-amounts#getamount1forliquidity)
- [getAmountsForLiquidity](https://docs.uniswap.org/contracts/v4/reference/core/libraries/liquidity-amounts#getamountsforliquidity)