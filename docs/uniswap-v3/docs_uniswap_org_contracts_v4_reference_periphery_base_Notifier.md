[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Notifier#)

On this page

# Notifier

[Git Source](https://github.com/uniswap/v4-periphery/blob/3f295d8435e4f776ea2daeb96ce1bc6d63f33fc7/src/base/Notifier.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:** [INotifier](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/INotifier)

Notifier is used to opt in to sending updates to external contracts about position modifications or transfers

## State Variables [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Notifier\#state-variables "Direct link to heading")

### NO\_SUBSCRIBER [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Notifier\#no_subscriber "Direct link to heading")

```codeBlockLines_mRuA
ISubscriber private constant NO_SUBSCRIBER = ISubscriber(address(0));

```

Copy

### unsubscribeGasLimit [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Notifier\#unsubscribegaslimit "Direct link to heading")

Returns and determines the maximum allowable gas-used for notifying unsubscribe

```codeBlockLines_mRuA
uint256 public immutable unsubscribeGasLimit;

```

Copy

### subscriber [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Notifier\#subscriber "Direct link to heading")

Returns the subscriber for a respective position

```codeBlockLines_mRuA
mapping(uint256 tokenId => ISubscriber subscriber) public subscriber;

```

Copy

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Notifier\#functions "Direct link to heading")

### constructor [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Notifier\#constructor "Direct link to heading")

```codeBlockLines_mRuA
constructor(uint256 _unsubscribeGasLimit);

```

Copy

### onlyIfApproved [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Notifier\#onlyifapproved "Direct link to heading")

Only allow callers that are approved as spenders or operators of the tokenId

_to be implemented by the parent contract (PositionManager)_

```codeBlockLines_mRuA
modifier onlyIfApproved(address caller, uint256 tokenId) virtual;

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `caller` | `address` | the address of the caller |
| `tokenId` | `uint256` | the tokenId of the position |

### onlyIfPoolManagerLocked [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Notifier\#onlyifpoolmanagerlocked "Direct link to heading")

Enforces that the PoolManager is locked.

```codeBlockLines_mRuA
modifier onlyIfPoolManagerLocked() virtual;

```

Copy

### \_setUnsubscribed [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Notifier\#_setunsubscribed "Direct link to heading")

```codeBlockLines_mRuA
function _setUnsubscribed(uint256 tokenId) internal virtual;

```

Copy

### \_setSubscribed [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Notifier\#_setsubscribed "Direct link to heading")

```codeBlockLines_mRuA
function _setSubscribed(uint256 tokenId) internal virtual;

```

Copy

### subscribe [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Notifier\#subscribe "Direct link to heading")

Enables the subscriber to receive notifications for a respective position

_Calling subscribe when a position is already subscribed will revert_

```codeBlockLines_mRuA
function subscribe(uint256 tokenId, address newSubscriber, bytes calldata data)
    external
    payable
    onlyIfPoolManagerLocked
    onlyIfApproved(msg.sender, tokenId);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `tokenId` | `uint256` | the ERC721 tokenId |
| `newSubscriber` | `address` | the address of the subscriber contract |
| `data` | `bytes` | caller-provided data that's forwarded to the subscriber contract |

### unsubscribe [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Notifier\#unsubscribe "Direct link to heading")

Removes the subscriber from receiving notifications for a respective position

_Callers must specify a high gas limit (remaining gas should be higher than unsubscriberGasLimit) such that the subscriber can be notified_

```codeBlockLines_mRuA
function unsubscribe(uint256 tokenId) external payable onlyIfPoolManagerLocked onlyIfApproved(msg.sender, tokenId);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `tokenId` | `uint256` | the ERC721 tokenId |

### \_unsubscribe [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Notifier\#_unsubscribe "Direct link to heading")

```codeBlockLines_mRuA
function _unsubscribe(uint256 tokenId) internal;

```

Copy

### \_notifyModifyLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Notifier\#_notifymodifyliquidity "Direct link to heading")

```codeBlockLines_mRuA
function _notifyModifyLiquidity(uint256 tokenId, int256 liquidityChange, BalanceDelta feesAccrued) internal;

```

Copy

### \_notifyTransfer [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Notifier\#_notifytransfer "Direct link to heading")

```codeBlockLines_mRuA
function _notifyTransfer(uint256 tokenId, address previousOwner, address newOwner) internal;

```

Copy

### \_call [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Notifier\#_call "Direct link to heading")

```codeBlockLines_mRuA
function _call(address target, bytes memory encodedCall) internal returns (bool success);

```

Copy

- [State Variables](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Notifier#state-variables)
  - [NO\_SUBSCRIBER](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Notifier#no_subscriber)
  - [unsubscribeGasLimit](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Notifier#unsubscribegaslimit)
  - [subscriber](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Notifier#subscriber)
- [Functions](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Notifier#functions)
  - [constructor](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Notifier#constructor)
  - [onlyIfApproved](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Notifier#onlyifapproved)
  - [onlyIfPoolManagerLocked](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Notifier#onlyifpoolmanagerlocked)
  - [\_setUnsubscribed](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Notifier#_setunsubscribed)
  - [\_setSubscribed](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Notifier#_setsubscribed)
  - [subscribe](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Notifier#subscribe)
  - [unsubscribe](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Notifier#unsubscribe)
  - [\_unsubscribe](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Notifier#_unsubscribe)
  - [\_notifyModifyLiquidity](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Notifier#_notifymodifyliquidity)
  - [\_notifyTransfer](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Notifier#_notifytransfer)
  - [\_call](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Notifier#_call)