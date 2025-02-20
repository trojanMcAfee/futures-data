[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/NoDelegateCall#)

On this page

# NoDelegateCall

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/NoDelegateCall.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

Base contract that provides a modifier for preventing delegatecall to methods in a child contract

## State Variables [​](https://docs.uniswap.org/contracts/v4/reference/core/NoDelegateCall\#state-variables "Direct link to heading")

### original [​](https://docs.uniswap.org/contracts/v4/reference/core/NoDelegateCall\#original "Direct link to heading")

_The original address of this contract_

```codeBlockLines_mRuA
address private immutable original;

```

Copy

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/NoDelegateCall\#functions "Direct link to heading")

### constructor [​](https://docs.uniswap.org/contracts/v4/reference/core/NoDelegateCall\#constructor "Direct link to heading")

```codeBlockLines_mRuA
constructor();

```

Copy

### checkNotDelegateCall [​](https://docs.uniswap.org/contracts/v4/reference/core/NoDelegateCall\#checknotdelegatecall "Direct link to heading")

_Private method is used instead of inlining into modifier because modifiers are copied into each method,_
_and the use of immutable means the address bytes are copied in every place the modifier is used._

```codeBlockLines_mRuA
function checkNotDelegateCall() private view;

```

Copy

### noDelegateCall [​](https://docs.uniswap.org/contracts/v4/reference/core/NoDelegateCall\#nodelegatecall-1 "Direct link to heading")

Prevents delegatecall into the modified method

```codeBlockLines_mRuA
modifier noDelegateCall();

```

Copy

## Errors [​](https://docs.uniswap.org/contracts/v4/reference/core/NoDelegateCall\#errors "Direct link to heading")

### DelegateCallNotAllowed [​](https://docs.uniswap.org/contracts/v4/reference/core/NoDelegateCall\#delegatecallnotallowed "Direct link to heading")

```codeBlockLines_mRuA
error DelegateCallNotAllowed();

```

Copy

- [State Variables](https://docs.uniswap.org/contracts/v4/reference/core/NoDelegateCall#state-variables)
  - [original](https://docs.uniswap.org/contracts/v4/reference/core/NoDelegateCall#original)
- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/NoDelegateCall#functions)
  - [constructor](https://docs.uniswap.org/contracts/v4/reference/core/NoDelegateCall#constructor)
  - [checkNotDelegateCall](https://docs.uniswap.org/contracts/v4/reference/core/NoDelegateCall#checknotdelegatecall)
  - [noDelegateCall](https://docs.uniswap.org/contracts/v4/reference/core/NoDelegateCall#nodelegatecall-1)
- [Errors](https://docs.uniswap.org/contracts/v4/reference/core/NoDelegateCall#errors)
  - [DelegateCallNotAllowed](https://docs.uniswap.org/contracts/v4/reference/core/NoDelegateCall#delegatecallnotallowed)