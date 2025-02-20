[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/periphery/lens/StateView#)

On this page

# StateView

[Git Source](https://github.com/uniswap/v4-periphery/blob/3f295d8435e4f776ea2daeb96ce1bc6d63f33fc7/src/lens/StateView.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:** [ImmutableState](https://docs.uniswap.org/contracts/v4/reference/periphery/base/ImmutableState)

A view only contract wrapping the StateLibrary.sol library for reading storage in v4-core.

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/periphery/lens/StateView\#functions "Direct link to heading")

### constructor [​](https://docs.uniswap.org/contracts/v4/reference/periphery/lens/StateView\#constructor "Direct link to heading")

```codeBlockLines_mRuA
constructor(IPoolManager _poolManager) ImmutableState(_poolManager);

```

Copy

### getSlot0 [​](https://docs.uniswap.org/contracts/v4/reference/periphery/lens/StateView\#getslot0 "Direct link to heading")

Get Slot0 of the pool: sqrtPriceX96, tick, protocolFee, lpFee

_Corresponds to pools\[poolId\].slot0_

```codeBlockLines_mRuA
function getSlot0(PoolId poolId)
    external
    view
    returns (uint160 sqrtPriceX96, int24 tick, uint24 protocolFee, uint24 lpFee);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `poolId` | `PoolId` | The ID of the pool. |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `sqrtPriceX96` | `uint160` | The square root of the price of the pool, in Q96 precision. |
| `tick` | `int24` | The current tick of the pool. |
| `protocolFee` | `uint24` | The protocol fee of the pool. |
| `lpFee` | `uint24` | The swap fee of the pool. |

### getTickInfo [​](https://docs.uniswap.org/contracts/v4/reference/periphery/lens/StateView\#gettickinfo "Direct link to heading")

Retrieves the tick information of a pool at a specific tick.

_Corresponds to pools\[poolId\].ticks\[tick\]_

```codeBlockLines_mRuA
function getTickInfo(PoolId poolId, int24 tick)
    external
    view
    returns (uint128 liquidityGross, int128 liquidityNet, uint256 feeGrowthOutside0X128, uint256 feeGrowthOutside1X128);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `poolId` | `PoolId` | The ID of the pool. |
| `tick` | `int24` | The tick to retrieve information for. |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `liquidityGross` | `uint128` | The total position liquidity that references this tick |
| `liquidityNet` | `int128` | The amount of net liquidity added (subtracted) when tick is crossed from left to right (right to left) |
| `feeGrowthOutside0X128` | `uint256` | fee growth per unit of liquidity on the _other_ side of this tick (relative to the current tick) |
| `feeGrowthOutside1X128` | `uint256` | fee growth per unit of liquidity on the _other_ side of this tick (relative to the current tick) |

### getTickLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/periphery/lens/StateView\#gettickliquidity "Direct link to heading")

Retrieves the liquidity information of a pool at a specific tick.

_Corresponds to pools\[poolId\].ticks\[tick\].liquidityGross and pools\[poolId\].ticks\[tick\].liquidityNet. A more gas efficient version of getTickInfo_

```codeBlockLines_mRuA
function getTickLiquidity(PoolId poolId, int24 tick)
    external
    view
    returns (uint128 liquidityGross, int128 liquidityNet);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `poolId` | `PoolId` | The ID of the pool. |
| `tick` | `int24` | The tick to retrieve liquidity for. |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `liquidityGross` | `uint128` | The total position liquidity that references this tick |
| `liquidityNet` | `int128` | The amount of net liquidity added (subtracted) when tick is crossed from left to right (right to left) |

### getTickFeeGrowthOutside [​](https://docs.uniswap.org/contracts/v4/reference/periphery/lens/StateView\#gettickfeegrowthoutside "Direct link to heading")

Retrieves the fee growth outside a tick range of a pool

_Corresponds to pools\[poolId\].ticks\[tick\].feeGrowthOutside0X128 and pools\[poolId\].ticks\[tick\].feeGrowthOutside1X128. A more gas efficient version of getTickInfo_

```codeBlockLines_mRuA
function getTickFeeGrowthOutside(PoolId poolId, int24 tick)
    external
    view
    returns (uint256 feeGrowthOutside0X128, uint256 feeGrowthOutside1X128);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `poolId` | `PoolId` | The ID of the pool. |
| `tick` | `int24` | The tick to retrieve fee growth for. |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `feeGrowthOutside0X128` | `uint256` | fee growth per unit of liquidity on the _other_ side of this tick (relative to the current tick) |
| `feeGrowthOutside1X128` | `uint256` | fee growth per unit of liquidity on the _other_ side of this tick (relative to the current tick) |

### getFeeGrowthGlobals [​](https://docs.uniswap.org/contracts/v4/reference/periphery/lens/StateView\#getfeegrowthglobals "Direct link to heading")

Retrieves the global fee growth of a pool.

_Corresponds to pools\[poolId\].feeGrowthGlobal0X128 and pools\[poolId\].feeGrowthGlobal1X128_

```codeBlockLines_mRuA
function getFeeGrowthGlobals(PoolId poolId)
    external
    view
    returns (uint256 feeGrowthGlobal0, uint256 feeGrowthGlobal1);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `poolId` | `PoolId` | The ID of the pool. |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `feeGrowthGlobal0` | `uint256` | The global fee growth for token0. |
| `feeGrowthGlobal1` | `uint256` | The global fee growth for token1. |

### getLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/periphery/lens/StateView\#getliquidity "Direct link to heading")

Retrieves the total liquidity of a pool.

_Corresponds to pools\[poolId\].liquidity_

```codeBlockLines_mRuA
function getLiquidity(PoolId poolId) external view returns (uint128 liquidity);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `poolId` | `PoolId` | The ID of the pool. |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `liquidity` | `uint128` | The liquidity of the pool. |

### getTickBitmap [​](https://docs.uniswap.org/contracts/v4/reference/periphery/lens/StateView\#gettickbitmap "Direct link to heading")

Retrieves the tick bitmap of a pool at a specific tick.

_Corresponds to pools\[poolId\].tickBitmap\[tick\]_

```codeBlockLines_mRuA
function getTickBitmap(PoolId poolId, int16 tick) external view returns (uint256 tickBitmap);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `poolId` | `PoolId` | The ID of the pool. |
| `tick` | `int16` | The tick to retrieve the bitmap for. |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `tickBitmap` | `uint256` | The bitmap of the tick. |

### getPositionInfo [​](https://docs.uniswap.org/contracts/v4/reference/periphery/lens/StateView\#getpositioninfo "Direct link to heading")

Retrieves the position info without needing to calculate the `positionId`.

_Corresponds to pools\[poolId\].positions\[positionId\]_

```codeBlockLines_mRuA
function getPositionInfo(PoolId poolId, address owner, int24 tickLower, int24 tickUpper, bytes32 salt)
    external
    view
    returns (uint128 liquidity, uint256 feeGrowthInside0LastX128, uint256 feeGrowthInside1LastX128);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
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

### getPositionInfo [​](https://docs.uniswap.org/contracts/v4/reference/periphery/lens/StateView\#getpositioninfo-1 "Direct link to heading")

Retrieves the position information of a pool at a specific position ID.

_Corresponds to pools\[poolId\].positions\[positionId\]_

```codeBlockLines_mRuA
function getPositionInfo(PoolId poolId, bytes32 positionId)
    external
    view
    returns (uint128 liquidity, uint256 feeGrowthInside0LastX128, uint256 feeGrowthInside1LastX128);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `poolId` | `PoolId` | The ID of the pool. |
| `positionId` | `bytes32` | The ID of the position. |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `liquidity` | `uint128` | The liquidity of the position. |
| `feeGrowthInside0LastX128` | `uint256` | The fee growth inside the position for token0. |
| `feeGrowthInside1LastX128` | `uint256` | The fee growth inside the position for token1. |

### getPositionLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/periphery/lens/StateView\#getpositionliquidity "Direct link to heading")

Retrieves the liquidity of a position.

_Corresponds to pools\[poolId\].positions\[positionId\].liquidity. More gas efficient for just retrieving liquidity as compared to getPositionInfo_

```codeBlockLines_mRuA
function getPositionLiquidity(PoolId poolId, bytes32 positionId) external view returns (uint128 liquidity);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `poolId` | `PoolId` | The ID of the pool. |
| `positionId` | `bytes32` | The ID of the position. |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `liquidity` | `uint128` | The liquidity of the position. |

### getFeeGrowthInside [​](https://docs.uniswap.org/contracts/v4/reference/periphery/lens/StateView\#getfeegrowthinside "Direct link to heading")

Calculate the fee growth inside a tick range of a pool

_pools\[poolId\].feeGrowthInside0LastX128 in Position.Info is cached and can become stale. This function will calculate the up to date feeGrowthInside_

```codeBlockLines_mRuA
function getFeeGrowthInside(PoolId poolId, int24 tickLower, int24 tickUpper)
    external
    view
    returns (uint256 feeGrowthInside0X128, uint256 feeGrowthInside1X128);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `poolId` | `PoolId` | The ID of the pool. |
| `tickLower` | `int24` | The lower tick of the range. |
| `tickUpper` | `int24` | The upper tick of the range. |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `feeGrowthInside0X128` | `uint256` | The fee growth inside the tick range for token0. |
| `feeGrowthInside1X128` | `uint256` | The fee growth inside the tick range for token1. |

- [Functions](https://docs.uniswap.org/contracts/v4/reference/periphery/lens/StateView#functions)
  - [constructor](https://docs.uniswap.org/contracts/v4/reference/periphery/lens/StateView#constructor)
  - [getSlot0](https://docs.uniswap.org/contracts/v4/reference/periphery/lens/StateView#getslot0)
  - [getTickInfo](https://docs.uniswap.org/contracts/v4/reference/periphery/lens/StateView#gettickinfo)
  - [getTickLiquidity](https://docs.uniswap.org/contracts/v4/reference/periphery/lens/StateView#gettickliquidity)
  - [getTickFeeGrowthOutside](https://docs.uniswap.org/contracts/v4/reference/periphery/lens/StateView#gettickfeegrowthoutside)
  - [getFeeGrowthGlobals](https://docs.uniswap.org/contracts/v4/reference/periphery/lens/StateView#getfeegrowthglobals)
  - [getLiquidity](https://docs.uniswap.org/contracts/v4/reference/periphery/lens/StateView#getliquidity)
  - [getTickBitmap](https://docs.uniswap.org/contracts/v4/reference/periphery/lens/StateView#gettickbitmap)
  - [getPositionInfo](https://docs.uniswap.org/contracts/v4/reference/periphery/lens/StateView#getpositioninfo)
  - [getPositionInfo](https://docs.uniswap.org/contracts/v4/reference/periphery/lens/StateView#getpositioninfo-1)
  - [getPositionLiquidity](https://docs.uniswap.org/contracts/v4/reference/periphery/lens/StateView#getpositionliquidity)
  - [getFeeGrowthInside](https://docs.uniswap.org/contracts/v4/reference/periphery/lens/StateView#getfeegrowthinside)