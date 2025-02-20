[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseV4Quoter#)

On this page

# BaseV4Quoter

[Git Source](https://github.com/uniswap/v4-periphery/blob/3f295d8435e4f776ea2daeb96ce1bc6d63f33fc7/src/base/BaseV4Quoter.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:** [SafeCallback](https://docs.uniswap.org/contracts/v4/reference/periphery/base/SafeCallback)

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseV4Quoter\#functions "Direct link to heading")

### constructor [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseV4Quoter\#constructor "Direct link to heading")

```codeBlockLines_mRuA
constructor(IPoolManager _poolManager) SafeCallback(_poolManager);

```

Copy

### selfOnly [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseV4Quoter\#selfonly "Direct link to heading")

_Only this address may call this function. Used to mimic internal functions, using an_
_external call to catch and parse revert reasons_

```codeBlockLines_mRuA
modifier selfOnly();

```

Copy

### \_unlockCallback [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseV4Quoter\#_unlockcallback "Direct link to heading")

```codeBlockLines_mRuA
function _unlockCallback(bytes calldata data) internal override returns (bytes memory);

```

Copy

### \_swap [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseV4Quoter\#_swap "Direct link to heading")

if amountSpecified < 0, the swap is exactInput, otherwise exactOutput

_Execute a swap and return the balance delta_

```codeBlockLines_mRuA
function _swap(PoolKey memory poolKey, bool zeroForOne, int256 amountSpecified, bytes calldata hookData)
    internal
    returns (BalanceDelta swapDelta);

```

Copy

## Errors [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseV4Quoter\#errors "Direct link to heading")

### NotEnoughLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseV4Quoter\#notenoughliquidity "Direct link to heading")

```codeBlockLines_mRuA
error NotEnoughLiquidity(PoolId poolId);

```

Copy

### NotSelf [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseV4Quoter\#notself "Direct link to heading")

```codeBlockLines_mRuA
error NotSelf();

```

Copy

### UnexpectedCallSuccess [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseV4Quoter\#unexpectedcallsuccess "Direct link to heading")

```codeBlockLines_mRuA
error UnexpectedCallSuccess();

```

Copy

- [Functions](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseV4Quoter#functions)
  - [constructor](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseV4Quoter#constructor)
  - [selfOnly](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseV4Quoter#selfonly)
  - [\_unlockCallback](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseV4Quoter#_unlockcallback)
  - [\_swap](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseV4Quoter#_swap)
- [Errors](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseV4Quoter#errors)
  - [NotEnoughLiquidity](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseV4Quoter#notenoughliquidity)
  - [NotSelf](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseV4Quoter#notself)
  - [UnexpectedCallSuccess](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseV4Quoter#unexpectedcallsuccess)