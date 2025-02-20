[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/types/currency#)

On this page

`Currency` is a custom type that represents either native currency (ETH) or ERC20 tokens.

## Type Definition [​](https://docs.uniswap.org/contracts/v4/reference/core/types/currency\#type-definition "Direct link to heading")

```codeBlockLines_mRuA
type Currency is address;

```

Copy

## Global Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/types/currency\#global-functions "Direct link to heading")

### equals [​](https://docs.uniswap.org/contracts/v4/reference/core/types/currency\#equals "Direct link to heading")

```codeBlockLines_mRuA
function equals(Currency currency, Currency other) pure returns (bool)

```

Copy

Checks if two `Currency` values are equal.

| Param Name | Type | Description |
| --- | --- | --- |
| currency | Currency | The first Currency value |
| other | Currency | The second Currency value |

Returns `true` if the Currency values are equal, `false` otherwise.

### greaterThan [​](https://docs.uniswap.org/contracts/v4/reference/core/types/currency\#greaterthan "Direct link to heading")

```codeBlockLines_mRuA
function greaterThan(Currency currency, Currency other) pure returns (bool)

```

Copy

Compares two `Currency` values based on their underlying addresses.

| Param Name | Type | Description |
| --- | --- | --- |
| currency | Currency | The first Currency value |
| other | Currency | The second Currency value |

Returns `true` if the underlying address of `currency` is numerically greater than the underlying address of `other`, `false` otherwise.

Note: This comparison is based on the numerical value of the addresses and does not imply any inherent ordering or value relationship between different currencies. It's primarily used for consistent ordering in data structures.

### lessThan [​](https://docs.uniswap.org/contracts/v4/reference/core/types/currency\#lessthan "Direct link to heading")

```codeBlockLines_mRuA
function lessThan(Currency currency, Currency other) pure returns (bool)

```

Copy

Compares two `Currency` values based on their underlying addresses.

| Param Name | Type | Description |
| --- | --- | --- |
| currency | Currency | The first Currency value |
| other | Currency | The second Currency value |

Returns `true` if the underlying address of `currency` is numerically less than the underlying address of `other`, `false` otherwise.

Note: As with `greaterThan`, this comparison is based on address values and does not imply any inherent ordering or value relationship between currencies.

### greaterThanOrEqualTo [​](https://docs.uniswap.org/contracts/v4/reference/core/types/currency\#greaterthanorequalto "Direct link to heading")

```codeBlockLines_mRuA
function greaterThanOrEqualTo(Currency currency, Currency other) pure returns (bool)

```

Copy

Checks if one `Currency` value is greater than or equal to another, based on their underlying addresses.

| Param Name | Type | Description |
| --- | --- | --- |
| currency | Currency | The first Currency value |
| other | Currency | The second Currency value |

Returns `true` if the underlying address of `currency` is numerically greater than or equal to the underlying address of `other`, `false` otherwise.

# CurrencyLibrary

The `CurrencyLibrary` provides utility functions for handling both native currency (ETH) and ERC20 tokens.

## Constants [​](https://docs.uniswap.org/contracts/v4/reference/core/types/currency\#constants "Direct link to heading")

```codeBlockLines_mRuA
Currency public constant NATIVE = Currency.wrap(address(0));

```

Copy

`NATIVE` represents the native currency (ETH). It is defined as a `Currency` with the underlying address of `address(0)`.

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/types/currency\#functions "Direct link to heading")

### transfer [​](https://docs.uniswap.org/contracts/v4/reference/core/types/currency\#transfer "Direct link to heading")

```codeBlockLines_mRuA
function transfer(Currency currency, address to, uint256 amount) internal

```

Copy

Transfers `amount` of `currency` to the `to` address.

| Param Name | Type | Description |
| --- | --- | --- |
| currency | Currency | The currency to transfer |
| to | address | The recipient address |
| amount | uint256 | The amount of currency to transfer |

### balanceOfSelf [​](https://docs.uniswap.org/contracts/v4/reference/core/types/currency\#balanceofself "Direct link to heading")

```codeBlockLines_mRuA
function balanceOfSelf(Currency currency) internal view returns (uint256)

```

Copy

Returns the balance of `currency` held by the contract itself.

| Param Name | Type | Description |
| --- | --- | --- |
| currency | Currency | The currency to check |

Returns the balance of the specified currency.

### balanceOf [​](https://docs.uniswap.org/contracts/v4/reference/core/types/currency\#balanceof "Direct link to heading")

```codeBlockLines_mRuA
function balanceOf(Currency currency, address owner) internal view returns (uint256)

```

Copy

Returns the balance of `currency` held by the `owner` address.

| Param Name | Type | Description |
| --- | --- | --- |
| currency | Currency | The currency to check |
| owner | address | The address to check |

Returns the balance of the specified currency for the given address.

### isNative [​](https://docs.uniswap.org/contracts/v4/reference/core/types/currency\#isnative "Direct link to heading")

```codeBlockLines_mRuA
function isNative(Currency currency) internal pure returns (bool)

```

Copy

Checks if the given `currency` is the native currency (ETH).

| Param Name | Type | Description |
| --- | --- | --- |
| currency | Currency | The currency to check |

Returns `true` if the currency is native (ETH), `false` otherwise.

### toId [​](https://docs.uniswap.org/contracts/v4/reference/core/types/currency\#toid "Direct link to heading")

```codeBlockLines_mRuA
function toId(Currency currency) internal pure returns (uint256)

```

Copy

Converts a `Currency` to its corresponding ID.

| Param Name | Type | Description |
| --- | --- | --- |
| currency | Currency | The currency to convert |

Returns the ID of the currency.

### fromId [​](https://docs.uniswap.org/contracts/v4/reference/core/types/currency\#fromid "Direct link to heading")

```codeBlockLines_mRuA
function fromId(uint256 id) internal pure returns (Currency)

```

Copy

Converts an ID to its corresponding `Currency`.

| Param Name | Type | Description |
| --- | --- | --- |
| id | uint256 | The ID to convert |

Returns the Currency corresponding to the given ID.

- [Type Definition](https://docs.uniswap.org/contracts/v4/reference/core/types/currency#type-definition)
- [Global Functions](https://docs.uniswap.org/contracts/v4/reference/core/types/currency#global-functions)
  - [equals](https://docs.uniswap.org/contracts/v4/reference/core/types/currency#equals)
  - [greaterThan](https://docs.uniswap.org/contracts/v4/reference/core/types/currency#greaterthan)
  - [lessThan](https://docs.uniswap.org/contracts/v4/reference/core/types/currency#lessthan)
  - [greaterThanOrEqualTo](https://docs.uniswap.org/contracts/v4/reference/core/types/currency#greaterthanorequalto)
- [Constants](https://docs.uniswap.org/contracts/v4/reference/core/types/currency#constants)
- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/types/currency#functions)
  - [transfer](https://docs.uniswap.org/contracts/v4/reference/core/types/currency#transfer)
  - [balanceOfSelf](https://docs.uniswap.org/contracts/v4/reference/core/types/currency#balanceofself)
  - [balanceOf](https://docs.uniswap.org/contracts/v4/reference/core/types/currency#balanceof)
  - [isNative](https://docs.uniswap.org/contracts/v4/reference/core/types/currency#isnative)
  - [toId](https://docs.uniswap.org/contracts/v4/reference/core/types/currency#toid)
  - [fromId](https://docs.uniswap.org/contracts/v4/reference/core/types/currency#fromid)