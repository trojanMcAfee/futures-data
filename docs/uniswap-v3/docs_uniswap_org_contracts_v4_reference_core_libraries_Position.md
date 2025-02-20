[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Position#)

On this page

# Position

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/libraries/Position.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

Positions represent an owner address' liquidity between a lower and upper tick boundary

_Positions store additional state for tracking fees owed to the position_

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Position\#functions "Direct link to heading")

### get [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Position\#get "Direct link to heading")

Returns the State struct of a position, given an owner and position boundaries

```codeBlockLines_mRuA
function get(mapping(bytes32 => State) storage self, address owner, int24 tickLower, int24 tickUpper, bytes32 salt)
    internal
    view
    returns (State storage position);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `self` | `mapping(bytes32 => State)` | The mapping containing all user positions |
| `owner` | `address` | The address of the position owner |
| `tickLower` | `int24` | The lower tick boundary of the position |
| `tickUpper` | `int24` | The upper tick boundary of the position |
| `salt` | `bytes32` | A unique value to differentiate between multiple positions in the same range |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `position` | `State` | The position info struct of the given owners' position |

### calculatePositionKey [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Position\#calculatepositionkey "Direct link to heading")

A helper function to calculate the position key

```codeBlockLines_mRuA
function calculatePositionKey(address owner, int24 tickLower, int24 tickUpper, bytes32 salt)
    internal
    pure
    returns (bytes32 positionKey);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `owner` | `address` | The address of the position owner |
| `tickLower` | `int24` | the lower tick boundary of the position |
| `tickUpper` | `int24` | the upper tick boundary of the position |
| `salt` | `bytes32` | A unique value to differentiate between multiple positions in the same range, by the same owner. Passed in by the caller. |

### update [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Position\#update "Direct link to heading")

Credits accumulated fees to a user's position

```codeBlockLines_mRuA
function update(State storage self, int128 liquidityDelta, uint256 feeGrowthInside0X128, uint256 feeGrowthInside1X128)
    internal
    returns (uint256 feesOwed0, uint256 feesOwed1);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `self` | `State` | The individual position to update |
| `liquidityDelta` | `int128` | The change in pool liquidity as a result of the position update |
| `feeGrowthInside0X128` | `uint256` | The all-time fee growth in currency0, per unit of liquidity, inside the position's tick boundaries |
| `feeGrowthInside1X128` | `uint256` | The all-time fee growth in currency1, per unit of liquidity, inside the position's tick boundaries |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `feesOwed0` | `uint256` | The amount of currency0 owed to the position owner |
| `feesOwed1` | `uint256` | The amount of currency1 owed to the position owner |

## Errors [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Position\#errors "Direct link to heading")

### CannotUpdateEmptyPosition [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Position\#cannotupdateemptyposition "Direct link to heading")

Cannot update a position with no liquidity

```codeBlockLines_mRuA
error CannotUpdateEmptyPosition();

```

Copy

## Structs [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Position\#structs "Direct link to heading")

### State [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Position\#state "Direct link to heading")

```codeBlockLines_mRuA
struct State {
    uint128 liquidity;
    uint256 feeGrowthInside0LastX128;
    uint256 feeGrowthInside1LastX128;
}

```

Copy

- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Position#functions)
  - [get](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Position#get)
  - [calculatePositionKey](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Position#calculatepositionkey)
  - [update](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Position#update)
- [Errors](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Position#errors)
  - [CannotUpdateEmptyPosition](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Position#cannotupdateemptyposition)
- [Structs](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Position#structs)
  - [State](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Position#state)