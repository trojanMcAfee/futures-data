[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager#)

On this page

# PositionManager

[Git Source](https://github.com/uniswap/v4-periphery/blob/3f295d8435e4f776ea2daeb96ce1bc6d63f33fc7/src/PositionManager.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:** [IPositionManager](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IPositionManager), [ERC721Permit\_v4](https://docs.uniswap.org/contracts/v4/reference/periphery/base/ERC721Permit_v4), [PoolInitializer](https://docs.uniswap.org/contracts/v4/reference/periphery/base/PoolInitializer), [Multicall\_v4](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Multicall_v4), [DeltaResolver](https://docs.uniswap.org/contracts/v4/reference/periphery/base/DeltaResolver), [ReentrancyLock](https://docs.uniswap.org/contracts/v4/reference/periphery/base/ReentrancyLock), [BaseActionsRouter](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseActionsRouter), [Notifier](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Notifier), [Permit2Forwarder](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Permit2Forwarder), [NativeWrapper](https://docs.uniswap.org/contracts/v4/reference/periphery/base/NativeWrapper)

The PositionManager (PosM) contract is responsible for creating liquidity positions on v4.
PosM mints and manages ERC721 tokens associated with each position.

## State Variables [​](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager\#state-variables "Direct link to heading")

### nextTokenId [​](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager\#nexttokenid "Direct link to heading")

Used to get the ID that will be used for the next minted liquidity position

_The ID of the next token that will be minted. Skips 0_

```codeBlockLines_mRuA
uint256 public nextTokenId = 1;

```

Copy

### tokenDescriptor [​](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager\#tokendescriptor "Direct link to heading")

```codeBlockLines_mRuA
IPositionDescriptor public immutable tokenDescriptor;

```

Copy

### positionInfo [​](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager\#positioninfo "Direct link to heading")

```codeBlockLines_mRuA
mapping(uint256 tokenId => PositionInfo info) public positionInfo;

```

Copy

### poolKeys [​](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager\#poolkeys "Direct link to heading")

```codeBlockLines_mRuA
mapping(bytes25 poolId => PoolKey poolKey) public poolKeys;

```

Copy

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager\#functions "Direct link to heading")

### constructor [​](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager\#constructor "Direct link to heading")

```codeBlockLines_mRuA
constructor(
    IPoolManager _poolManager,
    IAllowanceTransfer _permit2,
    uint256 _unsubscribeGasLimit,
    IPositionDescriptor _tokenDescriptor,
    IWETH9 _weth9
)
    BaseActionsRouter(_poolManager)
    Permit2Forwarder(_permit2)
    ERC721Permit_v4("Uniswap v4 Positions NFT", "UNI-V4-POSM")
    Notifier(_unsubscribeGasLimit)
    NativeWrapper(_weth9);

```

Copy

### checkDeadline [​](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager\#checkdeadline "Direct link to heading")

Reverts if the deadline has passed

```codeBlockLines_mRuA
modifier checkDeadline(uint256 deadline);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `deadline` | `uint256` | The timestamp at which the call is no longer valid, passed in by the caller |

### onlyIfApproved [​](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager\#onlyifapproved "Direct link to heading")

Reverts if the caller is not the owner or approved for the ERC721 token

_either msg.sender or msgSender() is passed in as the caller_
_msgSender() should ONLY be used if this is called from within the unlockCallback, unless the codepath has reentrancy protection_

```codeBlockLines_mRuA
modifier onlyIfApproved(address caller, uint256 tokenId) override;

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `caller` | `address` | The address of the caller |
| `tokenId` | `uint256` | the unique identifier of the ERC721 token |

### onlyIfPoolManagerLocked [​](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager\#onlyifpoolmanagerlocked "Direct link to heading")

Enforces that the PoolManager is locked.

```codeBlockLines_mRuA
modifier onlyIfPoolManagerLocked() override;

```

Copy

### tokenURI [​](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager\#tokenuri "Direct link to heading")

```codeBlockLines_mRuA
function tokenURI(uint256 tokenId) public view override returns (string memory);

```

Copy

### modifyLiquidities [​](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager\#modifyliquidities "Direct link to heading")

Unlocks Uniswap v4 PoolManager and batches actions for modifying liquidity

_This is the standard entrypoint for the PositionManager_

```codeBlockLines_mRuA
function modifyLiquidities(bytes calldata unlockData, uint256 deadline)
    external
    payable
    isNotLocked
    checkDeadline(deadline);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `unlockData` | `bytes` | is an encoding of actions, and parameters for those actions |
| `deadline` | `uint256` | is the deadline for the batched actions to be executed |

### modifyLiquiditiesWithoutUnlock [​](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager\#modifyliquiditieswithoutunlock "Direct link to heading")

Batches actions for modifying liquidity without unlocking v4 PoolManager

_This must be called by a contract that has already unlocked the v4 PoolManager_

```codeBlockLines_mRuA
function modifyLiquiditiesWithoutUnlock(bytes calldata actions, bytes[] calldata params) external payable isNotLocked;

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `actions` | `bytes` | the actions to perform |
| `params` | `bytes[]` | the parameters to provide for the actions |

### msgSender [​](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager\#msgsender "Direct link to heading")

function that returns address considered executor of the actions

_The other context functions, \_msgData and \_msgValue, are not supported by this contract_
_In many contracts this will be the address that calls the initial entry point that calls `_executeActions` `msg.sender` shouldn't be used, as this will be the v4 pool manager contract that calls `unlockCallback`_
_If using ReentrancyLock.sol, this function can return \_getLocker()_

```codeBlockLines_mRuA
function msgSender() public view override returns (address);

```

Copy

### \_handleAction [​](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager\#_handleaction "Direct link to heading")

```codeBlockLines_mRuA
function _handleAction(uint256 action, bytes calldata params) internal virtual override;

```

Copy

### \_increase [​](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager\#_increase "Direct link to heading")

_Calling increase with 0 liquidity will credit the caller with any underlying fees of the position_

```codeBlockLines_mRuA
function _increase(uint256 tokenId, uint256 liquidity, uint128 amount0Max, uint128 amount1Max, bytes calldata hookData)
    internal
    onlyIfApproved(msgSender(), tokenId);

```

Copy

### \_decrease [​](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager\#_decrease "Direct link to heading")

_Calling decrease with 0 liquidity will credit the caller with any underlying fees of the position_

```codeBlockLines_mRuA
function _decrease(uint256 tokenId, uint256 liquidity, uint128 amount0Min, uint128 amount1Min, bytes calldata hookData)
    internal
    onlyIfApproved(msgSender(), tokenId);

```

Copy

### \_mint [​](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager\#_mint "Direct link to heading")

```codeBlockLines_mRuA
function _mint(
    PoolKey calldata poolKey,
    int24 tickLower,
    int24 tickUpper,
    uint256 liquidity,
    uint128 amount0Max,
    uint128 amount1Max,
    address owner,
    bytes calldata hookData
) internal;

```

Copy

### \_burn [​](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager\#_burn "Direct link to heading")

_this is overloaded with ERC721Permit\_v4.\_burn_

```codeBlockLines_mRuA
function _burn(uint256 tokenId, uint128 amount0Min, uint128 amount1Min, bytes calldata hookData)
    internal
    onlyIfApproved(msgSender(), tokenId);

```

Copy

### \_settlePair [​](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager\#_settlepair "Direct link to heading")

```codeBlockLines_mRuA
function _settlePair(Currency currency0, Currency currency1) internal;

```

Copy

### \_takePair [​](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager\#_takepair "Direct link to heading")

```codeBlockLines_mRuA
function _takePair(Currency currency0, Currency currency1, address recipient) internal;

```

Copy

### \_close [​](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager\#_close "Direct link to heading")

```codeBlockLines_mRuA
function _close(Currency currency) internal;

```

Copy

### \_clearOrTake [​](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager\#_clearortake "Direct link to heading")

_integrators may elect to forfeit positive deltas with clear_
_if the forfeit amount exceeds the user-specified max, the amount is taken instead_

```codeBlockLines_mRuA
function _clearOrTake(Currency currency, uint256 amountMax) internal;

```

Copy

### \_sweep [​](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager\#_sweep "Direct link to heading")

Sweeps the entire contract balance of specified currency to the recipient

```codeBlockLines_mRuA
function _sweep(Currency currency, address to) internal;

```

Copy

### \_modifyLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager\#_modifyliquidity "Direct link to heading")

```codeBlockLines_mRuA
function _modifyLiquidity(
    PositionInfo info,
    PoolKey memory poolKey,
    int256 liquidityChange,
    bytes32 salt,
    bytes calldata hookData
) internal returns (BalanceDelta liquidityDelta, BalanceDelta feesAccrued);

```

Copy

### \_pay [​](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager\#_pay "Direct link to heading")

```codeBlockLines_mRuA
function _pay(Currency currency, address payer, uint256 amount) internal override;

```

Copy

### \_setSubscribed [​](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager\#_setsubscribed "Direct link to heading")

an internal helper used by Notifier

```codeBlockLines_mRuA
function _setSubscribed(uint256 tokenId) internal override;

```

Copy

### \_setUnsubscribed [​](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager\#_setunsubscribed "Direct link to heading")

an internal helper used by Notifier

```codeBlockLines_mRuA
function _setUnsubscribed(uint256 tokenId) internal override;

```

Copy

### transferFrom [​](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager\#transferfrom "Direct link to heading")

_overrides solmate transferFrom in case a notification to subscribers is needed_

_will revert if pool manager is locked_

```codeBlockLines_mRuA
function transferFrom(address from, address to, uint256 id) public virtual override onlyIfPoolManagerLocked;

```

Copy

### getPoolAndPositionInfo [​](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager\#getpoolandpositioninfo "Direct link to heading")

```codeBlockLines_mRuA
function getPoolAndPositionInfo(uint256 tokenId) public view returns (PoolKey memory poolKey, PositionInfo info);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `tokenId` | `uint256` | the ERC721 tokenId |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `poolKey` | `PoolKey` | the pool key of the position |
| `info` | `PositionInfo` | poolKey the pool key of the position |

### getPositionLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager\#getpositionliquidity "Direct link to heading")

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

### \_getLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager\#_getliquidity "Direct link to heading")

```codeBlockLines_mRuA
function _getLiquidity(uint256 tokenId, PoolKey memory poolKey, int24 tickLower, int24 tickUpper)
    internal
    view
    returns (uint128 liquidity);

```

Copy

- [State Variables](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager#state-variables)
  - [nextTokenId](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager#nexttokenid)
  - [tokenDescriptor](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager#tokendescriptor)
  - [positionInfo](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager#positioninfo)
  - [poolKeys](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager#poolkeys)
- [Functions](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager#functions)
  - [constructor](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager#constructor)
  - [checkDeadline](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager#checkdeadline)
  - [onlyIfApproved](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager#onlyifapproved)
  - [onlyIfPoolManagerLocked](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager#onlyifpoolmanagerlocked)
  - [tokenURI](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager#tokenuri)
  - [modifyLiquidities](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager#modifyliquidities)
  - [modifyLiquiditiesWithoutUnlock](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager#modifyliquiditieswithoutunlock)
  - [msgSender](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager#msgsender)
  - [\_handleAction](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager#_handleaction)
  - [\_increase](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager#_increase)
  - [\_decrease](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager#_decrease)
  - [\_mint](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager#_mint)
  - [\_burn](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager#_burn)
  - [\_settlePair](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager#_settlepair)
  - [\_takePair](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager#_takepair)
  - [\_close](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager#_close)
  - [\_clearOrTake](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager#_clearortake)
  - [\_sweep](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager#_sweep)
  - [\_modifyLiquidity](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager#_modifyliquidity)
  - [\_pay](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager#_pay)
  - [\_setSubscribed](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager#_setsubscribed)
  - [\_setUnsubscribed](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager#_setunsubscribed)
  - [transferFrom](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager#transferfrom)
  - [getPoolAndPositionInfo](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager#getpoolandpositioninfo)
  - [getPositionLiquidity](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager#getpositionliquidity)
  - [\_getLiquidity](https://docs.uniswap.org/contracts/v4/reference/periphery/PositionManager#_getliquidity)