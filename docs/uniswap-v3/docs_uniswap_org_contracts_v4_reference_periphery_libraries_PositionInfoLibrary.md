[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/PositionInfoLibrary#)

# PositionInfo

[Git Source](https://github.com/uniswap/v4-periphery/blob/3f295d8435e4f776ea2daeb96ce1bc6d63f33fc7/src/libraries/PositionInfoLibrary.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

_PositionInfo is a packed version of solidity structure._
_Using the packaged version saves gas and memory by not storing the structure fields in memory slots._
_Layout:_
_200 bits poolId \| 24 bits tickUpper \| 24 bits tickLower \| 8 bits hasSubscriber_
_Fields in the direction from the least significant bit:_
_A flag to know if the tokenId is subscribed to an address_
_uint8 hasSubscriber;_
_The tickUpper of the position_
_int24 tickUpper;_
_The tickLower of the position_
_int24 tickLower;_
_The truncated poolId. Truncates a bytes32 value so the most signifcant (highest) 200 bits are used._
_bytes25 poolId;_
_Note: If more bits are needed, hasSubscriber can be a single bit._

```codeBlockLines_mRuA
type PositionInfo is uint256;

```

Copy