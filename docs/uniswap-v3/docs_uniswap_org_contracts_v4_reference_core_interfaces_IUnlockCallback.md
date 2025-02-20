[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IUnlockCallback#)

On this page

# IUnlockCallback

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/interfaces/callback/IUnlockCallback.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

Interface for the callback executed when an address unlocks the pool manager

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IUnlockCallback\#functions "Direct link to heading")

### unlockCallback [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IUnlockCallback\#unlockcallback "Direct link to heading")

Called by the pool manager on `msg.sender` when the manager is unlocked

```codeBlockLines_mRuA
function unlockCallback(bytes calldata data) external returns (bytes memory);

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

- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IUnlockCallback#functions)
  - [unlockCallback](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IUnlockCallback#unlockcallback)