[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/test/SwapRouterNoChecks#)

On this page

# SwapRouterNoChecks

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/test/SwapRouterNoChecks.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:** [PoolTestBase](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolTestBase)

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/test/SwapRouterNoChecks\#functions "Direct link to heading")

### constructor [​](https://docs.uniswap.org/contracts/v4/reference/core/test/SwapRouterNoChecks\#constructor "Direct link to heading")

```codeBlockLines_mRuA
constructor(IPoolManager _manager) PoolTestBase(_manager);

```

Copy

### swap [​](https://docs.uniswap.org/contracts/v4/reference/core/test/SwapRouterNoChecks\#swap "Direct link to heading")

```codeBlockLines_mRuA
function swap(PoolKey memory key, IPoolManager.SwapParams memory params) external payable;

```

Copy

### unlockCallback [​](https://docs.uniswap.org/contracts/v4/reference/core/test/SwapRouterNoChecks\#unlockcallback "Direct link to heading")

```codeBlockLines_mRuA
function unlockCallback(bytes calldata rawData) external returns (bytes memory);

```

Copy

## Errors [​](https://docs.uniswap.org/contracts/v4/reference/core/test/SwapRouterNoChecks\#errors "Direct link to heading")

### NoSwapOccurred [​](https://docs.uniswap.org/contracts/v4/reference/core/test/SwapRouterNoChecks\#noswapoccurred "Direct link to heading")

```codeBlockLines_mRuA
error NoSwapOccurred();

```

Copy

## Structs [​](https://docs.uniswap.org/contracts/v4/reference/core/test/SwapRouterNoChecks\#structs "Direct link to heading")

### CallbackData [​](https://docs.uniswap.org/contracts/v4/reference/core/test/SwapRouterNoChecks\#callbackdata "Direct link to heading")

```codeBlockLines_mRuA
struct CallbackData {
    address sender;
    PoolKey key;
    IPoolManager.SwapParams params;
}

```

Copy

- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/test/SwapRouterNoChecks#functions)
  - [constructor](https://docs.uniswap.org/contracts/v4/reference/core/test/SwapRouterNoChecks#constructor)
  - [swap](https://docs.uniswap.org/contracts/v4/reference/core/test/SwapRouterNoChecks#swap)
  - [unlockCallback](https://docs.uniswap.org/contracts/v4/reference/core/test/SwapRouterNoChecks#unlockcallback)
- [Errors](https://docs.uniswap.org/contracts/v4/reference/core/test/SwapRouterNoChecks#errors)
  - [NoSwapOccurred](https://docs.uniswap.org/contracts/v4/reference/core/test/SwapRouterNoChecks#noswapoccurred)
- [Structs](https://docs.uniswap.org/contracts/v4/reference/core/test/SwapRouterNoChecks#structs)
  - [CallbackData](https://docs.uniswap.org/contracts/v4/reference/core/test/SwapRouterNoChecks#callbackdata)