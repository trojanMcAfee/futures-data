[Skip to main content](https://docs.uniswap.org/contracts/v4/quickstart/subscriber#)

On this page

# Context

For developers looking to support custom _liquidity mining_, Subscriber contracts can be used to receive notifications about position modifications or transfers.

# Guide

## 1\. Implement the [`ISubscriber`](https://github.com/Uniswap/v4-periphery/blob/main/src/interfaces/ISubscriber.sol) interface [​](https://docs.uniswap.org/contracts/v4/quickstart/subscriber\#1-implement-the-isubscriber-interface "Direct link to heading")

Can also refer to [MockSubscriber](https://github.com/Uniswap/v4-periphery/blob/main/test/mocks/MockSubscriber.sol) for an actual implementation example.

```codeBlockLines_mRuA
import {ISubscriber} from "v4-periphery/src/interfaces/ISubscriber.sol";

contract MySubscriber is ISubscriber {
    uint256 public notifySubscribeCount;
    uint256 public notifyUnsubscribeCount;
    uint256 public notifyModifyLiquidityCount;
    uint256 public notifyBurnCount;
    // other implementations...

    function notifySubscribe(uint256, bytes memory) external onlyByPosm {
        notifySubscribeCount++;
    }

    function notifyUnsubscribe(uint256) external onlyByPosm {
        notifyUnsubscribeCount++;
    }

    function notifyModifyLiquidity(uint256, int256, BalanceDelta) external onlyByPosm {
        notifyModifyLiquidityCount++;
    }

    function notifyBurn(uint256, address, PositionInfo, uint256, BalanceDelta)
        external
        onlyByPosm
    {
        notifyBurnCount++;
    }
}

```

Copy

## 2\. A caveat on `unsubscribe()` [​](https://docs.uniswap.org/contracts/v4/quickstart/subscriber\#2-a-caveat-on-unsubscribe "Direct link to heading")

There is a variable [`unsubscribeGasLimit`](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/INotifier#unsubscribegaslimit) specifically set at deployment of `PositionManager` to prevent gas griefing on `unsubscribe()` \- which could result in the subscriber contract not being notified during `unsubscribe()`.

If notifying the subscriber contract is not necessary users can still specify a gas limit where `notifyUnsubscribe()` hits `OutOfGas` and reverts yet the unsubscription will still succeed.

From [`_unsubscribe()`](https://github.com/Uniswap/v4-periphery/blob/main/src/base/Notifier.sol#L80) on `Notifier`:

```codeBlockLines_mRuA
if (address(_subscriber).code.length > 0) {
    // require that the remaining gas is sufficient to notify the subscriber
    // otherwise, users can select a gas limit where .notifyUnsubscribe hits OutOfGas yet the
    // transaction/unsubscription can still succee
    if (gasleft() < unsubscribeGasLimit) GasLimitTooLow.selector.revertWith();
    try _subscriber.notifyUnsubscribe{gas: unsubscribeGasLimit}(tokenId) {} catch {}
}

```

Copy

## 3\. Opt-in to a subscriber contract [​](https://docs.uniswap.org/contracts/v4/quickstart/subscriber\#3-opt-in-to-a-subscriber-contract "Direct link to heading")

To opt-in to a subscriber contract, call [`subscribe()`](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/INotifier#subscribe) on `PositionManager`.

```codeBlockLines_mRuA
import {IPositionManager} from "v4-periphery/src/interfaces/IPositionManager.sol";

IPositionManager posm = IPositionManager(<address>);
ISubscriber mySubscriber = ISubscriber(<address>);

bytes memory optionalData = ...;
posm.subscribe(tokenId, mySubscriber, optionalData);

```

Copy

- [1\. Implement the `ISubscriber` interface](https://docs.uniswap.org/contracts/v4/quickstart/subscriber#1-implement-the-isubscriber-interface)
- [2\. A caveat on `unsubscribe()`](https://docs.uniswap.org/contracts/v4/quickstart/subscriber#2-a-caveat-on-unsubscribe)
- [3\. Opt-in to a subscriber contract](https://docs.uniswap.org/contracts/v4/quickstart/subscriber#3-opt-in-to-a-subscriber-contract)