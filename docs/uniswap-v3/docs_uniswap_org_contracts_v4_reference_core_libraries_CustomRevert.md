[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/libraries/CustomRevert#)

On this page

# CustomRevert

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/libraries/CustomRevert.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

Contains functions for reverting with custom errors with different argument types efficiently

_To use this library, declare `using CustomRevert for bytes4;` and replace `revert CustomError()` with_
_`CustomError.selector.revertWith()`_

_The functions may tamper with the free memory pointer but it is fine since the call context is exited immediately_

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/CustomRevert\#functions "Direct link to heading")

### revertWith [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/CustomRevert\#revertwith "Direct link to heading")

_Reverts with the selector of a custom error in the scratch space_

```codeBlockLines_mRuA
function revertWith(bytes4 selector) internal pure;

```

Copy

### revertWith [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/CustomRevert\#revertwith-1 "Direct link to heading")

_Reverts with a custom error with an address argument in the scratch space_

```codeBlockLines_mRuA
function revertWith(bytes4 selector, address addr) internal pure;

```

Copy

### revertWith [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/CustomRevert\#revertwith-2 "Direct link to heading")

_Reverts with a custom error with an int24 argument in the scratch space_

```codeBlockLines_mRuA
function revertWith(bytes4 selector, int24 value) internal pure;

```

Copy

### revertWith [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/CustomRevert\#revertwith-3 "Direct link to heading")

_Reverts with a custom error with a uint160 argument in the scratch space_

```codeBlockLines_mRuA
function revertWith(bytes4 selector, uint160 value) internal pure;

```

Copy

### revertWith [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/CustomRevert\#revertwith-4 "Direct link to heading")

_Reverts with a custom error with two int24 arguments_

```codeBlockLines_mRuA
function revertWith(bytes4 selector, int24 value1, int24 value2) internal pure;

```

Copy

### revertWith [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/CustomRevert\#revertwith-5 "Direct link to heading")

_Reverts with a custom error with two uint160 arguments_

```codeBlockLines_mRuA
function revertWith(bytes4 selector, uint160 value1, uint160 value2) internal pure;

```

Copy

### revertWith [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/CustomRevert\#revertwith-6 "Direct link to heading")

_Reverts with a custom error with two address arguments_

```codeBlockLines_mRuA
function revertWith(bytes4 selector, address value1, address value2) internal pure;

```

Copy

### bubbleUpAndRevertWith [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/CustomRevert\#bubbleupandrevertwith "Direct link to heading")

bubble up the revert message returned by a call and revert with a wrapped ERC-7751 error

_this method can be vulnerable to revert data bombs_

```codeBlockLines_mRuA
function bubbleUpAndRevertWith(address revertingContract, bytes4 revertingFunctionSelector, bytes4 additionalContext)
    internal
    pure;

```

Copy

## Errors [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/CustomRevert\#errors "Direct link to heading")

### WrappedError [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/CustomRevert\#wrappederror "Direct link to heading")

_ERC-7751 error for wrapping bubbled up reverts_

```codeBlockLines_mRuA
error WrappedError(address target, bytes4 selector, bytes reason, bytes details);

```

Copy

- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/libraries/CustomRevert#functions)
  - [revertWith](https://docs.uniswap.org/contracts/v4/reference/core/libraries/CustomRevert#revertwith)
  - [revertWith](https://docs.uniswap.org/contracts/v4/reference/core/libraries/CustomRevert#revertwith-1)
  - [revertWith](https://docs.uniswap.org/contracts/v4/reference/core/libraries/CustomRevert#revertwith-2)
  - [revertWith](https://docs.uniswap.org/contracts/v4/reference/core/libraries/CustomRevert#revertwith-3)
  - [revertWith](https://docs.uniswap.org/contracts/v4/reference/core/libraries/CustomRevert#revertwith-4)
  - [revertWith](https://docs.uniswap.org/contracts/v4/reference/core/libraries/CustomRevert#revertwith-5)
  - [revertWith](https://docs.uniswap.org/contracts/v4/reference/core/libraries/CustomRevert#revertwith-6)
  - [bubbleUpAndRevertWith](https://docs.uniswap.org/contracts/v4/reference/core/libraries/CustomRevert#bubbleupandrevertwith)
- [Errors](https://docs.uniswap.org/contracts/v4/reference/core/libraries/CustomRevert#errors)
  - [WrappedError](https://docs.uniswap.org/contracts/v4/reference/core/libraries/CustomRevert#wrappederror)