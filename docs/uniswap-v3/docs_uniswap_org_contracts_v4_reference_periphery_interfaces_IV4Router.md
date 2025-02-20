[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IV4Router#)

On this page

# IV4Router

[Git Source](https://github.com/uniswap/v4-periphery/blob/3f295d8435e4f776ea2daeb96ce1bc6d63f33fc7/src/interfaces/IV4Router.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:** [IImmutableState](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IImmutableState)

Interface containing all the structs and errors for different v4 swap types

## Errors [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IV4Router\#errors "Direct link to heading")

### V4TooLittleReceived [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IV4Router\#v4toolittlereceived "Direct link to heading")

Emitted when an exactInput swap does not receive its minAmountOut

```codeBlockLines_mRuA
error V4TooLittleReceived(uint256 minAmountOutReceived, uint256 amountReceived);

```

Copy

### V4TooMuchRequested [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IV4Router\#v4toomuchrequested "Direct link to heading")

Emitted when an exactOutput is asked for more than its maxAmountIn

```codeBlockLines_mRuA
error V4TooMuchRequested(uint256 maxAmountInRequested, uint256 amountRequested);

```

Copy

## Structs [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IV4Router\#structs "Direct link to heading")

### ExactInputSingleParams [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IV4Router\#exactinputsingleparams "Direct link to heading")

Parameters for a single-hop exact-input swap

```codeBlockLines_mRuA
struct ExactInputSingleParams {
    PoolKey poolKey;
    bool zeroForOne;
    uint128 amountIn;
    uint128 amountOutMinimum;
    bytes hookData;
}

```

Copy

### ExactInputParams [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IV4Router\#exactinputparams "Direct link to heading")

Parameters for a multi-hop exact-input swap

```codeBlockLines_mRuA
struct ExactInputParams {
    Currency currencyIn;
    PathKey[] path;
    uint128 amountIn;
    uint128 amountOutMinimum;
}

```

Copy

### ExactOutputSingleParams [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IV4Router\#exactoutputsingleparams "Direct link to heading")

Parameters for a single-hop exact-output swap

```codeBlockLines_mRuA
struct ExactOutputSingleParams {
    PoolKey poolKey;
    bool zeroForOne;
    uint128 amountOut;
    uint128 amountInMaximum;
    bytes hookData;
}

```

Copy

### ExactOutputParams [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IV4Router\#exactoutputparams "Direct link to heading")

Parameters for a multi-hop exact-output swap

```codeBlockLines_mRuA
struct ExactOutputParams {
    Currency currencyOut;
    PathKey[] path;
    uint128 amountOut;
    uint128 amountInMaximum;
}

```

Copy

- [Errors](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IV4Router#errors)
  - [V4TooLittleReceived](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IV4Router#v4toolittlereceived)
  - [V4TooMuchRequested](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IV4Router#v4toomuchrequested)
- [Structs](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IV4Router#structs)
  - [ExactInputSingleParams](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IV4Router#exactinputsingleparams)
  - [ExactInputParams](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IV4Router#exactinputparams)
  - [ExactOutputSingleParams](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IV4Router#exactoutputsingleparams)
  - [ExactOutputParams](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IV4Router#exactoutputparams)