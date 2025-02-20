[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/test/DynamicReturnFeeTestHook#)

On this page

# DynamicReturnFeeTestHook

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/test/DynamicReturnFeeTestHook.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:** [BaseTestHooks](https://docs.uniswap.org/contracts/v4/reference/core/test/BaseTestHooks)

## State Variables [​](https://docs.uniswap.org/contracts/v4/reference/core/test/DynamicReturnFeeTestHook\#state-variables "Direct link to heading")

### fee [​](https://docs.uniswap.org/contracts/v4/reference/core/test/DynamicReturnFeeTestHook\#fee "Direct link to heading")

```codeBlockLines_mRuA
uint24 internal fee;

```

Copy

### manager [​](https://docs.uniswap.org/contracts/v4/reference/core/test/DynamicReturnFeeTestHook\#manager "Direct link to heading")

```codeBlockLines_mRuA
IPoolManager manager;

```

Copy

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/test/DynamicReturnFeeTestHook\#functions "Direct link to heading")

### setManager [​](https://docs.uniswap.org/contracts/v4/reference/core/test/DynamicReturnFeeTestHook\#setmanager "Direct link to heading")

```codeBlockLines_mRuA
function setManager(IPoolManager _manager) external;

```

Copy

### setFee [​](https://docs.uniswap.org/contracts/v4/reference/core/test/DynamicReturnFeeTestHook\#setfee "Direct link to heading")

```codeBlockLines_mRuA
function setFee(uint24 _fee) external;

```

Copy

### beforeSwap [​](https://docs.uniswap.org/contracts/v4/reference/core/test/DynamicReturnFeeTestHook\#beforeswap "Direct link to heading")

```codeBlockLines_mRuA
function beforeSwap(address, PoolKey calldata, IPoolManager.SwapParams calldata, bytes calldata)
    external
    view
    override
    returns (bytes4, BeforeSwapDelta, uint24);

```

Copy

### forcePoolFeeUpdate [​](https://docs.uniswap.org/contracts/v4/reference/core/test/DynamicReturnFeeTestHook\#forcepoolfeeupdate "Direct link to heading")

```codeBlockLines_mRuA
function forcePoolFeeUpdate(PoolKey calldata _key, uint24 _fee) external;

```

Copy

- [State Variables](https://docs.uniswap.org/contracts/v4/reference/core/test/DynamicReturnFeeTestHook#state-variables)
  - [fee](https://docs.uniswap.org/contracts/v4/reference/core/test/DynamicReturnFeeTestHook#fee)
  - [manager](https://docs.uniswap.org/contracts/v4/reference/core/test/DynamicReturnFeeTestHook#manager)
- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/test/DynamicReturnFeeTestHook#functions)
  - [setManager](https://docs.uniswap.org/contracts/v4/reference/core/test/DynamicReturnFeeTestHook#setmanager)
  - [setFee](https://docs.uniswap.org/contracts/v4/reference/core/test/DynamicReturnFeeTestHook#setfee)
  - [beforeSwap](https://docs.uniswap.org/contracts/v4/reference/core/test/DynamicReturnFeeTestHook#beforeswap)
  - [forcePoolFeeUpdate](https://docs.uniswap.org/contracts/v4/reference/core/test/DynamicReturnFeeTestHook#forcepoolfeeupdate)