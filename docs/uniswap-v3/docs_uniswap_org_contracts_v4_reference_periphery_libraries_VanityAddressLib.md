[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/VanityAddressLib#)

On this page

# VanityAddressLib

[Git Source](https://github.com/uniswap/v4-periphery/blob/3f295d8435e4f776ea2daeb96ce1bc6d63f33fc7/src/libraries/VanityAddressLib.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

A library to score addresses based on their vanity

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/VanityAddressLib\#functions "Direct link to heading")

### betterThan [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/VanityAddressLib\#betterthan "Direct link to heading")

Compares two addresses and returns true if the first address has a better vanity score

```codeBlockLines_mRuA
function betterThan(address first, address second) internal pure returns (bool better);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `first` | `address` | The first address to compare |
| `second` | `address` | The second address to compare |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `better` | `bool` | True if the first address has a better vanity score |

### score [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/VanityAddressLib\#score "Direct link to heading")

Scores an address based on its vanity

_Scoring rules:_
_Requirement: The first nonzero nibble must be 4_
_10 points for every leading 0 nibble_
_40 points if the first 4 is followed by 3 more 4s_
_20 points if the first nibble after the 4 4s is NOT a 4_
_20 points if the last 4 nibbles are 4s_
_1 point for every 4_

```codeBlockLines_mRuA
function score(address addr) internal pure returns (uint256 calculatedScore);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `addr` | `address` | The address to score |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `calculatedScore` | `uint256` | The vanity score of the address |

### getLeadingNibbleCount [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/VanityAddressLib\#getleadingnibblecount "Direct link to heading")

Returns the number of leading nibbles in an address that match a given value

```codeBlockLines_mRuA
function getLeadingNibbleCount(bytes20 addrBytes, uint256 startIndex, uint8 comparison)
    internal
    pure
    returns (uint256 count);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `addrBytes` | `bytes20` | The address to count the leading zero nibbles in |
| `startIndex` | `uint256` |  |
| `comparison` | `uint8` |  |

### getNibble [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/VanityAddressLib\#getnibble "Direct link to heading")

Returns the nibble at a given index in an address

```codeBlockLines_mRuA
function getNibble(bytes20 input, uint256 nibbleIndex) internal pure returns (uint8 currentNibble);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `input` | `bytes20` | The address to get the nibble from |
| `nibbleIndex` | `uint256` | The index of the nibble to get |

- [Functions](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/VanityAddressLib#functions)
  - [betterThan](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/VanityAddressLib#betterthan)
  - [score](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/VanityAddressLib#score)
  - [getLeadingNibbleCount](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/VanityAddressLib#getleadingnibblecount)
  - [getNibble](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/VanityAddressLib#getnibble)