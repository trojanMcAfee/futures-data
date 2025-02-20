[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/periphery/base/NativeWrapper#)

On this page

# NativeWrapper

[Git Source](https://github.com/uniswap/v4-periphery/blob/3f295d8435e4f776ea2daeb96ce1bc6d63f33fc7/src/base/NativeWrapper.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:** [ImmutableState](https://docs.uniswap.org/contracts/v4/reference/periphery/base/ImmutableState)

Used for wrapping and unwrapping native

## State Variables [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/NativeWrapper\#state-variables "Direct link to heading")

### WETH9 [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/NativeWrapper\#weth9 "Direct link to heading")

The address for WETH9

```codeBlockLines_mRuA
IWETH9 public immutable WETH9;

```

Copy

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/NativeWrapper\#functions "Direct link to heading")

### constructor [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/NativeWrapper\#constructor "Direct link to heading")

```codeBlockLines_mRuA
constructor(IWETH9 _weth9);

```

Copy

### \_wrap [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/NativeWrapper\#_wrap "Direct link to heading")

_The amount should already be <= the current balance in this contract._

```codeBlockLines_mRuA
function _wrap(uint256 amount) internal;

```

Copy

### \_unwrap [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/NativeWrapper\#_unwrap "Direct link to heading")

_The amount should already be <= the current balance in this contract._

```codeBlockLines_mRuA
function _unwrap(uint256 amount) internal;

```

Copy

### receive [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/NativeWrapper\#receive "Direct link to heading")

```codeBlockLines_mRuA
receive() external payable;

```

Copy

## Errors [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/NativeWrapper\#errors "Direct link to heading")

### InvalidEthSender [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/NativeWrapper\#invalidethsender "Direct link to heading")

Thrown when an unexpected address sends ETH to this contract

```codeBlockLines_mRuA
error InvalidEthSender();

```

Copy

- [State Variables](https://docs.uniswap.org/contracts/v4/reference/periphery/base/NativeWrapper#state-variables)
  - [WETH9](https://docs.uniswap.org/contracts/v4/reference/periphery/base/NativeWrapper#weth9)
- [Functions](https://docs.uniswap.org/contracts/v4/reference/periphery/base/NativeWrapper#functions)
  - [constructor](https://docs.uniswap.org/contracts/v4/reference/periphery/base/NativeWrapper#constructor)
  - [\_wrap](https://docs.uniswap.org/contracts/v4/reference/periphery/base/NativeWrapper#_wrap)
  - [\_unwrap](https://docs.uniswap.org/contracts/v4/reference/periphery/base/NativeWrapper#_unwrap)
  - [receive](https://docs.uniswap.org/contracts/v4/reference/periphery/base/NativeWrapper#receive)
- [Errors](https://docs.uniswap.org/contracts/v4/reference/periphery/base/NativeWrapper#errors)
  - [InvalidEthSender](https://docs.uniswap.org/contracts/v4/reference/periphery/base/NativeWrapper#invalidethsender)