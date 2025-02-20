[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/libraries/SqrtPriceMath#)

On this page

# SqrtPriceMath

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/libraries/SqrtPriceMath.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

Contains the math that uses square root of price as a Q64.96 and liquidity to compute deltas

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/SqrtPriceMath\#functions "Direct link to heading")

### getNextSqrtPriceFromAmount0RoundingUp [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/SqrtPriceMath\#getnextsqrtpricefromamount0roundingup "Direct link to heading")

Gets the next sqrt price given a delta of currency0

_Always rounds up, because in the exact output case (increasing price) we need to move the price at least_
_far enough to get the desired output amount, and in the exact input case (decreasing price) we need to move the_
_price less in order to not send too much output._
_The most precise formula for this is liquidity_ sqrtPX96 / (liquidity +- amount _sqrtPX96),_
_if this is impossible because of overflow, we calculate liquidity / (liquidity / sqrtPX96 +- amount)._

```codeBlockLines_mRuA
function getNextSqrtPriceFromAmount0RoundingUp(uint160 sqrtPX96, uint128 liquidity, uint256 amount, bool add)
    internal
    pure
    returns (uint160);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `sqrtPX96` | `uint160` | The starting price, i.e. before accounting for the currency0 delta |
| `liquidity` | `uint128` | The amount of usable liquidity |
| `amount` | `uint256` | How much of currency0 to add or remove from virtual reserves |
| `add` | `bool` | Whether to add or remove the amount of currency0 |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `uint160` | The price after adding or removing amount, depending on add |

### getNextSqrtPriceFromAmount1RoundingDown [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/SqrtPriceMath\#getnextsqrtpricefromamount1roundingdown "Direct link to heading")

Gets the next sqrt price given a delta of currency1

_Always rounds down, because in the exact output case (decreasing price) we need to move the price at least_
_far enough to get the desired output amount, and in the exact input case (increasing price) we need to move the_
_price less in order to not send too much output._
_The formula we compute is within <1 wei of the lossless version: sqrtPX96 +- amount / liquidity_

```codeBlockLines_mRuA
function getNextSqrtPriceFromAmount1RoundingDown(uint160 sqrtPX96, uint128 liquidity, uint256 amount, bool add)
    internal
    pure
    returns (uint160);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `sqrtPX96` | `uint160` | The starting price, i.e., before accounting for the currency1 delta |
| `liquidity` | `uint128` | The amount of usable liquidity |
| `amount` | `uint256` | How much of currency1 to add, or remove, from virtual reserves |
| `add` | `bool` | Whether to add, or remove, the amount of currency1 |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `uint160` | The price after adding or removing `amount` |

### getNextSqrtPriceFromInput [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/SqrtPriceMath\#getnextsqrtpricefrominput "Direct link to heading")

Gets the next sqrt price given an input amount of currency0 or currency1

_Throws if price or liquidity are 0, or if the next price is out of bounds_

```codeBlockLines_mRuA
function getNextSqrtPriceFromInput(uint160 sqrtPX96, uint128 liquidity, uint256 amountIn, bool zeroForOne)
    internal
    pure
    returns (uint160);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `sqrtPX96` | `uint160` | The starting price, i.e., before accounting for the input amount |
| `liquidity` | `uint128` | The amount of usable liquidity |
| `amountIn` | `uint256` | How much of currency0, or currency1, is being swapped in |
| `zeroForOne` | `bool` | Whether the amount in is currency0 or currency1 |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `uint160` | uint160 The price after adding the input amount to currency0 or currency1 |

### getNextSqrtPriceFromOutput [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/SqrtPriceMath\#getnextsqrtpricefromoutput "Direct link to heading")

Gets the next sqrt price given an output amount of currency0 or currency1

_Throws if price or liquidity are 0 or the next price is out of bounds_

```codeBlockLines_mRuA
function getNextSqrtPriceFromOutput(uint160 sqrtPX96, uint128 liquidity, uint256 amountOut, bool zeroForOne)
    internal
    pure
    returns (uint160);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `sqrtPX96` | `uint160` | The starting price before accounting for the output amount |
| `liquidity` | `uint128` | The amount of usable liquidity |
| `amountOut` | `uint256` | How much of currency0, or currency1, is being swapped out |
| `zeroForOne` | `bool` | Whether the amount out is currency1 or currency0 |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `uint160` | uint160 The price after removing the output amount of currency0 or currency1 |

### getAmount0Delta [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/SqrtPriceMath\#getamount0delta "Direct link to heading")

Gets the amount0 delta between two prices

_Calculates liquidity / sqrt(lower) - liquidity / sqrt(upper),_
_i.e. liquidity_ (sqrt(upper) - sqrt(lower)) / (sqrt(upper) _sqrt(lower))_

```codeBlockLines_mRuA
function getAmount0Delta(uint160 sqrtPriceAX96, uint160 sqrtPriceBX96, uint128 liquidity, bool roundUp)
    internal
    pure
    returns (uint256);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `sqrtPriceAX96` | `uint160` | A sqrt price |
| `sqrtPriceBX96` | `uint160` | Another sqrt price |
| `liquidity` | `uint128` | The amount of usable liquidity |
| `roundUp` | `bool` | Whether to round the amount up or down |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `uint256` | uint256 Amount of currency0 required to cover a position of size liquidity between the two passed prices |

### absDiff [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/SqrtPriceMath\#absdiff "Direct link to heading")

Equivalent to: `a >= b ? a - b : b - a`

```codeBlockLines_mRuA
function absDiff(uint160 a, uint160 b) internal pure returns (uint256 res);

```

Copy

### getAmount1Delta [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/SqrtPriceMath\#getamount1delta "Direct link to heading")

Gets the amount1 delta between two prices

_Calculates liquidity_ (sqrt(upper) - sqrt(lower))\*

```codeBlockLines_mRuA
function getAmount1Delta(uint160 sqrtPriceAX96, uint160 sqrtPriceBX96, uint128 liquidity, bool roundUp)
    internal
    pure
    returns (uint256 amount1);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `sqrtPriceAX96` | `uint160` | A sqrt price |
| `sqrtPriceBX96` | `uint160` | Another sqrt price |
| `liquidity` | `uint128` | The amount of usable liquidity |
| `roundUp` | `bool` | Whether to round the amount up, or down |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `amount1` | `uint256` | Amount of currency1 required to cover a position of size liquidity between the two passed prices |

### getAmount0Delta [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/SqrtPriceMath\#getamount0delta-1 "Direct link to heading")

Equivalent to:
amount1 = roundUp
? FullMath.mulDivRoundingUp(liquidity, sqrtPriceBX96 - sqrtPriceAX96, FixedPoint96.Q96)
: FullMath.mulDiv(liquidity, sqrtPriceBX96 - sqrtPriceAX96, FixedPoint96.Q96);
Cannot overflow because `type(uint128).max * type(uint160).max >> 96 < (1 << 192)`.

Helper that gets signed currency0 delta

```codeBlockLines_mRuA
function getAmount0Delta(uint160 sqrtPriceAX96, uint160 sqrtPriceBX96, int128 liquidity)
    internal
    pure
    returns (int256);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `sqrtPriceAX96` | `uint160` | A sqrt price |
| `sqrtPriceBX96` | `uint160` | Another sqrt price |
| `liquidity` | `int128` | The change in liquidity for which to compute the amount0 delta |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `int256` | int256 Amount of currency0 corresponding to the passed liquidityDelta between the two prices |

### getAmount1Delta [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/SqrtPriceMath\#getamount1delta-1 "Direct link to heading")

Helper that gets signed currency1 delta

```codeBlockLines_mRuA
function getAmount1Delta(uint160 sqrtPriceAX96, uint160 sqrtPriceBX96, int128 liquidity)
    internal
    pure
    returns (int256);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `sqrtPriceAX96` | `uint160` | A sqrt price |
| `sqrtPriceBX96` | `uint160` | Another sqrt price |
| `liquidity` | `int128` | The change in liquidity for which to compute the amount1 delta |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `int256` | int256 Amount of currency1 corresponding to the passed liquidityDelta between the two prices |

## Errors [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/SqrtPriceMath\#errors "Direct link to heading")

### InvalidPriceOrLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/SqrtPriceMath\#invalidpriceorliquidity "Direct link to heading")

```codeBlockLines_mRuA
error InvalidPriceOrLiquidity();

```

Copy

### InvalidPrice [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/SqrtPriceMath\#invalidprice "Direct link to heading")

```codeBlockLines_mRuA
error InvalidPrice();

```

Copy

### NotEnoughLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/SqrtPriceMath\#notenoughliquidity "Direct link to heading")

```codeBlockLines_mRuA
error NotEnoughLiquidity();

```

Copy

### PriceOverflow [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/SqrtPriceMath\#priceoverflow "Direct link to heading")

```codeBlockLines_mRuA
error PriceOverflow();

```

Copy

- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/libraries/SqrtPriceMath#functions)
  - [getNextSqrtPriceFromAmount0RoundingUp](https://docs.uniswap.org/contracts/v4/reference/core/libraries/SqrtPriceMath#getnextsqrtpricefromamount0roundingup)
  - [getNextSqrtPriceFromAmount1RoundingDown](https://docs.uniswap.org/contracts/v4/reference/core/libraries/SqrtPriceMath#getnextsqrtpricefromamount1roundingdown)
  - [getNextSqrtPriceFromInput](https://docs.uniswap.org/contracts/v4/reference/core/libraries/SqrtPriceMath#getnextsqrtpricefrominput)
  - [getNextSqrtPriceFromOutput](https://docs.uniswap.org/contracts/v4/reference/core/libraries/SqrtPriceMath#getnextsqrtpricefromoutput)
  - [getAmount0Delta](https://docs.uniswap.org/contracts/v4/reference/core/libraries/SqrtPriceMath#getamount0delta)
  - [absDiff](https://docs.uniswap.org/contracts/v4/reference/core/libraries/SqrtPriceMath#absdiff)
  - [getAmount1Delta](https://docs.uniswap.org/contracts/v4/reference/core/libraries/SqrtPriceMath#getamount1delta)
  - [getAmount0Delta](https://docs.uniswap.org/contracts/v4/reference/core/libraries/SqrtPriceMath#getamount0delta-1)
  - [getAmount1Delta](https://docs.uniswap.org/contracts/v4/reference/core/libraries/SqrtPriceMath#getamount1delta-1)
- [Errors](https://docs.uniswap.org/contracts/v4/reference/core/libraries/SqrtPriceMath#errors)
  - [InvalidPriceOrLiquidity](https://docs.uniswap.org/contracts/v4/reference/core/libraries/SqrtPriceMath#invalidpriceorliquidity)
  - [InvalidPrice](https://docs.uniswap.org/contracts/v4/reference/core/libraries/SqrtPriceMath#invalidprice)
  - [NotEnoughLiquidity](https://docs.uniswap.org/contracts/v4/reference/core/libraries/SqrtPriceMath#notenoughliquidity)
  - [PriceOverflow](https://docs.uniswap.org/contracts/v4/reference/core/libraries/SqrtPriceMath#priceoverflow)