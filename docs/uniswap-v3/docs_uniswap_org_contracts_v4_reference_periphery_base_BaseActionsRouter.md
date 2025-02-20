[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseActionsRouter#)

On this page

# BaseActionsRouter

[Git Source](https://github.com/uniswap/v4-periphery/blob/3f295d8435e4f776ea2daeb96ce1bc6d63f33fc7/src/base/BaseActionsRouter.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:** [SafeCallback](https://docs.uniswap.org/contracts/v4/reference/periphery/base/SafeCallback)

Abstract contract for performing a combination of actions on Uniswap v4.

_Suggested uint256 action values are defined in Actions.sol, however any definition can be used_

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseActionsRouter\#functions "Direct link to heading")

### constructor [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseActionsRouter\#constructor "Direct link to heading")

```codeBlockLines_mRuA
constructor(IPoolManager _poolManager) SafeCallback(_poolManager);

```

Copy

### \_executeActions [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseActionsRouter\#_executeactions "Direct link to heading")

internal function that triggers the execution of a set of actions on v4

_inheriting contracts should call this function to trigger execution_

```codeBlockLines_mRuA
function _executeActions(bytes calldata unlockData) internal;

```

Copy

### \_unlockCallback [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseActionsRouter\#_unlockcallback "Direct link to heading")

function that is called by the PoolManager through the SafeCallback.unlockCallback

```codeBlockLines_mRuA
function _unlockCallback(bytes calldata data) internal override returns (bytes memory);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `data` | `bytes` | Abi encoding of (bytes actions, bytes\[\] params) where params\[i\] is the encoded parameters for actions\[i\] |

### \_executeActionsWithoutUnlock [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseActionsRouter\#_executeactionswithoutunlock "Direct link to heading")

```codeBlockLines_mRuA
function _executeActionsWithoutUnlock(bytes calldata actions, bytes[] calldata params) internal;

```

Copy

### \_handleAction [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseActionsRouter\#_handleaction "Direct link to heading")

function to handle the parsing and execution of an action and its parameters

```codeBlockLines_mRuA
function _handleAction(uint256 action, bytes calldata params) internal virtual;

```

Copy

### msgSender [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseActionsRouter\#msgsender "Direct link to heading")

function that returns address considered executor of the actions

_The other context functions, \_msgData and \_msgValue, are not supported by this contract_
_In many contracts this will be the address that calls the initial entry point that calls `_executeActions` `msg.sender` shouldn't be used, as this will be the v4 pool manager contract that calls `unlockCallback`_
_If using ReentrancyLock.sol, this function can return \_getLocker()_

```codeBlockLines_mRuA
function msgSender() public view virtual returns (address);

```

Copy

### \_mapRecipient [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseActionsRouter\#_maprecipient "Direct link to heading")

Calculates the address for a action

```codeBlockLines_mRuA
function _mapRecipient(address recipient) internal view returns (address);

```

Copy

### \_mapPayer [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseActionsRouter\#_mappayer "Direct link to heading")

Calculates the payer for an action

```codeBlockLines_mRuA
function _mapPayer(bool payerIsUser) internal view returns (address);

```

Copy

## Errors [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseActionsRouter\#errors "Direct link to heading")

### InputLengthMismatch [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseActionsRouter\#inputlengthmismatch "Direct link to heading")

emitted when different numbers of parameters and actions are provided

```codeBlockLines_mRuA
error InputLengthMismatch();

```

Copy

### UnsupportedAction [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseActionsRouter\#unsupportedaction "Direct link to heading")

emitted when an inheriting contract does not support an action

```codeBlockLines_mRuA
error UnsupportedAction(uint256 action);

```

Copy

- [Functions](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseActionsRouter#functions)
  - [constructor](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseActionsRouter#constructor)
  - [\_executeActions](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseActionsRouter#_executeactions)
  - [\_unlockCallback](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseActionsRouter#_unlockcallback)
  - [\_executeActionsWithoutUnlock](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseActionsRouter#_executeactionswithoutunlock)
  - [\_handleAction](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseActionsRouter#_handleaction)
  - [msgSender](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseActionsRouter#msgsender)
  - [\_mapRecipient](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseActionsRouter#_maprecipient)
  - [\_mapPayer](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseActionsRouter#_mappayer)
- [Errors](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseActionsRouter#errors)
  - [InputLengthMismatch](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseActionsRouter#inputlengthmismatch)
  - [UnsupportedAction](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseActionsRouter#unsupportedaction)