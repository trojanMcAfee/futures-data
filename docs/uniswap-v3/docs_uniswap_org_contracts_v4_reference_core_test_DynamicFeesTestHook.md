[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/test/DynamicFeesTestHook#)

On this page

# DynamicFeesTestHook

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/test/DynamicFeesTestHook.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:** [BaseTestHooks](https://docs.uniswap.org/contracts/v4/reference/core/test/BaseTestHooks)

## State Variables [​](https://docs.uniswap.org/contracts/v4/reference/core/test/DynamicFeesTestHook\#state-variables "Direct link to heading")

### fee [​](https://docs.uniswap.org/contracts/v4/reference/core/test/DynamicFeesTestHook\#fee "Direct link to heading")

```codeBlockLines_mRuA
uint24 internal fee;

```

Copy

### manager [​](https://docs.uniswap.org/contracts/v4/reference/core/test/DynamicFeesTestHook\#manager "Direct link to heading")

```codeBlockLines_mRuA
IPoolManager manager;

```

Copy

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/test/DynamicFeesTestHook\#functions "Direct link to heading")

### setManager [​](https://docs.uniswap.org/contracts/v4/reference/core/test/DynamicFeesTestHook\#setmanager "Direct link to heading")

```codeBlockLines_mRuA
function setManager(IPoolManager _manager) external;

```

Copy

### setFee [​](https://docs.uniswap.org/contracts/v4/reference/core/test/DynamicFeesTestHook\#setfee "Direct link to heading")

```codeBlockLines_mRuA
function setFee(uint24 _fee) external;

```

Copy

### afterInitialize [​](https://docs.uniswap.org/contracts/v4/reference/core/test/DynamicFeesTestHook\#afterinitialize "Direct link to heading")

```codeBlockLines_mRuA
function afterInitialize(address, PoolKey calldata key, uint160, int24) external override returns (bytes4);

```

Copy

### beforeSwap [​](https://docs.uniswap.org/contracts/v4/reference/core/test/DynamicFeesTestHook\#beforeswap "Direct link to heading")

```codeBlockLines_mRuA
function beforeSwap(address, PoolKey calldata key, IPoolManager.SwapParams calldata, bytes calldata)
    external
    override
    returns (bytes4, BeforeSwapDelta, uint24);

```

Copy

### forcePoolFeeUpdate [​](https://docs.uniswap.org/contracts/v4/reference/core/test/DynamicFeesTestHook\#forcepoolfeeupdate "Direct link to heading")

```codeBlockLines_mRuA
function forcePoolFeeUpdate(PoolKey calldata _key, uint24 _fee) external;

```

Copy

- [State Variables](https://docs.uniswap.org/contracts/v4/reference/core/test/DynamicFeesTestHook#state-variables)
  - [fee](https://docs.uniswap.org/contracts/v4/reference/core/test/DynamicFeesTestHook#fee)
  - [manager](https://docs.uniswap.org/contracts/v4/reference/core/test/DynamicFeesTestHook#manager)
- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/test/DynamicFeesTestHook#functions)
  - [setManager](https://docs.uniswap.org/contracts/v4/reference/core/test/DynamicFeesTestHook#setmanager)
  - [setFee](https://docs.uniswap.org/contracts/v4/reference/core/test/DynamicFeesTestHook#setfee)
  - [afterInitialize](https://docs.uniswap.org/contracts/v4/reference/core/test/DynamicFeesTestHook#afterinitialize)
  - [beforeSwap](https://docs.uniswap.org/contracts/v4/reference/core/test/DynamicFeesTestHook#beforeswap)
  - [forcePoolFeeUpdate](https://docs.uniswap.org/contracts/v4/reference/core/test/DynamicFeesTestHook#forcepoolfeeupdate)