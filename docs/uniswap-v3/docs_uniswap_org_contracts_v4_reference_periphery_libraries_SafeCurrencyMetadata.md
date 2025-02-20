[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/SafeCurrencyMetadata#)

On this page

# SafeCurrencyMetadata

[Git Source](https://github.com/uniswap/v4-periphery/blob/3f295d8435e4f776ea2daeb96ce1bc6d63f33fc7/src/libraries/SafeCurrencyMetadata.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

can produce symbols and decimals from inconsistent or absent ERC20 implementations

_Reference: [https://github.com/Uniswap/solidity-lib/blob/master/contracts/libraries/SafeERC20Namer.sol](https://github.com/Uniswap/solidity-lib/blob/master/contracts/libraries/SafeERC20Namer.sol)_

## State Variables [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/SafeCurrencyMetadata\#state-variables "Direct link to heading")

### MAX\_SYMBOL\_LENGTH [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/SafeCurrencyMetadata\#max_symbol_length "Direct link to heading")

```codeBlockLines_mRuA
uint8 constant MAX_SYMBOL_LENGTH = 12;

```

Copy

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/SafeCurrencyMetadata\#functions "Direct link to heading")

### currencySymbol [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/SafeCurrencyMetadata\#currencysymbol "Direct link to heading")

attempts to extract the currency symbol. if it does not implement symbol, returns a symbol derived from the address

```codeBlockLines_mRuA
function currencySymbol(address currency, string memory nativeLabel) internal view returns (string memory);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `currency` | `address` | The currency address |
| `nativeLabel` | `string` | The native label |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `string` | the currency symbol |

### currencyDecimals [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/SafeCurrencyMetadata\#currencydecimals "Direct link to heading")

attempts to extract the token decimals, returns 0 if not implemented or not a uint8

```codeBlockLines_mRuA
function currencyDecimals(address currency) internal view returns (uint8);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `currency` | `address` | The currency address |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `uint8` | the currency decimals |

### bytes32ToString [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/SafeCurrencyMetadata\#bytes32tostring "Direct link to heading")

```codeBlockLines_mRuA
function bytes32ToString(bytes32 x) private pure returns (string memory);

```

Copy

### addressToSymbol [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/SafeCurrencyMetadata\#addresstosymbol "Direct link to heading")

produces a symbol from the address - the first 6 hex of the address string in upper case

```codeBlockLines_mRuA
function addressToSymbol(address currencyAddress) private pure returns (string memory);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `currencyAddress` | `address` | the address of the currency |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `string` | the symbol |

### callAndParseStringReturn [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/SafeCurrencyMetadata\#callandparsestringreturn "Direct link to heading")

calls an external view contract method that returns a symbol, and parses the output into a string

```codeBlockLines_mRuA
function callAndParseStringReturn(address currencyAddress, bytes4 selector) private view returns (string memory);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `currencyAddress` | `address` | the address of the currency |
| `selector` | `bytes4` | the selector of the symbol method |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `string` | the symbol |

### truncateSymbol [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/SafeCurrencyMetadata\#truncatesymbol "Direct link to heading")

truncates the symbol to the MAX\_SYMBOL\_LENGTH

_assumes the string is already longer than MAX\_SYMBOL\_LENGTH (or the same)_

```codeBlockLines_mRuA
function truncateSymbol(string memory str) internal pure returns (string memory);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `str` | `string` | the symbol |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `string` | the truncated symbol |

- [State Variables](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/SafeCurrencyMetadata#state-variables)
  - [MAX\_SYMBOL\_LENGTH](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/SafeCurrencyMetadata#max_symbol_length)
- [Functions](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/SafeCurrencyMetadata#functions)
  - [currencySymbol](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/SafeCurrencyMetadata#currencysymbol)
  - [currencyDecimals](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/SafeCurrencyMetadata#currencydecimals)
  - [bytes32ToString](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/SafeCurrencyMetadata#bytes32tostring)
  - [addressToSymbol](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/SafeCurrencyMetadata#addresstosymbol)
  - [callAndParseStringReturn](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/SafeCurrencyMetadata#callandparsestringreturn)
  - [truncateSymbol](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/SafeCurrencyMetadata#truncatesymbol)