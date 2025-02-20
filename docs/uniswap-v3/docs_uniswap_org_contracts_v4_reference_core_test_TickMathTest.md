[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/test/TickMathTest#)

On this page

# TickMathTest

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/test/TickMathTest.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/test/TickMathTest\#functions "Direct link to heading")

### getSqrtPriceAtTick [​](https://docs.uniswap.org/contracts/v4/reference/core/test/TickMathTest\#getsqrtpriceattick "Direct link to heading")

```codeBlockLines_mRuA
function getSqrtPriceAtTick(int24 tick) external pure returns (uint160);

```

Copy

### getGasCostOfGetSqrtPriceAtTick [​](https://docs.uniswap.org/contracts/v4/reference/core/test/TickMathTest\#getgascostofgetsqrtpriceattick "Direct link to heading")

```codeBlockLines_mRuA
function getGasCostOfGetSqrtPriceAtTick(int24 tick) external view returns (uint256);

```

Copy

### getTickAtSqrtPrice [​](https://docs.uniswap.org/contracts/v4/reference/core/test/TickMathTest\#gettickatsqrtprice "Direct link to heading")

```codeBlockLines_mRuA
function getTickAtSqrtPrice(uint160 sqrtPriceX96) external pure returns (int24);

```

Copy

### getGasCostOfGetTickAtSqrtPrice [​](https://docs.uniswap.org/contracts/v4/reference/core/test/TickMathTest\#getgascostofgettickatsqrtprice "Direct link to heading")

```codeBlockLines_mRuA
function getGasCostOfGetTickAtSqrtPrice(uint160 sqrtPriceX96) external view returns (uint256);

```

Copy

### MIN\_SQRT\_PRICE [​](https://docs.uniswap.org/contracts/v4/reference/core/test/TickMathTest\#min_sqrt_price "Direct link to heading")

```codeBlockLines_mRuA
function MIN_SQRT_PRICE() external pure returns (uint160);

```

Copy

### MAX\_SQRT\_PRICE [​](https://docs.uniswap.org/contracts/v4/reference/core/test/TickMathTest\#max_sqrt_price "Direct link to heading")

```codeBlockLines_mRuA
function MAX_SQRT_PRICE() external pure returns (uint160);

```

Copy

### MIN\_TICK [​](https://docs.uniswap.org/contracts/v4/reference/core/test/TickMathTest\#min_tick "Direct link to heading")

```codeBlockLines_mRuA
function MIN_TICK() external pure returns (int24);

```

Copy

### MAX\_TICK [​](https://docs.uniswap.org/contracts/v4/reference/core/test/TickMathTest\#max_tick "Direct link to heading")

```codeBlockLines_mRuA
function MAX_TICK() external pure returns (int24);

```

Copy

- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/test/TickMathTest#functions)
  - [getSqrtPriceAtTick](https://docs.uniswap.org/contracts/v4/reference/core/test/TickMathTest#getsqrtpriceattick)
  - [getGasCostOfGetSqrtPriceAtTick](https://docs.uniswap.org/contracts/v4/reference/core/test/TickMathTest#getgascostofgetsqrtpriceattick)
  - [getTickAtSqrtPrice](https://docs.uniswap.org/contracts/v4/reference/core/test/TickMathTest#gettickatsqrtprice)
  - [getGasCostOfGetTickAtSqrtPrice](https://docs.uniswap.org/contracts/v4/reference/core/test/TickMathTest#getgascostofgettickatsqrtprice)
  - [MIN\_SQRT\_PRICE](https://docs.uniswap.org/contracts/v4/reference/core/test/TickMathTest#min_sqrt_price)
  - [MAX\_SQRT\_PRICE](https://docs.uniswap.org/contracts/v4/reference/core/test/TickMathTest#max_sqrt_price)
  - [MIN\_TICK](https://docs.uniswap.org/contracts/v4/reference/core/test/TickMathTest#min_tick)
  - [MAX\_TICK](https://docs.uniswap.org/contracts/v4/reference/core/test/TickMathTest#max_tick)