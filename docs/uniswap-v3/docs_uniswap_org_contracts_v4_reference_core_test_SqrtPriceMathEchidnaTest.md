[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/test/SqrtPriceMathEchidnaTest#)

On this page

# SqrtPriceMathEchidnaTest

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/test/SqrtPriceMathEchidnaTest.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/test/SqrtPriceMathEchidnaTest\#functions "Direct link to heading")

### mulDivRoundingUpInvariants [​](https://docs.uniswap.org/contracts/v4/reference/core/test/SqrtPriceMathEchidnaTest\#muldivroundingupinvariants "Direct link to heading")

```codeBlockLines_mRuA
function mulDivRoundingUpInvariants(uint256 x, uint256 y, uint256 z) external pure;

```

Copy

### getNextSqrtPriceFromInputInvariants [​](https://docs.uniswap.org/contracts/v4/reference/core/test/SqrtPriceMathEchidnaTest\#getnextsqrtpricefrominputinvariants "Direct link to heading")

```codeBlockLines_mRuA
function getNextSqrtPriceFromInputInvariants(uint160 sqrtP, uint128 liquidity, uint256 amountIn, bool zeroForOne)
    external
    pure;

```

Copy

### getNextSqrtPriceFromOutputInvariants [​](https://docs.uniswap.org/contracts/v4/reference/core/test/SqrtPriceMathEchidnaTest\#getnextsqrtpricefromoutputinvariants "Direct link to heading")

```codeBlockLines_mRuA
function getNextSqrtPriceFromOutputInvariants(uint160 sqrtP, uint128 liquidity, uint256 amountOut, bool zeroForOne)
    external
    pure;

```

Copy

### getNextSqrtPriceFromAmount0RoundingUpInvariants [​](https://docs.uniswap.org/contracts/v4/reference/core/test/SqrtPriceMathEchidnaTest\#getnextsqrtpricefromamount0roundingupinvariants "Direct link to heading")

```codeBlockLines_mRuA
function getNextSqrtPriceFromAmount0RoundingUpInvariants(uint160 sqrtPX96, uint128 liquidity, uint256 amount, bool add)
    external
    pure;

```

Copy

### getNextSqrtPriceFromAmount1RoundingDownInvariants [​](https://docs.uniswap.org/contracts/v4/reference/core/test/SqrtPriceMathEchidnaTest\#getnextsqrtpricefromamount1roundingdowninvariants "Direct link to heading")

```codeBlockLines_mRuA
function getNextSqrtPriceFromAmount1RoundingDownInvariants(
    uint160 sqrtPX96,
    uint128 liquidity,
    uint256 amount,
    bool add
) external pure;

```

Copy

### getAmount0DeltaInvariants [​](https://docs.uniswap.org/contracts/v4/reference/core/test/SqrtPriceMathEchidnaTest\#getamount0deltainvariants "Direct link to heading")

```codeBlockLines_mRuA
function getAmount0DeltaInvariants(uint160 sqrtP, uint160 sqrtQ, uint128 liquidity) external pure;

```

Copy

### getAmount0DeltaEquivalency [​](https://docs.uniswap.org/contracts/v4/reference/core/test/SqrtPriceMathEchidnaTest\#getamount0deltaequivalency "Direct link to heading")

```codeBlockLines_mRuA
function getAmount0DeltaEquivalency(uint160 sqrtP, uint160 sqrtQ, uint128 liquidity, bool roundUp) external pure;

```

Copy

### getAmount1DeltaInvariants [​](https://docs.uniswap.org/contracts/v4/reference/core/test/SqrtPriceMathEchidnaTest\#getamount1deltainvariants "Direct link to heading")

```codeBlockLines_mRuA
function getAmount1DeltaInvariants(uint160 sqrtP, uint160 sqrtQ, uint128 liquidity) external pure;

```

Copy

### getAmount0DeltaSignedInvariants [​](https://docs.uniswap.org/contracts/v4/reference/core/test/SqrtPriceMathEchidnaTest\#getamount0deltasignedinvariants "Direct link to heading")

```codeBlockLines_mRuA
function getAmount0DeltaSignedInvariants(uint160 sqrtP, uint160 sqrtQ, int128 liquidity) external pure;

```

Copy

### getAmount1DeltaSignedInvariants [​](https://docs.uniswap.org/contracts/v4/reference/core/test/SqrtPriceMathEchidnaTest\#getamount1deltasignedinvariants "Direct link to heading")

```codeBlockLines_mRuA
function getAmount1DeltaSignedInvariants(uint160 sqrtP, uint160 sqrtQ, int128 liquidity) external pure;

```

Copy

### getOutOfRangeMintInvariants [​](https://docs.uniswap.org/contracts/v4/reference/core/test/SqrtPriceMathEchidnaTest\#getoutofrangemintinvariants "Direct link to heading")

```codeBlockLines_mRuA
function getOutOfRangeMintInvariants(uint160 sqrtA, uint160 sqrtB, int128 liquidity) external pure;

```

Copy

### getInRangeMintInvariants [​](https://docs.uniswap.org/contracts/v4/reference/core/test/SqrtPriceMathEchidnaTest\#getinrangemintinvariants "Direct link to heading")

```codeBlockLines_mRuA
function getInRangeMintInvariants(uint160 sqrtLower, uint160 sqrtCurrent, uint160 sqrtUpper, int128 liquidity)
    external
    pure;

```

Copy

- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/test/SqrtPriceMathEchidnaTest#functions)
  - [mulDivRoundingUpInvariants](https://docs.uniswap.org/contracts/v4/reference/core/test/SqrtPriceMathEchidnaTest#muldivroundingupinvariants)
  - [getNextSqrtPriceFromInputInvariants](https://docs.uniswap.org/contracts/v4/reference/core/test/SqrtPriceMathEchidnaTest#getnextsqrtpricefrominputinvariants)
  - [getNextSqrtPriceFromOutputInvariants](https://docs.uniswap.org/contracts/v4/reference/core/test/SqrtPriceMathEchidnaTest#getnextsqrtpricefromoutputinvariants)
  - [getNextSqrtPriceFromAmount0RoundingUpInvariants](https://docs.uniswap.org/contracts/v4/reference/core/test/SqrtPriceMathEchidnaTest#getnextsqrtpricefromamount0roundingupinvariants)
  - [getNextSqrtPriceFromAmount1RoundingDownInvariants](https://docs.uniswap.org/contracts/v4/reference/core/test/SqrtPriceMathEchidnaTest#getnextsqrtpricefromamount1roundingdowninvariants)
  - [getAmount0DeltaInvariants](https://docs.uniswap.org/contracts/v4/reference/core/test/SqrtPriceMathEchidnaTest#getamount0deltainvariants)
  - [getAmount0DeltaEquivalency](https://docs.uniswap.org/contracts/v4/reference/core/test/SqrtPriceMathEchidnaTest#getamount0deltaequivalency)
  - [getAmount1DeltaInvariants](https://docs.uniswap.org/contracts/v4/reference/core/test/SqrtPriceMathEchidnaTest#getamount1deltainvariants)
  - [getAmount0DeltaSignedInvariants](https://docs.uniswap.org/contracts/v4/reference/core/test/SqrtPriceMathEchidnaTest#getamount0deltasignedinvariants)
  - [getAmount1DeltaSignedInvariants](https://docs.uniswap.org/contracts/v4/reference/core/test/SqrtPriceMathEchidnaTest#getamount1deltasignedinvariants)
  - [getOutOfRangeMintInvariants](https://docs.uniswap.org/contracts/v4/reference/core/test/SqrtPriceMathEchidnaTest#getoutofrangemintinvariants)
  - [getInRangeMintInvariants](https://docs.uniswap.org/contracts/v4/reference/core/test/SqrtPriceMathEchidnaTest#getinrangemintinvariants)