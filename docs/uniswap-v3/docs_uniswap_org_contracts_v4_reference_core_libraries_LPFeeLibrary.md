[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/libraries/LPFeeLibrary#)

On this page

# LPFeeLibrary

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/libraries/LPFeeLibrary.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

Library of helper functions for a pools LP fee

## State Variables [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/LPFeeLibrary\#state-variables "Direct link to heading")

### DYNAMIC\_FEE\_FLAG [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/LPFeeLibrary\#dynamic_fee_flag "Direct link to heading")

An lp fee of exactly 0b1000000... signals a dynamic fee pool. This isn't a valid static fee as it is > MAX\_LP\_FEE

```codeBlockLines_mRuA
uint24 public constant DYNAMIC_FEE_FLAG = 0x800000;

```

Copy

### OVERRIDE\_FEE\_FLAG [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/LPFeeLibrary\#override_fee_flag "Direct link to heading")

the second bit of the fee returned by beforeSwap is used to signal if the stored LP fee should be overridden in this swap

```codeBlockLines_mRuA
uint24 public constant OVERRIDE_FEE_FLAG = 0x400000;

```

Copy

### REMOVE\_OVERRIDE\_MASK [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/LPFeeLibrary\#remove_override_mask "Direct link to heading")

mask to remove the override fee flag from a fee returned by the beforeSwaphook

```codeBlockLines_mRuA
uint24 public constant REMOVE_OVERRIDE_MASK = 0xBFFFFF;

```

Copy

### MAX\_LP\_FEE [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/LPFeeLibrary\#max_lp_fee "Direct link to heading")

the lp fee is represented in hundredths of a bip, so the max is 100%

```codeBlockLines_mRuA
uint24 public constant MAX_LP_FEE = 1000000;

```

Copy

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/LPFeeLibrary\#functions "Direct link to heading")

### isDynamicFee [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/LPFeeLibrary\#isdynamicfee "Direct link to heading")

returns true if a pool's LP fee signals that the pool has a dynamic fee

```codeBlockLines_mRuA
function isDynamicFee(uint24 self) internal pure returns (bool);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `self` | `uint24` | The fee to check |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `bool` | bool True of the fee is dynamic |

### isValid [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/LPFeeLibrary\#isvalid "Direct link to heading")

returns true if an LP fee is valid, aka not above the maximum permitted fee

```codeBlockLines_mRuA
function isValid(uint24 self) internal pure returns (bool);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `self` | `uint24` | The fee to check |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `bool` | bool True of the fee is valid |

### validate [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/LPFeeLibrary\#validate "Direct link to heading")

validates whether an LP fee is larger than the maximum, and reverts if invalid

```codeBlockLines_mRuA
function validate(uint24 self) internal pure;

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `self` | `uint24` | The fee to validate |

### getInitialLPFee [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/LPFeeLibrary\#getinitiallpfee "Direct link to heading")

gets and validates the initial LP fee for a pool. Dynamic fee pools have an initial fee of 0.

_if a dynamic fee pool wants a non-0 initial fee, it should call `updateDynamicLPFee` in the afterInitialize hook_

```codeBlockLines_mRuA
function getInitialLPFee(uint24 self) internal pure returns (uint24);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `self` | `uint24` | The fee to get the initial LP from |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `uint24` | initialFee 0 if the fee is dynamic, otherwise the fee (if valid) |

### isOverride [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/LPFeeLibrary\#isoverride "Direct link to heading")

returns true if the fee has the override flag set (2nd highest bit of the uint24)

```codeBlockLines_mRuA
function isOverride(uint24 self) internal pure returns (bool);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `self` | `uint24` | The fee to check |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `bool` | bool True of the fee has the override flag set |

### removeOverrideFlag [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/LPFeeLibrary\#removeoverrideflag "Direct link to heading")

returns a fee with the override flag removed

```codeBlockLines_mRuA
function removeOverrideFlag(uint24 self) internal pure returns (uint24);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `self` | `uint24` | The fee to remove the override flag from |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `uint24` | fee The fee without the override flag set |

### removeOverrideFlagAndValidate [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/LPFeeLibrary\#removeoverrideflagandvalidate "Direct link to heading")

Removes the override flag and validates the fee (reverts if the fee is too large)

```codeBlockLines_mRuA
function removeOverrideFlagAndValidate(uint24 self) internal pure returns (uint24 fee);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `self` | `uint24` | The fee to remove the override flag from, and then validate |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `fee` | `uint24` | The fee without the override flag set (if valid) |

## Errors [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/LPFeeLibrary\#errors "Direct link to heading")

### LPFeeTooLarge [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/LPFeeLibrary\#lpfeetoolarge "Direct link to heading")

Thrown when the static or dynamic fee on a pool exceeds 100%.

```codeBlockLines_mRuA
error LPFeeTooLarge(uint24 fee);

```

Copy

- [State Variables](https://docs.uniswap.org/contracts/v4/reference/core/libraries/LPFeeLibrary#state-variables)
  - [DYNAMIC\_FEE\_FLAG](https://docs.uniswap.org/contracts/v4/reference/core/libraries/LPFeeLibrary#dynamic_fee_flag)
  - [OVERRIDE\_FEE\_FLAG](https://docs.uniswap.org/contracts/v4/reference/core/libraries/LPFeeLibrary#override_fee_flag)
  - [REMOVE\_OVERRIDE\_MASK](https://docs.uniswap.org/contracts/v4/reference/core/libraries/LPFeeLibrary#remove_override_mask)
  - [MAX\_LP\_FEE](https://docs.uniswap.org/contracts/v4/reference/core/libraries/LPFeeLibrary#max_lp_fee)
- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/libraries/LPFeeLibrary#functions)
  - [isDynamicFee](https://docs.uniswap.org/contracts/v4/reference/core/libraries/LPFeeLibrary#isdynamicfee)
  - [isValid](https://docs.uniswap.org/contracts/v4/reference/core/libraries/LPFeeLibrary#isvalid)
  - [validate](https://docs.uniswap.org/contracts/v4/reference/core/libraries/LPFeeLibrary#validate)
  - [getInitialLPFee](https://docs.uniswap.org/contracts/v4/reference/core/libraries/LPFeeLibrary#getinitiallpfee)
  - [isOverride](https://docs.uniswap.org/contracts/v4/reference/core/libraries/LPFeeLibrary#isoverride)
  - [removeOverrideFlag](https://docs.uniswap.org/contracts/v4/reference/core/libraries/LPFeeLibrary#removeoverrideflag)
  - [removeOverrideFlagAndValidate](https://docs.uniswap.org/contracts/v4/reference/core/libraries/LPFeeLibrary#removeoverrideflagandvalidate)
- [Errors](https://docs.uniswap.org/contracts/v4/reference/core/libraries/LPFeeLibrary#errors)
  - [LPFeeTooLarge](https://docs.uniswap.org/contracts/v4/reference/core/libraries/LPFeeLibrary#lpfeetoolarge)