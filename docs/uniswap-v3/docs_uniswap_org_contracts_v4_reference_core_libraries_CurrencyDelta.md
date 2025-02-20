[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/libraries/CurrencyDelta#)

On this page

# CurrencyDelta

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/libraries/CurrencyDelta.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

_this library implements the equivalent of a mapping, as transient storage can only be accessed in assembly_

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/CurrencyDelta\#functions "Direct link to heading")

### \_computeSlot [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/CurrencyDelta\#_computeslot "Direct link to heading")

calculates which storage slot a delta should be stored in for a given account and currency

```codeBlockLines_mRuA
function _computeSlot(address target, Currency currency) internal pure returns (bytes32 hashSlot);

```

Copy

### getDelta [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/CurrencyDelta\#getdelta "Direct link to heading")

```codeBlockLines_mRuA
function getDelta(Currency currency, address target) internal view returns (int256 delta);

```

Copy

### applyDelta [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/CurrencyDelta\#applydelta "Direct link to heading")

applies a new currency delta for a given account and currency

```codeBlockLines_mRuA
function applyDelta(Currency currency, address target, int128 delta) internal returns (int256 previous, int256 next);

```

Copy

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `previous` | `int256` | The prior value |
| `next` | `int256` | The modified result |

- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/libraries/CurrencyDelta#functions)
  - [\_computeSlot](https://docs.uniswap.org/contracts/v4/reference/core/libraries/CurrencyDelta#_computeslot)
  - [getDelta](https://docs.uniswap.org/contracts/v4/reference/core/libraries/CurrencyDelta#getdelta)
  - [applyDelta](https://docs.uniswap.org/contracts/v4/reference/core/libraries/CurrencyDelta#applydelta)