[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/test/TickOverflowSafetyEchidnaTest#)

On this page

# TickOverflowSafetyEchidnaTest

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/test/TickOverflowSafetyEchidnaTest.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

## State Variables [​](https://docs.uniswap.org/contracts/v4/reference/core/test/TickOverflowSafetyEchidnaTest\#state-variables "Direct link to heading")

### MIN\_TICK [​](https://docs.uniswap.org/contracts/v4/reference/core/test/TickOverflowSafetyEchidnaTest\#min_tick "Direct link to heading")

```codeBlockLines_mRuA
int24 private constant MIN_TICK = -16;

```

Copy

### MAX\_TICK [​](https://docs.uniswap.org/contracts/v4/reference/core/test/TickOverflowSafetyEchidnaTest\#max_tick "Direct link to heading")

```codeBlockLines_mRuA
int24 private constant MAX_TICK = 16;

```

Copy

### pool [​](https://docs.uniswap.org/contracts/v4/reference/core/test/TickOverflowSafetyEchidnaTest\#pool "Direct link to heading")

```codeBlockLines_mRuA
Pool.State private pool;

```

Copy

### tick [​](https://docs.uniswap.org/contracts/v4/reference/core/test/TickOverflowSafetyEchidnaTest\#tick "Direct link to heading")

```codeBlockLines_mRuA
int24 private tick = 0;

```

Copy

### feeGrowthGlobal0X128 [​](https://docs.uniswap.org/contracts/v4/reference/core/test/TickOverflowSafetyEchidnaTest\#feegrowthglobal0x128 "Direct link to heading")

```codeBlockLines_mRuA
uint256 feeGrowthGlobal0X128 = type(uint256).max / 2;

```

Copy

### feeGrowthGlobal1X128 [​](https://docs.uniswap.org/contracts/v4/reference/core/test/TickOverflowSafetyEchidnaTest\#feegrowthglobal1x128 "Direct link to heading")

```codeBlockLines_mRuA
uint256 feeGrowthGlobal1X128 = type(uint256).max / 2;

```

Copy

### totalLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/core/test/TickOverflowSafetyEchidnaTest\#totalliquidity "Direct link to heading")

```codeBlockLines_mRuA
int256 totalLiquidity = 0;

```

Copy

### totalGrowth0 [​](https://docs.uniswap.org/contracts/v4/reference/core/test/TickOverflowSafetyEchidnaTest\#totalgrowth0 "Direct link to heading")

```codeBlockLines_mRuA
uint256 private totalGrowth0 = 0;

```

Copy

### totalGrowth1 [​](https://docs.uniswap.org/contracts/v4/reference/core/test/TickOverflowSafetyEchidnaTest\#totalgrowth1 "Direct link to heading")

```codeBlockLines_mRuA
uint256 private totalGrowth1 = 0;

```

Copy

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/test/TickOverflowSafetyEchidnaTest\#functions "Direct link to heading")

### increaseFeeGrowthGlobal0X128 [​](https://docs.uniswap.org/contracts/v4/reference/core/test/TickOverflowSafetyEchidnaTest\#increasefeegrowthglobal0x128 "Direct link to heading")

```codeBlockLines_mRuA
function increaseFeeGrowthGlobal0X128(uint256 amount) external;

```

Copy

### increaseFeeGrowthGlobal1X128 [​](https://docs.uniswap.org/contracts/v4/reference/core/test/TickOverflowSafetyEchidnaTest\#increasefeegrowthglobal1x128 "Direct link to heading")

```codeBlockLines_mRuA
function increaseFeeGrowthGlobal1X128(uint256 amount) external;

```

Copy

### setPosition [​](https://docs.uniswap.org/contracts/v4/reference/core/test/TickOverflowSafetyEchidnaTest\#setposition "Direct link to heading")

```codeBlockLines_mRuA
function setPosition(int24 tickLower, int24 tickUpper, int128 liquidityDelta) external;

```

Copy

### moveToTick [​](https://docs.uniswap.org/contracts/v4/reference/core/test/TickOverflowSafetyEchidnaTest\#movetotick "Direct link to heading")

```codeBlockLines_mRuA
function moveToTick(int24 target) external;

```

Copy

- [State Variables](https://docs.uniswap.org/contracts/v4/reference/core/test/TickOverflowSafetyEchidnaTest#state-variables)
  - [MIN\_TICK](https://docs.uniswap.org/contracts/v4/reference/core/test/TickOverflowSafetyEchidnaTest#min_tick)
  - [MAX\_TICK](https://docs.uniswap.org/contracts/v4/reference/core/test/TickOverflowSafetyEchidnaTest#max_tick)
  - [pool](https://docs.uniswap.org/contracts/v4/reference/core/test/TickOverflowSafetyEchidnaTest#pool)
  - [tick](https://docs.uniswap.org/contracts/v4/reference/core/test/TickOverflowSafetyEchidnaTest#tick)
  - [feeGrowthGlobal0X128](https://docs.uniswap.org/contracts/v4/reference/core/test/TickOverflowSafetyEchidnaTest#feegrowthglobal0x128)
  - [feeGrowthGlobal1X128](https://docs.uniswap.org/contracts/v4/reference/core/test/TickOverflowSafetyEchidnaTest#feegrowthglobal1x128)
  - [totalLiquidity](https://docs.uniswap.org/contracts/v4/reference/core/test/TickOverflowSafetyEchidnaTest#totalliquidity)
  - [totalGrowth0](https://docs.uniswap.org/contracts/v4/reference/core/test/TickOverflowSafetyEchidnaTest#totalgrowth0)
  - [totalGrowth1](https://docs.uniswap.org/contracts/v4/reference/core/test/TickOverflowSafetyEchidnaTest#totalgrowth1)
- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/test/TickOverflowSafetyEchidnaTest#functions)
  - [increaseFeeGrowthGlobal0X128](https://docs.uniswap.org/contracts/v4/reference/core/test/TickOverflowSafetyEchidnaTest#increasefeegrowthglobal0x128)
  - [increaseFeeGrowthGlobal1X128](https://docs.uniswap.org/contracts/v4/reference/core/test/TickOverflowSafetyEchidnaTest#increasefeegrowthglobal1x128)
  - [setPosition](https://docs.uniswap.org/contracts/v4/reference/core/test/TickOverflowSafetyEchidnaTest#setposition)
  - [moveToTick](https://docs.uniswap.org/contracts/v4/reference/core/test/TickOverflowSafetyEchidnaTest#movetotick)