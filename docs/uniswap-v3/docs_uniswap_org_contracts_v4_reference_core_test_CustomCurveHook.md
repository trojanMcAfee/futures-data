[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/test/CustomCurveHook#)

On this page

# CustomCurveHook

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/test/CustomCurveHook.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:** [BaseTestHooks](https://docs.uniswap.org/contracts/v4/reference/core/test/BaseTestHooks)

## State Variables [​](https://docs.uniswap.org/contracts/v4/reference/core/test/CustomCurveHook\#state-variables "Direct link to heading")

### manager [​](https://docs.uniswap.org/contracts/v4/reference/core/test/CustomCurveHook\#manager "Direct link to heading")

```codeBlockLines_mRuA
IPoolManager immutable manager;

```

Copy

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/test/CustomCurveHook\#functions "Direct link to heading")

### constructor [​](https://docs.uniswap.org/contracts/v4/reference/core/test/CustomCurveHook\#constructor "Direct link to heading")

```codeBlockLines_mRuA
constructor(IPoolManager _manager);

```

Copy

### onlyPoolManager [​](https://docs.uniswap.org/contracts/v4/reference/core/test/CustomCurveHook\#onlypoolmanager "Direct link to heading")

```codeBlockLines_mRuA
modifier onlyPoolManager();

```

Copy

### beforeSwap [​](https://docs.uniswap.org/contracts/v4/reference/core/test/CustomCurveHook\#beforeswap "Direct link to heading")

```codeBlockLines_mRuA
function beforeSwap(address, PoolKey calldata key, IPoolManager.SwapParams calldata params, bytes calldata)
    external
    override
    onlyPoolManager
    returns (bytes4, BeforeSwapDelta, uint24);

```

Copy

### afterAddLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/core/test/CustomCurveHook\#afteraddliquidity "Direct link to heading")

```codeBlockLines_mRuA
function afterAddLiquidity(
    address,
    PoolKey calldata,
    IPoolManager.ModifyLiquidityParams calldata,
    BalanceDelta,
    BalanceDelta,
    bytes calldata
) external view override onlyPoolManager returns (bytes4, BalanceDelta);

```

Copy

### \_getInputOutputAndAmount [​](https://docs.uniswap.org/contracts/v4/reference/core/test/CustomCurveHook\#_getinputoutputandamount "Direct link to heading")

```codeBlockLines_mRuA
function _getInputOutputAndAmount(PoolKey calldata key, IPoolManager.SwapParams calldata params)
    internal
    pure
    returns (Currency input, Currency output, uint256 amount);

```

Copy

## Errors [​](https://docs.uniswap.org/contracts/v4/reference/core/test/CustomCurveHook\#errors "Direct link to heading")

### AddLiquidityDirectToHook [​](https://docs.uniswap.org/contracts/v4/reference/core/test/CustomCurveHook\#addliquiditydirecttohook "Direct link to heading")

```codeBlockLines_mRuA
error AddLiquidityDirectToHook();

```

Copy

- [State Variables](https://docs.uniswap.org/contracts/v4/reference/core/test/CustomCurveHook#state-variables)
  - [manager](https://docs.uniswap.org/contracts/v4/reference/core/test/CustomCurveHook#manager)
- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/test/CustomCurveHook#functions)
  - [constructor](https://docs.uniswap.org/contracts/v4/reference/core/test/CustomCurveHook#constructor)
  - [onlyPoolManager](https://docs.uniswap.org/contracts/v4/reference/core/test/CustomCurveHook#onlypoolmanager)
  - [beforeSwap](https://docs.uniswap.org/contracts/v4/reference/core/test/CustomCurveHook#beforeswap)
  - [afterAddLiquidity](https://docs.uniswap.org/contracts/v4/reference/core/test/CustomCurveHook#afteraddliquidity)
  - [\_getInputOutputAndAmount](https://docs.uniswap.org/contracts/v4/reference/core/test/CustomCurveHook#_getinputoutputandamount)
- [Errors](https://docs.uniswap.org/contracts/v4/reference/core/test/CustomCurveHook#errors)
  - [AddLiquidityDirectToHook](https://docs.uniswap.org/contracts/v4/reference/core/test/CustomCurveHook#addliquiditydirecttohook)