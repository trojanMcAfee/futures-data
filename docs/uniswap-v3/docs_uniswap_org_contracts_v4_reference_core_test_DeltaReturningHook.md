[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/test/DeltaReturningHook#)

On this page

# DeltaReturningHook

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/test/DeltaReturningHook.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:** [BaseTestHooks](https://docs.uniswap.org/contracts/v4/reference/core/test/BaseTestHooks)

## State Variables [​](https://docs.uniswap.org/contracts/v4/reference/core/test/DeltaReturningHook\#state-variables "Direct link to heading")

### manager [​](https://docs.uniswap.org/contracts/v4/reference/core/test/DeltaReturningHook\#manager "Direct link to heading")

```codeBlockLines_mRuA
IPoolManager immutable manager;

```

Copy

### deltaSpecified [​](https://docs.uniswap.org/contracts/v4/reference/core/test/DeltaReturningHook\#deltaspecified "Direct link to heading")

```codeBlockLines_mRuA
int128 deltaSpecified;

```

Copy

### deltaUnspecifiedBeforeSwap [​](https://docs.uniswap.org/contracts/v4/reference/core/test/DeltaReturningHook\#deltaunspecifiedbeforeswap "Direct link to heading")

```codeBlockLines_mRuA
int128 deltaUnspecifiedBeforeSwap;

```

Copy

### deltaUnspecifiedAfterSwap [​](https://docs.uniswap.org/contracts/v4/reference/core/test/DeltaReturningHook\#deltaunspecifiedafterswap "Direct link to heading")

```codeBlockLines_mRuA
int128 deltaUnspecifiedAfterSwap;

```

Copy

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/test/DeltaReturningHook\#functions "Direct link to heading")

### constructor [​](https://docs.uniswap.org/contracts/v4/reference/core/test/DeltaReturningHook\#constructor "Direct link to heading")

```codeBlockLines_mRuA
constructor(IPoolManager _manager);

```

Copy

### onlyPoolManager [​](https://docs.uniswap.org/contracts/v4/reference/core/test/DeltaReturningHook\#onlypoolmanager "Direct link to heading")

```codeBlockLines_mRuA
modifier onlyPoolManager();

```

Copy

### setDeltaSpecified [​](https://docs.uniswap.org/contracts/v4/reference/core/test/DeltaReturningHook\#setdeltaspecified "Direct link to heading")

```codeBlockLines_mRuA
function setDeltaSpecified(int128 delta) external;

```

Copy

### setDeltaUnspecifiedBeforeSwap [​](https://docs.uniswap.org/contracts/v4/reference/core/test/DeltaReturningHook\#setdeltaunspecifiedbeforeswap "Direct link to heading")

```codeBlockLines_mRuA
function setDeltaUnspecifiedBeforeSwap(int128 delta) external;

```

Copy

### setDeltaUnspecifiedAfterSwap [​](https://docs.uniswap.org/contracts/v4/reference/core/test/DeltaReturningHook\#setdeltaunspecifiedafterswap "Direct link to heading")

```codeBlockLines_mRuA
function setDeltaUnspecifiedAfterSwap(int128 delta) external;

```

Copy

### beforeSwap [​](https://docs.uniswap.org/contracts/v4/reference/core/test/DeltaReturningHook\#beforeswap "Direct link to heading")

```codeBlockLines_mRuA
function beforeSwap(address, PoolKey calldata key, IPoolManager.SwapParams calldata params, bytes calldata)
    external
    override
    onlyPoolManager
    returns (bytes4, BeforeSwapDelta, uint24);

```

Copy

### afterSwap [​](https://docs.uniswap.org/contracts/v4/reference/core/test/DeltaReturningHook\#afterswap "Direct link to heading")

```codeBlockLines_mRuA
function afterSwap(address, PoolKey calldata key, IPoolManager.SwapParams calldata params, BalanceDelta, bytes calldata)
    external
    override
    onlyPoolManager
    returns (bytes4, int128);

```

Copy

### \_sortCurrencies [​](https://docs.uniswap.org/contracts/v4/reference/core/test/DeltaReturningHook\#_sortcurrencies "Direct link to heading")

```codeBlockLines_mRuA
function _sortCurrencies(PoolKey calldata key, IPoolManager.SwapParams calldata params)
    internal
    pure
    returns (Currency specified, Currency unspecified);

```

Copy

### \_settleOrTake [​](https://docs.uniswap.org/contracts/v4/reference/core/test/DeltaReturningHook\#_settleortake "Direct link to heading")

```codeBlockLines_mRuA
function _settleOrTake(Currency currency, int128 delta) internal;

```

Copy

- [State Variables](https://docs.uniswap.org/contracts/v4/reference/core/test/DeltaReturningHook#state-variables)
  - [manager](https://docs.uniswap.org/contracts/v4/reference/core/test/DeltaReturningHook#manager)
  - [deltaSpecified](https://docs.uniswap.org/contracts/v4/reference/core/test/DeltaReturningHook#deltaspecified)
  - [deltaUnspecifiedBeforeSwap](https://docs.uniswap.org/contracts/v4/reference/core/test/DeltaReturningHook#deltaunspecifiedbeforeswap)
  - [deltaUnspecifiedAfterSwap](https://docs.uniswap.org/contracts/v4/reference/core/test/DeltaReturningHook#deltaunspecifiedafterswap)
- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/test/DeltaReturningHook#functions)
  - [constructor](https://docs.uniswap.org/contracts/v4/reference/core/test/DeltaReturningHook#constructor)
  - [onlyPoolManager](https://docs.uniswap.org/contracts/v4/reference/core/test/DeltaReturningHook#onlypoolmanager)
  - [setDeltaSpecified](https://docs.uniswap.org/contracts/v4/reference/core/test/DeltaReturningHook#setdeltaspecified)
  - [setDeltaUnspecifiedBeforeSwap](https://docs.uniswap.org/contracts/v4/reference/core/test/DeltaReturningHook#setdeltaunspecifiedbeforeswap)
  - [setDeltaUnspecifiedAfterSwap](https://docs.uniswap.org/contracts/v4/reference/core/test/DeltaReturningHook#setdeltaunspecifiedafterswap)
  - [beforeSwap](https://docs.uniswap.org/contracts/v4/reference/core/test/DeltaReturningHook#beforeswap)
  - [afterSwap](https://docs.uniswap.org/contracts/v4/reference/core/test/DeltaReturningHook#afterswap)
  - [\_sortCurrencies](https://docs.uniswap.org/contracts/v4/reference/core/test/DeltaReturningHook#_sortcurrencies)
  - [\_settleOrTake](https://docs.uniswap.org/contracts/v4/reference/core/test/DeltaReturningHook#_settleortake)