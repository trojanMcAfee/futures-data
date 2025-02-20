[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Lock#)

On this page

# Lock

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/libraries/Lock.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

This is a temporary library that allows us to use transient storage (tstore/tload)
TODO: This library can be deleted when we have the transient keyword support in solidity.

## State Variables [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Lock\#state-variables "Direct link to heading")

### IS\_UNLOCKED\_SLOT [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Lock\#is_unlocked_slot "Direct link to heading")

```codeBlockLines_mRuA
bytes32 internal constant IS_UNLOCKED_SLOT = 0xc090fc4683624cfc3884e9d8de5eca132f2d0ec062aff75d43c0465d5ceeab23;

```

Copy

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Lock\#functions "Direct link to heading")

### unlock [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Lock\#unlock "Direct link to heading")

```codeBlockLines_mRuA
function unlock() internal;

```

Copy

### lock [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Lock\#lock-1 "Direct link to heading")

```codeBlockLines_mRuA
function lock() internal;

```

Copy

### isUnlocked [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Lock\#isunlocked "Direct link to heading")

```codeBlockLines_mRuA
function isUnlocked() internal view returns (bool unlocked);

```

Copy

- [State Variables](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Lock#state-variables)
  - [IS\_UNLOCKED\_SLOT](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Lock#is_unlocked_slot)
- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Lock#functions)
  - [unlock](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Lock#unlock)
  - [lock](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Lock#lock-1)
  - [isUnlocked](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Lock#isunlocked)