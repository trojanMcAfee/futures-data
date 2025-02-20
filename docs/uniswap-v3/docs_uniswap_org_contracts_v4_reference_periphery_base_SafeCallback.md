[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/periphery/base/SafeCallback#)

On this page

# SafeCallback

[Git Source](https://github.com/uniswap/v4-periphery/blob/3f295d8435e4f776ea2daeb96ce1bc6d63f33fc7/src/base/SafeCallback.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:** [ImmutableState](https://docs.uniswap.org/contracts/v4/reference/periphery/base/ImmutableState), IUnlockCallback

A contract that only allows the Uniswap v4 PoolManager to call the unlockCallback

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/SafeCallback\#functions "Direct link to heading")

### constructor [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/SafeCallback\#constructor "Direct link to heading")

```codeBlockLines_mRuA
constructor(IPoolManager _poolManager) ImmutableState(_poolManager);

```

Copy

### onlyPoolManager [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/SafeCallback\#onlypoolmanager "Direct link to heading")

Only allow calls from the PoolManager contract

```codeBlockLines_mRuA
modifier onlyPoolManager();

```

Copy

### unlockCallback [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/SafeCallback\#unlockcallback "Direct link to heading")

Called by the pool manager on `msg.sender` when the manager is unlocked

_We force the onlyPoolManager modifier by exposing a virtual function after the onlyPoolManager check._

```codeBlockLines_mRuA
function unlockCallback(bytes calldata data) external onlyPoolManager returns (bytes memory);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `data` | `bytes` | The data that was passed to the call to unlock |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `bytes` | Any data that you want to be returned from the unlock call |

### \_unlockCallback [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/SafeCallback\#_unlockcallback "Direct link to heading")

_to be implemented by the child contract, to safely guarantee the logic is only executed by the PoolManager_

```codeBlockLines_mRuA
function _unlockCallback(bytes calldata data) internal virtual returns (bytes memory);

```

Copy

## Errors [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/SafeCallback\#errors "Direct link to heading")

### NotPoolManager [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/SafeCallback\#notpoolmanager "Direct link to heading")

Thrown when calling unlockCallback where the caller is not PoolManager

```codeBlockLines_mRuA
error NotPoolManager();

```

Copy

- [Functions](https://docs.uniswap.org/contracts/v4/reference/periphery/base/SafeCallback#functions)
  - [constructor](https://docs.uniswap.org/contracts/v4/reference/periphery/base/SafeCallback#constructor)
  - [onlyPoolManager](https://docs.uniswap.org/contracts/v4/reference/periphery/base/SafeCallback#onlypoolmanager)
  - [unlockCallback](https://docs.uniswap.org/contracts/v4/reference/periphery/base/SafeCallback#unlockcallback)
  - [\_unlockCallback](https://docs.uniswap.org/contracts/v4/reference/periphery/base/SafeCallback#_unlockcallback)
- [Errors](https://docs.uniswap.org/contracts/v4/reference/periphery/base/SafeCallback#errors)
  - [NotPoolManager](https://docs.uniswap.org/contracts/v4/reference/periphery/base/SafeCallback#notpoolmanager)