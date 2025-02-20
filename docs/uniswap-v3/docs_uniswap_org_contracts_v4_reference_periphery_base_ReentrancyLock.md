[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/periphery/base/ReentrancyLock#)

On this page

# ReentrancyLock

[Git Source](https://github.com/uniswap/v4-periphery/blob/3f295d8435e4f776ea2daeb96ce1bc6d63f33fc7/src/base/ReentrancyLock.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

A transient reentrancy lock, that stores the caller's address as the lock

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/ReentrancyLock\#functions "Direct link to heading")

### isNotLocked [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/ReentrancyLock\#isnotlocked "Direct link to heading")

```codeBlockLines_mRuA
modifier isNotLocked();

```

Copy

### \_getLocker [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/ReentrancyLock\#_getlocker "Direct link to heading")

```codeBlockLines_mRuA
function _getLocker() internal view returns (address);

```

Copy

## Errors [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/ReentrancyLock\#errors "Direct link to heading")

### ContractLocked [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/ReentrancyLock\#contractlocked "Direct link to heading")

```codeBlockLines_mRuA
error ContractLocked();

```

Copy

- [Functions](https://docs.uniswap.org/contracts/v4/reference/periphery/base/ReentrancyLock#functions)
  - [isNotLocked](https://docs.uniswap.org/contracts/v4/reference/periphery/base/ReentrancyLock#isnotlocked)
  - [\_getLocker](https://docs.uniswap.org/contracts/v4/reference/periphery/base/ReentrancyLock#_getlocker)
- [Errors](https://docs.uniswap.org/contracts/v4/reference/periphery/base/ReentrancyLock#errors)
  - [ContractLocked](https://docs.uniswap.org/contracts/v4/reference/periphery/base/ReentrancyLock#contractlocked)