[Skip to main content](https://docs.uniswap.org/contracts/v4/guides/unlock-callback#)

On this page

### Refresher [​](https://docs.uniswap.org/contracts/v4/guides/unlock-callback\#refresher "Direct link to heading")

In order to have access to the liquidity inside the `PoolManager`,
it needs to be _unlocked_ to begin with. After being unlocked, any
number of operations can be executed, which at the end of must be _locked_
again. At this point, if there are any _non-zero deltas_, meaning the
PoolManager is owed or owes tokens back to some address, the whole
execution reverts. Otherwise, both parties have paid or received
the right amount of tokens and the operations have successfully
carried out.

# Unlocking the PoolManager

### Implementing the unlock callback [​](https://docs.uniswap.org/contracts/v4/guides/unlock-callback\#implementing-the-unlock-callback "Direct link to heading")

Prior to unlocking the PoolManager, the integrating contract must
implement the `unlockCallback` function. This function will be
called by the PoolManager after being unlocked. An easy way to
do this is to inherit the `SafeCallback` abstract contract.

```codeBlockLines_mRuA
import {SafeCallback} from "v4-periphery/src/base/SafeCallback.sol";

contract IntegratingContract is SafeCallback {
    constructor(IPoolManager _poolManager) SafeCallback(_poolManager) {}
}

```

Copy

### Calling the unlock function [​](https://docs.uniswap.org/contracts/v4/guides/unlock-callback\#calling-the-unlock-function "Direct link to heading")

After implementing the callback, the integrating contract can now
invoke the `unlock()` function. It receives a _bytes_ parameter
that is further passed to your callback function as an argument.
This parameter is used to encode the sequence of operations to be
executed in the context of the `PoolManager`.

```codeBlockLines_mRuA
bytes memory unlockData = abi.encode(encode_operations_here);
bytes memory unlockResultData = poolManager.unlock(unlockData);

```

Copy

Next, we must override the `_unlockCallback` function inherited from
the `SafeCallback` contract. In your implementation, you should
decode your operations and continue with the desired logic.

```codeBlockLines_mRuA
function _unlockCallback(bytes calldata data) internal override returns (bytes memory) {
    (...) = abi.decode(data, (...));
}

```

Copy

# Operations

There are **9** operations that can be done in the `PoolManager`
which fall in two categories: _liquidity-accessing_ and _delta-resolving_.

### Deltas [​](https://docs.uniswap.org/contracts/v4/guides/unlock-callback\#deltas "Direct link to heading")

Deltas are the `PoolManager`'s method to keep track of token amounts it
needs to receive, respectively to distribute. A negative delta signals that
the `PoolManager` is owed tokens, while a positive one expresses a
token balance that needs to be paid to its user.

### Liquidity-accessing [​](https://docs.uniswap.org/contracts/v4/guides/unlock-callback\#liquidity-accessing "Direct link to heading")

_Liquidity-accessing_ operations will create non-zero _deltas_ and
produce a state transition of the selected pool.
They are the following:

- _modify liquidity_ \- used to increase or decrease liquidity; increasing
liquidity will result in a negative token delta, while decreasing yields a positive one
- _swap_ \- used to trade one token for another; will result in a negative tokenA delta
and a positive tokenB delta
- _donate_ \- used to provide direct token revenue to positions in range;
will result in a negative delta for the pool's tokens the user wishes
to provide

### Delta-resolving [​](https://docs.uniswap.org/contracts/v4/guides/unlock-callback\#delta-resolving "Direct link to heading")

_Delta-resolving_ operations are used to even out the deltas created
by the _liquidity-accessing_ operations.
They are the following:

- _settle_ \- used following token transfers to the manager
or burning of ERC6909 claims to resolve negative deltas
- _take_ \- transfer tokens from the manager, used to resolve
positive deltas but also provide token loans, producing negative deltas
- _mint_ \- used to create ERC6909 claims, creating a negative delta
that needs to be resolved by transferring the corresponding token and
_settling_ afterwards
- _burn_ \- removes ERC6909 claims, creating a positive delta for tokens to
be transferred back to the owner or used in settling negative balances
- _clear_ \- used to zero out positive token deltas, helpful to forfeit
insignificant token amounts in order to avoid paying further transfer costs

- [Refresher](https://docs.uniswap.org/contracts/v4/guides/unlock-callback#refresher)
- [Implementing the unlock callback](https://docs.uniswap.org/contracts/v4/guides/unlock-callback#implementing-the-unlock-callback)
- [Calling the unlock function](https://docs.uniswap.org/contracts/v4/guides/unlock-callback#calling-the-unlock-function)
- [Deltas](https://docs.uniswap.org/contracts/v4/guides/unlock-callback#deltas)
- [Liquidity-accessing](https://docs.uniswap.org/contracts/v4/guides/unlock-callback#liquidity-accessing)
- [Delta-resolving](https://docs.uniswap.org/contracts/v4/guides/unlock-callback#delta-resolving)