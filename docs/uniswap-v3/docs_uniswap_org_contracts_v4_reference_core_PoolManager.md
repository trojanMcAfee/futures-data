[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager#)

On this page

# PoolManager

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/PoolManager.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:** [IPoolManager](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IPoolManager), [ProtocolFees](https://docs.uniswap.org/contracts/v4/reference/core/ProtocolFees), [NoDelegateCall](https://docs.uniswap.org/contracts/v4/reference/core/NoDelegateCall), [ERC6909Claims](https://docs.uniswap.org/contracts/v4/reference/core/ERC6909Claims), [Extsload](https://docs.uniswap.org/contracts/v4/reference/core/Extsload), [Exttload](https://docs.uniswap.org/contracts/v4/reference/core/Exttload)

Holds the state for all pools

## State Variables [​](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager\#state-variables "Direct link to heading")

### MAX\_TICK\_SPACING [​](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager\#max_tick_spacing "Direct link to heading")

```codeBlockLines_mRuA
int24 private constant MAX_TICK_SPACING = TickMath.MAX_TICK_SPACING;

```

Copy

### MIN\_TICK\_SPACING [​](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager\#min_tick_spacing "Direct link to heading")

```codeBlockLines_mRuA
int24 private constant MIN_TICK_SPACING = TickMath.MIN_TICK_SPACING;

```

Copy

### \_pools [​](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager\#_pools "Direct link to heading")

```codeBlockLines_mRuA
mapping(PoolId id => Pool.State) internal _pools;

```

Copy

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager\#functions "Direct link to heading")

### onlyWhenUnlocked [​](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager\#onlywhenunlocked "Direct link to heading")

This will revert if the contract is locked

```codeBlockLines_mRuA
modifier onlyWhenUnlocked();

```

Copy

### constructor [​](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager\#constructor "Direct link to heading")

```codeBlockLines_mRuA
constructor(address initialOwner) ProtocolFees(initialOwner);

```

Copy

### unlock [​](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager\#unlock "Direct link to heading")

All interactions on the contract that account deltas require unlocking. A caller that calls `unlock` must implement
`IUnlockCallback(msg.sender).unlockCallback(data)`, where they interact with the remaining functions on this contract.

_The only functions callable without an unlocking are `initialize` and `updateDynamicLPFee`_

```codeBlockLines_mRuA
function unlock(bytes calldata data) external override returns (bytes memory result);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `data` | `bytes` | Any data to pass to the callback, via `IUnlockCallback(msg.sender).unlockCallback(data)` |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `result` | `bytes` | The data returned by the call to `IUnlockCallback(msg.sender).unlockCallback(data)` |

### initialize [​](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager\#initialize "Direct link to heading")

Initialize the state for a given pool ID

_A swap fee totaling MAX\_SWAP\_FEE (100%) makes exact output swaps impossible since the input is entirely consumed by the fee_

```codeBlockLines_mRuA
function initialize(PoolKey memory key, uint160 sqrtPriceX96) external noDelegateCall returns (int24 tick);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `key` | `PoolKey` | The pool key for the pool to initialize |
| `sqrtPriceX96` | `uint160` | The initial square root price |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `tick` | `int24` | The initial tick of the pool |

### modifyLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager\#modifyliquidity "Direct link to heading")

Modify the liquidity for the given pool

_Poke by calling with a zero liquidityDelta_

```codeBlockLines_mRuA
function modifyLiquidity(PoolKey memory key, IPoolManager.ModifyLiquidityParams memory params, bytes calldata hookData)
    external
    onlyWhenUnlocked
    noDelegateCall
    returns (BalanceDelta callerDelta, BalanceDelta feesAccrued);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `key` | `PoolKey` | The pool to modify liquidity in |
| `params` | `IPoolManager.ModifyLiquidityParams` | The parameters for modifying the liquidity |
| `hookData` | `bytes` | The data to pass through to the add/removeLiquidity hooks |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `callerDelta` | `BalanceDelta` | The balance delta of the caller of modifyLiquidity. This is the total of both principal, fee deltas, and hook deltas if applicable |
| `feesAccrued` | `BalanceDelta` | The balance delta of the fees generated in the liquidity range. Returned for informational purposes |

### swap [​](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager\#swap "Direct link to heading")

Swap against the given pool

_Swapping on low liquidity pools may cause unexpected swap amounts when liquidity available is less than amountSpecified._
_Additionally note that if interacting with hooks that have the BEFORE\_SWAP\_RETURNS\_DELTA\_FLAG or AFTER\_SWAP\_RETURNS\_DELTA\_FLAG_
_the hook may alter the swap input/output. Integrators should perform checks on the returned swapDelta._

```codeBlockLines_mRuA
function swap(PoolKey memory key, IPoolManager.SwapParams memory params, bytes calldata hookData)
    external
    onlyWhenUnlocked
    noDelegateCall
    returns (BalanceDelta swapDelta);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `key` | `PoolKey` | The pool to swap in |
| `params` | `IPoolManager.SwapParams` | The parameters for swapping |
| `hookData` | `bytes` | The data to pass through to the swap hooks |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `swapDelta` | `BalanceDelta` | The balance delta of the address swapping |

### \_swap [​](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager\#_swap "Direct link to heading")

Internal swap function to execute a swap, take protocol fees on input token, and emit the swap event

```codeBlockLines_mRuA
function _swap(Pool.State storage pool, PoolId id, Pool.SwapParams memory params, Currency inputCurrency)
    internal
    returns (BalanceDelta);

```

Copy

### donate [​](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager\#donate "Direct link to heading")

Donate the given currency amounts to the in-range liquidity providers of a pool

_Calls to donate can be frontrun adding just-in-time liquidity, with the aim of receiving a portion donated funds._
_Donors should keep this in mind when designing donation mechanisms._

```codeBlockLines_mRuA
function donate(PoolKey memory key, uint256 amount0, uint256 amount1, bytes calldata hookData)
    external
    onlyWhenUnlocked
    noDelegateCall
    returns (BalanceDelta delta);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `key` | `PoolKey` | The key of the pool to donate to |
| `amount0` | `uint256` | The amount of currency0 to donate |
| `amount1` | `uint256` | The amount of currency1 to donate |
| `hookData` | `bytes` | The data to pass through to the donate hooks |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `delta` | `BalanceDelta` | BalanceDelta The delta of the caller after the donate |

### sync [​](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager\#sync "Direct link to heading")

Writes the current ERC20 balance of the specified currency to transient storage
This is used to checkpoint balances for the manager and derive deltas for the caller.

_This MUST be called before any ERC20 tokens are sent into the contract, but can be skipped_
_for native tokens because the amount to settle is determined by the sent value._
_However, if an ERC20 token has been synced and not settled, and the caller instead wants to settle_
_native funds, this function can be called with the native currency to then be able to settle the native currency_

```codeBlockLines_mRuA
function sync(Currency currency) external;

```

Copy

### take [​](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager\#take "Direct link to heading")

Called by the user to net out some value owed to the user

_Will revert if the requested amount is not available, consider using `mint` instead_

```codeBlockLines_mRuA
function take(Currency currency, address to, uint256 amount) external onlyWhenUnlocked;

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `currency` | `Currency` | The currency to withdraw from the pool manager |
| `to` | `address` | The address to withdraw to |
| `amount` | `uint256` | The amount of currency to withdraw |

### settle [​](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager\#settle "Direct link to heading")

Called by the user to pay what is owed

```codeBlockLines_mRuA
function settle() external payable onlyWhenUnlocked returns (uint256);

```

Copy

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `uint256` | paid The amount of currency settled |

### settleFor [​](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager\#settlefor "Direct link to heading")

Called by the user to pay on behalf of another address

```codeBlockLines_mRuA
function settleFor(address recipient) external payable onlyWhenUnlocked returns (uint256);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `recipient` | `address` | The address to credit for the payment |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `uint256` | paid The amount of currency settled |

### clear [​](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager\#clear "Direct link to heading")

WARNING - Any currency that is cleared, will be non-retrievable, and locked in the contract permanently.
A call to clear will zero out a positive balance WITHOUT a corresponding transfer.

_This could be used to clear a balance that is considered dust._
_Additionally, the amount must be the exact positive balance. This is to enforce that the caller is aware of the amount being cleared._

```codeBlockLines_mRuA
function clear(Currency currency, uint256 amount) external onlyWhenUnlocked;

```

Copy

### mint [​](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager\#mint "Direct link to heading")

Called by the user to move value into ERC6909 balance

_The id is converted to a uint160 to correspond to a currency address_
_If the upper 12 bytes are not 0, they will be 0-ed out_

```codeBlockLines_mRuA
function mint(address to, uint256 id, uint256 amount) external onlyWhenUnlocked;

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `to` | `address` | The address to mint the tokens to |
| `id` | `uint256` | The currency address to mint to ERC6909s, as a uint256 |
| `amount` | `uint256` | The amount of currency to mint |

### burn [​](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager\#burn "Direct link to heading")

Called by the user to move value from ERC6909 balance

_The id is converted to a uint160 to correspond to a currency address_
_If the upper 12 bytes are not 0, they will be 0-ed out_

```codeBlockLines_mRuA
function burn(address from, uint256 id, uint256 amount) external onlyWhenUnlocked;

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `from` | `address` | The address to burn the tokens from |
| `id` | `uint256` | The currency address to burn from ERC6909s, as a uint256 |
| `amount` | `uint256` | The amount of currency to burn |

### updateDynamicLPFee [​](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager\#updatedynamiclpfee "Direct link to heading")

Updates the pools lp fees for the a pool that has enabled dynamic lp fees.

_A swap fee totaling MAX\_SWAP\_FEE (100%) makes exact output swaps impossible since the input is entirely consumed by the fee_

```codeBlockLines_mRuA
function updateDynamicLPFee(PoolKey memory key, uint24 newDynamicLPFee) external;

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `key` | `PoolKey` | The key of the pool to update dynamic LP fees for |
| `newDynamicLPFee` | `uint24` | The new dynamic pool LP fee |

### \_settle [​](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager\#_settle "Direct link to heading")

```codeBlockLines_mRuA
function _settle(address recipient) internal returns (uint256 paid);

```

Copy

### \_accountDelta [​](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager\#_accountdelta "Direct link to heading")

Adds a balance delta in a currency for a target address

```codeBlockLines_mRuA
function _accountDelta(Currency currency, int128 delta, address target) internal;

```

Copy

### \_accountPoolBalanceDelta [​](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager\#_accountpoolbalancedelta "Direct link to heading")

Accounts the deltas of 2 currencies to a target address

```codeBlockLines_mRuA
function _accountPoolBalanceDelta(PoolKey memory key, BalanceDelta delta, address target) internal;

```

Copy

### \_getPool [​](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager\#_getpool "Direct link to heading")

Implementation of the \_getPool function defined in ProtocolFees

```codeBlockLines_mRuA
function _getPool(PoolId id) internal view override returns (Pool.State storage);

```

Copy

### \_isUnlocked [​](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager\#_isunlocked "Direct link to heading")

Implementation of the \_isUnlocked function defined in ProtocolFees

```codeBlockLines_mRuA
function _isUnlocked() internal view override returns (bool);

```

Copy

- [State Variables](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager#state-variables)
  - [MAX\_TICK\_SPACING](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager#max_tick_spacing)
  - [MIN\_TICK\_SPACING](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager#min_tick_spacing)
  - [\_pools](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager#_pools)
- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager#functions)
  - [onlyWhenUnlocked](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager#onlywhenunlocked)
  - [constructor](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager#constructor)
  - [unlock](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager#unlock)
  - [initialize](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager#initialize)
  - [modifyLiquidity](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager#modifyliquidity)
  - [swap](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager#swap)
  - [\_swap](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager#_swap)
  - [donate](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager#donate)
  - [sync](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager#sync)
  - [take](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager#take)
  - [settle](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager#settle)
  - [settleFor](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager#settlefor)
  - [clear](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager#clear)
  - [mint](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager#mint)
  - [burn](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager#burn)
  - [updateDynamicLPFee](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager#updatedynamiclpfee)
  - [\_settle](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager#_settle)
  - [\_accountDelta](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager#_accountdelta)
  - [\_accountPoolBalanceDelta](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager#_accountpoolbalancedelta)
  - [\_getPool](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager#_getpool)
  - [\_isUnlocked](https://docs.uniswap.org/contracts/v4/reference/core/PoolManager#_isunlocked)