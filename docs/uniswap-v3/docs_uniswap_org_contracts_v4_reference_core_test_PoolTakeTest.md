[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolTakeTest#)

On this page

# PoolTakeTest

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/test/PoolTakeTest.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:** [PoolTestBase](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolTestBase)

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolTakeTest\#functions "Direct link to heading")

### constructor [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolTakeTest\#constructor "Direct link to heading")

```codeBlockLines_mRuA
constructor(IPoolManager _manager) PoolTestBase(_manager);

```

Copy

### take [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolTakeTest\#take "Direct link to heading")

```codeBlockLines_mRuA
function take(PoolKey memory key, uint256 amount0, uint256 amount1) external payable;

```

Copy

### unlockCallback [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolTakeTest\#unlockcallback "Direct link to heading")

```codeBlockLines_mRuA
function unlockCallback(bytes calldata rawData) external returns (bytes memory);

```

Copy

### \_testTake [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolTakeTest\#_testtake "Direct link to heading")

```codeBlockLines_mRuA
function _testTake(Currency currency, address sender, uint256 amount) internal;

```

Copy

## Structs [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolTakeTest\#structs "Direct link to heading")

### CallbackData [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolTakeTest\#callbackdata "Direct link to heading")

```codeBlockLines_mRuA
struct CallbackData {
    address sender;
    PoolKey key;
    uint256 amount0;
    uint256 amount1;
}

```

Copy

- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolTakeTest#functions)
  - [constructor](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolTakeTest#constructor)
  - [take](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolTakeTest#take)
  - [unlockCallback](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolTakeTest#unlockcallback)
  - [\_testTake](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolTakeTest#_testtake)
- [Structs](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolTakeTest#structs)
  - [CallbackData](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolTakeTest#callbackdata)