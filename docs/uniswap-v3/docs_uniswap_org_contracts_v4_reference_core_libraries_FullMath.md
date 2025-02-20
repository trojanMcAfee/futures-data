[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/libraries/FullMath#)

On this page

# FullMath

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/libraries/FullMath.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

Facilitates multiplication and division that can have overflow of an intermediate value without any loss of precision

_Handles "phantom overflow" i.e., allows multiplication and division where an intermediate value overflows 256 bits_

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/FullMath\#functions "Direct link to heading")

### mulDiv [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/FullMath\#muldiv "Direct link to heading")

Calculates floor(a×b÷denominator) with full precision. Throws if result overflows a uint256 or denominator == 0

_Credit to Remco Bloemen under MIT license [https://xn--2-umb.com/21/muldiv](https://xn--2-umb.com/21/muldiv)_

```codeBlockLines_mRuA
function mulDiv(uint256 a, uint256 b, uint256 denominator) internal pure returns (uint256 result);

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
| `result` | `uint256` | The 256-bit result |

### mulDivRoundingUp [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/FullMath\#muldivroundingup "Direct link to heading")

Calculates ceil(a×b÷denominator) with full precision. Throws if result overflows a uint256 or denominator == 0

```codeBlockLines_mRuA
function mulDivRoundingUp(uint256 a, uint256 b, uint256 denominator) internal pure returns (uint256 result);

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
| `result` | `uint256` | The 256-bit result |

- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/libraries/FullMath#functions)
  - [mulDiv](https://docs.uniswap.org/contracts/v4/reference/core/libraries/FullMath#muldiv)
  - [mulDivRoundingUp](https://docs.uniswap.org/contracts/v4/reference/core/libraries/FullMath#muldivroundingup)