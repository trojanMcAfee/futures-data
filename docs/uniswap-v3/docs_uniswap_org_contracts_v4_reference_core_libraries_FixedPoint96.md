[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/libraries/FixedPoint96#)

On this page

# FixedPoint96

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/libraries/FixedPoint96.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

A library for handling binary fixed point numbers, see [https://en.wikipedia.org/wiki/Q\_(number\_format)](https://en.wikipedia.org/wiki/Q_(number_format))

_Used in SqrtPriceMath.sol_

## State Variables [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/FixedPoint96\#state-variables "Direct link to heading")

### RESOLUTION [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/FixedPoint96\#resolution "Direct link to heading")

```codeBlockLines_mRuA
uint8 internal constant RESOLUTION = 96;

```

Copy

### Q96 [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/FixedPoint96\#q96 "Direct link to heading")

```codeBlockLines_mRuA
uint256 internal constant Q96 = 0x1000000000000000000000000;

```

Copy

- [State Variables](https://docs.uniswap.org/contracts/v4/reference/core/libraries/FixedPoint96#state-variables)
  - [RESOLUTION](https://docs.uniswap.org/contracts/v4/reference/core/libraries/FixedPoint96#resolution)
  - [Q96](https://docs.uniswap.org/contracts/v4/reference/core/libraries/FixedPoint96#q96)