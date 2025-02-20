[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/HexStrings#)

On this page

# HexStrings

[Git Source](https://github.com/uniswap/v4-periphery/blob/3f295d8435e4f776ea2daeb96ce1bc6d63f33fc7/src/libraries/HexStrings.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

Provides function for converting numbers to hexadecimal strings

_Reference: [https://github.com/Uniswap/v3-periphery/blob/main/contracts/libraries/HexStrings.sol](https://github.com/Uniswap/v3-periphery/blob/main/contracts/libraries/HexStrings.sol)_

## State Variables [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/HexStrings\#state-variables "Direct link to heading")

### ALPHABET [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/HexStrings\#alphabet "Direct link to heading")

```codeBlockLines_mRuA
bytes16 internal constant ALPHABET = "0123456789abcdef";

```

Copy

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/HexStrings\#functions "Direct link to heading")

### toHexStringNoPrefix [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/HexStrings\#tohexstringnoprefix "Direct link to heading")

Convert a number to a hex string without the '0x' prefix with a fixed length

```codeBlockLines_mRuA
function toHexStringNoPrefix(uint256 value, uint256 length) internal pure returns (string memory);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `value` | `uint256` | The number to convert |
| `length` | `uint256` | The length of the output string, starting from the last character of the string |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `string` | The hex string |

- [State Variables](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/HexStrings#state-variables)
  - [ALPHABET](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/HexStrings#alphabet)
- [Functions](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/HexStrings#functions)
  - [toHexStringNoPrefix](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/HexStrings#tohexstringnoprefix)