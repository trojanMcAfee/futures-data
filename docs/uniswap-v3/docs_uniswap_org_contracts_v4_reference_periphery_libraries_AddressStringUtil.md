[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/AddressStringUtil#)

On this page

# AddressStringUtil

[Git Source](https://github.com/uniswap/v4-periphery/blob/3f295d8435e4f776ea2daeb96ce1bc6d63f33fc7/src/libraries/AddressStringUtil.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

provides utility functions for converting addresses to strings

_Reference: [https://github.com/Uniswap/solidity-lib/blob/master/contracts/libraries/AddressStringUtil.sol](https://github.com/Uniswap/solidity-lib/blob/master/contracts/libraries/AddressStringUtil.sol)_

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/AddressStringUtil\#functions "Direct link to heading")

### toAsciiString [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/AddressStringUtil\#toasciistring "Direct link to heading")

Converts an address to the uppercase hex string, extracting only len bytes (up to 20, multiple of 2)

```codeBlockLines_mRuA
function toAsciiString(address addr, uint256 len) internal pure returns (string memory);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `addr` | `address` | the address to convert |
| `len` | `uint256` | the number of bytes to extract |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `string` | the hex string |

### char [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/AddressStringUtil\#char "Direct link to heading")

Converts a value into is corresponding ASCII character for the hex representation

```codeBlockLines_mRuA
function char(uint8 b) private pure returns (bytes1 c);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `b` | `uint8` | the value to convert |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `c` | `bytes1` | the ASCII character |

## Errors [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/AddressStringUtil\#errors "Direct link to heading")

### InvalidAddressLength [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/AddressStringUtil\#invalidaddresslength "Direct link to heading")

```codeBlockLines_mRuA
error InvalidAddressLength(uint256 len);

```

Copy

- [Functions](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/AddressStringUtil#functions)
  - [toAsciiString](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/AddressStringUtil#toasciistring)
  - [char](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/AddressStringUtil#char)
- [Errors](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/AddressStringUtil#errors)
  - [InvalidAddressLength](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/AddressStringUtil#invalidaddresslength)