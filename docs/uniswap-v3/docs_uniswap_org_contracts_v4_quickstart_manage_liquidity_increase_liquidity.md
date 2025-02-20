[Skip to main content](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/increase-liquidity#)

On this page

### Context [​](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/increase-liquidity\#context "Direct link to heading")

Please note that `PositionManager` is a command-based contract, where integrators will be encoding commands and their corresponding
parameters.

Increasing liquidity assumes the position already exists and the user wants to add more tokens to the position.

### Setup [​](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/increase-liquidity\#setup "Direct link to heading")

See the [setup guide](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/setup-liquidity)

# Guide

Below is a step-by-step guide for increasing a position's liquidity, in _solidity_.

### 1\. Import and define `IPositionManager` [​](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/increase-liquidity\#1-import-and-define-ipositionmanager "Direct link to heading")

```codeBlockLines_mRuA
import {IPositionManager} from "v4-periphery/src/interfaces/IPositionManager.sol";

// inside a contract, test, or foundry script:
IPositionManager posm = IPositionManager(<address>);

```

Copy

### 2\. Encode Actions [​](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/increase-liquidity\#2-encode-actions "Direct link to heading")

To increase a position's liquidity, the first action must be:

- _increase_ operation - the addition of liquidity to an existing position.

For _delta resolving_ operations, developers may need to choose between `SETTLE_PAIR`, `CLOSE_CURRENCY`, or `CLEAR_OR_TAKE` actions.

> In Uniswap v4, fee revenue is automatically credited to a position on increasing liquidity

> There are some cases, where the fee revenue can entirely "pay" for a liquidity increase, and remainder tokens need to be collected

If increasing the liquidity requires the transfer of both tokens:

- _settle pair_ \- pays a pair of tokens, to increase liquidity

Otherwise:

- _close currency_ \- automatically determines if a currency should be settled or taken.
- OR _clear or take_ \- if the token amount to-be-collected is below a threshold, opt to forfeit the dust. Otherwise, claim the tokens

```codeBlockLines_mRuA
import {Actions} from "v4-periphery/src/libraries/Actions.sol";

```

Copy

If both tokens need to be sent:

```codeBlockLines_mRuA
bytes memory actions = abi.encodePacked(uint8(Actions.INCREASE_LIQUIDITY), uint8(Actions.SETTLE_PAIR));

```

Copy

If converting fees to liquidity, and expect excess fees to be collected

```codeBlockLines_mRuA
bytes memory actions = abi.encodePacked(uint8(Actions.INCREASE_LIQUIDITY), uint8(Actions.CLOSE_CURRENCY), uint8(Actions.CLOSE_CURRENCY));

```

Copy

If converting fees to liquidity, forfeiting dust:

```codeBlockLines_mRuA
bytes memory actions = abi.encodePacked(uint8(Actions.INCREASE_LIQUIDITY), uint8(Actions.CLEAR_OR_TAKE), uint8(Actions.CLEAR_OR_TAKE));

```

Copy

### 3\. Encoded Parameters [​](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/increase-liquidity\#3-encoded-parameters "Direct link to heading")

When settling pair:

```codeBlockLines_mRuA
bytes[] memory params = new bytes[](2);

```

Copy

Otherwise:

```codeBlockLines_mRuA
bytes[] memory params = new bytes[](3);

```

Copy

The `INCREASE_LIQUIDITY` action requires the following parameters:

| Parameter | Type | Description |
| --- | --- | --- |
| `tokenId` | _uint256_ | position identifier |
| `liquidity` | _uint256_ | the amount of liquidity to add |
| `amount0Max` | _uint128_ | the maximum amount of currency0 liquidity msg.sender is willing to pay |
| `amount1Max` | _uint128_ | the maximum amount of currency1 liquidity msg.sender is willing to pay |
| `hookData` | _bytes_ | arbitrary data that will be forwarded to hook functions |

```codeBlockLines_mRuA
params[0] = abi.encode(tokenId, liquidity, amount0Max, amount1Max, hookData);

```

Copy

The `SETTLE_PAIR` action requires the following parameters:

- `currency0` \- _Currency_, one of the tokens to be paid by msg.sender
- `currency1` \- _Currency_, the other token to be paid by msg.sender

In the above case, the parameter encoding is:

```codeBlockLines_mRuA
Currency currency0 = Currency.wrap(<tokenAddress1>); // tokenAddress1 = 0 for native ETH
Currency currency1 = Currency.wrap(<tokenAddress2>);
params[1] = abi.encode(currency0, currency1);

```

Copy

The `CLOSE_CURRENCY` action requires only one `currency` parameter
and the encoding is:

```codeBlockLines_mRuA
params[1] = abi.encode(currency0)
params[2] = abi.encode(currency1)

```

Copy

The `CLEAR_OR_TAKE` action requires one `currency` and:

- `amountMax` \- _uint256_, the maximum threshold to concede dust,
otherwise taking the dust.

In this case, the parameter encoding is:

```codeBlockLines_mRuA
params[1] = abi.encode(currency0, amount0Max);
params[2] = abi.encode(currency1, amount1Max);

```

Copy

### 4\. Submit Call [​](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/increase-liquidity\#4-submit-call "Direct link to heading")

The entrypoint for all liquidity operations is `modifyLiquidities()`.

```codeBlockLines_mRuA
uint256 deadline = block.timestamp + 60;

uint256 valueToPass = currency0.isAddressZero() ? amount0Max : 0;

posm.modifyLiquidities{value: valueToPass}(
    abi.encode(actions, params),
    deadline
);

```

Copy

- [Context](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/increase-liquidity#context)
- [Setup](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/increase-liquidity#setup)
- [1\. Import and define `IPositionManager`](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/increase-liquidity#1-import-and-define-ipositionmanager)
- [2\. Encode Actions](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/increase-liquidity#2-encode-actions)
- [3\. Encoded Parameters](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/increase-liquidity#3-encoded-parameters)
- [4\. Submit Call](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/increase-liquidity#4-submit-call)