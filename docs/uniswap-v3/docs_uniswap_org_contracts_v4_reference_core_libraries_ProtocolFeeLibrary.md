[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/libraries/ProtocolFeeLibrary#)

On this page

# ProtocolFeeLibrary

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/libraries/ProtocolFeeLibrary.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

library of functions related to protocol fees

## State Variables [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/ProtocolFeeLibrary\#state-variables "Direct link to heading")

### MAX\_PROTOCOL\_FEE [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/ProtocolFeeLibrary\#max_protocol_fee "Direct link to heading")

Max protocol fee is 0.1% (1000 pips)

_Increasing these values could lead to overflow in Pool.swap_

```codeBlockLines_mRuA
uint16 public constant MAX_PROTOCOL_FEE = 1000;

```

Copy

### FEE\_0\_THRESHOLD [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/ProtocolFeeLibrary\#fee_0_threshold "Direct link to heading")

Thresholds used for optimized bounds checks on protocol fees

```codeBlockLines_mRuA
uint24 internal constant FEE_0_THRESHOLD = 1001;

```

Copy

### FEE\_1\_THRESHOLD [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/ProtocolFeeLibrary\#fee_1_threshold "Direct link to heading")

```codeBlockLines_mRuA
uint24 internal constant FEE_1_THRESHOLD = 1001 << 12;

```

Copy

### PIPS\_DENOMINATOR [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/ProtocolFeeLibrary\#pips_denominator "Direct link to heading")

the protocol fee is represented in hundredths of a bip

```codeBlockLines_mRuA
uint256 internal constant PIPS_DENOMINATOR = 1_000_000;

```

Copy

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/ProtocolFeeLibrary\#functions "Direct link to heading")

### getZeroForOneFee [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/ProtocolFeeLibrary\#getzeroforonefee "Direct link to heading")

```codeBlockLines_mRuA
function getZeroForOneFee(uint24 self) internal pure returns (uint16);

```

Copy

### getOneForZeroFee [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/ProtocolFeeLibrary\#getoneforzerofee "Direct link to heading")

```codeBlockLines_mRuA
function getOneForZeroFee(uint24 self) internal pure returns (uint16);

```

Copy

### isValidProtocolFee [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/ProtocolFeeLibrary\#isvalidprotocolfee "Direct link to heading")

```codeBlockLines_mRuA
function isValidProtocolFee(uint24 self) internal pure returns (bool valid);

```

Copy

### calculateSwapFee [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/ProtocolFeeLibrary\#calculateswapfee "Direct link to heading")

_here `self` is just a single direction's protocol fee, not a packed type of 2 protocol fees_

```codeBlockLines_mRuA
function calculateSwapFee(uint16 self, uint24 lpFee) internal pure returns (uint24 swapFee);

```

Copy

- [State Variables](https://docs.uniswap.org/contracts/v4/reference/core/libraries/ProtocolFeeLibrary#state-variables)
  - [MAX\_PROTOCOL\_FEE](https://docs.uniswap.org/contracts/v4/reference/core/libraries/ProtocolFeeLibrary#max_protocol_fee)
  - [FEE\_0\_THRESHOLD](https://docs.uniswap.org/contracts/v4/reference/core/libraries/ProtocolFeeLibrary#fee_0_threshold)
  - [FEE\_1\_THRESHOLD](https://docs.uniswap.org/contracts/v4/reference/core/libraries/ProtocolFeeLibrary#fee_1_threshold)
  - [PIPS\_DENOMINATOR](https://docs.uniswap.org/contracts/v4/reference/core/libraries/ProtocolFeeLibrary#pips_denominator)
- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/libraries/ProtocolFeeLibrary#functions)
  - [getZeroForOneFee](https://docs.uniswap.org/contracts/v4/reference/core/libraries/ProtocolFeeLibrary#getzeroforonefee)
  - [getOneForZeroFee](https://docs.uniswap.org/contracts/v4/reference/core/libraries/ProtocolFeeLibrary#getoneforzerofee)
  - [isValidProtocolFee](https://docs.uniswap.org/contracts/v4/reference/core/libraries/ProtocolFeeLibrary#isvalidprotocolfee)
  - [calculateSwapFee](https://docs.uniswap.org/contracts/v4/reference/core/libraries/ProtocolFeeLibrary#calculateswapfee)