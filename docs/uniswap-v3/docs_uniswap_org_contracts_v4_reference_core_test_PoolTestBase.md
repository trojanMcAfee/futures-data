[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolTestBase#)

On this page

# PoolTestBase

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/test/PoolTestBase.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:** [IUnlockCallback](https://docs.uniswap.org/src/interfaces/callback/IUnlockCallback.sol/interface.IUnlockCallback.md)

## State Variables [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolTestBase\#state-variables "Direct link to heading")

### manager [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolTestBase\#manager "Direct link to heading")

```codeBlockLines_mRuA
IPoolManager public immutable manager;

```

Copy

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolTestBase\#functions "Direct link to heading")

### constructor [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolTestBase\#constructor "Direct link to heading")

```codeBlockLines_mRuA
constructor(IPoolManager _manager);

```

Copy

### \_fetchBalances [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolTestBase\#_fetchbalances "Direct link to heading")

```codeBlockLines_mRuA
function _fetchBalances(Currency currency, address user, address deltaHolder)
    internal
    view
    returns (uint256 userBalance, uint256 poolBalance, int256 delta);

```

Copy

- [State Variables](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolTestBase#state-variables)
  - [manager](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolTestBase#manager)
- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolTestBase#functions)
  - [constructor](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolTestBase#constructor)
  - [\_fetchBalances](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolTestBase#_fetchbalances)