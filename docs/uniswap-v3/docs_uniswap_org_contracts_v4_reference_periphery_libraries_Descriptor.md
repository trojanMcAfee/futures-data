[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor#)

On this page

# Descriptor

[Git Source](https://github.com/uniswap/v4-periphery/blob/3f295d8435e4f776ea2daeb96ce1bc6d63f33fc7/src/libraries/Descriptor.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

Describes NFT token positions

_Reference: [https://github.com/Uniswap/v3-periphery/blob/main/contracts/libraries/NFTDescriptor.sol](https://github.com/Uniswap/v3-periphery/blob/main/contracts/libraries/NFTDescriptor.sol)_

## State Variables [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor\#state-variables "Direct link to heading")

### sqrt10X128 [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor\#sqrt10x128 "Direct link to heading")

```codeBlockLines_mRuA
uint256 constant sqrt10X128 = 1076067327063303206878105757264492625226;

```

Copy

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor\#functions "Direct link to heading")

### constructTokenURI [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor\#constructtokenuri "Direct link to heading")

Constructs the token URI for a Uniswap v4 NFT

```codeBlockLines_mRuA
function constructTokenURI(ConstructTokenURIParams memory params) internal pure returns (string memory);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `params` | `ConstructTokenURIParams` | Parameters needed to construct the token URI |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `string` | The token URI as a string |

### escapeSpecialCharacters [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor\#escapespecialcharacters "Direct link to heading")

Escapes special characters in a string if they are present

```codeBlockLines_mRuA
function escapeSpecialCharacters(string memory symbol) internal pure returns (string memory);

```

Copy

### generateDescriptionPartOne [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor\#generatedescriptionpartone "Direct link to heading")

Generates the first part of the description for a Uniswap v4 NFT

```codeBlockLines_mRuA
function generateDescriptionPartOne(
    string memory quoteCurrencySymbol,
    string memory baseCurrencySymbol,
    string memory poolManager
) private pure returns (string memory);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `quoteCurrencySymbol` | `string` | The symbol of the quote currency |
| `baseCurrencySymbol` | `string` | The symbol of the base currency |
| `poolManager` | `string` | The address of the pool manager |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `string` | The first part of the description |

### generateDescriptionPartTwo [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor\#generatedescriptionparttwo "Direct link to heading")

Generates the second part of the description for a Uniswap v4 NFTs

```codeBlockLines_mRuA
function generateDescriptionPartTwo(
    string memory tokenId,
    string memory baseCurrencySymbol,
    string memory quoteCurrency,
    string memory baseCurrency,
    string memory hooks,
    string memory feeTier
) private pure returns (string memory);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `tokenId` | `string` | The token ID |
| `baseCurrencySymbol` | `string` | The symbol of the base currency |
| `quoteCurrency` | `string` | The address of the quote currency |
| `baseCurrency` | `string` | The address of the base currency |
| `hooks` | `string` | The address of the hooks contract |
| `feeTier` | `string` | The fee tier of the pool |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `string` | The second part of the description |

### generateName [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor\#generatename "Direct link to heading")

Generates the name for a Uniswap v4 NFT

```codeBlockLines_mRuA
function generateName(ConstructTokenURIParams memory params, string memory feeTier)
    private
    pure
    returns (string memory);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `params` | `ConstructTokenURIParams` | Parameters needed to generate the name |
| `feeTier` | `string` | The fee tier of the pool |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `string` | The name of the NFT |

### generateDecimalString [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor\#generatedecimalstring "Direct link to heading")

```codeBlockLines_mRuA
function generateDecimalString(DecimalStringParams memory params) private pure returns (string memory);

```

Copy

### tickToDecimalString [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor\#ticktodecimalstring "Direct link to heading")

Gets the price (quote/base) at a specific tick in decimal form
MIN or MAX are returned if tick is at the bottom or top of the price curve

```codeBlockLines_mRuA
function tickToDecimalString(
    int24 tick,
    int24 tickSpacing,
    uint8 baseCurrencyDecimals,
    uint8 quoteCurrencyDecimals,
    bool flipRatio
) internal pure returns (string memory);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `tick` | `int24` | The tick (either tickLower or tickUpper) |
| `tickSpacing` | `int24` | The tick spacing of the pool |
| `baseCurrencyDecimals` | `uint8` | The decimals of the base currency |
| `quoteCurrencyDecimals` | `uint8` | The decimals of the quote currency |
| `flipRatio` | `bool` | True if the ratio was flipped |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `string` | The ratio value as a string |

### sigfigsRounded [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor\#sigfigsrounded "Direct link to heading")

```codeBlockLines_mRuA
function sigfigsRounded(uint256 value, uint8 digits) private pure returns (uint256, bool);

```

Copy

### adjustForDecimalPrecision [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor\#adjustfordecimalprecision "Direct link to heading")

Adjusts the sqrt price for different currencies with different decimals

```codeBlockLines_mRuA
function adjustForDecimalPrecision(uint160 sqrtRatioX96, uint8 baseCurrencyDecimals, uint8 quoteCurrencyDecimals)
    private
    pure
    returns (uint256 adjustedSqrtRatioX96);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `sqrtRatioX96` | `uint160` | The sqrt price at a specific tick |
| `baseCurrencyDecimals` | `uint8` | The decimals of the base currency |
| `quoteCurrencyDecimals` | `uint8` | The decimals of the quote currency |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `adjustedSqrtRatioX96` | `uint256` | The adjusted sqrt price |

### abs [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor\#abs "Direct link to heading")

Absolute value of a signed integer

```codeBlockLines_mRuA
function abs(int256 x) private pure returns (uint256);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `x` | `int256` | The signed integer |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `uint256` | The absolute value of x |

### fixedPointToDecimalString [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor\#fixedpointtodecimalstring "Direct link to heading")

```codeBlockLines_mRuA
function fixedPointToDecimalString(uint160 sqrtRatioX96, uint8 baseCurrencyDecimals, uint8 quoteCurrencyDecimals)
    internal
    pure
    returns (string memory);

```

Copy

### feeToPercentString [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor\#feetopercentstring "Direct link to heading")

Converts fee amount in pips to decimal string with percent sign

```codeBlockLines_mRuA
function feeToPercentString(uint24 fee) internal pure returns (string memory);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `fee` | `uint24` | fee amount |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `string` | fee as a decimal string with percent sign |

### addressToString [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor\#addresstostring "Direct link to heading")

```codeBlockLines_mRuA
function addressToString(address addr) internal pure returns (string memory);

```

Copy

### generateSVGImage [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor\#generatesvgimage "Direct link to heading")

Generates the SVG image for a Uniswap v4 NFT

```codeBlockLines_mRuA
function generateSVGImage(ConstructTokenURIParams memory params) internal pure returns (string memory svg);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `params` | `ConstructTokenURIParams` | Parameters needed to generate the SVG image |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `svg` | `string` | The SVG image as a string |

### overRange [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor\#overrange "Direct link to heading")

Checks if the current price is within your position range, above, or below

```codeBlockLines_mRuA
function overRange(int24 tickLower, int24 tickUpper, int24 tickCurrent) private pure returns (int8);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `tickLower` | `int24` | The lower tick |
| `tickUpper` | `int24` | The upper tick |
| `tickCurrent` | `int24` | The current tick |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `int8` | 0 if the current price is within the position range, -1 if below, 1 if above |

### isSpecialCharacter [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor\#isspecialcharacter "Direct link to heading")

```codeBlockLines_mRuA
function isSpecialCharacter(bytes1 b) private pure returns (bool);

```

Copy

### scale [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor\#scale "Direct link to heading")

```codeBlockLines_mRuA
function scale(uint256 n, uint256 inMn, uint256 inMx, uint256 outMn, uint256 outMx)
    private
    pure
    returns (string memory);

```

Copy

### currencyToColorHex [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor\#currencytocolorhex "Direct link to heading")

```codeBlockLines_mRuA
function currencyToColorHex(uint256 currency, uint256 offset) internal pure returns (string memory str);

```

Copy

### getCircleCoord [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor\#getcirclecoord "Direct link to heading")

```codeBlockLines_mRuA
function getCircleCoord(uint256 currency, uint256 offset, uint256 tokenId) internal pure returns (uint256);

```

Copy

### sliceCurrencyHex [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor\#slicecurrencyhex "Direct link to heading")

```codeBlockLines_mRuA
function sliceCurrencyHex(uint256 currency, uint256 offset) internal pure returns (uint256);

```

Copy

## Structs [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor\#structs "Direct link to heading")

### ConstructTokenURIParams [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor\#constructtokenuriparams "Direct link to heading")

```codeBlockLines_mRuA
struct ConstructTokenURIParams {
    uint256 tokenId;
    address quoteCurrency;
    address baseCurrency;
    string quoteCurrencySymbol;
    string baseCurrencySymbol;
    uint8 quoteCurrencyDecimals;
    uint8 baseCurrencyDecimals;
    bool flipRatio;
    int24 tickLower;
    int24 tickUpper;
    int24 tickCurrent;
    int24 tickSpacing;
    uint24 fee;
    address poolManager;
    address hooks;
}

```

Copy

### DecimalStringParams [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor\#decimalstringparams "Direct link to heading")

```codeBlockLines_mRuA
struct DecimalStringParams {
    uint256 sigfigs;
    uint8 bufferLength;
    uint8 sigfigIndex;
    uint8 decimalIndex;
    uint8 zerosStartIndex;
    uint8 zerosEndIndex;
    bool isLessThanOne;
    bool isPercent;
}

```

Copy

- [State Variables](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor#state-variables)
  - [sqrt10X128](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor#sqrt10x128)
- [Functions](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor#functions)
  - [constructTokenURI](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor#constructtokenuri)
  - [escapeSpecialCharacters](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor#escapespecialcharacters)
  - [generateDescriptionPartOne](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor#generatedescriptionpartone)
  - [generateDescriptionPartTwo](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor#generatedescriptionparttwo)
  - [generateName](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor#generatename)
  - [generateDecimalString](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor#generatedecimalstring)
  - [tickToDecimalString](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor#ticktodecimalstring)
  - [sigfigsRounded](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor#sigfigsrounded)
  - [adjustForDecimalPrecision](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor#adjustfordecimalprecision)
  - [abs](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor#abs)
  - [fixedPointToDecimalString](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor#fixedpointtodecimalstring)
  - [feeToPercentString](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor#feetopercentstring)
  - [addressToString](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor#addresstostring)
  - [generateSVGImage](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor#generatesvgimage)
  - [overRange](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor#overrange)
  - [isSpecialCharacter](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor#isspecialcharacter)
  - [scale](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor#scale)
  - [currencyToColorHex](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor#currencytocolorhex)
  - [getCircleCoord](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor#getcirclecoord)
  - [sliceCurrencyHex](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor#slicecurrencyhex)
- [Structs](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor#structs)
  - [ConstructTokenURIParams](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor#constructtokenuriparams)
  - [DecimalStringParams](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Descriptor#decimalstringparams)