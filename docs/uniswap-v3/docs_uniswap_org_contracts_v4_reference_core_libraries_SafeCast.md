[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/libraries/SafeCast#)

On this page

# SafeCast

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/libraries/SafeCast.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

Contains methods for safely casting between types

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/SafeCast\#functions "Direct link to heading")

### toUint160 [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/SafeCast\#touint160 "Direct link to heading")

Cast a uint256 to a uint160, revert on overflow

```codeBlockLines_mRuA
function toUint160(uint256 x) internal pure returns (uint160 y);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `x` | `uint256` | The uint256 to be downcasted |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `y` | `uint160` | The downcasted integer, now type uint160 |

### toUint128 [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/SafeCast\#touint128 "Direct link to heading")

Cast a uint256 to a uint128, revert on overflow

```codeBlockLines_mRuA
function toUint128(uint256 x) internal pure returns (uint128 y);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `x` | `uint256` | The uint256 to be downcasted |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `y` | `uint128` | The downcasted integer, now type uint128 |

### toUint128 [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/SafeCast\#touint128-1 "Direct link to heading")

Cast a int128 to a uint128, revert on overflow or underflow

```codeBlockLines_mRuA
function toUint128(int128 x) internal pure returns (uint128 y);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `x` | `int128` | The int128 to be casted |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `y` | `uint128` | The casted integer, now type uint128 |

### toInt128 [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/SafeCast\#toint128 "Direct link to heading")

Cast a int256 to a int128, revert on overflow or underflow

```codeBlockLines_mRuA
function toInt128(int256 x) internal pure returns (int128 y);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `x` | `int256` | The int256 to be downcasted |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `y` | `int128` | The downcasted integer, now type int128 |

### toInt256 [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/SafeCast\#toint256 "Direct link to heading")

Cast a uint256 to a int256, revert on overflow

```codeBlockLines_mRuA
function toInt256(uint256 x) internal pure returns (int256 y);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `x` | `uint256` | The uint256 to be casted |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `y` | `int256` | The casted integer, now type int256 |

### toInt128 [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/SafeCast\#toint128-1 "Direct link to heading")

Cast a uint256 to a int128, revert on overflow

```codeBlockLines_mRuA
function toInt128(uint256 x) internal pure returns (int128);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `x` | `uint256` | The uint256 to be downcasted |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `int128` | The downcasted integer, now type int128 |

## Errors [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/SafeCast\#errors "Direct link to heading")

### SafeCastOverflow [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/SafeCast\#safecastoverflow "Direct link to heading")

```codeBlockLines_mRuA
error SafeCastOverflow();

```

Copy

- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/libraries/SafeCast#functions)
  - [toUint160](https://docs.uniswap.org/contracts/v4/reference/core/libraries/SafeCast#touint160)
  - [toUint128](https://docs.uniswap.org/contracts/v4/reference/core/libraries/SafeCast#touint128)
  - [toUint128](https://docs.uniswap.org/contracts/v4/reference/core/libraries/SafeCast#touint128-1)
  - [toInt128](https://docs.uniswap.org/contracts/v4/reference/core/libraries/SafeCast#toint128)
  - [toInt256](https://docs.uniswap.org/contracts/v4/reference/core/libraries/SafeCast#toint256)
  - [toInt128](https://docs.uniswap.org/contracts/v4/reference/core/libraries/SafeCast#toint128-1)
- [Errors](https://docs.uniswap.org/contracts/v4/reference/core/libraries/SafeCast#errors)
  - [SafeCastOverflow](https://docs.uniswap.org/contracts/v4/reference/core/libraries/SafeCast#safecastoverflow)