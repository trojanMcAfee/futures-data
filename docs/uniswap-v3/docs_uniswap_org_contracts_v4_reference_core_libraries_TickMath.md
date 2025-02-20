[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TickMath#)

On this page

# TickMath

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/libraries/TickMath.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

Computes sqrt price for ticks of size 1.0001, i.e. sqrt(1.0001^tick) as fixed point Q64.96 numbers. Supports
prices between 2 **-128 and 2** 128

## State Variables [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TickMath\#state-variables "Direct link to heading")

### MIN\_TICK [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TickMath\#min_tick "Direct link to heading")

_The minimum tick that may be passed to #getSqrtPriceAtTick computed from log base 1.0001 of 2\*\*-128_

_If ever MIN\_TICK and MAX\_TICK are not centered around 0, the absTick logic in getSqrtPriceAtTick cannot be used_

```codeBlockLines_mRuA
int24 internal constant MIN_TICK = -887272;

```

Copy

### MAX\_TICK [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TickMath\#max_tick "Direct link to heading")

_The maximum tick that may be passed to #getSqrtPriceAtTick computed from log base 1.0001 of 2\*\*128_

_If ever MIN\_TICK and MAX\_TICK are not centered around 0, the absTick logic in getSqrtPriceAtTick cannot be used_

```codeBlockLines_mRuA
int24 internal constant MAX_TICK = 887272;

```

Copy

### MIN\_TICK\_SPACING [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TickMath\#min_tick_spacing "Direct link to heading")

_The minimum tick spacing value drawn from the range of type int16 that is greater than 0, i.e. min from the range \[1, 32767\]_

```codeBlockLines_mRuA
int24 internal constant MIN_TICK_SPACING = 1;

```

Copy

### MAX\_TICK\_SPACING [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TickMath\#max_tick_spacing "Direct link to heading")

_The maximum tick spacing value drawn from the range of type int16, i.e. max from the range \[1, 32767\]_

```codeBlockLines_mRuA
int24 internal constant MAX_TICK_SPACING = type(int16).max;

```

Copy

### MIN\_SQRT\_PRICE [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TickMath\#min_sqrt_price "Direct link to heading")

_The minimum value that can be returned from #getSqrtPriceAtTick. Equivalent to getSqrtPriceAtTick(MIN\_TICK)_

```codeBlockLines_mRuA
uint160 internal constant MIN_SQRT_PRICE = 4295128739;

```

Copy

### MAX\_SQRT\_PRICE [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TickMath\#max_sqrt_price "Direct link to heading")

_The maximum value that can be returned from #getSqrtPriceAtTick. Equivalent to getSqrtPriceAtTick(MAX\_TICK)_

```codeBlockLines_mRuA
uint160 internal constant MAX_SQRT_PRICE = 1461446703485210103287273052203988822378723970342;

```

Copy

### MAX\_SQRT\_PRICE\_MINUS\_MIN\_SQRT\_PRICE\_MINUS\_ONE [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TickMath\#max_sqrt_price_minus_min_sqrt_price_minus_one "Direct link to heading")

_A threshold used for optimized bounds check, equals `MAX_SQRT_PRICE - MIN_SQRT_PRICE - 1`_

```codeBlockLines_mRuA
uint160 internal constant MAX_SQRT_PRICE_MINUS_MIN_SQRT_PRICE_MINUS_ONE =
    1461446703485210103287273052203988822378723970342 - 4295128739 - 1;

```

Copy

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TickMath\#functions "Direct link to heading")

### maxUsableTick [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TickMath\#maxusabletick "Direct link to heading")

Given a tickSpacing, compute the maximum usable tick

```codeBlockLines_mRuA
function maxUsableTick(int24 tickSpacing) internal pure returns (int24);

```

Copy

### minUsableTick [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TickMath\#minusabletick "Direct link to heading")

Given a tickSpacing, compute the minimum usable tick

```codeBlockLines_mRuA
function minUsableTick(int24 tickSpacing) internal pure returns (int24);

```

Copy

### getSqrtPriceAtTick [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TickMath\#getsqrtpriceattick "Direct link to heading")

Calculates sqrt(1.0001^tick) \* 2^96

_Throws if \|tick\| > max tick_

```codeBlockLines_mRuA
function getSqrtPriceAtTick(int24 tick) internal pure returns (uint160 sqrtPriceX96);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `tick` | `int24` | The input tick for the above formula |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `sqrtPriceX96` | `uint160` | A Fixed point Q64.96 number representing the sqrt of the price of the two assets (currency1/currency0) at the given tick |

### getTickAtSqrtPrice [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TickMath\#gettickatsqrtprice "Direct link to heading")

Calculates the greatest tick value such that getSqrtPriceAtTick(tick) <= sqrtPriceX96

_Throws in case sqrtPriceX96 < MIN\_SQRT\_PRICE, as MIN\_SQRT\_PRICE is the lowest value getSqrtPriceAtTick may_
_ever return._

```codeBlockLines_mRuA
function getTickAtSqrtPrice(uint160 sqrtPriceX96) internal pure returns (int24 tick);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `sqrtPriceX96` | `uint160` | The sqrt price for which to compute the tick as a Q64.96 |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `tick` | `int24` | The greatest tick for which the getSqrtPriceAtTick(tick) is less than or equal to the input sqrtPriceX96 |

## Errors [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TickMath\#errors "Direct link to heading")

### InvalidTick [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TickMath\#invalidtick "Direct link to heading")

Thrown when the tick passed to #getSqrtPriceAtTick is not between MIN\_TICK and MAX\_TICK

```codeBlockLines_mRuA
error InvalidTick(int24 tick);

```

Copy

### InvalidSqrtPrice [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TickMath\#invalidsqrtprice "Direct link to heading")

Thrown when the price passed to #getTickAtSqrtPrice does not correspond to a price between MIN\_TICK and MAX\_TICK

```codeBlockLines_mRuA
error InvalidSqrtPrice(uint160 sqrtPriceX96);

```

Copy

- [State Variables](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TickMath#state-variables)
  - [MIN\_TICK](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TickMath#min_tick)
  - [MAX\_TICK](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TickMath#max_tick)
  - [MIN\_TICK\_SPACING](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TickMath#min_tick_spacing)
  - [MAX\_TICK\_SPACING](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TickMath#max_tick_spacing)
  - [MIN\_SQRT\_PRICE](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TickMath#min_sqrt_price)
  - [MAX\_SQRT\_PRICE](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TickMath#max_sqrt_price)
  - [MAX\_SQRT\_PRICE\_MINUS\_MIN\_SQRT\_PRICE\_MINUS\_ONE](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TickMath#max_sqrt_price_minus_min_sqrt_price_minus_one)
- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TickMath#functions)
  - [maxUsableTick](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TickMath#maxusabletick)
  - [minUsableTick](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TickMath#minusabletick)
  - [getSqrtPriceAtTick](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TickMath#getsqrtpriceattick)
  - [getTickAtSqrtPrice](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TickMath#gettickatsqrtprice)
- [Errors](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TickMath#errors)
  - [InvalidTick](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TickMath#invalidtick)
  - [InvalidSqrtPrice](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TickMath#invalidsqrtprice)