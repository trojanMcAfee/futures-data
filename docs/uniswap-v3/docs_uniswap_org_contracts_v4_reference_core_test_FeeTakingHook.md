[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/test/FeeTakingHook#)

On this page

# FeeTakingHook

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/test/FeeTakingHook.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:** [BaseTestHooks](https://docs.uniswap.org/contracts/v4/reference/core/test/BaseTestHooks)

## State Variables [​](https://docs.uniswap.org/contracts/v4/reference/core/test/FeeTakingHook\#state-variables "Direct link to heading")

### manager [​](https://docs.uniswap.org/contracts/v4/reference/core/test/FeeTakingHook\#manager "Direct link to heading")

```codeBlockLines_mRuA
IPoolManager immutable manager;

```

Copy

### LIQUIDITY\_FEE [​](https://docs.uniswap.org/contracts/v4/reference/core/test/FeeTakingHook\#liquidity_fee "Direct link to heading")

```codeBlockLines_mRuA
uint128 public constant LIQUIDITY_FEE = 543;

```

Copy

### SWAP\_FEE\_BIPS [​](https://docs.uniswap.org/contracts/v4/reference/core/test/FeeTakingHook\#swap_fee_bips "Direct link to heading")

```codeBlockLines_mRuA
uint128 public constant SWAP_FEE_BIPS = 123;

```

Copy

### TOTAL\_BIPS [​](https://docs.uniswap.org/contracts/v4/reference/core/test/FeeTakingHook\#total_bips "Direct link to heading")

```codeBlockLines_mRuA
uint128 public constant TOTAL_BIPS = 10000;

```

Copy

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/test/FeeTakingHook\#functions "Direct link to heading")

### constructor [​](https://docs.uniswap.org/contracts/v4/reference/core/test/FeeTakingHook\#constructor "Direct link to heading")

```codeBlockLines_mRuA
constructor(IPoolManager _manager);

```

Copy

### onlyPoolManager [​](https://docs.uniswap.org/contracts/v4/reference/core/test/FeeTakingHook\#onlypoolmanager "Direct link to heading")

```codeBlockLines_mRuA
modifier onlyPoolManager();

```

Copy

### afterSwap [​](https://docs.uniswap.org/contracts/v4/reference/core/test/FeeTakingHook\#afterswap "Direct link to heading")

```codeBlockLines_mRuA
function afterSwap(
    address,
    PoolKey calldata key,
    IPoolManager.SwapParams calldata params,
    BalanceDelta delta,
    bytes calldata
) external override onlyPoolManager returns (bytes4, int128);

```

Copy

### afterRemoveLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/core/test/FeeTakingHook\#afterremoveliquidity "Direct link to heading")

```codeBlockLines_mRuA
function afterRemoveLiquidity(
    address,
    PoolKey calldata key,
    IPoolManager.ModifyLiquidityParams calldata,
    BalanceDelta delta,
    BalanceDelta,
    bytes calldata
) external override onlyPoolManager returns (bytes4, BalanceDelta);

```

Copy

### afterAddLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/core/test/FeeTakingHook\#afteraddliquidity "Direct link to heading")

```codeBlockLines_mRuA
function afterAddLiquidity(
    address,
    PoolKey calldata key,
    IPoolManager.ModifyLiquidityParams calldata,
    BalanceDelta delta,
    BalanceDelta,
    bytes calldata
) external override onlyPoolManager returns (bytes4, BalanceDelta);

```

Copy

- [State Variables](https://docs.uniswap.org/contracts/v4/reference/core/test/FeeTakingHook#state-variables)
  - [manager](https://docs.uniswap.org/contracts/v4/reference/core/test/FeeTakingHook#manager)
  - [LIQUIDITY\_FEE](https://docs.uniswap.org/contracts/v4/reference/core/test/FeeTakingHook#liquidity_fee)
  - [SWAP\_FEE\_BIPS](https://docs.uniswap.org/contracts/v4/reference/core/test/FeeTakingHook#swap_fee_bips)
  - [TOTAL\_BIPS](https://docs.uniswap.org/contracts/v4/reference/core/test/FeeTakingHook#total_bips)
- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/test/FeeTakingHook#functions)
  - [constructor](https://docs.uniswap.org/contracts/v4/reference/core/test/FeeTakingHook#constructor)
  - [onlyPoolManager](https://docs.uniswap.org/contracts/v4/reference/core/test/FeeTakingHook#onlypoolmanager)
  - [afterSwap](https://docs.uniswap.org/contracts/v4/reference/core/test/FeeTakingHook#afterswap)
  - [afterRemoveLiquidity](https://docs.uniswap.org/contracts/v4/reference/core/test/FeeTakingHook#afterremoveliquidity)
  - [afterAddLiquidity](https://docs.uniswap.org/contracts/v4/reference/core/test/FeeTakingHook#afteraddliquidity)