[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/libraries/UnsafeMath#)

On this page

# UnsafeMath

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/libraries/UnsafeMath.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

Contains methods that perform common math functions but do not do any overflow or underflow checks

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/UnsafeMath\#functions "Direct link to heading")

### divRoundingUp [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/UnsafeMath\#divroundingup "Direct link to heading")

Returns ceil(x / y)

_division by 0 will return 0, and should be checked externally_

```codeBlockLines_mRuA
function divRoundingUp(uint256 x, uint256 y) internal pure returns (uint256 z);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `x` | `uint256` | The dividend |
| `y` | `uint256` | The divisor |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `z` | `uint256` | The quotient, ceil(x / y) |

### simpleMulDiv [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/UnsafeMath\#simplemuldiv "Direct link to heading")

Calculates floor(a×b÷denominator)

_division by 0 will return 0, and should be checked externally_

```codeBlockLines_mRuA
function simpleMulDiv(uint256 a, uint256 b, uint256 denominator) internal pure returns (uint256 result);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `a` | `uint256` | The multiplicand |
| `b` | `uint256` | The multiplier |
| `denominator` | `uint256` | The divisor |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `result` | `uint256` | The 256-bit result, floor(a×b÷denominator) |

- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/libraries/UnsafeMath#functions)
  - [divRoundingUp](https://docs.uniswap.org/contracts/v4/reference/core/libraries/UnsafeMath#divroundingup)
  - [simpleMulDiv](https://docs.uniswap.org/contracts/v4/reference/core/libraries/UnsafeMath#simplemuldiv)