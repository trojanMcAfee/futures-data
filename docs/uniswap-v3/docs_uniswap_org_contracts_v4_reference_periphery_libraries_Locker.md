[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Locker#)

On this page

# Locker

[Git Source](https://github.com/uniswap/v4-periphery/blob/3f295d8435e4f776ea2daeb96ce1bc6d63f33fc7/src/libraries/Locker.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

This is a temporary library that allows us to use transient storage (tstore/tload)
TODO: This library can be deleted when we have the transient keyword support in solidity.

## State Variables [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Locker\#state-variables "Direct link to heading")

### LOCKED\_BY\_SLOT [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Locker\#locked_by_slot "Direct link to heading")

```codeBlockLines_mRuA
bytes32 constant LOCKED_BY_SLOT = 0x0aedd6bde10e3aa2adec092b02a3e3e805795516cda41f27aa145b8f300af87a;

```

Copy

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Locker\#functions "Direct link to heading")

### set [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Locker\#set "Direct link to heading")

```codeBlockLines_mRuA
function set(address locker) internal;

```

Copy

### get [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Locker\#get "Direct link to heading")

```codeBlockLines_mRuA
function get() internal view returns (address locker);

```

Copy

- [State Variables](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Locker#state-variables)
  - [LOCKED\_BY\_SLOT](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Locker#locked_by_slot)
- [Functions](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Locker#functions)
  - [set](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Locker#set)
  - [get](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Locker#get)