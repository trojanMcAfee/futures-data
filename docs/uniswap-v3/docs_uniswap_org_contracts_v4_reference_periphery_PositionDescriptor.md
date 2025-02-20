[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionDescriptor#)

On this page

# PositionDescriptor

[Git Source](https://github.com/uniswap/v4-periphery/blob/3f295d8435e4f776ea2daeb96ce1bc6d63f33fc7/src/PositionDescriptor.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:** [IPositionDescriptor](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IPositionDescriptor)

Produces a string containing the data URI for a JSON metadata string

## State Variables [​](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionDescriptor\#state-variables "Direct link to heading")

### DAI [​](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionDescriptor\#dai "Direct link to heading")

```codeBlockLines_mRuA
address private constant DAI = 0x6B175474E89094C44Da98b954EedeAC495271d0F;

```

Copy

### USDC [​](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionDescriptor\#usdc "Direct link to heading")

```codeBlockLines_mRuA
address private constant USDC = 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48;

```

Copy

### USDT [​](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionDescriptor\#usdt "Direct link to heading")

```codeBlockLines_mRuA
address private constant USDT = 0xdAC17F958D2ee523a2206206994597C13D831ec7;

```

Copy

### TBTC [​](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionDescriptor\#tbtc "Direct link to heading")

```codeBlockLines_mRuA
address private constant TBTC = 0x8dAEBADE922dF735c38C80C7eBD708Af50815fAa;

```

Copy

### WBTC [​](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionDescriptor\#wbtc "Direct link to heading")

```codeBlockLines_mRuA
address private constant WBTC = 0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599;

```

Copy

### wrappedNative [​](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionDescriptor\#wrappednative "Direct link to heading")

```codeBlockLines_mRuA
address public immutable wrappedNative;

```

Copy

### nativeCurrencyLabel [​](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionDescriptor\#nativecurrencylabel "Direct link to heading")

```codeBlockLines_mRuA
string public nativeCurrencyLabel;

```

Copy

### poolManager [​](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionDescriptor\#poolmanager "Direct link to heading")

```codeBlockLines_mRuA
IPoolManager public immutable poolManager;

```

Copy

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionDescriptor\#functions "Direct link to heading")

### constructor [​](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionDescriptor\#constructor "Direct link to heading")

```codeBlockLines_mRuA
constructor(IPoolManager _poolManager, address _wrappedNative, string memory _nativeCurrencyLabel);

```

Copy

### tokenURI [​](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionDescriptor\#tokenuri "Direct link to heading")

Produces the URI describing a particular token ID

_Note this URI may be a data: URI with the JSON contents directly inlined_

```codeBlockLines_mRuA
function tokenURI(IPositionManager positionManager, uint256 tokenId) external view override returns (string memory);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `positionManager` | `IPositionManager` | The position manager for which to describe the token |
| `tokenId` | `uint256` | The ID of the token for which to produce a description, which may not be valid |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `string` | The URI of the ERC721-compliant metadata |

### flipRatio [​](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionDescriptor\#flipratio "Direct link to heading")

Returns true if currency0 has higher priority than currency1

```codeBlockLines_mRuA
function flipRatio(address currency0, address currency1) public view returns (bool);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `currency0` | `address` | The first currency address |
| `currency1` | `address` | The second currency address |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `bool` | flipRatio True if currency0 has higher priority than currency1 |

### currencyRatioPriority [​](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionDescriptor\#currencyratiopriority "Direct link to heading")

Returns the priority of a currency.
For certain currencies on mainnet, the smaller the currency, the higher the priority

```codeBlockLines_mRuA
function currencyRatioPriority(address currency) public view returns (int256);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `currency` | `address` | The currency address |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `int256` | priority The priority of the currency |

## Errors [​](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionDescriptor\#errors "Direct link to heading")

### InvalidTokenId [​](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionDescriptor\#invalidtokenid "Direct link to heading")

```codeBlockLines_mRuA
error InvalidTokenId(uint256 tokenId);

```

Copy

- [State Variables](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionDescriptor#state-variables)
  - [DAI](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionDescriptor#dai)
  - [USDC](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionDescriptor#usdc)
  - [USDT](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionDescriptor#usdt)
  - [TBTC](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionDescriptor#tbtc)
  - [WBTC](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionDescriptor#wbtc)
  - [wrappedNative](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionDescriptor#wrappednative)
  - [nativeCurrencyLabel](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionDescriptor#nativecurrencylabel)
  - [poolManager](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionDescriptor#poolmanager)
- [Functions](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionDescriptor#functions)
  - [constructor](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionDescriptor#constructor)
  - [tokenURI](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionDescriptor#tokenuri)
  - [flipRatio](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionDescriptor#flipratio)
  - [currencyRatioPriority](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionDescriptor#currencyratiopriority)
- [Errors](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionDescriptor#errors)
  - [InvalidTokenId](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionDescriptor#invalidtokenid)