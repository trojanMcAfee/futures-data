[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/periphery/base/ImmutableState#)

On this page

# ImmutableState

[Git Source](https://github.com/uniswap/v4-periphery/blob/3f295d8435e4f776ea2daeb96ce1bc6d63f33fc7/src/base/ImmutableState.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:** [IImmutableState](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IImmutableState)

A collection of immutable state variables, commonly used across multiple contracts

## State Variables [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/ImmutableState\#state-variables "Direct link to heading")

### poolManager [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/ImmutableState\#poolmanager "Direct link to heading")

The Uniswap v4 PoolManager contract

```codeBlockLines_mRuA
IPoolManager public immutable poolManager;

```

Copy

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/ImmutableState\#functions "Direct link to heading")

### constructor [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/ImmutableState\#constructor "Direct link to heading")

```codeBlockLines_mRuA
constructor(IPoolManager _poolManager);

```

Copy

- [State Variables](https://docs.uniswap.org/contracts/v4/reference/periphery/base/ImmutableState#state-variables)
  - [poolManager](https://docs.uniswap.org/contracts/v4/reference/periphery/base/ImmutableState#poolmanager)
- [Functions](https://docs.uniswap.org/contracts/v4/reference/periphery/base/ImmutableState#functions)
  - [constructor](https://docs.uniswap.org/contracts/v4/reference/periphery/base/ImmutableState#constructor)