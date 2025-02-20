[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IPositionManager#)

On this page

# IPositionManager

[Git Source](https://github.com/uniswap/v4-periphery/blob/3f295d8435e4f776ea2daeb96ce1bc6d63f33fc7/src/interfaces/IPositionManager.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:** [INotifier](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/INotifier), [IImmutableState](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IImmutableState)

Interface for the PositionManager contract

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IPositionManager\#functions "Direct link to heading")

### modifyLiquidities [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IPositionManager\#modifyliquidities "Direct link to heading")

Unlocks Uniswap v4 PoolManager and batches actions for modifying liquidity

_This is the standard entrypoint for the PositionManager_

```codeBlockLines_mRuA
function modifyLiquidities(bytes calldata unlockData, uint256 deadline) external payable;

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `unlockData` | `bytes` | is an encoding of actions, and parameters for those actions |
| `deadline` | `uint256` | is the deadline for the batched actions to be executed |

### modifyLiquiditiesWithoutUnlock [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IPositionManager\#modifyliquiditieswithoutunlock "Direct link to heading")

Batches actions for modifying liquidity without unlocking v4 PoolManager

_This must be called by a contract that has already unlocked the v4 PoolManager_

```codeBlockLines_mRuA
function modifyLiquiditiesWithoutUnlock(bytes calldata actions, bytes[] calldata params) external payable;

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `actions` | `bytes` | the actions to perform |
| `params` | `bytes[]` | the parameters to provide for the actions |

### nextTokenId [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IPositionManager\#nexttokenid "Direct link to heading")

Used to get the ID that will be used for the next minted liquidity position

```codeBlockLines_mRuA
function nextTokenId() external view returns (uint256);

```

Copy

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `uint256` | uint256 The next token ID |

### getPositionLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IPositionManager\#getpositionliquidity "Direct link to heading")

_this value can be processed as an amount0 and amount1 by using the LiquidityAmounts library_

```codeBlockLines_mRuA
function getPositionLiquidity(uint256 tokenId) external view returns (uint128 liquidity);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `tokenId` | `uint256` | the ERC721 tokenId |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `liquidity` | `uint128` | the position's liquidity, as a liquidityAmount |

### getPoolAndPositionInfo [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IPositionManager\#getpoolandpositioninfo "Direct link to heading")

```codeBlockLines_mRuA
function getPoolAndPositionInfo(uint256 tokenId) external view returns (PoolKey memory, PositionInfo);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `tokenId` | `uint256` | the ERC721 tokenId |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `PoolKey` | PositionInfo a uint256 packed value holding information about the position including the range (tickLower, tickUpper) |
| `<none>` | `PositionInfo` | poolKey the pool key of the position |

## Errors [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IPositionManager\#errors "Direct link to heading")

### NotApproved [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IPositionManager\#notapproved "Direct link to heading")

Thrown when the caller is not approved to modify a position

```codeBlockLines_mRuA
error NotApproved(address caller);

```

Copy

### DeadlinePassed [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IPositionManager\#deadlinepassed "Direct link to heading")

Thrown when the block.timestamp exceeds the user-provided deadline

```codeBlockLines_mRuA
error DeadlinePassed(uint256 deadline);

```

Copy

### PoolManagerMustBeLocked [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IPositionManager\#poolmanagermustbelocked "Direct link to heading")

Thrown when calling transfer, subscribe, or unsubscribe when the PoolManager is unlocked.

_This is to prevent hooks from being able to trigger notifications at the same time the position is being modified._

```codeBlockLines_mRuA
error PoolManagerMustBeLocked();

```

Copy

- [Functions](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IPositionManager#functions)
  - [modifyLiquidities](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IPositionManager#modifyliquidities)
  - [modifyLiquiditiesWithoutUnlock](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IPositionManager#modifyliquiditieswithoutunlock)
  - [nextTokenId](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IPositionManager#nexttokenid)
  - [getPositionLiquidity](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IPositionManager#getpositionliquidity)
  - [getPoolAndPositionInfo](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IPositionManager#getpoolandpositioninfo)
- [Errors](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IPositionManager#errors)
  - [NotApproved](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IPositionManager#notapproved)
  - [DeadlinePassed](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IPositionManager#deadlinepassed)
  - [PoolManagerMustBeLocked](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IPositionManager#poolmanagermustbelocked)