[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/libraries/StateLibrary#)

On this page

# StateLibrary

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/libraries/StateLibrary.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

A helper library to provide state getters that use extsload

## State Variables [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/StateLibrary\#state-variables "Direct link to heading")

### POOLS\_SLOT [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/StateLibrary\#pools_slot "Direct link to heading")

index of pools mapping in the PoolManager

```codeBlockLines_mRuA
bytes32 public constant POOLS_SLOT = bytes32(uint256(6));

```

Copy

### FEE\_GROWTH\_GLOBAL0\_OFFSET [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/StateLibrary\#fee_growth_global0_offset "Direct link to heading")

index of feeGrowthGlobal0X128 in Pool.State

```codeBlockLines_mRuA
uint256 public constant FEE_GROWTH_GLOBAL0_OFFSET = 1;

```

Copy

### LIQUIDITY\_OFFSET [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/StateLibrary\#liquidity_offset "Direct link to heading")

index of liquidity in Pool.State

```codeBlockLines_mRuA
uint256 public constant LIQUIDITY_OFFSET = 3;

```

Copy

### TICKS\_OFFSET [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/StateLibrary\#ticks_offset "Direct link to heading")

index of TicksInfo mapping in Pool.State: mapping(int24 => TickInfo) ticks;

```codeBlockLines_mRuA
uint256 public constant TICKS_OFFSET = 4;

```

Copy

### TICK\_BITMAP\_OFFSET [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/StateLibrary\#tick_bitmap_offset "Direct link to heading")

index of tickBitmap mapping in Pool.State

```codeBlockLines_mRuA
uint256 public constant TICK_BITMAP_OFFSET = 5;

```

Copy

### POSITIONS\_OFFSET [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/StateLibrary\#positions_offset "Direct link to heading")

index of Position.State mapping in Pool.State: mapping(bytes32 => Position.State) positions;

```codeBlockLines_mRuA
uint256 public constant POSITIONS_OFFSET = 6;

```

Copy

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/StateLibrary\#functions "Direct link to heading")

### getSlot0 [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/StateLibrary\#getslot0 "Direct link to heading")

Get Slot0 of the pool: sqrtPriceX96, tick, protocolFee, lpFee

_Corresponds to pools\[poolId\].slot0_

```codeBlockLines_mRuA
function getSlot0(IPoolManager manager, PoolId poolId)
    internal
    view
    returns (uint160 sqrtPriceX96, int24 tick, uint24 protocolFee, uint24 lpFee);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `manager` | `IPoolManager` | The pool manager contract. |
| `poolId` | `PoolId` | The ID of the pool. |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `sqrtPriceX96` | `uint160` | The square root of the price of the pool, in Q96 precision. |
| `tick` | `int24` | The current tick of the pool. |
| `protocolFee` | `uint24` | The protocol fee of the pool. |
| `lpFee` | `uint24` | The swap fee of the pool. |

### getTickInfo [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/StateLibrary\#gettickinfo "Direct link to heading")

Retrieves the tick information of a pool at a specific tick.

_Corresponds to pools\[poolId\].ticks\[tick\]_

```codeBlockLines_mRuA
function getTickInfo(IPoolManager manager, PoolId poolId, int24 tick)
    internal
    view
    returns (uint128 liquidityGross, int128 liquidityNet, uint256 feeGrowthOutside0X128, uint256 feeGrowthOutside1X128);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `manager` | `IPoolManager` | The pool manager contract. |
| `poolId` | `PoolId` | The ID of the pool. |
| `tick` | `int24` | The tick to retrieve information for. |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `liquidityGross` | `uint128` | The total position liquidity that references this tick |
| `liquidityNet` | `int128` | The amount of net liquidity added (subtracted) when tick is crossed from left to right (right to left) |
| `feeGrowthOutside0X128` | `uint256` | fee growth per unit of liquidity on the _other_ side of this tick (relative to the current tick) |
| `feeGrowthOutside1X128` | `uint256` | fee growth per unit of liquidity on the _other_ side of this tick (relative to the current tick) |

### getTickLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/StateLibrary\#gettickliquidity "Direct link to heading")

Retrieves the liquidity information of a pool at a specific tick.

_Corresponds to pools\[poolId\].ticks\[tick\].liquidityGross and pools\[poolId\].ticks\[tick\].liquidityNet. A more gas efficient version of getTickInfo_

```codeBlockLines_mRuA
function getTickLiquidity(IPoolManager manager, PoolId poolId, int24 tick)
    internal
    view
    returns (uint128 liquidityGross, int128 liquidityNet);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `manager` | `IPoolManager` | The pool manager contract. |
| `poolId` | `PoolId` | The ID of the pool. |
| `tick` | `int24` | The tick to retrieve liquidity for. |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `liquidityGross` | `uint128` | The total position liquidity that references this tick |
| `liquidityNet` | `int128` | The amount of net liquidity added (subtracted) when tick is crossed from left to right (right to left) |

### getTickFeeGrowthOutside [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/StateLibrary\#gettickfeegrowthoutside "Direct link to heading")

Retrieves the fee growth outside a tick range of a pool

_Corresponds to pools\[poolId\].ticks\[tick\].feeGrowthOutside0X128 and pools\[poolId\].ticks\[tick\].feeGrowthOutside1X128. A more gas efficient version of getTickInfo_

```codeBlockLines_mRuA
function getTickFeeGrowthOutside(IPoolManager manager, PoolId poolId, int24 tick)
    internal
    view
    returns (uint256 feeGrowthOutside0X128, uint256 feeGrowthOutside1X128);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `manager` | `IPoolManager` | The pool manager contract. |
| `poolId` | `PoolId` | The ID of the pool. |
| `tick` | `int24` | The tick to retrieve fee growth for. |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `feeGrowthOutside0X128` | `uint256` | fee growth per unit of liquidity on the _other_ side of this tick (relative to the current tick) |
| `feeGrowthOutside1X128` | `uint256` | fee growth per unit of liquidity on the _other_ side of this tick (relative to the current tick) |

### getFeeGrowthGlobals [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/StateLibrary\#getfeegrowthglobals "Direct link to heading")

Retrieves the global fee growth of a pool.

_Corresponds to pools\[poolId\].feeGrowthGlobal0X128 and pools\[poolId\].feeGrowthGlobal1X128_

```codeBlockLines_mRuA
function getFeeGrowthGlobals(IPoolManager manager, PoolId poolId)
    internal
    view
    returns (uint256 feeGrowthGlobal0, uint256 feeGrowthGlobal1);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `manager` | `IPoolManager` | The pool manager contract. |
| `poolId` | `PoolId` | The ID of the pool. |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `feeGrowthGlobal0` | `uint256` | The global fee growth for token0. |
| `feeGrowthGlobal1` | `uint256` | The global fee growth for token1. |

### getLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/StateLibrary\#getliquidity "Direct link to heading")

Retrieves total the liquidity of a pool.

_Corresponds to pools\[poolId\].liquidity_

```codeBlockLines_mRuA
function getLiquidity(IPoolManager manager, PoolId poolId) internal view returns (uint128 liquidity);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `manager` | `IPoolManager` | The pool manager contract. |
| `poolId` | `PoolId` | The ID of the pool. |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `liquidity` | `uint128` | The liquidity of the pool. |

### getTickBitmap [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/StateLibrary\#gettickbitmap "Direct link to heading")

Retrieves the tick bitmap of a pool at a specific tick.

_Corresponds to pools\[poolId\].tickBitmap\[tick\]_

```codeBlockLines_mRuA
function getTickBitmap(IPoolManager manager, PoolId poolId, int16 tick) internal view returns (uint256 tickBitmap);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `manager` | `IPoolManager` | The pool manager contract. |
| `poolId` | `PoolId` | The ID of the pool. |
| `tick` | `int16` | The tick to retrieve the bitmap for. |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `tickBitmap` | `uint256` | The bitmap of the tick. |

### getPositionInfo [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/StateLibrary\#getpositioninfo "Direct link to heading")

Retrieves the position information of a pool without needing to calculate the `positionId`.

_Corresponds to pools\[poolId\].positions\[positionId\]_

```codeBlockLines_mRuA
function getPositionInfo(
    IPoolManager manager,
    PoolId poolId,
    address owner,
    int24 tickLower,
    int24 tickUpper,
    bytes32 salt
) internal view returns (uint128 liquidity, uint256 feeGrowthInside0LastX128, uint256 feeGrowthInside1LastX128);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `manager` | `IPoolManager` |  |
| `poolId` | `PoolId` | The ID of the pool. |
| `owner` | `address` | The owner of the liquidity position. |
| `tickLower` | `int24` | The lower tick of the liquidity range. |
| `tickUpper` | `int24` | The upper tick of the liquidity range. |
| `salt` | `bytes32` | The bytes32 randomness to further distinguish position state. |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `liquidity` | `uint128` | The liquidity of the position. |
| `feeGrowthInside0LastX128` | `uint256` | The fee growth inside the position for token0. |
| `feeGrowthInside1LastX128` | `uint256` | The fee growth inside the position for token1. |

### getPositionInfo [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/StateLibrary\#getpositioninfo-1 "Direct link to heading")

Retrieves the position information of a pool at a specific position ID.

_Corresponds to pools\[poolId\].positions\[positionId\]_

```codeBlockLines_mRuA
function getPositionInfo(IPoolManager manager, PoolId poolId, bytes32 positionId)
    internal
    view
    returns (uint128 liquidity, uint256 feeGrowthInside0LastX128, uint256 feeGrowthInside1LastX128);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `manager` | `IPoolManager` | The pool manager contract. |
| `poolId` | `PoolId` | The ID of the pool. |
| `positionId` | `bytes32` | The ID of the position. |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `liquidity` | `uint128` | The liquidity of the position. |
| `feeGrowthInside0LastX128` | `uint256` | The fee growth inside the position for token0. |
| `feeGrowthInside1LastX128` | `uint256` | The fee growth inside the position for token1. |

### getPositionLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/StateLibrary\#getpositionliquidity "Direct link to heading")

Retrieves the liquidity of a position.

_Corresponds to pools\[poolId\].positions\[positionId\].liquidity. More gas efficient for just retrieiving liquidity as compared to getPositionInfo_

```codeBlockLines_mRuA
function getPositionLiquidity(IPoolManager manager, PoolId poolId, bytes32 positionId)
    internal
    view
    returns (uint128 liquidity);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `manager` | `IPoolManager` | The pool manager contract. |
| `poolId` | `PoolId` | The ID of the pool. |
| `positionId` | `bytes32` | The ID of the position. |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `liquidity` | `uint128` | The liquidity of the position. |

### getFeeGrowthInside [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/StateLibrary\#getfeegrowthinside "Direct link to heading")

Calculate the fee growth inside a tick range of a pool

_pools\[poolId\].feeGrowthInside0LastX128 in Position.State is cached and can become stale. This function will calculate the up to date feeGrowthInside_

```codeBlockLines_mRuA
function getFeeGrowthInside(IPoolManager manager, PoolId poolId, int24 tickLower, int24 tickUpper)
    internal
    view
    returns (uint256 feeGrowthInside0X128, uint256 feeGrowthInside1X128);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `manager` | `IPoolManager` | The pool manager contract. |
| `poolId` | `PoolId` | The ID of the pool. |
| `tickLower` | `int24` | The lower tick of the range. |
| `tickUpper` | `int24` | The upper tick of the range. |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `feeGrowthInside0X128` | `uint256` | The fee growth inside the tick range for token0. |
| `feeGrowthInside1X128` | `uint256` | The fee growth inside the tick range for token1. |

### \_getPoolStateSlot [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/StateLibrary\#_getpoolstateslot "Direct link to heading")

```codeBlockLines_mRuA
function _getPoolStateSlot(PoolId poolId) internal pure returns (bytes32);

```

Copy

### \_getTickInfoSlot [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/StateLibrary\#_gettickinfoslot "Direct link to heading")

```codeBlockLines_mRuA
function _getTickInfoSlot(PoolId poolId, int24 tick) internal pure returns (bytes32);

```

Copy

### \_getPositionInfoSlot [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/StateLibrary\#_getpositioninfoslot "Direct link to heading")

```codeBlockLines_mRuA
function _getPositionInfoSlot(PoolId poolId, bytes32 positionId) internal pure returns (bytes32);

```

Copy

- [State Variables](https://docs.uniswap.org/contracts/v4/reference/core/libraries/StateLibrary#state-variables)
  - [POOLS\_SLOT](https://docs.uniswap.org/contracts/v4/reference/core/libraries/StateLibrary#pools_slot)
  - [FEE\_GROWTH\_GLOBAL0\_OFFSET](https://docs.uniswap.org/contracts/v4/reference/core/libraries/StateLibrary#fee_growth_global0_offset)
  - [LIQUIDITY\_OFFSET](https://docs.uniswap.org/contracts/v4/reference/core/libraries/StateLibrary#liquidity_offset)
  - [TICKS\_OFFSET](https://docs.uniswap.org/contracts/v4/reference/core/libraries/StateLibrary#ticks_offset)
  - [TICK\_BITMAP\_OFFSET](https://docs.uniswap.org/contracts/v4/reference/core/libraries/StateLibrary#tick_bitmap_offset)
  - [POSITIONS\_OFFSET](https://docs.uniswap.org/contracts/v4/reference/core/libraries/StateLibrary#positions_offset)
- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/libraries/StateLibrary#functions)
  - [getSlot0](https://docs.uniswap.org/contracts/v4/reference/core/libraries/StateLibrary#getslot0)
  - [getTickInfo](https://docs.uniswap.org/contracts/v4/reference/core/libraries/StateLibrary#gettickinfo)
  - [getTickLiquidity](https://docs.uniswap.org/contracts/v4/reference/core/libraries/StateLibrary#gettickliquidity)
  - [getTickFeeGrowthOutside](https://docs.uniswap.org/contracts/v4/reference/core/libraries/StateLibrary#gettickfeegrowthoutside)
  - [getFeeGrowthGlobals](https://docs.uniswap.org/contracts/v4/reference/core/libraries/StateLibrary#getfeegrowthglobals)
  - [getLiquidity](https://docs.uniswap.org/contracts/v4/reference/core/libraries/StateLibrary#getliquidity)
  - [getTickBitmap](https://docs.uniswap.org/contracts/v4/reference/core/libraries/StateLibrary#gettickbitmap)
  - [getPositionInfo](https://docs.uniswap.org/contracts/v4/reference/core/libraries/StateLibrary#getpositioninfo)
  - [getPositionInfo](https://docs.uniswap.org/contracts/v4/reference/core/libraries/StateLibrary#getpositioninfo-1)
  - [getPositionLiquidity](https://docs.uniswap.org/contracts/v4/reference/core/libraries/StateLibrary#getpositionliquidity)
  - [getFeeGrowthInside](https://docs.uniswap.org/contracts/v4/reference/core/libraries/StateLibrary#getfeegrowthinside)
  - [\_getPoolStateSlot](https://docs.uniswap.org/contracts/v4/reference/core/libraries/StateLibrary#_getpoolstateslot)
  - [\_getTickInfoSlot](https://docs.uniswap.org/contracts/v4/reference/core/libraries/StateLibrary#_gettickinfoslot)
  - [\_getPositionInfoSlot](https://docs.uniswap.org/contracts/v4/reference/core/libraries/StateLibrary#_getpositioninfoslot)