[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseHook#)

On this page

# BaseHook

[Git Source](https://github.com/uniswap/v4-periphery/blob/3f295d8435e4f776ea2daeb96ce1bc6d63f33fc7/src/base/hooks/BaseHook.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:**
IHooks, [SafeCallback](https://docs.uniswap.org/contracts/v4/reference/periphery/base/SafeCallback)

abstract contract for hook implementations

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseHook\#functions "Direct link to heading")

### constructor [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseHook\#constructor "Direct link to heading")

```codeBlockLines_mRuA
constructor(IPoolManager _manager) SafeCallback(_manager);

```

Copy

### selfOnly [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseHook\#selfonly "Direct link to heading")

_Only this address may call this function_

```codeBlockLines_mRuA
modifier selfOnly();

```

Copy

### onlyValidPools [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseHook\#onlyvalidpools "Direct link to heading")

_Only pools with hooks set to this contract may call this function_

```codeBlockLines_mRuA
modifier onlyValidPools(IHooks hooks);

```

Copy

### getHookPermissions [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseHook\#gethookpermissions "Direct link to heading")

Returns a struct of permissions to signal which hook functions are to be implemented

_Used at deployment to validate the address correctly represents the expected permissions_

```codeBlockLines_mRuA
function getHookPermissions() public pure virtual returns (Hooks.Permissions memory);

```

Copy

### validateHookAddress [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseHook\#validatehookaddress "Direct link to heading")

Validates the deployed hook address agrees with the expected permissions of the hook

_this function is virtual so that we can override it during testing,_
_which allows us to deploy an implementation to any address_
_and then etch the bytecode into the correct address_

```codeBlockLines_mRuA
function validateHookAddress(BaseHook _this) internal pure virtual;

```

Copy

### \_unlockCallback [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseHook\#_unlockcallback "Direct link to heading")

```codeBlockLines_mRuA
function _unlockCallback(bytes calldata data) internal virtual override returns (bytes memory);

```

Copy

### beforeInitialize [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseHook\#beforeinitialize "Direct link to heading")

The hook called before the state of a pool is initialized

```codeBlockLines_mRuA
function beforeInitialize(address, PoolKey calldata, uint160) external virtual returns (bytes4);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `address` |  |
| `<none>` | `PoolKey` |  |
| `<none>` | `uint160` |  |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `bytes4` | bytes4 The function selector for the hook |

### afterInitialize [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseHook\#afterinitialize "Direct link to heading")

The hook called after the state of a pool is initialized

```codeBlockLines_mRuA
function afterInitialize(address, PoolKey calldata, uint160, int24) external virtual returns (bytes4);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `address` |  |
| `<none>` | `PoolKey` |  |
| `<none>` | `uint160` |  |
| `<none>` | `int24` |  |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `bytes4` | bytes4 The function selector for the hook |

### beforeAddLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseHook\#beforeaddliquidity "Direct link to heading")

The hook called before liquidity is added

```codeBlockLines_mRuA
function beforeAddLiquidity(address, PoolKey calldata, IPoolManager.ModifyLiquidityParams calldata, bytes calldata)
    external
    virtual
    returns (bytes4);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `address` |  |
| `<none>` | `PoolKey` |  |
| `<none>` | `IPoolManager.ModifyLiquidityParams` |  |
| `<none>` | `bytes` |  |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `bytes4` | bytes4 The function selector for the hook |

### beforeRemoveLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseHook\#beforeremoveliquidity "Direct link to heading")

The hook called before liquidity is removed

```codeBlockLines_mRuA
function beforeRemoveLiquidity(address, PoolKey calldata, IPoolManager.ModifyLiquidityParams calldata, bytes calldata)
    external
    virtual
    returns (bytes4);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `address` |  |
| `<none>` | `PoolKey` |  |
| `<none>` | `IPoolManager.ModifyLiquidityParams` |  |
| `<none>` | `bytes` |  |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `bytes4` | bytes4 The function selector for the hook |

### afterAddLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseHook\#afteraddliquidity "Direct link to heading")

The hook called after liquidity is added

```codeBlockLines_mRuA
function afterAddLiquidity(
    address,
    PoolKey calldata,
    IPoolManager.ModifyLiquidityParams calldata,
    BalanceDelta,
    BalanceDelta,
    bytes calldata
) external virtual returns (bytes4, BalanceDelta);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `address` |  |
| `<none>` | `PoolKey` |  |
| `<none>` | `IPoolManager.ModifyLiquidityParams` |  |
| `<none>` | `BalanceDelta` |  |
| `<none>` | `BalanceDelta` |  |
| `<none>` | `bytes` |  |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `bytes4` | bytes4 The function selector for the hook |
| `<none>` | `BalanceDelta` | BalanceDelta The hook's delta in token0 and token1. Positive: the hook is owed/took currency, negative: the hook owes/sent currency |

### afterRemoveLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseHook\#afterremoveliquidity "Direct link to heading")

The hook called after liquidity is removed

```codeBlockLines_mRuA
function afterRemoveLiquidity(
    address,
    PoolKey calldata,
    IPoolManager.ModifyLiquidityParams calldata,
    BalanceDelta,
    BalanceDelta,
    bytes calldata
) external virtual returns (bytes4, BalanceDelta);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `address` |  |
| `<none>` | `PoolKey` |  |
| `<none>` | `IPoolManager.ModifyLiquidityParams` |  |
| `<none>` | `BalanceDelta` |  |
| `<none>` | `BalanceDelta` |  |
| `<none>` | `bytes` |  |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `bytes4` | bytes4 The function selector for the hook |
| `<none>` | `BalanceDelta` | BalanceDelta The hook's delta in token0 and token1. Positive: the hook is owed/took currency, negative: the hook owes/sent currency |

### beforeSwap [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseHook\#beforeswap "Direct link to heading")

The hook called before a swap

```codeBlockLines_mRuA
function beforeSwap(address, PoolKey calldata, IPoolManager.SwapParams calldata, bytes calldata)
    external
    virtual
    returns (bytes4, BeforeSwapDelta, uint24);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `address` |  |
| `<none>` | `PoolKey` |  |
| `<none>` | `IPoolManager.SwapParams` |  |
| `<none>` | `bytes` |  |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `bytes4` | bytes4 The function selector for the hook |
| `<none>` | `BeforeSwapDelta` | BeforeSwapDelta The hook's delta in specified and unspecified currencies. Positive: the hook is owed/took currency, negative: the hook owes/sent currency |
| `<none>` | `uint24` | uint24 Optionally override the lp fee, only used if three conditions are met: 1. the Pool has a dynamic fee, 2. the value's 2nd highest bit is set (23rd bit, 0x400000), and 3. the value is less than or equal to the maximum fee (1 million) |

### afterSwap [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseHook\#afterswap "Direct link to heading")

The hook called after a swap

```codeBlockLines_mRuA
function afterSwap(address, PoolKey calldata, IPoolManager.SwapParams calldata, BalanceDelta, bytes calldata)
    external
    virtual
    returns (bytes4, int128);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `address` |  |
| `<none>` | `PoolKey` |  |
| `<none>` | `IPoolManager.SwapParams` |  |
| `<none>` | `BalanceDelta` |  |
| `<none>` | `bytes` |  |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `bytes4` | bytes4 The function selector for the hook |
| `<none>` | `int128` | int128 The hook's delta in unspecified currency. Positive: the hook is owed/took currency, negative: the hook owes/sent currency |

### beforeDonate [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseHook\#beforedonate "Direct link to heading")

The hook called before donate

```codeBlockLines_mRuA
function beforeDonate(address, PoolKey calldata, uint256, uint256, bytes calldata) external virtual returns (bytes4);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `address` |  |
| `<none>` | `PoolKey` |  |
| `<none>` | `uint256` |  |
| `<none>` | `uint256` |  |
| `<none>` | `bytes` |  |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `bytes4` | bytes4 The function selector for the hook |

### afterDonate [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseHook\#afterdonate "Direct link to heading")

The hook called after donate

```codeBlockLines_mRuA
function afterDonate(address, PoolKey calldata, uint256, uint256, bytes calldata) external virtual returns (bytes4);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `address` |  |
| `<none>` | `PoolKey` |  |
| `<none>` | `uint256` |  |
| `<none>` | `uint256` |  |
| `<none>` | `bytes` |  |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `bytes4` | bytes4 The function selector for the hook |

## Errors [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseHook\#errors "Direct link to heading")

### NotSelf [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseHook\#notself "Direct link to heading")

```codeBlockLines_mRuA
error NotSelf();

```

Copy

### InvalidPool [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseHook\#invalidpool "Direct link to heading")

```codeBlockLines_mRuA
error InvalidPool();

```

Copy

### LockFailure [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseHook\#lockfailure "Direct link to heading")

```codeBlockLines_mRuA
error LockFailure();

```

Copy

### HookNotImplemented [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseHook\#hooknotimplemented "Direct link to heading")

```codeBlockLines_mRuA
error HookNotImplemented();

```

Copy

- [Functions](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseHook#functions)
  - [constructor](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseHook#constructor)
  - [selfOnly](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseHook#selfonly)
  - [onlyValidPools](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseHook#onlyvalidpools)
  - [getHookPermissions](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseHook#gethookpermissions)
  - [validateHookAddress](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseHook#validatehookaddress)
  - [\_unlockCallback](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseHook#_unlockcallback)
  - [beforeInitialize](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseHook#beforeinitialize)
  - [afterInitialize](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseHook#afterinitialize)
  - [beforeAddLiquidity](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseHook#beforeaddliquidity)
  - [beforeRemoveLiquidity](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseHook#beforeremoveliquidity)
  - [afterAddLiquidity](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseHook#afteraddliquidity)
  - [afterRemoveLiquidity](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseHook#afterremoveliquidity)
  - [beforeSwap](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseHook#beforeswap)
  - [afterSwap](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseHook#afterswap)
  - [beforeDonate](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseHook#beforedonate)
  - [afterDonate](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseHook#afterdonate)
- [Errors](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseHook#errors)
  - [NotSelf](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseHook#notself)
  - [InvalidPool](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseHook#invalidpool)
  - [LockFailure](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseHook#lockfailure)
  - [HookNotImplemented](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseHook#hooknotimplemented)