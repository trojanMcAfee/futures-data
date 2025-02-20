[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolEmptyUnlockTest#)

On this page

# PoolEmptyUnlockTest

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/test/PoolEmptyUnlockTest.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:** [IUnlockCallback](https://docs.uniswap.org/src/interfaces/callback/IUnlockCallback.sol/interface.IUnlockCallback.md)

## State Variables [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolEmptyUnlockTest\#state-variables "Direct link to heading")

### manager [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolEmptyUnlockTest\#manager "Direct link to heading")

```codeBlockLines_mRuA
IPoolManager manager;

```

Copy

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolEmptyUnlockTest\#functions "Direct link to heading")

### constructor [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolEmptyUnlockTest\#constructor "Direct link to heading")

```codeBlockLines_mRuA
constructor(IPoolManager _manager);

```

Copy

### unlock [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolEmptyUnlockTest\#unlock "Direct link to heading")

```codeBlockLines_mRuA
function unlock() external;

```

Copy

### unlockCallback [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolEmptyUnlockTest\#unlockcallback "Direct link to heading")

Called by the pool manager on `msg.sender` when the manager is unlocked

```codeBlockLines_mRuA
function unlockCallback(bytes calldata) external override returns (bytes memory);

```

Copy

## Events [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolEmptyUnlockTest\#events "Direct link to heading")

### UnlockCallback [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolEmptyUnlockTest\#unlockcallback-1 "Direct link to heading")

```codeBlockLines_mRuA
event UnlockCallback();

```

Copy

- [State Variables](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolEmptyUnlockTest#state-variables)
  - [manager](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolEmptyUnlockTest#manager)
- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolEmptyUnlockTest#functions)
  - [constructor](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolEmptyUnlockTest#constructor)
  - [unlock](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolEmptyUnlockTest#unlock)
  - [unlockCallback](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolEmptyUnlockTest#unlockcallback)
- [Events](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolEmptyUnlockTest#events)
  - [UnlockCallback](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolEmptyUnlockTest#unlockcallback-1)