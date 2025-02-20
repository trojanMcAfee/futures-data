[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IHooks#)

On this page

# IHooks

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/interfaces/IHooks.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

V4 decides whether to invoke specific hooks by inspecting the least significant bits
of the address that the hooks contract is deployed to.
For example, a hooks contract deployed to address: 0x0000000000000000000000000000000000002400
has the lowest bits '10 0100 0000 0000' which would cause the 'before initialize' and 'after add liquidity' hooks to be used.
See the Hooks library for the full spec.

_Should only be callable by the v4 PoolManager._

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IHooks\#functions "Direct link to heading")

### beforeInitialize [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IHooks\#beforeinitialize "Direct link to heading")

The hook called before the state of a pool is initialized

```codeBlockLines_mRuA
function beforeInitialize(address sender, PoolKey calldata key, uint160 sqrtPriceX96) external returns (bytes4);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `sender` | `address` | The initial msg.sender for the initialize call |
| `key` | `PoolKey` | The key for the pool being initialized |
| `sqrtPriceX96` | `uint160` | The sqrt(price) of the pool as a Q64.96 |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `bytes4` | bytes4 The function selector for the hook |

### afterInitialize [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IHooks\#afterinitialize "Direct link to heading")

The hook called after the state of a pool is initialized

```codeBlockLines_mRuA
function afterInitialize(address sender, PoolKey calldata key, uint160 sqrtPriceX96, int24 tick)
    external
    returns (bytes4);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `sender` | `address` | The initial msg.sender for the initialize call |
| `key` | `PoolKey` | The key for the pool being initialized |
| `sqrtPriceX96` | `uint160` | The sqrt(price) of the pool as a Q64.96 |
| `tick` | `int24` | The current tick after the state of a pool is initialized |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `bytes4` | bytes4 The function selector for the hook |

### beforeAddLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IHooks\#beforeaddliquidity "Direct link to heading")

The hook called before liquidity is added

```codeBlockLines_mRuA
function beforeAddLiquidity(
    address sender,
    PoolKey calldata key,
    IPoolManager.ModifyLiquidityParams calldata params,
    bytes calldata hookData
) external returns (bytes4);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `sender` | `address` | The initial msg.sender for the add liquidity call |
| `key` | `PoolKey` | The key for the pool |
| `params` | `IPoolManager.ModifyLiquidityParams` | The parameters for adding liquidity |
| `hookData` | `bytes` | Arbitrary data handed into the PoolManager by the liquidity provider to be passed on to the hook |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `bytes4` | bytes4 The function selector for the hook |

### afterAddLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IHooks\#afteraddliquidity "Direct link to heading")

The hook called after liquidity is added

```codeBlockLines_mRuA
function afterAddLiquidity(
    address sender,
    PoolKey calldata key,
    IPoolManager.ModifyLiquidityParams calldata params,
    BalanceDelta delta,
    BalanceDelta feesAccrued,
    bytes calldata hookData
) external returns (bytes4, BalanceDelta);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `sender` | `address` | The initial msg.sender for the add liquidity call |
| `key` | `PoolKey` | The key for the pool |
| `params` | `IPoolManager.ModifyLiquidityParams` | The parameters for adding liquidity |
| `delta` | `BalanceDelta` | The caller's balance delta after adding liquidity; the sum of principal delta, fees accrued, and hook delta |
| `feesAccrued` | `BalanceDelta` | The fees accrued since the last time fees were collected from this position |
| `hookData` | `bytes` | Arbitrary data handed into the PoolManager by the liquidity provider to be passed on to the hook |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `bytes4` | bytes4 The function selector for the hook |
| `<none>` | `BalanceDelta` | BalanceDelta The hook's delta in token0 and token1. Positive: the hook is owed/took currency, negative: the hook owes/sent currency |

### beforeRemoveLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IHooks\#beforeremoveliquidity "Direct link to heading")

The hook called before liquidity is removed

```codeBlockLines_mRuA
function beforeRemoveLiquidity(
    address sender,
    PoolKey calldata key,
    IPoolManager.ModifyLiquidityParams calldata params,
    bytes calldata hookData
) external returns (bytes4);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `sender` | `address` | The initial msg.sender for the remove liquidity call |
| `key` | `PoolKey` | The key for the pool |
| `params` | `IPoolManager.ModifyLiquidityParams` | The parameters for removing liquidity |
| `hookData` | `bytes` | Arbitrary data handed into the PoolManager by the liquidity provider to be be passed on to the hook |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `bytes4` | bytes4 The function selector for the hook |

### afterRemoveLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IHooks\#afterremoveliquidity "Direct link to heading")

The hook called after liquidity is removed

```codeBlockLines_mRuA
function afterRemoveLiquidity(
    address sender,
    PoolKey calldata key,
    IPoolManager.ModifyLiquidityParams calldata params,
    BalanceDelta delta,
    BalanceDelta feesAccrued,
    bytes calldata hookData
) external returns (bytes4, BalanceDelta);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `sender` | `address` | The initial msg.sender for the remove liquidity call |
| `key` | `PoolKey` | The key for the pool |
| `params` | `IPoolManager.ModifyLiquidityParams` | The parameters for removing liquidity |
| `delta` | `BalanceDelta` | The caller's balance delta after removing liquidity; the sum of principal delta, fees accrued, and hook delta |
| `feesAccrued` | `BalanceDelta` | The fees accrued since the last time fees were collected from this position |
| `hookData` | `bytes` | Arbitrary data handed into the PoolManager by the liquidity provider to be be passed on to the hook |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `bytes4` | bytes4 The function selector for the hook |
| `<none>` | `BalanceDelta` | BalanceDelta The hook's delta in token0 and token1. Positive: the hook is owed/took currency, negative: the hook owes/sent currency |

### beforeSwap [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IHooks\#beforeswap "Direct link to heading")

The hook called before a swap

```codeBlockLines_mRuA
function beforeSwap(
    address sender,
    PoolKey calldata key,
    IPoolManager.SwapParams calldata params,
    bytes calldata hookData
) external returns (bytes4, BeforeSwapDelta, uint24);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `sender` | `address` | The initial msg.sender for the swap call |
| `key` | `PoolKey` | The key for the pool |
| `params` | `IPoolManager.SwapParams` | The parameters for the swap |
| `hookData` | `bytes` | Arbitrary data handed into the PoolManager by the swapper to be be passed on to the hook |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `bytes4` | bytes4 The function selector for the hook |
| `<none>` | `BeforeSwapDelta` | BeforeSwapDelta The hook's delta in specified and unspecified currencies. Positive: the hook is owed/took currency, negative: the hook owes/sent currency |
| `<none>` | `uint24` | uint24 Optionally override the lp fee, only used if three conditions are met: 1. the Pool has a dynamic fee, 2. the value's 2nd highest bit is set (23rd bit, 0x400000), and 3. the value is less than or equal to the maximum fee (1 million) |

### afterSwap [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IHooks\#afterswap "Direct link to heading")

The hook called after a swap

```codeBlockLines_mRuA
function afterSwap(
    address sender,
    PoolKey calldata key,
    IPoolManager.SwapParams calldata params,
    BalanceDelta delta,
    bytes calldata hookData
) external returns (bytes4, int128);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `sender` | `address` | The initial msg.sender for the swap call |
| `key` | `PoolKey` | The key for the pool |
| `params` | `IPoolManager.SwapParams` | The parameters for the swap |
| `delta` | `BalanceDelta` | The amount owed to the caller (positive) or owed to the pool (negative) |
| `hookData` | `bytes` | Arbitrary data handed into the PoolManager by the swapper to be be passed on to the hook |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `bytes4` | bytes4 The function selector for the hook |
| `<none>` | `int128` | int128 The hook's delta in unspecified currency. Positive: the hook is owed/took currency, negative: the hook owes/sent currency |

### beforeDonate [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IHooks\#beforedonate "Direct link to heading")

The hook called before donate

```codeBlockLines_mRuA
function beforeDonate(address sender, PoolKey calldata key, uint256 amount0, uint256 amount1, bytes calldata hookData)
    external
    returns (bytes4);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `sender` | `address` | The initial msg.sender for the donate call |
| `key` | `PoolKey` | The key for the pool |
| `amount0` | `uint256` | The amount of token0 being donated |
| `amount1` | `uint256` | The amount of token1 being donated |
| `hookData` | `bytes` | Arbitrary data handed into the PoolManager by the donor to be be passed on to the hook |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `bytes4` | bytes4 The function selector for the hook |

### afterDonate [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IHooks\#afterdonate "Direct link to heading")

The hook called after donate

```codeBlockLines_mRuA
function afterDonate(address sender, PoolKey calldata key, uint256 amount0, uint256 amount1, bytes calldata hookData)
    external
    returns (bytes4);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `sender` | `address` | The initial msg.sender for the donate call |
| `key` | `PoolKey` | The key for the pool |
| `amount0` | `uint256` | The amount of token0 being donated |
| `amount1` | `uint256` | The amount of token1 being donated |
| `hookData` | `bytes` | Arbitrary data handed into the PoolManager by the donor to be be passed on to the hook |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `bytes4` | bytes4 The function selector for the hook |

- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IHooks#functions)
  - [beforeInitialize](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IHooks#beforeinitialize)
  - [afterInitialize](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IHooks#afterinitialize)
  - [beforeAddLiquidity](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IHooks#beforeaddliquidity)
  - [afterAddLiquidity](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IHooks#afteraddliquidity)
  - [beforeRemoveLiquidity](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IHooks#beforeremoveliquidity)
  - [afterRemoveLiquidity](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IHooks#afterremoveliquidity)
  - [beforeSwap](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IHooks#beforeswap)
  - [afterSwap](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IHooks#afterswap)
  - [beforeDonate](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IHooks#beforedonate)
  - [afterDonate](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IHooks#afterdonate)