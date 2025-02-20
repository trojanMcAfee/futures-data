[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolDonateTest#)

On this page

# PoolDonateTest

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/test/PoolDonateTest.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:** [PoolTestBase](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolTestBase)

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolDonateTest\#functions "Direct link to heading")

### constructor [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolDonateTest\#constructor "Direct link to heading")

```codeBlockLines_mRuA
constructor(IPoolManager _manager) PoolTestBase(_manager);

```

Copy

### donate [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolDonateTest\#donate "Direct link to heading")

```codeBlockLines_mRuA
function donate(PoolKey memory key, uint256 amount0, uint256 amount1, bytes memory hookData)
    external
    payable
    returns (BalanceDelta delta);

```

Copy

### unlockCallback [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolDonateTest\#unlockcallback "Direct link to heading")

```codeBlockLines_mRuA
function unlockCallback(bytes calldata rawData) external returns (bytes memory);

```

Copy

## Structs [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolDonateTest\#structs "Direct link to heading")

### CallbackData [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolDonateTest\#callbackdata "Direct link to heading")

```codeBlockLines_mRuA
struct CallbackData {
    address sender;
    PoolKey key;
    uint256 amount0;
    uint256 amount1;
    bytes hookData;
}

```

Copy

- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolDonateTest#functions)
  - [constructor](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolDonateTest#constructor)
  - [donate](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolDonateTest#donate)
  - [unlockCallback](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolDonateTest#unlockcallback)
- [Structs](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolDonateTest#structs)
  - [CallbackData](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolDonateTest#callbackdata)