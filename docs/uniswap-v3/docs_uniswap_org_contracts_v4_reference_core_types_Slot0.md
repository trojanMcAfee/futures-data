[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/types/Slot0#)

# Slot0

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/types/Slot0.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

_Slot0 is a packed version of solidity structure._
_Using the packaged version saves gas by not storing the structure fields in memory slots._
_Layout:_
_24 bits empty \| 24 bits lpFee \| 12 bits protocolFee 1->0 \| 12 bits protocolFee 0->1 \| 24 bits tick \| 160 bits sqrtPriceX96_
_Fields in the direction from the least significant bit:_
_The current price_
_uint160 sqrtPriceX96;_
_The current tick_
_int24 tick;_
_Protocol fee, expressed in hundredths of a bip, upper 12 bits are for 1->0, and the lower 12 are for 0->1_
_the maximum is 1000 - meaning the maximum protocol fee is 0.1%_
_the protocolFee is taken from the input first, then the lpFee is taken from the remaining input_
_uint24 protocolFee;_
_The current LP fee of the pool. If the pool is dynamic, this does not include the dynamic fee flag._
_uint24 lpFee;_

```codeBlockLines_mRuA
type Slot0 is bytes32;

```

Copy