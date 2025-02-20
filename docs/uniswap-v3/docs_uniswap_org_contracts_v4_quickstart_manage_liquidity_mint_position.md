[Skip to main content](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/mint-position#)

On this page

Similar to Uniswap v3, liquidity positions are minted as ERC-721 tokens and depend on a _periphery_ contract.
v4's `PositionManager` contract will facilitate liquidity management

### Context [​](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/mint-position\#context "Direct link to heading")

Please note that `PositionManager` is a command-based contract, where integrators will be encoding commands and their corresponding
parameters.

### Setup [​](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/mint-position\#setup "Direct link to heading")

See the [setup guide](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/setup-liquidity)

# Guide

Below is a step-by-step guide for minting a v4 liquidity position, in _solidity_

### 1\. Import and define `IPositionManager` [​](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/mint-position\#1-import-and-define-ipositionmanager "Direct link to heading")

```codeBlockLines_mRuA
import {IPositionManager} from "v4-periphery/src/interfaces/IPositionManager.sol";

// inside a contract, test, or foundry script:
IPositionManager posm = IPositionManager(<address>);

```

Copy

### 2\. Encode Actions [​](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/mint-position\#2-encode-actions "Direct link to heading")

To mint a position, two actions are required:

- mint operation - the creation of the liquidity position
- settle pair - the two tokens to be paid by msg.sender

```codeBlockLines_mRuA
import {Actions} from "v4-periphery/src/libraries/Actions.sol";

bytes memory actions = abi.encodePacked(uint8(Actions.MINT_POSITION), uint8(Actions.SETTLE_PAIR));

```

Copy

### 3\. Encode Parameters [​](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/mint-position\#3-encode-parameters "Direct link to heading")

```codeBlockLines_mRuA
bytes[] memory params = new bytes[](2);

```

Copy

The `MINT_POSITION` action requires the following parameters:

| Parameter | Type | Description |
| --- | --- | --- |
| `poolKey` | _PoolKey_ | where the liquidity will be added to |
| `tickLower` | _int24_ | the lower tick boundary of the position |
| `tickUpper` | _int24_ | the upper tick boundary of the position |
| `liquidity` | _uint256_ | the amount of liquidity units to mint |
| `amount0Max` | _uint128_ | the maximum amount of currency0 msg.sender is willing to pay |
| `amount1Max` | _uint128_ | the maximum amount of currency1 msg.sender is willing to pay |
| `recipient` | _address_ | the address that will receive the liquidity position (ERC-721) |
| `hookData` | _bytes_ | arbitrary data that will be forwarded to hook functions |

```codeBlockLines_mRuA
Currency currency0 = Currency.wrap(<tokenAddress1>); // tokenAddress1 = 0 for native ETH
Currency currency1 = Currency.wrap(<tokenAddress2>);
PoolKey poolKey = PoolKey(currency0, currency1, 3000, 60, IHooks(hook));

params[0] = abi.encode(poolKey, tickLower, tickUpper, liquidity, amount0Max, amount1Max, recipient, hookData);

```

Copy

The `SETTLE_PAIR` action requires the following parameters:

- `currency0` \- _Currency_, one of the tokens to be paid by msg.sender
- `currency1` \- _Currency_, the other token to be paid by msg.sender

```codeBlockLines_mRuA
params[1] = abi.encode(currency0, currency1);

```

Copy

### 4\. Submit Call [​](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/mint-position\#4-submit-call "Direct link to heading")

The entrypoint for all liquidity operations is `modifyLiquidities()`

```codeBlockLines_mRuA
uint256 deadline = block.timestamp + 60;

uint256 valueToPass = currency0.isAddressZero() ? amount0Max : 0;

posm.modifyLiquidities{value: valueToPass}(
    abi.encode(actions, params),
    deadline
);

```

Copy

## Additional notes: [​](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/mint-position\#additional-notes "Direct link to heading")

- To obtain balance changes, callers should read token balances before and after the `.modifyLiquidities()` call

- [Context](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/mint-position#context)
- [Setup](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/mint-position#setup)
- [1\. Import and define `IPositionManager`](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/mint-position#1-import-and-define-ipositionmanager)
- [2\. Encode Actions](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/mint-position#2-encode-actions)
- [3\. Encode Parameters](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/mint-position#3-encode-parameters)
- [4\. Submit Call](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/mint-position#4-submit-call)
- [Additional notes:](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/mint-position#additional-notes)