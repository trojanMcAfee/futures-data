[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CalldataDecoder#)

On this page

# CalldataDecoder

[Git Source](https://github.com/uniswap/v4-periphery/blob/3f295d8435e4f776ea2daeb96ce1bc6d63f33fc7/src/libraries/CalldataDecoder.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

## State Variables [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CalldataDecoder\#state-variables "Direct link to heading")

### OFFSET\_OR\_LENGTH\_MASK [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CalldataDecoder\#offset_or_length_mask "Direct link to heading")

mask used for offsets and lengths to ensure no overflow

_no sane abi encoding will pass in an offset or length greater than type(uint32).max_
_(note that this does deviate from standard solidity behavior and offsets/lengths will_
_be interpreted as mod type(uint32).max which will only impact malicious/buggy callers)_

```codeBlockLines_mRuA
uint256 constant OFFSET_OR_LENGTH_MASK = 0xffffffff;

```

Copy

### OFFSET\_OR\_LENGTH\_MASK\_AND\_WORD\_ALIGN [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CalldataDecoder\#offset_or_length_mask_and_word_align "Direct link to heading")

```codeBlockLines_mRuA
uint256 constant OFFSET_OR_LENGTH_MASK_AND_WORD_ALIGN = 0xffffffe0;

```

Copy

### SLICE\_ERROR\_SELECTOR [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CalldataDecoder\#slice_error_selector "Direct link to heading")

equivalent to SliceOutOfBounds.selector, stored in least-significant bits

```codeBlockLines_mRuA
uint256 constant SLICE_ERROR_SELECTOR = 0x3b99b53d;

```

Copy

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CalldataDecoder\#functions "Direct link to heading")

### decodeActionsRouterParams [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CalldataDecoder\#decodeactionsrouterparams "Direct link to heading")

_equivalent to: abi.decode(params, (bytes, bytes\[\])) in calldata (requires strict abi encoding)_

```codeBlockLines_mRuA
function decodeActionsRouterParams(bytes calldata _bytes)
    internal
    pure
    returns (bytes calldata actions, bytes[] calldata params);

```

Copy

### decodeModifyLiquidityParams [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CalldataDecoder\#decodemodifyliquidityparams "Direct link to heading")

_equivalent to: abi.decode(params, (uint256, uint256, uint128, uint128, bytes)) in calldata_

```codeBlockLines_mRuA
function decodeModifyLiquidityParams(bytes calldata params)
    internal
    pure
    returns (uint256 tokenId, uint256 liquidity, uint128 amount0, uint128 amount1, bytes calldata hookData);

```

Copy

### decodeMintParams [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CalldataDecoder\#decodemintparams "Direct link to heading")

_equivalent to: abi.decode(params, (PoolKey, int24, int24, uint256, uint128, uint128, address, bytes)) in calldata_

```codeBlockLines_mRuA
function decodeMintParams(bytes calldata params)
    internal
    pure
    returns (
        PoolKey calldata poolKey,
        int24 tickLower,
        int24 tickUpper,
        uint256 liquidity,
        uint128 amount0Max,
        uint128 amount1Max,
        address owner,
        bytes calldata hookData
    );

```

Copy

### decodeBurnParams [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CalldataDecoder\#decodeburnparams "Direct link to heading")

_equivalent to: abi.decode(params, (uint256, uint128, uint128, bytes)) in calldata_

```codeBlockLines_mRuA
function decodeBurnParams(bytes calldata params)
    internal
    pure
    returns (uint256 tokenId, uint128 amount0Min, uint128 amount1Min, bytes calldata hookData);

```

Copy

### decodeSwapExactInParams [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CalldataDecoder\#decodeswapexactinparams "Direct link to heading")

_equivalent to: abi.decode(params, (IV4Router.ExactInputParams))_

```codeBlockLines_mRuA
function decodeSwapExactInParams(bytes calldata params)
    internal
    pure
    returns (IV4Router.ExactInputParams calldata swapParams);

```

Copy

### decodeSwapExactInSingleParams [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CalldataDecoder\#decodeswapexactinsingleparams "Direct link to heading")

_equivalent to: abi.decode(params, (IV4Router.ExactInputSingleParams))_

```codeBlockLines_mRuA
function decodeSwapExactInSingleParams(bytes calldata params)
    internal
    pure
    returns (IV4Router.ExactInputSingleParams calldata swapParams);

```

Copy

### decodeSwapExactOutParams [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CalldataDecoder\#decodeswapexactoutparams "Direct link to heading")

_equivalent to: abi.decode(params, (IV4Router.ExactOutputParams))_

```codeBlockLines_mRuA
function decodeSwapExactOutParams(bytes calldata params)
    internal
    pure
    returns (IV4Router.ExactOutputParams calldata swapParams);

```

Copy

### decodeSwapExactOutSingleParams [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CalldataDecoder\#decodeswapexactoutsingleparams "Direct link to heading")

_equivalent to: abi.decode(params, (IV4Router.ExactOutputSingleParams))_

```codeBlockLines_mRuA
function decodeSwapExactOutSingleParams(bytes calldata params)
    internal
    pure
    returns (IV4Router.ExactOutputSingleParams calldata swapParams);

```

Copy

### decodeCurrency [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CalldataDecoder\#decodecurrency "Direct link to heading")

_equivalent to: abi.decode(params, (Currency)) in calldata_

```codeBlockLines_mRuA
function decodeCurrency(bytes calldata params) internal pure returns (Currency currency);

```

Copy

### decodeCurrencyPair [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CalldataDecoder\#decodecurrencypair "Direct link to heading")

_equivalent to: abi.decode(params, (Currency, Currency)) in calldata_

```codeBlockLines_mRuA
function decodeCurrencyPair(bytes calldata params) internal pure returns (Currency currency0, Currency currency1);

```

Copy

### decodeCurrencyPairAndAddress [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CalldataDecoder\#decodecurrencypairandaddress "Direct link to heading")

_equivalent to: abi.decode(params, (Currency, Currency, address)) in calldata_

```codeBlockLines_mRuA
function decodeCurrencyPairAndAddress(bytes calldata params)
    internal
    pure
    returns (Currency currency0, Currency currency1, address _address);

```

Copy

### decodeCurrencyAndAddress [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CalldataDecoder\#decodecurrencyandaddress "Direct link to heading")

_equivalent to: abi.decode(params, (Currency, address)) in calldata_

```codeBlockLines_mRuA
function decodeCurrencyAndAddress(bytes calldata params) internal pure returns (Currency currency, address _address);

```

Copy

### decodeCurrencyAddressAndUint256 [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CalldataDecoder\#decodecurrencyaddressanduint256 "Direct link to heading")

_equivalent to: abi.decode(params, (Currency, address, uint256)) in calldata_

```codeBlockLines_mRuA
function decodeCurrencyAddressAndUint256(bytes calldata params)
    internal
    pure
    returns (Currency currency, address _address, uint256 amount);

```

Copy

### decodeCurrencyAndUint256 [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CalldataDecoder\#decodecurrencyanduint256 "Direct link to heading")

_equivalent to: abi.decode(params, (Currency, uint256)) in calldata_

```codeBlockLines_mRuA
function decodeCurrencyAndUint256(bytes calldata params) internal pure returns (Currency currency, uint256 amount);

```

Copy

### decodeUint256 [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CalldataDecoder\#decodeuint256 "Direct link to heading")

_equivalent to: abi.decode(params, (uint256)) in calldata_

```codeBlockLines_mRuA
function decodeUint256(bytes calldata params) internal pure returns (uint256 amount);

```

Copy

### decodeCurrencyUint256AndBool [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CalldataDecoder\#decodecurrencyuint256andbool "Direct link to heading")

_equivalent to: abi.decode(params, (Currency, uint256, bool)) in calldata_

```codeBlockLines_mRuA
function decodeCurrencyUint256AndBool(bytes calldata params)
    internal
    pure
    returns (Currency currency, uint256 amount, bool boolean);

```

Copy

### toBytes [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CalldataDecoder\#tobytes "Direct link to heading")

Decode the `_arg`-th element in `_bytes` as `bytes`

```codeBlockLines_mRuA
function toBytes(bytes calldata _bytes, uint256 _arg) internal pure returns (bytes calldata res);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `_bytes` | `bytes` | The input bytes string to extract a bytes string from |
| `_arg` | `uint256` | The index of the argument to extract |

## Errors [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CalldataDecoder\#errors "Direct link to heading")

### SliceOutOfBounds [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CalldataDecoder\#sliceoutofbounds "Direct link to heading")

```codeBlockLines_mRuA
error SliceOutOfBounds();

```

Copy

- [State Variables](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CalldataDecoder#state-variables)
  - [OFFSET\_OR\_LENGTH\_MASK](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CalldataDecoder#offset_or_length_mask)
  - [OFFSET\_OR\_LENGTH\_MASK\_AND\_WORD\_ALIGN](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CalldataDecoder#offset_or_length_mask_and_word_align)
  - [SLICE\_ERROR\_SELECTOR](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CalldataDecoder#slice_error_selector)
- [Functions](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CalldataDecoder#functions)
  - [decodeActionsRouterParams](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CalldataDecoder#decodeactionsrouterparams)
  - [decodeModifyLiquidityParams](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CalldataDecoder#decodemodifyliquidityparams)
  - [decodeMintParams](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CalldataDecoder#decodemintparams)
  - [decodeBurnParams](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CalldataDecoder#decodeburnparams)
  - [decodeSwapExactInParams](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CalldataDecoder#decodeswapexactinparams)
  - [decodeSwapExactInSingleParams](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CalldataDecoder#decodeswapexactinsingleparams)
  - [decodeSwapExactOutParams](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CalldataDecoder#decodeswapexactoutparams)
  - [decodeSwapExactOutSingleParams](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CalldataDecoder#decodeswapexactoutsingleparams)
  - [decodeCurrency](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CalldataDecoder#decodecurrency)
  - [decodeCurrencyPair](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CalldataDecoder#decodecurrencypair)
  - [decodeCurrencyPairAndAddress](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CalldataDecoder#decodecurrencypairandaddress)
  - [decodeCurrencyAndAddress](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CalldataDecoder#decodecurrencyandaddress)
  - [decodeCurrencyAddressAndUint256](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CalldataDecoder#decodecurrencyaddressanduint256)
  - [decodeCurrencyAndUint256](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CalldataDecoder#decodecurrencyanduint256)
  - [decodeUint256](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CalldataDecoder#decodeuint256)
  - [decodeCurrencyUint256AndBool](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CalldataDecoder#decodecurrencyuint256andbool)
  - [toBytes](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CalldataDecoder#tobytes)
- [Errors](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CalldataDecoder#errors)
  - [SliceOutOfBounds](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CalldataDecoder#sliceoutofbounds)