[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/test/BaseTestHooks#)

On this page

# BaseTestHooks

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/test/BaseTestHooks.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:** [IHooks](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IHooks)

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/test/BaseTestHooks\#functions "Direct link to heading")

### beforeInitialize [​](https://docs.uniswap.org/contracts/v4/reference/core/test/BaseTestHooks\#beforeinitialize "Direct link to heading")

```codeBlockLines_mRuA
function beforeInitialize(address, PoolKey calldata, uint160) external virtual returns (bytes4);

```

Copy

### afterInitialize [​](https://docs.uniswap.org/contracts/v4/reference/core/test/BaseTestHooks\#afterinitialize "Direct link to heading")

```codeBlockLines_mRuA
function afterInitialize(address, PoolKey calldata, uint160, int24) external virtual returns (bytes4);

```

Copy

### beforeAddLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/core/test/BaseTestHooks\#beforeaddliquidity "Direct link to heading")

```codeBlockLines_mRuA
function beforeAddLiquidity(address, PoolKey calldata, IPoolManager.ModifyLiquidityParams calldata, bytes calldata)
    external
    virtual
    returns (bytes4);

```

Copy

### afterAddLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/core/test/BaseTestHooks\#afteraddliquidity "Direct link to heading")

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

### beforeRemoveLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/core/test/BaseTestHooks\#beforeremoveliquidity "Direct link to heading")

```codeBlockLines_mRuA
function beforeRemoveLiquidity(address, PoolKey calldata, IPoolManager.ModifyLiquidityParams calldata, bytes calldata)
    external
    virtual
    returns (bytes4);

```

Copy

### afterRemoveLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/core/test/BaseTestHooks\#afterremoveliquidity "Direct link to heading")

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

### beforeSwap [​](https://docs.uniswap.org/contracts/v4/reference/core/test/BaseTestHooks\#beforeswap "Direct link to heading")

```codeBlockLines_mRuA
function beforeSwap(address, PoolKey calldata, IPoolManager.SwapParams calldata, bytes calldata)
    external
    virtual
    returns (bytes4, BeforeSwapDelta, uint24);

```

Copy

### afterSwap [​](https://docs.uniswap.org/contracts/v4/reference/core/test/BaseTestHooks\#afterswap "Direct link to heading")

```codeBlockLines_mRuA
function afterSwap(address, PoolKey calldata, IPoolManager.SwapParams calldata, BalanceDelta, bytes calldata)
    external
    virtual
    returns (bytes4, int128);

```

Copy

### beforeDonate [​](https://docs.uniswap.org/contracts/v4/reference/core/test/BaseTestHooks\#beforedonate "Direct link to heading")

```codeBlockLines_mRuA
function beforeDonate(address, PoolKey calldata, uint256, uint256, bytes calldata) external virtual returns (bytes4);

```

Copy

### afterDonate [​](https://docs.uniswap.org/contracts/v4/reference/core/test/BaseTestHooks\#afterdonate "Direct link to heading")

```codeBlockLines_mRuA
function afterDonate(address, PoolKey calldata, uint256, uint256, bytes calldata) external virtual returns (bytes4);

```

Copy

## Errors [​](https://docs.uniswap.org/contracts/v4/reference/core/test/BaseTestHooks\#errors "Direct link to heading")

### HookNotImplemented [​](https://docs.uniswap.org/contracts/v4/reference/core/test/BaseTestHooks\#hooknotimplemented "Direct link to heading")

```codeBlockLines_mRuA
error HookNotImplemented();

```

Copy

- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/test/BaseTestHooks#functions)
  - [beforeInitialize](https://docs.uniswap.org/contracts/v4/reference/core/test/BaseTestHooks#beforeinitialize)
  - [afterInitialize](https://docs.uniswap.org/contracts/v4/reference/core/test/BaseTestHooks#afterinitialize)
  - [beforeAddLiquidity](https://docs.uniswap.org/contracts/v4/reference/core/test/BaseTestHooks#beforeaddliquidity)
  - [afterAddLiquidity](https://docs.uniswap.org/contracts/v4/reference/core/test/BaseTestHooks#afteraddliquidity)
  - [beforeRemoveLiquidity](https://docs.uniswap.org/contracts/v4/reference/core/test/BaseTestHooks#beforeremoveliquidity)
  - [afterRemoveLiquidity](https://docs.uniswap.org/contracts/v4/reference/core/test/BaseTestHooks#afterremoveliquidity)
  - [beforeSwap](https://docs.uniswap.org/contracts/v4/reference/core/test/BaseTestHooks#beforeswap)
  - [afterSwap](https://docs.uniswap.org/contracts/v4/reference/core/test/BaseTestHooks#afterswap)
  - [beforeDonate](https://docs.uniswap.org/contracts/v4/reference/core/test/BaseTestHooks#beforedonate)
  - [afterDonate](https://docs.uniswap.org/contracts/v4/reference/core/test/BaseTestHooks#afterdonate)
- [Errors](https://docs.uniswap.org/contracts/v4/reference/core/test/BaseTestHooks#errors)
  - [HookNotImplemented](https://docs.uniswap.org/contracts/v4/reference/core/test/BaseTestHooks#hooknotimplemented)