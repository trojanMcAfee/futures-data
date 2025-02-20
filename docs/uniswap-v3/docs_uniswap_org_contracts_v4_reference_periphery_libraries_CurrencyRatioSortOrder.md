[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CurrencyRatioSortOrder#)

On this page

# CurrencyRatioSortOrder

[Git Source](https://github.com/uniswap/v4-periphery/blob/3f295d8435e4f776ea2daeb96ce1bc6d63f33fc7/src/libraries/CurrencyRatioSortOrder.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

Provides constants for sorting currencies when displaying price ratios
Currencies given larger values will be in the numerator of the price ratio

_Reference: [https://github.com/Uniswap/v3-periphery/blob/main/contracts/libraries/TokenRatioSortOrder.sol](https://github.com/Uniswap/v3-periphery/blob/main/contracts/libraries/TokenRatioSortOrder.sol)_

## State Variables [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CurrencyRatioSortOrder\#state-variables "Direct link to heading")

### NUMERATOR\_MOST [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CurrencyRatioSortOrder\#numerator_most "Direct link to heading")

```codeBlockLines_mRuA
int256 constant NUMERATOR_MOST = 300;

```

Copy

### NUMERATOR\_MORE [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CurrencyRatioSortOrder\#numerator_more "Direct link to heading")

```codeBlockLines_mRuA
int256 constant NUMERATOR_MORE = 200;

```

Copy

### NUMERATOR [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CurrencyRatioSortOrder\#numerator "Direct link to heading")

```codeBlockLines_mRuA
int256 constant NUMERATOR = 100;

```

Copy

### DENOMINATOR\_MOST [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CurrencyRatioSortOrder\#denominator_most "Direct link to heading")

```codeBlockLines_mRuA
int256 constant DENOMINATOR_MOST = -300;

```

Copy

### DENOMINATOR\_MORE [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CurrencyRatioSortOrder\#denominator_more "Direct link to heading")

```codeBlockLines_mRuA
int256 constant DENOMINATOR_MORE = -200;

```

Copy

### DENOMINATOR [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CurrencyRatioSortOrder\#denominator "Direct link to heading")

```codeBlockLines_mRuA
int256 constant DENOMINATOR = -100;

```

Copy

- [State Variables](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CurrencyRatioSortOrder#state-variables)
  - [NUMERATOR\_MOST](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CurrencyRatioSortOrder#numerator_most)
  - [NUMERATOR\_MORE](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CurrencyRatioSortOrder#numerator_more)
  - [NUMERATOR](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CurrencyRatioSortOrder#numerator)
  - [DENOMINATOR\_MOST](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CurrencyRatioSortOrder#denominator_most)
  - [DENOMINATOR\_MORE](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CurrencyRatioSortOrder#denominator_more)
  - [DENOMINATOR](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/CurrencyRatioSortOrder#denominator)