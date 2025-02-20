[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/ISubscriber#)

On this page

# ISubscriber

[Git Source](https://github.com/uniswap/v4-periphery/blob/3f295d8435e4f776ea2daeb96ce1bc6d63f33fc7/src/interfaces/ISubscriber.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

Interface that a Subscriber contract should implement to receive updates from the v4 position manager

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/ISubscriber\#functions "Direct link to heading")

### notifySubscribe [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/ISubscriber\#notifysubscribe "Direct link to heading")

```codeBlockLines_mRuA
function notifySubscribe(uint256 tokenId, bytes memory data) external;

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `tokenId` | `uint256` | the token ID of the position |
| `data` | `bytes` | additional data passed in by the caller |

### notifyUnsubscribe [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/ISubscriber\#notifyunsubscribe "Direct link to heading")

Called when a position unsubscribes from the subscriber

_This call's gas is capped at `unsubscribeGasLimit` (set at deployment)_

_Because of EIP-150, solidity may only allocate 63/64 of gasleft()_

```codeBlockLines_mRuA
function notifyUnsubscribe(uint256 tokenId) external;

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `tokenId` | `uint256` | the token ID of the position |

### notifyModifyLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/ISubscriber\#notifymodifyliquidity "Direct link to heading")

```codeBlockLines_mRuA
function notifyModifyLiquidity(uint256 tokenId, int256 liquidityChange, BalanceDelta feesAccrued) external;

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `tokenId` | `uint256` | the token ID of the position |
| `liquidityChange` | `int256` | the change in liquidity on the underlying position |
| `feesAccrued` | `BalanceDelta` | the fees to be collected from the position as a result of the modifyLiquidity call |

### notifyTransfer [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/ISubscriber\#notifytransfer "Direct link to heading")

```codeBlockLines_mRuA
function notifyTransfer(uint256 tokenId, address previousOwner, address newOwner) external;

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `tokenId` | `uint256` | the token ID of the position |
| `previousOwner` | `address` | address of the old owner |
| `newOwner` | `address` | address of the new owner |

- [Functions](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/ISubscriber#functions)
  - [notifySubscribe](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/ISubscriber#notifysubscribe)
  - [notifyUnsubscribe](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/ISubscriber#notifyunsubscribe)
  - [notifyModifyLiquidity](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/ISubscriber#notifymodifyliquidity)
  - [notifyTransfer](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/ISubscriber#notifytransfer)