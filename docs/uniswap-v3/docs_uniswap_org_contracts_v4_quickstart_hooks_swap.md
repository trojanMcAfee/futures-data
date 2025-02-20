[Skip to main content](https://docs.uniswap.org/contracts/v4/quickstart/hooks/swap#)

On this page

Swaps are the most common interaction with the Uniswap protocol. When it comes to swap there are two hook functions available to customize and extend its behavior:

- `beforeSwap`
- `afterSwap`

As the names suggest `beforeSwap`/ `afterSwap` are functions called before or after a swap is executed on a pool.

This guide will go through the parameters for `beforeSwap` and `afterSwap`, and a simple example of a swap hook.

Note: The swap hook is not production ready code, and is implemented in a simplistic manner for the purpose of learning.

## Set Up the Contract [​](https://docs.uniswap.org/contracts/v4/quickstart/hooks/swap\#set-up-the-contract "Direct link to heading")

Declare the solidity version used to compile the contract, here we will use `>=0.8.24` for the solidity version as transient storage is used.

```codeBlockLines_mRuA
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

```

Copy

Import the relevant dependencies from `v4-core` and `v4-periphery`:

```codeBlockLines_mRuA
import {BaseHook} from "v4-periphery/src/base/hooks/BaseHook.sol";

import {Hooks} from "v4-core/src/libraries/Hooks.sol";
import {IPoolManager} from "v4-core/src/interfaces/IPoolManager.sol";
import {PoolKey} from "v4-core/src/types/PoolKey.sol";
import {PoolId, PoolIdLibrary} from "v4-core/src/types/PoolId.sol";
import {BalanceDelta} from "v4-core/src/types/BalanceDelta.sol";
import {BeforeSwapDelta, BeforeSwapDeltaLibrary} from "v4-core/src/types/BeforeSwapDelta.sol";

```

Copy

Create a contract called `SwapHook`, use `PoolIdLibrary` to attach functions of computing `poolId` for `PoolKey`. Declare two mappings as counters for `beforeSwap` and `afterSwap`.

```codeBlockLines_mRuA
contract SwapHook is BaseHook {
    using PoolIdLibrary for PoolKey;

    // NOTE: ---------------------------------------------------------
    // state variables should typically be unique to a pool
    // a single hook contract should be able to service multiple pools
    // ---------------------------------------------------------------

    mapping(PoolId => uint256 count) public beforeSwapCount;
    mapping(PoolId => uint256 count) public afterSwapCount;

    constructor(IPoolManager _poolManager) BaseHook(_poolManager) {}

```

Copy

Override `getHookPermissions()` from `BaseHook` to return a struct of permissions to signal which hook functions are to be implemented.
It will also be used at deployment to validate the hook address correctly represents the expected permissions.

```codeBlockLines_mRuA
function getHookPermissions() public pure override returns (Hooks.Permissions memory) {
    return Hooks.Permissions({
        beforeInitialize: false,
        afterInitialize: false,
        beforeAddLiquidity: false,
        afterAddLiquidity: false,
        beforeRemoveLiquidity: false,
        afterRemoveLiquidity: false,
        beforeSwap: true,
        afterSwap: true,
        beforeDonate: false,
        afterDonate: false,
        beforeSwapReturnDelta: false,
        afterSwapReturnDelta: false,
        afterAddLiquidityReturnDelta: false,
        afterRemoveLiquidityReturnDelta: false
    });
}

```

Copy

## beforeSwap [​](https://docs.uniswap.org/contracts/v4/quickstart/hooks/swap\#beforeswap "Direct link to heading")

Here the example shows that every time **before** a swap is executed in a pool, `beforeSwapCount` for that pool will be incremented by one.

```codeBlockLines_mRuA
function beforeSwap(address, PoolKey calldata key, IPoolManager.SwapParams calldata, bytes calldata)
    external
    override
    returns (bytes4, BeforeSwapDelta, uint24)
{
    beforeSwapCount[key.toId()]++;
    return (BaseHook.beforeSwap.selector, BeforeSwapDeltaLibrary.ZERO_DELTA, 0);
}

```

Copy

### `beforeSwap` Parameters [​](https://docs.uniswap.org/contracts/v4/quickstart/hooks/swap\#beforeswap-parameters "Direct link to heading")

When triggering the `beforeSwap` hook function, there are some parameters we can make use of to customize or extend the behavior of `swap`. These parameters are described in [`beforeSwap`](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IHooks#beforeswap) from `IHooks`.

A brief overview of the parameters:

- `sender` The initial `msg.sender` for the `PoolManager.swap` call - typically a swap router
- `key` The key for the pool
- `params` The parameters for the swap i.e. [`SwapParams`](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IPoolManager#swapparams) from `IPoolManager`
- `hookData` Arbitrary data handed into the `PoolManager` by the swapper to be be passed on to the hook

## afterSwap [​](https://docs.uniswap.org/contracts/v4/quickstart/hooks/swap\#afterswap "Direct link to heading")

Similiar as above, every time **after** a swap is executed in a pool, `afterSwapCount` for that pool will be incremented by one.

```codeBlockLines_mRuA
function afterSwap(address, PoolKey calldata key, IPoolManager.SwapParams calldata, BalanceDelta, bytes calldata)
    external
    override
    returns (bytes4, int128)
{
    afterSwapCount[key.toId()]++;
    return (BaseHook.afterSwap.selector, 0);
}

```

Copy

### `afterSwap` Parameters [​](https://docs.uniswap.org/contracts/v4/quickstart/hooks/swap\#afterswap-parameters "Direct link to heading")

When triggering the `afterSwap` hook function, there are some parameters we can make use of to customize or extend the behavior of `swap`. These parameters are described in [`afterSwap`](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IPoolManager#swapparams) from `IHooks`.

A brief overview of the parameters:

- `sender` The initial `msg.sender` for the `PoolManager.swap` call - typically a swap router
- `key` The key for the pool
- `params` The parameters for the swap i.e. [`SwapParams`](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IPoolManager#swapparams) from `IPoolManager`
- `delta` The amount owed to the caller (positive) or owed to the pool (negative)
- `hookData` Arbitrary data handed into the `PoolManager` by the swapper to be be passed on to the hook


## A Complete Swap Hook Contract [​](https://docs.uniswap.org/contracts/v4/quickstart/hooks/swap\#a-complete-swap-hook-contract "Direct link to heading")

```codeBlockLines_mRuA
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {BaseHook} from "v4-periphery/src/base/hooks/BaseHook.sol";

import {Hooks} from "v4-core/src/libraries/Hooks.sol";
import {IPoolManager} from "v4-core/src/interfaces/IPoolManager.sol";
import {PoolKey} from "v4-core/src/types/PoolKey.sol";
import {PoolId, PoolIdLibrary} from "v4-core/src/types/PoolId.sol";
import {BalanceDelta} from "v4-core/src/types/BalanceDelta.sol";
import {BeforeSwapDelta, BeforeSwapDeltaLibrary} from "v4-core/src/types/BeforeSwapDelta.sol";

contract SwapHook is BaseHook {
    using PoolIdLibrary for PoolKey;

    // NOTE: ---------------------------------------------------------
    // state variables should typically be unique to a pool
    // a single hook contract should be able to service multiple pools
    // ---------------------------------------------------------------

    mapping(PoolId => uint256 count) public beforeSwapCount;
    mapping(PoolId => uint256 count) public afterSwapCount;

    constructor(IPoolManager _poolManager) BaseHook(_poolManager) {}

    function getHookPermissions() public pure override returns (Hooks.Permissions memory) {
        return Hooks.Permissions({
            beforeInitialize: false,
            afterInitialize: false,
            beforeAddLiquidity: true,
            afterAddLiquidity: false,
            beforeRemoveLiquidity: true,
            afterRemoveLiquidity: false,
            beforeSwap: true,
            afterSwap: true,
            beforeDonate: false,
            afterDonate: false,
            beforeSwapReturnDelta: false,
            afterSwapReturnDelta: false,
            afterAddLiquidityReturnDelta: false,
            afterRemoveLiquidityReturnDelta: false
        });
    }

    // -----------------------------------------------
    // NOTE: see IHooks.sol for function documentation
    // -----------------------------------------------

    function beforeSwap(address, PoolKey calldata key, IPoolManager.SwapParams calldata, bytes calldata)
        external
        override
        returns (bytes4, BeforeSwapDelta, uint24)
    {
        beforeSwapCount[key.toId()]++;
        return (BaseHook.beforeSwap.selector, BeforeSwapDeltaLibrary.ZERO_DELTA, 0);
    }

    function afterSwap(address, PoolKey calldata key, IPoolManager.SwapParams calldata, BalanceDelta, bytes calldata)
        external
        override
        returns (bytes4, int128)
    {
        afterSwapCount[key.toId()]++;
        return (BaseHook.afterSwap.selector, 0);
    }
}

```

Copy

- [Set Up the Contract](https://docs.uniswap.org/contracts/v4/quickstart/hooks/swap#set-up-the-contract)
- [beforeSwap](https://docs.uniswap.org/contracts/v4/quickstart/hooks/swap#beforeswap)
  - [`beforeSwap` Parameters](https://docs.uniswap.org/contracts/v4/quickstart/hooks/swap#beforeswap-parameters)
- [afterSwap](https://docs.uniswap.org/contracts/v4/quickstart/hooks/swap#afterswap)
  - [`afterSwap` Parameters](https://docs.uniswap.org/contracts/v4/quickstart/hooks/swap#afterswap-parameters)
- [A Complete Swap Hook Contract](https://docs.uniswap.org/contracts/v4/quickstart/hooks/swap#a-complete-swap-hook-contract)