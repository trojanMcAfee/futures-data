[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolSwapTest#)

On this page

# PoolSwapTest

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/test/PoolSwapTest.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:** [PoolTestBase](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolTestBase)

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolSwapTest\#functions "Direct link to heading")

### constructor [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolSwapTest\#constructor "Direct link to heading")

```codeBlockLines_mRuA
constructor(IPoolManager _manager) PoolTestBase(_manager);

```

Copy

### swap [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolSwapTest\#swap "Direct link to heading")

```codeBlockLines_mRuA
function swap(
    PoolKey memory key,
    IPoolManager.SwapParams memory params,
    TestSettings memory testSettings,
    bytes memory hookData
) external payable returns (BalanceDelta delta);

```

Copy

### unlockCallback [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolSwapTest\#unlockcallback "Direct link to heading")

```codeBlockLines_mRuA
function unlockCallback(bytes calldata rawData) external returns (bytes memory);

```

Copy

## Errors [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolSwapTest\#errors "Direct link to heading")

### NoSwapOccurred [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolSwapTest\#noswapoccurred "Direct link to heading")

```codeBlockLines_mRuA
error NoSwapOccurred();

```

Copy

## Structs [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolSwapTest\#structs "Direct link to heading")

### CallbackData [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolSwapTest\#callbackdata "Direct link to heading")

```codeBlockLines_mRuA
struct CallbackData {
    address sender;
    TestSettings testSettings;
    PoolKey key;
    IPoolManager.SwapParams params;
    bytes hookData;
}

```

Copy

### TestSettings [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolSwapTest\#testsettings "Direct link to heading")

```codeBlockLines_mRuA
struct TestSettings {
    bool takeClaims;
    bool settleUsingBurn;
}

```

Copy

- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolSwapTest#functions)
  - [constructor](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolSwapTest#constructor)
  - [swap](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolSwapTest#swap)
  - [unlockCallback](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolSwapTest#unlockcallback)
- [Errors](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolSwapTest#errors)
  - [NoSwapOccurred](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolSwapTest#noswapoccurred)
- [Structs](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolSwapTest#structs)
  - [CallbackData](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolSwapTest#callbackdata)
  - [TestSettings](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolSwapTest#testsettings)