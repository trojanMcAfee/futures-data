[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/libraries/CurrencyReserves#)

On this page

# CurrencyReserves

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/libraries/CurrencyReserves.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

## State Variables [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/CurrencyReserves\#state-variables "Direct link to heading")

### RESERVES\_OF\_SLOT [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/CurrencyReserves\#reserves_of_slot "Direct link to heading")

bytes32(uint256(keccak256("ReservesOf")) - 1)

```codeBlockLines_mRuA
bytes32 constant RESERVES_OF_SLOT = 0x1e0745a7db1623981f0b2a5d4232364c00787266eb75ad546f190e6cebe9bd95;

```

Copy

### CURRENCY\_SLOT [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/CurrencyReserves\#currency_slot "Direct link to heading")

bytes32(uint256(keccak256("Currency")) - 1)

```codeBlockLines_mRuA
bytes32 constant CURRENCY_SLOT = 0x27e098c505d44ec3574004bca052aabf76bd35004c182099d8c575fb238593b9;

```

Copy

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/CurrencyReserves\#functions "Direct link to heading")

### getSyncedCurrency [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/CurrencyReserves\#getsyncedcurrency "Direct link to heading")

```codeBlockLines_mRuA
function getSyncedCurrency() internal view returns (Currency currency);

```

Copy

### resetCurrency [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/CurrencyReserves\#resetcurrency "Direct link to heading")

```codeBlockLines_mRuA
function resetCurrency() internal;

```

Copy

### syncCurrencyAndReserves [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/CurrencyReserves\#synccurrencyandreserves "Direct link to heading")

```codeBlockLines_mRuA
function syncCurrencyAndReserves(Currency currency, uint256 value) internal;

```

Copy

### getSyncedReserves [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/CurrencyReserves\#getsyncedreserves "Direct link to heading")

```codeBlockLines_mRuA
function getSyncedReserves() internal view returns (uint256 value);

```

Copy

- [State Variables](https://docs.uniswap.org/contracts/v4/reference/core/libraries/CurrencyReserves#state-variables)
  - [RESERVES\_OF\_SLOT](https://docs.uniswap.org/contracts/v4/reference/core/libraries/CurrencyReserves#reserves_of_slot)
  - [CURRENCY\_SLOT](https://docs.uniswap.org/contracts/v4/reference/core/libraries/CurrencyReserves#currency_slot)
- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/libraries/CurrencyReserves#functions)
  - [getSyncedCurrency](https://docs.uniswap.org/contracts/v4/reference/core/libraries/CurrencyReserves#getsyncedcurrency)
  - [resetCurrency](https://docs.uniswap.org/contracts/v4/reference/core/libraries/CurrencyReserves#resetcurrency)
  - [syncCurrencyAndReserves](https://docs.uniswap.org/contracts/v4/reference/core/libraries/CurrencyReserves#synccurrencyandreserves)
  - [getSyncedReserves](https://docs.uniswap.org/contracts/v4/reference/core/libraries/CurrencyReserves#getsyncedreserves)