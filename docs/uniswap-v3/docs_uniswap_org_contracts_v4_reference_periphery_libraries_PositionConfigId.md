[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/PositionConfigId#)

On this page

# PositionConfigIdLibrary

[Git Source](https://github.com/uniswap/v4-periphery/blob/3f295d8435e4f776ea2daeb96ce1bc6d63f33fc7/src/libraries/PositionConfigId.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

## State Variables [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/PositionConfigId\#state-variables "Direct link to heading")

### MASK\_UPPER\_BIT [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/PositionConfigId\#mask_upper_bit "Direct link to heading")

```codeBlockLines_mRuA
bytes32 constant MASK_UPPER_BIT = 0x7FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF;

```

Copy

### DIRTY\_UPPER\_BIT [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/PositionConfigId\#dirty_upper_bit "Direct link to heading")

```codeBlockLines_mRuA
bytes32 constant DIRTY_UPPER_BIT = 0x8000000000000000000000000000000000000000000000000000000000000000;

```

Copy

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/PositionConfigId\#functions "Direct link to heading")

### getConfigId [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/PositionConfigId\#getconfigid "Direct link to heading")

returns the truncated hash of the PositionConfig for a given tokenId

```codeBlockLines_mRuA
function getConfigId(PositionConfigId storage _configId) internal view returns (bytes32 configId);

```

Copy

### setConfigId [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/PositionConfigId\#setconfigid "Direct link to heading")

_We only set the config on mint, guaranteeing that the most significant bit is unset, so we can just assign the entire 32 bytes to the id._

```codeBlockLines_mRuA
function setConfigId(PositionConfigId storage _configId, bytes32 configId) internal;

```

Copy

### setSubscribe [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/PositionConfigId\#setsubscribe "Direct link to heading")

```codeBlockLines_mRuA
function setSubscribe(PositionConfigId storage configId) internal;

```

Copy

### setUnsubscribe [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/PositionConfigId\#setunsubscribe "Direct link to heading")

```codeBlockLines_mRuA
function setUnsubscribe(PositionConfigId storage configId) internal;

```

Copy

### hasSubscriber [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/PositionConfigId\#hassubscriber "Direct link to heading")

```codeBlockLines_mRuA
function hasSubscriber(PositionConfigId storage configId) internal view returns (bool subscribed);

```

Copy

- [State Variables](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/PositionConfigId#state-variables)
  - [MASK\_UPPER\_BIT](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/PositionConfigId#mask_upper_bit)
  - [DIRTY\_UPPER\_BIT](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/PositionConfigId#dirty_upper_bit)
- [Functions](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/PositionConfigId#functions)
  - [getConfigId](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/PositionConfigId#getconfigid)
  - [setConfigId](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/PositionConfigId#setconfigid)
  - [setSubscribe](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/PositionConfigId#setsubscribe)
  - [setUnsubscribe](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/PositionConfigId#setunsubscribe)
  - [hasSubscriber](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/PositionConfigId#hassubscriber)