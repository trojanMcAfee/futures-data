[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/test/ProtocolFeesImplementation#)

On this page

# ProtocolFeesImplementation

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/test/ProtocolFeesImplementation.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:** [ProtocolFees](https://docs.uniswap.org/contracts/v4/reference/core/ProtocolFees)

## State Variables [​](https://docs.uniswap.org/contracts/v4/reference/core/test/ProtocolFeesImplementation\#state-variables "Direct link to heading")

### \_pools [​](https://docs.uniswap.org/contracts/v4/reference/core/test/ProtocolFeesImplementation\#_pools "Direct link to heading")

```codeBlockLines_mRuA
mapping(PoolId id => Pool.State) internal _pools;

```

Copy

### isUnlocked [​](https://docs.uniswap.org/contracts/v4/reference/core/test/ProtocolFeesImplementation\#isunlocked "Direct link to heading")

```codeBlockLines_mRuA
bool internal isUnlocked;

```

Copy

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/test/ProtocolFeesImplementation\#functions "Direct link to heading")

### constructor [​](https://docs.uniswap.org/contracts/v4/reference/core/test/ProtocolFeesImplementation\#constructor "Direct link to heading")

```codeBlockLines_mRuA
constructor() ProtocolFees(msg.sender);

```

Copy

### setPrice [​](https://docs.uniswap.org/contracts/v4/reference/core/test/ProtocolFeesImplementation\#setprice "Direct link to heading")

```codeBlockLines_mRuA
function setPrice(PoolKey memory key, uint160 sqrtPriceX96) public;

```

Copy

### \_getPool [​](https://docs.uniswap.org/contracts/v4/reference/core/test/ProtocolFeesImplementation\#_getpool "Direct link to heading")

```codeBlockLines_mRuA
function _getPool(PoolId id) internal view override returns (Pool.State storage);

```

Copy

### setIsUnlocked [​](https://docs.uniswap.org/contracts/v4/reference/core/test/ProtocolFeesImplementation\#setisunlocked "Direct link to heading")

```codeBlockLines_mRuA
function setIsUnlocked(bool newValue) public;

```

Copy

### \_isUnlocked [​](https://docs.uniswap.org/contracts/v4/reference/core/test/ProtocolFeesImplementation\#_isunlocked "Direct link to heading")

```codeBlockLines_mRuA
function _isUnlocked() internal view override returns (bool);

```

Copy

### updateProtocolFees [​](https://docs.uniswap.org/contracts/v4/reference/core/test/ProtocolFeesImplementation\#updateprotocolfees "Direct link to heading")

```codeBlockLines_mRuA
function updateProtocolFees(Currency currency, uint256 amount) public;

```

Copy

- [State Variables](https://docs.uniswap.org/contracts/v4/reference/core/test/ProtocolFeesImplementation#state-variables)
  - [\_pools](https://docs.uniswap.org/contracts/v4/reference/core/test/ProtocolFeesImplementation#_pools)
  - [isUnlocked](https://docs.uniswap.org/contracts/v4/reference/core/test/ProtocolFeesImplementation#isunlocked)
- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/test/ProtocolFeesImplementation#functions)
  - [constructor](https://docs.uniswap.org/contracts/v4/reference/core/test/ProtocolFeesImplementation#constructor)
  - [setPrice](https://docs.uniswap.org/contracts/v4/reference/core/test/ProtocolFeesImplementation#setprice)
  - [\_getPool](https://docs.uniswap.org/contracts/v4/reference/core/test/ProtocolFeesImplementation#_getpool)
  - [setIsUnlocked](https://docs.uniswap.org/contracts/v4/reference/core/test/ProtocolFeesImplementation#setisunlocked)
  - [\_isUnlocked](https://docs.uniswap.org/contracts/v4/reference/core/test/ProtocolFeesImplementation#_isunlocked)
  - [updateProtocolFees](https://docs.uniswap.org/contracts/v4/reference/core/test/ProtocolFeesImplementation#updateprotocolfees)