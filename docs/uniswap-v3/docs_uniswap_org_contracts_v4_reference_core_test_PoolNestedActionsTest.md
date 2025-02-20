[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolNestedActionsTest#)

On this page

# NestedActionExecutor

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/test/PoolNestedActionsTest.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:**
Test, [PoolTestBase](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolTestBase)

## State Variables [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolNestedActionsTest\#state-variables "Direct link to heading")

### key [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolNestedActionsTest\#key "Direct link to heading")

```codeBlockLines_mRuA
PoolKey internal key;

```

Copy

### user [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolNestedActionsTest\#user "Direct link to heading")

```codeBlockLines_mRuA
address user;

```

Copy

### ADD\_LIQUIDITY\_PARAMS [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolNestedActionsTest\#add_liquidity_params "Direct link to heading")

```codeBlockLines_mRuA
IPoolManager.ModifyLiquidityParams internal ADD_LIQUIDITY_PARAMS =
    IPoolManager.ModifyLiquidityParams({tickLower: -120, tickUpper: 120, liquidityDelta: 1e18, salt: 0});

```

Copy

### REMOVE\_LIQUIDITY\_PARAMS [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolNestedActionsTest\#remove_liquidity_params "Direct link to heading")

```codeBlockLines_mRuA
IPoolManager.ModifyLiquidityParams internal REMOVE_LIQUIDITY_PARAMS =
    IPoolManager.ModifyLiquidityParams({tickLower: -120, tickUpper: 120, liquidityDelta: -1e18, salt: 0});

```

Copy

### SWAP\_PARAMS [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolNestedActionsTest\#swap_params "Direct link to heading")

```codeBlockLines_mRuA
IPoolManager.SwapParams internal SWAP_PARAMS =
    IPoolManager.SwapParams({zeroForOne: true, amountSpecified: -100, sqrtPriceLimitX96: Constants.SQRT_PRICE_1_2});

```

Copy

### DONATE\_AMOUNT0 [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolNestedActionsTest\#donate_amount0 "Direct link to heading")

```codeBlockLines_mRuA
uint256 internal DONATE_AMOUNT0 = 12345e6;

```

Copy

### DONATE\_AMOUNT1 [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolNestedActionsTest\#donate_amount1 "Direct link to heading")

```codeBlockLines_mRuA
uint256 internal DONATE_AMOUNT1 = 98765e4;

```

Copy

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolNestedActionsTest\#functions "Direct link to heading")

### constructor [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolNestedActionsTest\#constructor "Direct link to heading")

```codeBlockLines_mRuA
constructor(IPoolManager _manager, address _user) PoolTestBase(_manager);

```

Copy

### setKey [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolNestedActionsTest\#setkey "Direct link to heading")

```codeBlockLines_mRuA
function setKey(PoolKey memory _key) external;

```

Copy

### execute [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolNestedActionsTest\#execute "Direct link to heading")

```codeBlockLines_mRuA
function execute(Action[] memory actions) public;

```

Copy

### \_nestedUnlock [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolNestedActionsTest\#_nestedunlock "Direct link to heading")

```codeBlockLines_mRuA
function _nestedUnlock() internal;

```

Copy

### \_swap [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolNestedActionsTest\#_swap "Direct link to heading")

```codeBlockLines_mRuA
function _swap(address caller) internal;

```

Copy

### \_addLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolNestedActionsTest\#_addliquidity "Direct link to heading")

```codeBlockLines_mRuA
function _addLiquidity(address caller) internal;

```

Copy

### \_removeLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolNestedActionsTest\#_removeliquidity "Direct link to heading")

```codeBlockLines_mRuA
function _removeLiquidity(address caller) internal;

```

Copy

### \_donate [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolNestedActionsTest\#_donate "Direct link to heading")

```codeBlockLines_mRuA
function _donate(address caller) internal;

```

Copy

### \_initialize [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolNestedActionsTest\#_initialize "Direct link to heading")

```codeBlockLines_mRuA
function _initialize() internal;

```

Copy

### unlockCallback [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolNestedActionsTest\#unlockcallback "Direct link to heading")

```codeBlockLines_mRuA
function unlockCallback(bytes calldata) external pure override returns (bytes memory);

```

Copy

## Errors [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolNestedActionsTest\#errors "Direct link to heading")

### KeyNotSet [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolNestedActionsTest\#keynotset "Direct link to heading")

```codeBlockLines_mRuA
error KeyNotSet();

```

Copy

- [State Variables](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolNestedActionsTest#state-variables)
  - [key](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolNestedActionsTest#key)
  - [user](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolNestedActionsTest#user)
  - [ADD\_LIQUIDITY\_PARAMS](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolNestedActionsTest#add_liquidity_params)
  - [REMOVE\_LIQUIDITY\_PARAMS](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolNestedActionsTest#remove_liquidity_params)
  - [SWAP\_PARAMS](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolNestedActionsTest#swap_params)
  - [DONATE\_AMOUNT0](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolNestedActionsTest#donate_amount0)
  - [DONATE\_AMOUNT1](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolNestedActionsTest#donate_amount1)
- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolNestedActionsTest#functions)
  - [constructor](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolNestedActionsTest#constructor)
  - [setKey](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolNestedActionsTest#setkey)
  - [execute](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolNestedActionsTest#execute)
  - [\_nestedUnlock](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolNestedActionsTest#_nestedunlock)
  - [\_swap](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolNestedActionsTest#_swap)
  - [\_addLiquidity](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolNestedActionsTest#_addliquidity)
  - [\_removeLiquidity](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolNestedActionsTest#_removeliquidity)
  - [\_donate](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolNestedActionsTest#_donate)
  - [\_initialize](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolNestedActionsTest#_initialize)
  - [unlockCallback](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolNestedActionsTest#unlockcallback)
- [Errors](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolNestedActionsTest#errors)
  - [KeyNotSet](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolNestedActionsTest#keynotset)