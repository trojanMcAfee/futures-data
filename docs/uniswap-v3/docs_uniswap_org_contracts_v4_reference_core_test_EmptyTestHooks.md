[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/test/EmptyTestHooks#)

On this page

# EmptyTestHooks

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/test/EmptyTestHooks.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:** [IHooks](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IHooks)

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/test/EmptyTestHooks\#functions "Direct link to heading")

### constructor [​](https://docs.uniswap.org/contracts/v4/reference/core/test/EmptyTestHooks\#constructor "Direct link to heading")

```codeBlockLines_mRuA
constructor();

```

Copy

### beforeInitialize [​](https://docs.uniswap.org/contracts/v4/reference/core/test/EmptyTestHooks\#beforeinitialize "Direct link to heading")

```codeBlockLines_mRuA
function beforeInitialize(address, PoolKey calldata, uint160) external pure override returns (bytes4);

```

Copy

### afterInitialize [​](https://docs.uniswap.org/contracts/v4/reference/core/test/EmptyTestHooks\#afterinitialize "Direct link to heading")

```codeBlockLines_mRuA
function afterInitialize(address, PoolKey calldata, uint160, int24) external pure override returns (bytes4);

```

Copy

### beforeAddLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/core/test/EmptyTestHooks\#beforeaddliquidity "Direct link to heading")

```codeBlockLines_mRuA
function beforeAddLiquidity(address, PoolKey calldata, IPoolManager.ModifyLiquidityParams calldata, bytes calldata)
    external
    pure
    override
    returns (bytes4);

```

Copy

### afterAddLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/core/test/EmptyTestHooks\#afteraddliquidity "Direct link to heading")

```codeBlockLines_mRuA
function afterAddLiquidity(
    address,
    PoolKey calldata,
    IPoolManager.ModifyLiquidityParams calldata,
    BalanceDelta,
    BalanceDelta,
    bytes calldata
) external pure override returns (bytes4, BalanceDelta);

```

Copy

### beforeRemoveLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/core/test/EmptyTestHooks\#beforeremoveliquidity "Direct link to heading")

```codeBlockLines_mRuA
function beforeRemoveLiquidity(address, PoolKey calldata, IPoolManager.ModifyLiquidityParams calldata, bytes calldata)
    external
    pure
    override
    returns (bytes4);

```

Copy

### afterRemoveLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/core/test/EmptyTestHooks\#afterremoveliquidity "Direct link to heading")

```codeBlockLines_mRuA
function afterRemoveLiquidity(
    address,
    PoolKey calldata,
    IPoolManager.ModifyLiquidityParams calldata,
    BalanceDelta,
    BalanceDelta,
    bytes calldata
) external pure override returns (bytes4, BalanceDelta);

```

Copy

### beforeSwap [​](https://docs.uniswap.org/contracts/v4/reference/core/test/EmptyTestHooks\#beforeswap "Direct link to heading")

```codeBlockLines_mRuA
function beforeSwap(address, PoolKey calldata, IPoolManager.SwapParams calldata, bytes calldata)
    external
    pure
    override
    returns (bytes4, BeforeSwapDelta, uint24);

```

Copy

### afterSwap [​](https://docs.uniswap.org/contracts/v4/reference/core/test/EmptyTestHooks\#afterswap "Direct link to heading")

```codeBlockLines_mRuA
function afterSwap(address, PoolKey calldata, IPoolManager.SwapParams calldata, BalanceDelta, bytes calldata)
    external
    pure
    override
    returns (bytes4, int128);

```

Copy

### beforeDonate [​](https://docs.uniswap.org/contracts/v4/reference/core/test/EmptyTestHooks\#beforedonate "Direct link to heading")

```codeBlockLines_mRuA
function beforeDonate(address, PoolKey calldata, uint256, uint256, bytes calldata)
    external
    pure
    override
    returns (bytes4);

```

Copy

### afterDonate [​](https://docs.uniswap.org/contracts/v4/reference/core/test/EmptyTestHooks\#afterdonate "Direct link to heading")

```codeBlockLines_mRuA
function afterDonate(address, PoolKey calldata, uint256, uint256, bytes calldata)
    external
    pure
    override
    returns (bytes4);

```

Copy

- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/test/EmptyTestHooks#functions)
  - [constructor](https://docs.uniswap.org/contracts/v4/reference/core/test/EmptyTestHooks#constructor)
  - [beforeInitialize](https://docs.uniswap.org/contracts/v4/reference/core/test/EmptyTestHooks#beforeinitialize)
  - [afterInitialize](https://docs.uniswap.org/contracts/v4/reference/core/test/EmptyTestHooks#afterinitialize)
  - [beforeAddLiquidity](https://docs.uniswap.org/contracts/v4/reference/core/test/EmptyTestHooks#beforeaddliquidity)
  - [afterAddLiquidity](https://docs.uniswap.org/contracts/v4/reference/core/test/EmptyTestHooks#afteraddliquidity)
  - [beforeRemoveLiquidity](https://docs.uniswap.org/contracts/v4/reference/core/test/EmptyTestHooks#beforeremoveliquidity)
  - [afterRemoveLiquidity](https://docs.uniswap.org/contracts/v4/reference/core/test/EmptyTestHooks#afterremoveliquidity)
  - [beforeSwap](https://docs.uniswap.org/contracts/v4/reference/core/test/EmptyTestHooks#beforeswap)
  - [afterSwap](https://docs.uniswap.org/contracts/v4/reference/core/test/EmptyTestHooks#afterswap)
  - [beforeDonate](https://docs.uniswap.org/contracts/v4/reference/core/test/EmptyTestHooks#beforedonate)
  - [afterDonate](https://docs.uniswap.org/contracts/v4/reference/core/test/EmptyTestHooks#afterdonate)