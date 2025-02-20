[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/INotifier#)

On this page

# INotifier

[Git Source](https://github.com/uniswap/v4-periphery/blob/3f295d8435e4f776ea2daeb96ce1bc6d63f33fc7/src/interfaces/INotifier.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

This interface is used to opt in to sending updates to external contracts about position modifications or transfers

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/INotifier\#functions "Direct link to heading")

### subscriber [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/INotifier\#subscriber "Direct link to heading")

Returns the subscriber for a respective position

```codeBlockLines_mRuA
function subscriber(uint256 tokenId) external view returns (ISubscriber subscriber);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `tokenId` | `uint256` | the ERC721 tokenId |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `subscriber` | `ISubscriber` | the subscriber contract |

### subscribe [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/INotifier\#subscribe "Direct link to heading")

Enables the subscriber to receive notifications for a respective position

_Calling subscribe when a position is already subscribed will revert_

_payable so it can be multicalled with NATIVE related actions_

_will revert if pool manager is locked_

```codeBlockLines_mRuA
function subscribe(uint256 tokenId, address newSubscriber, bytes calldata data) external payable;

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `tokenId` | `uint256` | the ERC721 tokenId |
| `newSubscriber` | `address` | the address of the subscriber contract |
| `data` | `bytes` | caller-provided data that's forwarded to the subscriber contract |

### unsubscribe [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/INotifier\#unsubscribe "Direct link to heading")

Removes the subscriber from receiving notifications for a respective position

_Callers must specify a high gas limit (remaining gas should be higher than unsubscriberGasLimit) such that the subscriber can be notified_

_payable so it can be multicalled with NATIVE related actions_

_Must always allow a user to unsubscribe. In the case of a malicious subscriber, a user can always unsubscribe safely, ensuring liquidity is always modifiable._

_will revert if pool manager is locked_

```codeBlockLines_mRuA
function unsubscribe(uint256 tokenId) external payable;

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `tokenId` | `uint256` | the ERC721 tokenId |

### unsubscribeGasLimit [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/INotifier\#unsubscribegaslimit "Direct link to heading")

Returns and determines the maximum allowable gas-used for notifying unsubscribe

```codeBlockLines_mRuA
function unsubscribeGasLimit() external view returns (uint256);

```

Copy

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `uint256` | uint256 the maximum gas limit when notifying a subscriber's `notifyUnsubscribe` function |

## Events [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/INotifier\#events "Direct link to heading")

### Subscription [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/INotifier\#subscription "Direct link to heading")

Emitted on a successful call to subscribe

```codeBlockLines_mRuA
event Subscription(uint256 indexed tokenId, address indexed subscriber);

```

Copy

### Unsubscription [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/INotifier\#unsubscription "Direct link to heading")

Emitted on a successful call to unsubscribe

```codeBlockLines_mRuA
event Unsubscription(uint256 indexed tokenId, address indexed subscriber);

```

Copy

## Errors [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/INotifier\#errors "Direct link to heading")

### NotSubscribed [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/INotifier\#notsubscribed "Direct link to heading")

Thrown when unsubscribing without a subscriber

```codeBlockLines_mRuA
error NotSubscribed();

```

Copy

### NoCodeSubscriber [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/INotifier\#nocodesubscriber "Direct link to heading")

Thrown when a subscriber does not have code

```codeBlockLines_mRuA
error NoCodeSubscriber();

```

Copy

### GasLimitTooLow [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/INotifier\#gaslimittoolow "Direct link to heading")

Thrown when a user specifies a gas limit too low to avoid valid unsubscribe notifications

```codeBlockLines_mRuA
error GasLimitTooLow();

```

Copy

### SubscriptionReverted [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/INotifier\#subscriptionreverted "Direct link to heading")

Wraps the revert message of the subscriber contract on a reverting subscription

```codeBlockLines_mRuA
error SubscriptionReverted(address subscriber, bytes reason);

```

Copy

### ModifyLiquidityNotificationReverted [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/INotifier\#modifyliquiditynotificationreverted "Direct link to heading")

Wraps the revert message of the subscriber contract on a reverting modify liquidity notification

```codeBlockLines_mRuA
error ModifyLiquidityNotificationReverted(address subscriber, bytes reason);

```

Copy

### TransferNotificationReverted [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/INotifier\#transfernotificationreverted "Direct link to heading")

Wraps the revert message of the subscriber contract on a reverting transfer notification

```codeBlockLines_mRuA
error TransferNotificationReverted(address subscriber, bytes reason);

```

Copy

### AlreadySubscribed [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/INotifier\#alreadysubscribed "Direct link to heading")

Thrown when a tokenId already has a subscriber

```codeBlockLines_mRuA
error AlreadySubscribed(uint256 tokenId, address subscriber);

```

Copy

- [Functions](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/INotifier#functions)
  - [subscriber](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/INotifier#subscriber)
  - [subscribe](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/INotifier#subscribe)
  - [unsubscribe](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/INotifier#unsubscribe)
  - [unsubscribeGasLimit](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/INotifier#unsubscribegaslimit)
- [Events](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/INotifier#events)
  - [Subscription](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/INotifier#subscription)
  - [Unsubscription](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/INotifier#unsubscription)
- [Errors](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/INotifier#errors)
  - [NotSubscribed](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/INotifier#notsubscribed)
  - [NoCodeSubscriber](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/INotifier#nocodesubscriber)
  - [GasLimitTooLow](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/INotifier#gaslimittoolow)
  - [SubscriptionReverted](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/INotifier#subscriptionreverted)
  - [ModifyLiquidityNotificationReverted](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/INotifier#modifyliquiditynotificationreverted)
  - [TransferNotificationReverted](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/INotifier#transfernotificationreverted)
  - [AlreadySubscribed](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/INotifier#alreadysubscribed)