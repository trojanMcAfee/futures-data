[Skip to main content](https://docs.uniswap.org/contracts/v4/guides/hooks/hook-deployment#)

On this page

## Hook Flags [​](https://docs.uniswap.org/contracts/v4/guides/hooks/hook-deployment\#hook-flags "Direct link to heading")

As mentioned in [Concept of Hooks](https://docs.uniswap.org/contracts/v4/concepts/hooks), hook contracts indicate their implemented functions by **encoding its behavior in the address of the contract**. The `PoolManager` uses these permissions to determine which hook functions to call for a given pool.

Each hook function e.g. `beforeSwap` \- corresponds to a certain _flag_. For example, the `beforeSwap` function is correlated to the [`BEFORE_SWAP_FLAG`](https://github.com/Uniswap/v4-core/blob/main/src/libraries/Hooks.sol#L37) which has a value of `1 << 7`.

These flags represent specific bits in the address of the hook smart contract - and the value of the bit (a one or a zero) represents whether that flag is true or false. An example:

Addresses on Ethereum are 20 bytes long (160 bits). So for example the address:

```codeBlockLines_mRuA
0x00000000000000000000000000000000000000C0

```

Copy

represented in binary is:

```codeBlockLines_mRuA
0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
0000 0000 0000 0000 0000 0000 1100 0000

```

Copy

In binary it goes from right-to-left - so the trailing 8 bits of this address are `1100 0000` where:

1st Bit to 6th Bit = `0`

7th Bit and 8th Bit = `1`

The `AFTER_SWAP` flag is represented by the 7th bit - which is set to `1` for the example contract address. In the `PoolManager` swap execution flow, it will observe the flag and make a call to the hook's `afterSwap` function.

Similarly, the 8th bit which is also a `1`, actually corresponds to the `BEFORE_SWAP` i.e. the `beforeSwap` hook function - which will also be called by the `PoolManager` during a `swap` workflow.

A full list of all flags can be found [here](https://github.com/Uniswap/v4-core/blob/main/src/libraries/Hooks.sol).

## Hook Miner [​](https://docs.uniswap.org/contracts/v4/guides/hooks/hook-deployment\#hook-miner "Direct link to heading")

Because of encoded addresses, hook developers must _mine_ an address to a their particular pattern.

For local testing, `deployCodeTo` cheatcode in Foundry can be used to deploy hook contract to any address.

But when deploying hooks to an actual network, address mining is required to find the proper deployment address
There is a helper library [`HookMiner.sol`](https://github.com/uniswapfoundation/v4-template/blob/main/test/utils/HookMiner.sol) that can be used to mine for correct addresses.

Let's see it in action for a Foundry script. We will make use of the example - Points Hook from [Building Your First Hook](https://docs.uniswap.org/contracts/v4/guides/hooks/your-first-hook).

First we set up the contract for Foundry script and import the relevant dependencies:

```codeBlockLines_mRuA
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "forge-std/Script.sol";
import {Hooks} from "v4-core/src/libraries/Hooks.sol";
import {IPoolManager} from "v4-core/src/interfaces/IPoolManager.sol";

import {Constants} from "./base/Constants.sol";
import {PointsHook} from "../src/PointsHook.sol";
import {HookMiner} from "../test/utils/HookMiner.sol";

/// @notice Mines the address and deploys the PointsHook.sol Hook contract
contract PointsHookScript is Script, Constants {
    function setUp() public {}

    function run() public {

```

Copy

Specify the flags needed to be encoded in the address:

```codeBlockLines_mRuA
uint160 flags = uint160(
    Hooks.AFTER_ADD_LIQUIDITY_FLAG | Hooks.AFTER_SWAP_FLAG
);

```

Copy

Mine the address by finding a `salt` that produces a hook address with the desired `flags`, use the Foundry deterministic deployer when deploying via Foundry script:

```codeBlockLines_mRuA
bytes memory constructorArgs = abi.encode(POOLMANAGER);
(address hookAddress, bytes32 salt) =
    HookMiner.find(CREATE2_DEPLOYER, flags, type(PointsHook).creationCode, constructorArgs);

```

Copy

Deploy the hook using CREATE2 with the `salt`, and compare the deployed address with the address mined:

```codeBlockLines_mRuA
vm.broadcast();
PointsHook pointsHook = new PointsHook{salt: salt}(IPoolManager(POOLMANAGER));
require(address(pointsHook) == hookAddress, "PointsHookScript: hook address mismatch");

```

Copy

## A Complete Foundry Script Contract [​](https://docs.uniswap.org/contracts/v4/guides/hooks/hook-deployment\#a-complete-foundry-script-contract "Direct link to heading")

```codeBlockLines_mRuA
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "forge-std/Script.sol";
import {Hooks} from "v4-core/src/libraries/Hooks.sol";
import {IPoolManager} from "v4-core/src/interfaces/IPoolManager.sol";

import {Constants} from "./base/Constants.sol";
import {PointsHook} from "../src/PointsHook.sol";
import {HookMiner} from "../test/utils/HookMiner.sol";

/// @notice Mines the address and deploys the PointsHook.sol Hook contract
contract PointsHookScript is Script, Constants {
    function setUp() public {}

    function run() public {
        // hook contracts must have specific flags encoded in the address
        uint160 flags = uint160(
            Hooks.BEFORE_SWAP_FLAG | Hooks.AFTER_SWAP_FLAG | Hooks.BEFORE_ADD_LIQUIDITY_FLAG
                | Hooks.BEFORE_REMOVE_LIQUIDITY_FLAG
        );

        // Mine a salt that will produce a hook address with the correct flags
        bytes memory constructorArgs = abi.encode(POOLMANAGER);
        (address hookAddress, bytes32 salt) =
            HookMiner.find(CREATE2_DEPLOYER, flags, type(PointsHook).creationCode, constructorArgs);

        // Deploy the hook using CREATE2
        vm.broadcast();
        PointsHook pointsHook = new PointsHook{salt: salt}(IPoolManager(POOLMANAGER));
        require(address(pointsHook) == hookAddress, "PointsHookScript: hook address mismatch");
    }
}

```

Copy

- [Hook Flags](https://docs.uniswap.org/contracts/v4/guides/hooks/hook-deployment#hook-flags)
- [Hook Miner](https://docs.uniswap.org/contracts/v4/guides/hooks/hook-deployment#hook-miner)
- [A Complete Foundry Script Contract](https://docs.uniswap.org/contracts/v4/guides/hooks/hook-deployment#a-complete-foundry-script-contract)