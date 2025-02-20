[Skip to main content](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/burn-liquidity#)

On this page

### Context [​](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/burn-liquidity\#context "Direct link to heading")

To liquidate a position, the _burn_ functionality can be invoked.
The funds in the position will be withdrawn and
all the information of the underlying token will be cleared.
Burning the position is a cost effective way to
exit as a liquidity provider.

### Setup [​](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/burn-liquidity\#setup "Direct link to heading")

See the [setup guide](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/setup-liquidity)

# Guide

Below is a step-by-step guide to burn a position.

### 1\. Import and define `IPositionManager` [​](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/burn-liquidity\#1-import-and-define-ipositionmanager "Direct link to heading")

```codeBlockLines_mRuA
import {IPositionManager} from "v4-periphery/src/interfaces/IPositionManager.sol";

// inside a contract, test, or foundry script:
IPositionManager posm = IPositionManager(<address>);

```

Copy

### 2\. Encode Actions [​](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/burn-liquidity\#2-encode-actions "Direct link to heading")

To burn a position, one action is required:

- burn operation - clears position entirely, withdrawing funds

```codeBlockLines_mRuA
import {Actions} from "v4-periphery/src/libraries/Actions.sol";

bytes memory actions = abi.encodePacked(Actions.BURN_POSITION);

```

Copy

### 3\. Encode Parameters [​](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/burn-liquidity\#3-encode-parameters "Direct link to heading")

```codeBlockLines_mRuA
bytes[] memory params = new bytes[](1);

```

Copy

The `BURN_POSITION` action requires the following parameters:

| Parameter | Type | Description |
| --- | --- | --- |
| `tokenId` | _uint256_ | position identifier |
| `amount0Min` | _uint128_ | the minimum amount of currency0 liquidity msg.sender is expecting to get back |
| `amount1Min` | _uint128_ | the minimum amount of currency1 liquidity msg.sender is expecting to get back |
| `hookData` | _bytes_ | arbitrary data that will be forwarded to hook functions |

```codeBlockLines_mRuA
params[0] = abi.encode(tokenId, amount0Min, amount1Min, hookData);

```

Copy

### 4\. Submit Call [​](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/burn-liquidity\#4-submit-call "Direct link to heading")

The entrypoint for all liquidity operations is `modifyLiquidities()`

```codeBlockLines_mRuA
uint256 deadline = block.timestamp + 60;

posm.modifyLiquidities(
    abi.encode(actions, params),
    deadline
);

```

Copy

- [Context](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/burn-liquidity#context)
- [Setup](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/burn-liquidity#setup)
- [1\. Import and define `IPositionManager`](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/burn-liquidity#1-import-and-define-ipositionmanager)
- [2\. Encode Actions](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/burn-liquidity#2-encode-actions)
- [3\. Encode Parameters](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/burn-liquidity#3-encode-parameters)
- [4\. Submit Call](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/burn-liquidity#4-submit-call)