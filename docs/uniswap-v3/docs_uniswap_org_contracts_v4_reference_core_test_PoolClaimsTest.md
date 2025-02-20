[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolClaimsTest#)

On this page

# PoolClaimsTest

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/test/PoolClaimsTest.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:** [PoolTestBase](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolTestBase)

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolClaimsTest\#functions "Direct link to heading")

### constructor [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolClaimsTest\#constructor "Direct link to heading")

```codeBlockLines_mRuA
constructor(IPoolManager _manager) PoolTestBase(_manager);

```

Copy

### deposit [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolClaimsTest\#deposit "Direct link to heading")

Convert ERC20 into a claimable 6909

```codeBlockLines_mRuA
function deposit(Currency currency, address user, uint256 amount) external payable;

```

Copy

### withdraw [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolClaimsTest\#withdraw "Direct link to heading")

Redeem claimable 6909 for ERC20

```codeBlockLines_mRuA
function withdraw(Currency currency, address user, uint256 amount) external payable;

```

Copy

### unlockCallback [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolClaimsTest\#unlockcallback "Direct link to heading")

```codeBlockLines_mRuA
function unlockCallback(bytes calldata rawData) external returns (bytes memory);

```

Copy

## Structs [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolClaimsTest\#structs "Direct link to heading")

### CallbackData [​](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolClaimsTest\#callbackdata "Direct link to heading")

```codeBlockLines_mRuA
struct CallbackData {
    address sender;
    address user;
    Currency currency;
    uint256 amount;
    bool deposit;
}

```

Copy

- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolClaimsTest#functions)
  - [constructor](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolClaimsTest#constructor)
  - [deposit](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolClaimsTest#deposit)
  - [withdraw](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolClaimsTest#withdraw)
  - [unlockCallback](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolClaimsTest#unlockcallback)
- [Structs](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolClaimsTest#structs)
  - [CallbackData](https://docs.uniswap.org/contracts/v4/reference/core/test/PoolClaimsTest#callbackdata)