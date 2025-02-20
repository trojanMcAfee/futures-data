[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/periphery/base/DeltaResolver#)

On this page

# DeltaResolver

[Git Source](https://github.com/uniswap/v4-periphery/blob/3f295d8435e4f776ea2daeb96ce1bc6d63f33fc7/src/base/DeltaResolver.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:** [ImmutableState](https://docs.uniswap.org/contracts/v4/reference/periphery/base/ImmutableState)

Abstract contract used to sync, send, and settle funds to the pool manager

_Note that sync() is called before any erc-20 transfer in `settle`._

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/DeltaResolver\#functions "Direct link to heading")

### \_take [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/DeltaResolver\#_take "Direct link to heading")

Take an amount of currency out of the PoolManager

_Returns early if the amount is 0_

```codeBlockLines_mRuA
function _take(Currency currency, address recipient, uint256 amount) internal;

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `currency` | `Currency` | Currency to take |
| `recipient` | `address` | Address to receive the currency |
| `amount` | `uint256` | Amount to take |

### \_settle [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/DeltaResolver\#_settle "Direct link to heading")

Pay and settle a currency to the PoolManager

_The implementing contract must ensure that the `payer` is a secure address_

_Returns early if the amount is 0_

```codeBlockLines_mRuA
function _settle(Currency currency, address payer, uint256 amount) internal;

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `currency` | `Currency` | Currency to settle |
| `payer` | `address` | Address of the payer |
| `amount` | `uint256` | Amount to send |

### \_pay [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/DeltaResolver\#_pay "Direct link to heading")

Abstract function for contracts to implement paying tokens to the poolManager

_The recipient of the payment should be the poolManager_

```codeBlockLines_mRuA
function _pay(Currency token, address payer, uint256 amount) internal virtual;

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `token` | `Currency` | The token to settle. This is known not to be the native currency |
| `payer` | `address` | The address who should pay tokens |
| `amount` | `uint256` | The number of tokens to send |

### \_getFullDebt [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/DeltaResolver\#_getfulldebt "Direct link to heading")

Obtain the full amount owed by this contract (negative delta)

```codeBlockLines_mRuA
function _getFullDebt(Currency currency) internal view returns (uint256 amount);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `currency` | `Currency` | Currency to get the delta for |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `amount` | `uint256` | The amount owed by this contract as a uint256 |

### \_getFullCredit [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/DeltaResolver\#_getfullcredit "Direct link to heading")

Obtain the full credit owed to this contract (positive delta)

```codeBlockLines_mRuA
function _getFullCredit(Currency currency) internal view returns (uint256 amount);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `currency` | `Currency` | Currency to get the delta for |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `amount` | `uint256` | The amount owed to this contract as a uint256 |

### \_mapSettleAmount [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/DeltaResolver\#_mapsettleamount "Direct link to heading")

Calculates the amount for a settle action

```codeBlockLines_mRuA
function _mapSettleAmount(uint256 amount, Currency currency) internal view returns (uint256);

```

Copy

### \_mapTakeAmount [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/DeltaResolver\#_maptakeamount "Direct link to heading")

Calculates the amount for a take action

```codeBlockLines_mRuA
function _mapTakeAmount(uint256 amount, Currency currency) internal view returns (uint256);

```

Copy

### \_mapWrapUnwrapAmount [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/DeltaResolver\#_mapwrapunwrapamount "Direct link to heading")

Calculates the sanitized amount before wrapping/unwrapping.

```codeBlockLines_mRuA
function _mapWrapUnwrapAmount(Currency inputCurrency, uint256 amount, Currency outputCurrency)
    internal
    view
    returns (uint256);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `inputCurrency` | `Currency` | The currency, either native or wrapped native, that this contract holds |
| `amount` | `uint256` | The amount to wrap or unwrap. Can be CONTRACT\_BALANCE, OPEN\_DELTA or a specific amount |
| `outputCurrency` | `Currency` | The currency after the wrap/unwrap that the user may owe a balance in on the poolManager |

## Errors [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/DeltaResolver\#errors "Direct link to heading")

### DeltaNotPositive [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/DeltaResolver\#deltanotpositive "Direct link to heading")

Emitted trying to settle a positive delta.

```codeBlockLines_mRuA
error DeltaNotPositive(Currency currency);

```

Copy

### DeltaNotNegative [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/DeltaResolver\#deltanotnegative "Direct link to heading")

Emitted trying to take a negative delta.

```codeBlockLines_mRuA
error DeltaNotNegative(Currency currency);

```

Copy

### InsufficientBalance [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/DeltaResolver\#insufficientbalance "Direct link to heading")

Emitted when the contract does not have enough balance to wrap or unwrap.

```codeBlockLines_mRuA
error InsufficientBalance();

```

Copy

- [Functions](https://docs.uniswap.org/contracts/v4/reference/periphery/base/DeltaResolver#functions)
  - [\_take](https://docs.uniswap.org/contracts/v4/reference/periphery/base/DeltaResolver#_take)
  - [\_settle](https://docs.uniswap.org/contracts/v4/reference/periphery/base/DeltaResolver#_settle)
  - [\_pay](https://docs.uniswap.org/contracts/v4/reference/periphery/base/DeltaResolver#_pay)
  - [\_getFullDebt](https://docs.uniswap.org/contracts/v4/reference/periphery/base/DeltaResolver#_getfulldebt)
  - [\_getFullCredit](https://docs.uniswap.org/contracts/v4/reference/periphery/base/DeltaResolver#_getfullcredit)
  - [\_mapSettleAmount](https://docs.uniswap.org/contracts/v4/reference/periphery/base/DeltaResolver#_mapsettleamount)
  - [\_mapTakeAmount](https://docs.uniswap.org/contracts/v4/reference/periphery/base/DeltaResolver#_maptakeamount)
  - [\_mapWrapUnwrapAmount](https://docs.uniswap.org/contracts/v4/reference/periphery/base/DeltaResolver#_mapwrapunwrapamount)
- [Errors](https://docs.uniswap.org/contracts/v4/reference/periphery/base/DeltaResolver#errors)
  - [DeltaNotPositive](https://docs.uniswap.org/contracts/v4/reference/periphery/base/DeltaResolver#deltanotpositive)
  - [DeltaNotNegative](https://docs.uniswap.org/contracts/v4/reference/periphery/base/DeltaResolver#deltanotnegative)
  - [InsufficientBalance](https://docs.uniswap.org/contracts/v4/reference/periphery/base/DeltaResolver#insufficientbalance)