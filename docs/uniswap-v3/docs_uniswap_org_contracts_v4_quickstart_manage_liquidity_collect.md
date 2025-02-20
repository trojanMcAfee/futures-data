[Skip to main content](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/collect#)

On this page

### Setup [​](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/collect\#setup "Direct link to heading")

See the [setup guide](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/setup-liquidity)

# Guide

In order to collect fees, the integrator must execute encoded actions
using the `PositionManager` contract. **Note** that there is no
`COLLECT` command, instead developers must decrease liquidity with a zero
liquidity change.

### 1\. Import and define `IPositionManager` [​](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/collect\#1-import-and-define-ipositionmanager "Direct link to heading")

```codeBlockLines_mRuA
import {IPositionManager} from "v4-periphery/src/interfaces/IPositionManager.sol";
// inside a contract, test, or foundry script:
IPositionManager posm = IPositionManager(<address>);

```

Copy

### 2\. Encode actions [​](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/collect\#2-encode-actions "Direct link to heading")

To collect fees, the following operations are required:

- decrease liquidity - collect fees from the core contract
- take pair - transfer the fee revenue, as both tokens, to a recipient

```codeBlockLines_mRuA
import {Actions} from "v4-periphery/src/libraries/Actions.sol";
bytes memory actions = abi.encodePacked(uint8(Actions.DECREASE_LIQUIDITY), uint8(Actions.TAKE_PAIR));

```

Copy

### 3\. Encode Parameters [​](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/collect\#3-encode-parameters "Direct link to heading")

```codeBlockLines_mRuA
bytes[] memory params = new bytes[](2);

```

Copy

The `DECREASE_LIQUIDITY` action requires the following parameters:

| Parameter | Type | Description |
| --- | --- | --- |
| `tokenId` | _uint256_ | position identifier |
| `liquidity` | _uint256_ | the amount of liquidity to withdraw |
| `amount0Min` | _uint128_ | the minimum amount of currency0 liquidity msg.sender is expecting to get back |
| `amount1Min` | _uint128_ | the minimum amount of currency1 liquidity msg.sender is expecting to get back |
| `hookData` | _bytes_ | arbitrary data that will be forwarded to hook functions |

**Note** that in order to collect fees we will default `liquidity`, `amount0Min` and `amount1Min` to 0.
Because fee collection can not be manipulated in a front-run attack, it is safe to set the slippage
values `amount0Min, amount1Min` to `0`.

```codeBlockLines_mRuA
/// @dev collecting fees is achieved with liquidity=0, the second parameter
params[0] = abi.encode(tokenId, 0, 0, 0, hookData);

```

Copy

The `TAKE_PAIR` action requires the following parameters:

- `currency0` \- _Currency_, one of the tokens to be paid by msg.sender
- `currency1` \- _Currency_, the other token to be paid by msg.sender
- `recipient` \- _address_, destination of the fee revenue for both tokens

```codeBlockLines_mRuA
Currency currency0 = Currency.wrap(<tokenAddress1>); // tokenAddress1 = 0 for native ETH
Currency currency1 = Currency.wrap(<tokenAddress2>);
params[1] = abi.encode(currency0, currency1, recipient);

```

Copy

### 4\. Submit Call [​](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/collect\#4-submit-call "Direct link to heading")

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

## Additional notes: [​](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/collect\#additional-notes "Direct link to heading")

- To obtain the amount of fees received, callers should read
token balances before and after the `.modifyLiquidities()` call.

- [Setup](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/collect#setup)
- [1\. Import and define `IPositionManager`](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/collect#1-import-and-define-ipositionmanager)
- [2\. Encode actions](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/collect#2-encode-actions)
- [3\. Encode Parameters](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/collect#3-encode-parameters)
- [4\. Submit Call](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/collect#4-submit-call)
- [Additional notes:](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/collect#additional-notes)