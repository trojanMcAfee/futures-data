[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/periphery/V4Router#)

On this page

# V4Router

[Git Source](https://github.com/uniswap/v4-periphery/blob/3f295d8435e4f776ea2daeb96ce1bc6d63f33fc7/src/V4Router.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:** [IV4Router](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IV4Router), [BaseActionsRouter](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseActionsRouter), [DeltaResolver](https://docs.uniswap.org/contracts/v4/reference/periphery/base/DeltaResolver)

Abstract contract that contains all internal logic needed for routing through Uniswap v4 pools

_the entry point to executing actions in this contract is calling `BaseActionsRouter._executeActions`_
_An inheriting contract should call \_executeActions at the point that they wish actions to be executed_

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/periphery/V4Router\#functions "Direct link to heading")

### constructor [​](https://docs.uniswap.org/contracts/v4/reference/periphery/V4Router\#constructor "Direct link to heading")

```codeBlockLines_mRuA
constructor(IPoolManager _poolManager) BaseActionsRouter(_poolManager);

```

Copy

### \_handleAction [​](https://docs.uniswap.org/contracts/v4/reference/periphery/V4Router\#_handleaction "Direct link to heading")

```codeBlockLines_mRuA
function _handleAction(uint256 action, bytes calldata params) internal override;

```

Copy

### \_swapExactInputSingle [​](https://docs.uniswap.org/contracts/v4/reference/periphery/V4Router\#_swapexactinputsingle "Direct link to heading")

```codeBlockLines_mRuA
function _swapExactInputSingle(IV4Router.ExactInputSingleParams calldata params) private;

```

Copy

### \_swapExactInput [​](https://docs.uniswap.org/contracts/v4/reference/periphery/V4Router\#_swapexactinput "Direct link to heading")

```codeBlockLines_mRuA
function _swapExactInput(IV4Router.ExactInputParams calldata params) private;

```

Copy

### \_swapExactOutputSingle [​](https://docs.uniswap.org/contracts/v4/reference/periphery/V4Router\#_swapexactoutputsingle "Direct link to heading")

```codeBlockLines_mRuA
function _swapExactOutputSingle(IV4Router.ExactOutputSingleParams calldata params) private;

```

Copy

### \_swapExactOutput [​](https://docs.uniswap.org/contracts/v4/reference/periphery/V4Router\#_swapexactoutput "Direct link to heading")

```codeBlockLines_mRuA
function _swapExactOutput(IV4Router.ExactOutputParams calldata params) private;

```

Copy

### \_swap [​](https://docs.uniswap.org/contracts/v4/reference/periphery/V4Router\#_swap "Direct link to heading")

```codeBlockLines_mRuA
function _swap(PoolKey memory poolKey, bool zeroForOne, int256 amountSpecified, bytes calldata hookData)
    private
    returns (int128 reciprocalAmount);

```

Copy

- [Functions](https://docs.uniswap.org/contracts/v4/reference/periphery/V4Router#functions)
  - [constructor](https://docs.uniswap.org/contracts/v4/reference/periphery/V4Router#constructor)
  - [\_handleAction](https://docs.uniswap.org/contracts/v4/reference/periphery/V4Router#_handleaction)
  - [\_swapExactInputSingle](https://docs.uniswap.org/contracts/v4/reference/periphery/V4Router#_swapexactinputsingle)
  - [\_swapExactInput](https://docs.uniswap.org/contracts/v4/reference/periphery/V4Router#_swapexactinput)
  - [\_swapExactOutputSingle](https://docs.uniswap.org/contracts/v4/reference/periphery/V4Router#_swapexactoutputsingle)
  - [\_swapExactOutput](https://docs.uniswap.org/contracts/v4/reference/periphery/V4Router#_swapexactoutput)
  - [\_swap](https://docs.uniswap.org/contracts/v4/reference/periphery/V4Router#_swap)