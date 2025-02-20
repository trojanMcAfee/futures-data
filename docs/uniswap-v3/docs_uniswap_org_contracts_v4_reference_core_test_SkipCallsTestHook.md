[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/test/SkipCallsTestHook#)

On this page

# SkipCallsTestHook

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/test/SkipCallsTestHook.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:** [BaseTestHooks](https://docs.uniswap.org/contracts/v4/reference/core/test/BaseTestHooks), Test

## State Variables [​](https://docs.uniswap.org/contracts/v4/reference/core/test/SkipCallsTestHook\#state-variables "Direct link to heading")

### counter [​](https://docs.uniswap.org/contracts/v4/reference/core/test/SkipCallsTestHook\#counter "Direct link to heading")

```codeBlockLines_mRuA
uint256 public counter;

```

Copy

### manager [​](https://docs.uniswap.org/contracts/v4/reference/core/test/SkipCallsTestHook\#manager "Direct link to heading")

```codeBlockLines_mRuA
IPoolManager manager;

```

Copy

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/test/SkipCallsTestHook\#functions "Direct link to heading")

### setManager [​](https://docs.uniswap.org/contracts/v4/reference/core/test/SkipCallsTestHook\#setmanager "Direct link to heading")

```codeBlockLines_mRuA
function setManager(IPoolManager _manager) external;

```

Copy

### beforeInitialize [​](https://docs.uniswap.org/contracts/v4/reference/core/test/SkipCallsTestHook\#beforeinitialize "Direct link to heading")

```codeBlockLines_mRuA
function beforeInitialize(address, PoolKey calldata key, uint160 sqrtPriceX96) external override returns (bytes4);

```

Copy

### afterInitialize [​](https://docs.uniswap.org/contracts/v4/reference/core/test/SkipCallsTestHook\#afterinitialize "Direct link to heading")

```codeBlockLines_mRuA
function afterInitialize(address, PoolKey calldata key, uint160 sqrtPriceX96, int24)
    external
    override
    returns (bytes4);

```

Copy

### beforeAddLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/core/test/SkipCallsTestHook\#beforeaddliquidity "Direct link to heading")

```codeBlockLines_mRuA
function beforeAddLiquidity(
    address,
    PoolKey calldata key,
    IPoolManager.ModifyLiquidityParams calldata params,
    bytes calldata hookData
) external override returns (bytes4);

```

Copy

### afterAddLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/core/test/SkipCallsTestHook\#afteraddliquidity "Direct link to heading")

```codeBlockLines_mRuA
function afterAddLiquidity(
    address,
    PoolKey calldata key,
    IPoolManager.ModifyLiquidityParams calldata params,
    BalanceDelta,
    BalanceDelta,
    bytes calldata hookData
) external override returns (bytes4, BalanceDelta);

```

Copy

### beforeRemoveLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/core/test/SkipCallsTestHook\#beforeremoveliquidity "Direct link to heading")

```codeBlockLines_mRuA
function beforeRemoveLiquidity(
    address,
    PoolKey calldata key,
    IPoolManager.ModifyLiquidityParams calldata params,
    bytes calldata hookData
) external override returns (bytes4);

```

Copy

### afterRemoveLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/core/test/SkipCallsTestHook\#afterremoveliquidity "Direct link to heading")

```codeBlockLines_mRuA
function afterRemoveLiquidity(
    address,
    PoolKey calldata key,
    IPoolManager.ModifyLiquidityParams calldata params,
    BalanceDelta,
    BalanceDelta,
    bytes calldata hookData
) external override returns (bytes4, BalanceDelta);

```

Copy

### beforeSwap [​](https://docs.uniswap.org/contracts/v4/reference/core/test/SkipCallsTestHook\#beforeswap "Direct link to heading")

```codeBlockLines_mRuA
function beforeSwap(address, PoolKey calldata key, IPoolManager.SwapParams calldata params, bytes calldata hookData)
    external
    override
    returns (bytes4, BeforeSwapDelta, uint24);

```

Copy

### afterSwap [​](https://docs.uniswap.org/contracts/v4/reference/core/test/SkipCallsTestHook\#afterswap "Direct link to heading")

```codeBlockLines_mRuA
function afterSwap(
    address,
    PoolKey calldata key,
    IPoolManager.SwapParams calldata params,
    BalanceDelta,
    bytes calldata hookData
) external override returns (bytes4, int128);

```

Copy

### beforeDonate [​](https://docs.uniswap.org/contracts/v4/reference/core/test/SkipCallsTestHook\#beforedonate "Direct link to heading")

```codeBlockLines_mRuA
function beforeDonate(address, PoolKey calldata key, uint256 amt0, uint256 amt1, bytes calldata hookData)
    external
    override
    returns (bytes4);

```

Copy

### afterDonate [​](https://docs.uniswap.org/contracts/v4/reference/core/test/SkipCallsTestHook\#afterdonate "Direct link to heading")

```codeBlockLines_mRuA
function afterDonate(address, PoolKey calldata key, uint256 amt0, uint256 amt1, bytes calldata hookData)
    external
    override
    returns (bytes4);

```

Copy

### \_initialize [​](https://docs.uniswap.org/contracts/v4/reference/core/test/SkipCallsTestHook\#_initialize "Direct link to heading")

```codeBlockLines_mRuA
function _initialize(PoolKey memory key, uint160 sqrtPriceX96) public;

```

Copy

### \_swap [​](https://docs.uniswap.org/contracts/v4/reference/core/test/SkipCallsTestHook\#_swap "Direct link to heading")

```codeBlockLines_mRuA
function _swap(PoolKey calldata key, IPoolManager.SwapParams memory params, bytes calldata hookData) public;

```

Copy

### \_addLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/core/test/SkipCallsTestHook\#_addliquidity "Direct link to heading")

```codeBlockLines_mRuA
function _addLiquidity(PoolKey calldata key, IPoolManager.ModifyLiquidityParams memory params, bytes calldata hookData)
    public;

```

Copy

### \_removeLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/core/test/SkipCallsTestHook\#_removeliquidity "Direct link to heading")

```codeBlockLines_mRuA
function _removeLiquidity(
    PoolKey calldata key,
    IPoolManager.ModifyLiquidityParams memory params,
    bytes calldata hookData
) public;

```

Copy

### \_donate [​](https://docs.uniswap.org/contracts/v4/reference/core/test/SkipCallsTestHook\#_donate "Direct link to heading")

```codeBlockLines_mRuA
function _donate(PoolKey calldata key, uint256 amt0, uint256 amt1, bytes calldata hookData) public;

```

Copy

- [State Variables](https://docs.uniswap.org/contracts/v4/reference/core/test/SkipCallsTestHook#state-variables)
  - [counter](https://docs.uniswap.org/contracts/v4/reference/core/test/SkipCallsTestHook#counter)
  - [manager](https://docs.uniswap.org/contracts/v4/reference/core/test/SkipCallsTestHook#manager)
- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/test/SkipCallsTestHook#functions)
  - [setManager](https://docs.uniswap.org/contracts/v4/reference/core/test/SkipCallsTestHook#setmanager)
  - [beforeInitialize](https://docs.uniswap.org/contracts/v4/reference/core/test/SkipCallsTestHook#beforeinitialize)
  - [afterInitialize](https://docs.uniswap.org/contracts/v4/reference/core/test/SkipCallsTestHook#afterinitialize)
  - [beforeAddLiquidity](https://docs.uniswap.org/contracts/v4/reference/core/test/SkipCallsTestHook#beforeaddliquidity)
  - [afterAddLiquidity](https://docs.uniswap.org/contracts/v4/reference/core/test/SkipCallsTestHook#afteraddliquidity)
  - [beforeRemoveLiquidity](https://docs.uniswap.org/contracts/v4/reference/core/test/SkipCallsTestHook#beforeremoveliquidity)
  - [afterRemoveLiquidity](https://docs.uniswap.org/contracts/v4/reference/core/test/SkipCallsTestHook#afterremoveliquidity)
  - [beforeSwap](https://docs.uniswap.org/contracts/v4/reference/core/test/SkipCallsTestHook#beforeswap)
  - [afterSwap](https://docs.uniswap.org/contracts/v4/reference/core/test/SkipCallsTestHook#afterswap)
  - [beforeDonate](https://docs.uniswap.org/contracts/v4/reference/core/test/SkipCallsTestHook#beforedonate)
  - [afterDonate](https://docs.uniswap.org/contracts/v4/reference/core/test/SkipCallsTestHook#afterdonate)
  - [\_initialize](https://docs.uniswap.org/contracts/v4/reference/core/test/SkipCallsTestHook#_initialize)
  - [\_swap](https://docs.uniswap.org/contracts/v4/reference/core/test/SkipCallsTestHook#_swap)
  - [\_addLiquidity](https://docs.uniswap.org/contracts/v4/reference/core/test/SkipCallsTestHook#_addliquidity)
  - [\_removeLiquidity](https://docs.uniswap.org/contracts/v4/reference/core/test/SkipCallsTestHook#_removeliquidity)
  - [\_donate](https://docs.uniswap.org/contracts/v4/reference/core/test/SkipCallsTestHook#_donate)