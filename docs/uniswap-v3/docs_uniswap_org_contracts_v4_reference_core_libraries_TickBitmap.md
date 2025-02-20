[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TickBitmap#)

On this page

# TickBitmap

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/libraries/TickBitmap.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

Stores a packed mapping of tick index to its initialized state

_The mapping uses int16 for keys since ticks are represented as int24 and there are 256 (2^8) values per word._

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TickBitmap\#functions "Direct link to heading")

### compress [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TickBitmap\#compress "Direct link to heading")

_round towards negative infinity_

```codeBlockLines_mRuA
function compress(int24 tick, int24 tickSpacing) internal pure returns (int24 compressed);

```

Copy

### position [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TickBitmap\#position "Direct link to heading")

Computes the position in the mapping where the initialized bit for a tick lives

```codeBlockLines_mRuA
function position(int24 tick) internal pure returns (int16 wordPos, uint8 bitPos);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `tick` | `int24` | The tick for which to compute the position |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `wordPos` | `int16` | The key in the mapping containing the word in which the bit is stored |
| `bitPos` | `uint8` | The bit position in the word where the flag is stored |

### flipTick [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TickBitmap\#fliptick "Direct link to heading")

Flips the initialized state for a given tick from false to true, or vice versa

```codeBlockLines_mRuA
function flipTick(mapping(int16 => uint256) storage self, int24 tick, int24 tickSpacing) internal;

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `self` | `mapping(int16 => uint256)` | The mapping in which to flip the tick |
| `tick` | `int24` | The tick to flip |
| `tickSpacing` | `int24` | The spacing between usable ticks |

### nextInitializedTickWithinOneWord [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TickBitmap\#nextinitializedtickwithinoneword "Direct link to heading")

Returns the next initialized tick contained in the same word (or adjacent word) as the tick that is either
to the left (less than or equal to) or right (greater than) of the given tick

```codeBlockLines_mRuA
function nextInitializedTickWithinOneWord(
    mapping(int16 => uint256) storage self,
    int24 tick,
    int24 tickSpacing,
    bool lte
) internal view returns (int24 next, bool initialized);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `self` | `mapping(int16 => uint256)` | The mapping in which to compute the next initialized tick |
| `tick` | `int24` | The starting tick |
| `tickSpacing` | `int24` | The spacing between usable ticks |
| `lte` | `bool` | Whether to search for the next initialized tick to the left (less than or equal to the starting tick) |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `next` | `int24` | The next initialized or uninitialized tick up to 256 ticks away from the current tick |
| `initialized` | `bool` | Whether the next tick is initialized, as the function only searches within up to 256 ticks |

## Errors [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TickBitmap\#errors "Direct link to heading")

### TickMisaligned [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TickBitmap\#tickmisaligned "Direct link to heading")

Thrown when the tick is not enumerated by the tick spacing

```codeBlockLines_mRuA
error TickMisaligned(int24 tick, int24 tickSpacing);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `tick` | `int24` | the invalid tick |
| `tickSpacing` | `int24` | The tick spacing of the pool |

- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TickBitmap#functions)
  - [compress](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TickBitmap#compress)
  - [position](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TickBitmap#position)
  - [flipTick](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TickBitmap#fliptick)
  - [nextInitializedTickWithinOneWord](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TickBitmap#nextinitializedtickwithinoneword)
- [Errors](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TickBitmap#errors)
  - [TickMisaligned](https://docs.uniswap.org/contracts/v4/reference/core/libraries/TickBitmap#tickmisaligned)