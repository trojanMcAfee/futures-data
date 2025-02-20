[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/libraries/NonzeroDeltaCount#)

On this page

# NonzeroDeltaCount

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/libraries/NonzeroDeltaCount.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

This is a temporary library that allows us to use transient storage (tstore/tload)
for the nonzero delta count.
TODO: This library can be deleted when we have the transient keyword support in solidity.

## State Variables [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/NonzeroDeltaCount\#state-variables "Direct link to heading")

### NONZERO\_DELTA\_COUNT\_SLOT [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/NonzeroDeltaCount\#nonzero_delta_count_slot "Direct link to heading")

```codeBlockLines_mRuA
bytes32 internal constant NONZERO_DELTA_COUNT_SLOT = 0x7d4b3164c6e45b97e7d87b7125a44c5828d005af88f9d751cfd78729c5d99a0b;

```

Copy

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/NonzeroDeltaCount\#functions "Direct link to heading")

### read [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/NonzeroDeltaCount\#read "Direct link to heading")

```codeBlockLines_mRuA
function read() internal view returns (uint256 count);

```

Copy

### increment [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/NonzeroDeltaCount\#increment "Direct link to heading")

```codeBlockLines_mRuA
function increment() internal;

```

Copy

### decrement [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/NonzeroDeltaCount\#decrement "Direct link to heading")

Potential to underflow. Ensure checks are performed by integrating contracts to ensure this does not happen.
Current usage ensures this will not happen because we call decrement with known boundaries (only up to the number of times we call increment).

```codeBlockLines_mRuA
function decrement() internal;

```

Copy

- [State Variables](https://docs.uniswap.org/contracts/v4/reference/core/libraries/NonzeroDeltaCount#state-variables)
  - [NONZERO\_DELTA\_COUNT\_SLOT](https://docs.uniswap.org/contracts/v4/reference/core/libraries/NonzeroDeltaCount#nonzero_delta_count_slot)
- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/libraries/NonzeroDeltaCount#functions)
  - [read](https://docs.uniswap.org/contracts/v4/reference/core/libraries/NonzeroDeltaCount#read)
  - [increment](https://docs.uniswap.org/contracts/v4/reference/core/libraries/NonzeroDeltaCount#increment)
  - [decrement](https://docs.uniswap.org/contracts/v4/reference/core/libraries/NonzeroDeltaCount#decrement)