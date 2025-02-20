[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolModifyLiquidityTest#)

On this page

# PoolModifyLiquidityTest

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/test/PoolModifyLiquidityTest.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:** [PoolTestBase](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolTestBase)

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolModifyLiquidityTest\#functions "Direct link to heading")

### constructor [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolModifyLiquidityTest\#constructor "Direct link to heading")

```codeBlockLines_mRuA
constructor(IPoolManager _manager) PoolTestBase(_manager);

```

Copy

### modifyLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolModifyLiquidityTest\#modifyliquidity "Direct link to heading")

```codeBlockLines_mRuA
function modifyLiquidity(PoolKey memory key, IPoolManager.ModifyLiquidityParams memory params, bytes memory hookData)
    external
    payable
    returns (BalanceDelta delta);

```

Copy

### modifyLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolModifyLiquidityTest\#modifyliquidity-1 "Direct link to heading")

```codeBlockLines_mRuA
function modifyLiquidity(
    PoolKey memory key,
    IPoolManager.ModifyLiquidityParams memory params,
    bytes memory hookData,
    bool settleUsingBurn,
    bool takeClaims
) public payable returns (BalanceDelta delta);

```

Copy

### unlockCallback [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolModifyLiquidityTest\#unlockcallback "Direct link to heading")

```codeBlockLines_mRuA
function unlockCallback(bytes calldata rawData) external returns (bytes memory);

```

Copy

## Structs [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolModifyLiquidityTest\#structs "Direct link to heading")

### CallbackData [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolModifyLiquidityTest\#callbackdata "Direct link to heading")

```codeBlockLines_mRuA
struct CallbackData {
    address sender;
    PoolKey key;
    IPoolManager.ModifyLiquidityParams params;
    bytes hookData;
    bool settleUsingBurn;
    bool takeClaims;
}

```

Copy

- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolModifyLiquidityTest#functions)
  - [constructor](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolModifyLiquidityTest#constructor)
  - [modifyLiquidity](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolModifyLiquidityTest#modifyliquidity)
  - [modifyLiquidity](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolModifyLiquidityTest#modifyliquidity-1)
  - [unlockCallback](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolModifyLiquidityTest#unlockcallback)
- [Structs](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolModifyLiquidityTest#structs)
  - [CallbackData](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolModifyLiquidityTest#callbackdata)