[Skip to main content](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/batch-liquidity#)

On this page

### Context [​](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/batch-liquidity\#context "Direct link to heading")

As seen in previous guides, `PositionManager` is a command-based contract. This design is conducive to
batching complex liquidity operations. For example, developers can encode efficient logic to move
liquidity between two positions on entirely different Pools.

### Setup [​](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/batch-liquidity\#setup "Direct link to heading")

See the [setup guide](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/setup-liquidity)

# Guide

Below is a general reference guide for batch-operating on multiple liquidity positions, in _solidity_.
This guide does _not_ focus on a specific batch sequence, and is intended to be a general guide for `PositionManager`'s command-based interface.

### 1\. Encoded Actions [​](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/batch-liquidity\#1-encoded-actions "Direct link to heading")

Actions are divided into two types: _liquidity-operations_ and _delta-resolving_.

- _liquidity-operations_ \- actions which that incur a _balance-change_, a change in the pool's liquidity
- _delta-resolving_ \- actions which facilitate token transfers, such as _settling_ and _taking_

The _ordering_ of `actions` determines the sequence of operations. The minimum number of actions is roughly two actions; and the maximum is limited by block gas limit.
Additionally, _liquidity-operations_ do not have to happen prior to _delta-resolving_ actions. Developers can mix / alternate between
the two types of actions.

> **However** is good practice to perform _liquidity-operations_ before _delta-resolving_ actions. Minimizing token transfers
> and leveraging [_flash accounting_](https://docs.uniswap.org/contracts/v4/concepts/flash-accounting) is more gas efficient

Example: `Action.Y` happens after `Action.X` but before `Action.Z`

```codeBlockLines_mRuA
import {Actions} from "v4-periphery/src/libraries/Actions.sol";

bytes memory actions = abi.encodePacked(uint8(Actions.X), uint8(Actions.Y), uint8(Actions.Z), ...);

```

Copy

**A Note on Special Actions**:

`PositionManager` supports a few _delta-resolving_ actions beyond the standard `SETTLE` and `TAKE` actions

- `CLOSE_CURRENCY` \- automatically determines if a currency should be settled (paid) or taken. Used for cases where callers may not know the final delta
- `CLEAR_OR_TAKE`\- forfeit tokens if the amount is below a specified threshold, otherwise take the tokens. Used for cases where callers may expect to produce dust
- `SWEEP` \- return any excess token balances to a recipient. Used for cases where callers may conversatively overpay tokens

### 2\. Encoded Parameters [​](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/batch-liquidity\#2-encoded-parameters "Direct link to heading")

Each action has its own parameters to encode. Generally:

- _liquidity-operations_ \- encode tokenIds, liquidity amounts, and slippage

- _delta-resolving_ \- encode currencies, amounts, and recipients


Because actions are ordered, the parameters "zip" with their corresponding actions. The second parameter corresponds to the second action.
Every action has its own encoded parameters

```codeBlockLines_mRuA
bytes[] memory params = new bytes[](3);

params[0] = abi.encode(...); // parameters for the first action
params[1] = abi.encode(...); // parameters for the second action
params[2] = abi.encode(...); // parameters for the third action

```

Copy

### 3\. Submit Call [​](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/batch-liquidity\#3-submit-call "Direct link to heading")

The entrypoint for all liquidity operations is `modifyLiquidities()`

```codeBlockLines_mRuA
uint256 deadline = block.timestamp + 60;

posm.modifyLiquidities(
    abi.encode(actions, params),
    deadline
);

```

Copy

- [Context](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/batch-liquidity#context)
- [Setup](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/batch-liquidity#setup)
- [1\. Encoded Actions](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/batch-liquidity#1-encoded-actions)
- [2\. Encoded Parameters](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/batch-liquidity#2-encoded-parameters)
- [3\. Submit Call](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/batch-liquidity#3-submit-call)