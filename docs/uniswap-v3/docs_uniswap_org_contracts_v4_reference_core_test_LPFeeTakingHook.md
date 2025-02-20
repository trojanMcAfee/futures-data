[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/test/LPFeeTakingHook#)

On this page

# LPFeeTakingHook

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/test/LPFeeTakingHook.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:** [BaseTestHooks](https://docs.uniswap.org/contracts/v4/reference/core/test/BaseTestHooks)

a hook that takes all of the LP fee revenue

_an example test hook to validate the data is provided correctly_

## State Variables [​](https://docs.uniswap.org/contracts/v4/reference/core/test/LPFeeTakingHook\#state-variables "Direct link to heading")

### manager [​](https://docs.uniswap.org/contracts/v4/reference/core/test/LPFeeTakingHook\#manager "Direct link to heading")

```codeBlockLines_mRuA
IPoolManager immutable manager;

```

Copy

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/test/LPFeeTakingHook\#functions "Direct link to heading")

### constructor [​](https://docs.uniswap.org/contracts/v4/reference/core/test/LPFeeTakingHook\#constructor "Direct link to heading")

```codeBlockLines_mRuA
constructor(IPoolManager _manager);

```

Copy

### onlyPoolManager [​](https://docs.uniswap.org/contracts/v4/reference/core/test/LPFeeTakingHook\#onlypoolmanager "Direct link to heading")

```codeBlockLines_mRuA
modifier onlyPoolManager();

```

Copy

### afterRemoveLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/core/test/LPFeeTakingHook\#afterremoveliquidity "Direct link to heading")

```codeBlockLines_mRuA
function afterRemoveLiquidity(
    address,
    PoolKey calldata key,
    IPoolManager.ModifyLiquidityParams calldata,
    BalanceDelta,
    BalanceDelta feeDelta,
    bytes calldata
) external override onlyPoolManager returns (bytes4, BalanceDelta);

```

Copy

### afterAddLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/core/test/LPFeeTakingHook\#afteraddliquidity "Direct link to heading")

```codeBlockLines_mRuA
function afterAddLiquidity(
    address,
    PoolKey calldata key,
    IPoolManager.ModifyLiquidityParams calldata,
    BalanceDelta,
    BalanceDelta feeDelta,
    bytes calldata
) external override onlyPoolManager returns (bytes4, BalanceDelta);

```

Copy

- [State Variables](https://docs.uniswap.org/contracts/v4/reference/core/test/LPFeeTakingHook#state-variables)
  - [manager](https://docs.uniswap.org/contracts/v4/reference/core/test/LPFeeTakingHook#manager)
- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/test/LPFeeTakingHook#functions)
  - [constructor](https://docs.uniswap.org/contracts/v4/reference/core/test/LPFeeTakingHook#constructor)
  - [onlyPoolManager](https://docs.uniswap.org/contracts/v4/reference/core/test/LPFeeTakingHook#onlypoolmanager)
  - [afterRemoveLiquidity](https://docs.uniswap.org/contracts/v4/reference/core/test/LPFeeTakingHook#afterremoveliquidity)
  - [afterAddLiquidity](https://docs.uniswap.org/contracts/v4/reference/core/test/LPFeeTakingHook#afteraddliquidity)