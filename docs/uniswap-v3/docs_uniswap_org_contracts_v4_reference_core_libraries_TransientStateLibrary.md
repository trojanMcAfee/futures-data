[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TransientStateLibrary#)

On this page

# TransientStateLibrary

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/libraries/TransientStateLibrary.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

A helper library to provide state getters that use exttload

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TransientStateLibrary\#functions "Direct link to heading")

### getSyncedReserves [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TransientStateLibrary\#getsyncedreserves "Direct link to heading")

returns the reserves for the synced currency

_returns 0 if the reserves are not synced or value is 0._
_Checks the synced currency to only return valid reserve values (after a sync and before a settle)._

```codeBlockLines_mRuA
function getSyncedReserves(IPoolManager manager) internal view returns (uint256);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `manager` | `IPoolManager` | The pool manager contract. |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `uint256` | uint256 The reserves of the currency. |

### getSyncedCurrency [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TransientStateLibrary\#getsyncedcurrency "Direct link to heading")

```codeBlockLines_mRuA
function getSyncedCurrency(IPoolManager manager) internal view returns (Currency);

```

Copy

### getNonzeroDeltaCount [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TransientStateLibrary\#getnonzerodeltacount "Direct link to heading")

Returns the number of nonzero deltas open on the PoolManager that must be zeroed out before the contract is locked

```codeBlockLines_mRuA
function getNonzeroDeltaCount(IPoolManager manager) internal view returns (uint256);

```

Copy

### currencyDelta [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TransientStateLibrary\#currencydelta "Direct link to heading")

Get the current delta for a caller in the given currency

```codeBlockLines_mRuA
function currencyDelta(IPoolManager manager, address target, Currency currency) internal view returns (int256);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `manager` | `IPoolManager` |  |
| `target` | `address` | The credited account address |
| `currency` | `Currency` | The currency for which to lookup the delta |

### isUnlocked [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TransientStateLibrary\#isunlocked "Direct link to heading")

Returns whether the contract is unlocked or not

```codeBlockLines_mRuA
function isUnlocked(IPoolManager manager) internal view returns (bool);

```

Copy

- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TransientStateLibrary#functions)
  - [getSyncedReserves](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TransientStateLibrary#getsyncedreserves)
  - [getSyncedCurrency](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TransientStateLibrary#getsyncedcurrency)
  - [getNonzeroDeltaCount](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TransientStateLibrary#getnonzerodeltacount)
  - [currencyDelta](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TransientStateLibrary#currencydelta)
  - [isUnlocked](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TransientStateLibrary#isunlocked)