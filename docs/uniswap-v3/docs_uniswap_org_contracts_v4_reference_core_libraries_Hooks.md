[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks#)

On this page

# Hooks

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/libraries/Hooks.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

V4 decides whether to invoke specific hooks by inspecting the least significant bits
of the address that the hooks contract is deployed to.
For example, a hooks contract deployed to address: 0x0000000000000000000000000000000000002400
has the lowest bits '10 0100 0000 0000' which would cause the 'before initialize' and 'after add liquidity' hooks to be used.

## State Variables [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks\#state-variables "Direct link to heading")

### ALL\_HOOK\_MASK [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks\#all_hook_mask "Direct link to heading")

```codeBlockLines_mRuA
uint160 internal constant ALL_HOOK_MASK = uint160((1 << 14) - 1);

```

Copy

### BEFORE\_INITIALIZE\_FLAG [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks\#before_initialize_flag "Direct link to heading")

```codeBlockLines_mRuA
uint160 internal constant BEFORE_INITIALIZE_FLAG = 1 << 13;

```

Copy

### AFTER\_INITIALIZE\_FLAG [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks\#after_initialize_flag "Direct link to heading")

```codeBlockLines_mRuA
uint160 internal constant AFTER_INITIALIZE_FLAG = 1 << 12;

```

Copy

### BEFORE\_ADD\_LIQUIDITY\_FLAG [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks\#before_add_liquidity_flag "Direct link to heading")

```codeBlockLines_mRuA
uint160 internal constant BEFORE_ADD_LIQUIDITY_FLAG = 1 << 11;

```

Copy

### AFTER\_ADD\_LIQUIDITY\_FLAG [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks\#after_add_liquidity_flag "Direct link to heading")

```codeBlockLines_mRuA
uint160 internal constant AFTER_ADD_LIQUIDITY_FLAG = 1 << 10;

```

Copy

### BEFORE\_REMOVE\_LIQUIDITY\_FLAG [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks\#before_remove_liquidity_flag "Direct link to heading")

```codeBlockLines_mRuA
uint160 internal constant BEFORE_REMOVE_LIQUIDITY_FLAG = 1 << 9;

```

Copy

### AFTER\_REMOVE\_LIQUIDITY\_FLAG [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks\#after_remove_liquidity_flag "Direct link to heading")

```codeBlockLines_mRuA
uint160 internal constant AFTER_REMOVE_LIQUIDITY_FLAG = 1 << 8;

```

Copy

### BEFORE\_SWAP\_FLAG [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks\#before_swap_flag "Direct link to heading")

```codeBlockLines_mRuA
uint160 internal constant BEFORE_SWAP_FLAG = 1 << 7;

```

Copy

### AFTER\_SWAP\_FLAG [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks\#after_swap_flag "Direct link to heading")

```codeBlockLines_mRuA
uint160 internal constant AFTER_SWAP_FLAG = 1 << 6;

```

Copy

### BEFORE\_DONATE\_FLAG [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks\#before_donate_flag "Direct link to heading")

```codeBlockLines_mRuA
uint160 internal constant BEFORE_DONATE_FLAG = 1 << 5;

```

Copy

### AFTER\_DONATE\_FLAG [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks\#after_donate_flag "Direct link to heading")

```codeBlockLines_mRuA
uint160 internal constant AFTER_DONATE_FLAG = 1 << 4;

```

Copy

### BEFORE\_SWAP\_RETURNS\_DELTA\_FLAG [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks\#before_swap_returns_delta_flag "Direct link to heading")

```codeBlockLines_mRuA
uint160 internal constant BEFORE_SWAP_RETURNS_DELTA_FLAG = 1 << 3;

```

Copy

### AFTER\_SWAP\_RETURNS\_DELTA\_FLAG [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks\#after_swap_returns_delta_flag "Direct link to heading")

```codeBlockLines_mRuA
uint160 internal constant AFTER_SWAP_RETURNS_DELTA_FLAG = 1 << 2;

```

Copy

### AFTER\_ADD\_LIQUIDITY\_RETURNS\_DELTA\_FLAG [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks\#after_add_liquidity_returns_delta_flag "Direct link to heading")

```codeBlockLines_mRuA
uint160 internal constant AFTER_ADD_LIQUIDITY_RETURNS_DELTA_FLAG = 1 << 1;

```

Copy

### AFTER\_REMOVE\_LIQUIDITY\_RETURNS\_DELTA\_FLAG [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks\#after_remove_liquidity_returns_delta_flag "Direct link to heading")

```codeBlockLines_mRuA
uint160 internal constant AFTER_REMOVE_LIQUIDITY_RETURNS_DELTA_FLAG = 1 << 0;

```

Copy

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks\#functions "Direct link to heading")

### validateHookPermissions [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks\#validatehookpermissions "Direct link to heading")

Utility function intended to be used in hook constructors to ensure
the deployed hooks address causes the intended hooks to be called

_permissions param is memory as the function will be called from constructors_

```codeBlockLines_mRuA
function validateHookPermissions(IHooks self, Permissions memory permissions) internal pure;

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `self` | `IHooks` |  |
| `permissions` | `Permissions` | The hooks that are intended to be called |

### isValidHookAddress [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks\#isvalidhookaddress "Direct link to heading")

Ensures that the hook address includes at least one hook flag or dynamic fees, or is the 0 address

```codeBlockLines_mRuA
function isValidHookAddress(IHooks self, uint24 fee) internal pure returns (bool);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `self` | `IHooks` | The hook to verify |
| `fee` | `uint24` | The fee of the pool the hook is used with |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `bool` | bool True if the hook address is valid |

### callHook [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks\#callhook "Direct link to heading")

performs a hook call using the given calldata on the given hook that doesn't return a delta

```codeBlockLines_mRuA
function callHook(IHooks self, bytes memory data) internal returns (bytes memory result);

```

Copy

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `result` | `bytes` | The complete data returned by the hook |

### callHookWithReturnDelta [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks\#callhookwithreturndelta "Direct link to heading")

performs a hook call using the given calldata on the given hook

```codeBlockLines_mRuA
function callHookWithReturnDelta(IHooks self, bytes memory data, bool parseReturn) internal returns (int256);

```

Copy

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `int256` | int256 The delta returned by the hook |

### noSelfCall [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks\#noselfcall "Direct link to heading")

modifier to prevent calling a hook if they initiated the action

```codeBlockLines_mRuA
modifier noSelfCall(IHooks self);

```

Copy

### beforeInitialize [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks\#beforeinitialize "Direct link to heading")

calls beforeInitialize hook if permissioned and validates return value

```codeBlockLines_mRuA
function beforeInitialize(IHooks self, PoolKey memory key, uint160 sqrtPriceX96) internal noSelfCall(self);

```

Copy

### afterInitialize [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks\#afterinitialize "Direct link to heading")

calls afterInitialize hook if permissioned and validates return value

```codeBlockLines_mRuA
function afterInitialize(IHooks self, PoolKey memory key, uint160 sqrtPriceX96, int24 tick) internal noSelfCall(self);

```

Copy

### beforeModifyLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks\#beforemodifyliquidity "Direct link to heading")

calls beforeModifyLiquidity hook if permissioned and validates return value

```codeBlockLines_mRuA
function beforeModifyLiquidity(
    IHooks self,
    PoolKey memory key,
    IPoolManager.ModifyLiquidityParams memory params,
    bytes calldata hookData
) internal noSelfCall(self);

```

Copy

### afterModifyLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks\#aftermodifyliquidity "Direct link to heading")

calls afterModifyLiquidity hook if permissioned and validates return value

```codeBlockLines_mRuA
function afterModifyLiquidity(
    IHooks self,
    PoolKey memory key,
    IPoolManager.ModifyLiquidityParams memory params,
    BalanceDelta delta,
    BalanceDelta feesAccrued,
    bytes calldata hookData
) internal returns (BalanceDelta callerDelta, BalanceDelta hookDelta);

```

Copy

### beforeSwap [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks\#beforeswap "Direct link to heading")

calls beforeSwap hook if permissioned and validates return value

```codeBlockLines_mRuA
function beforeSwap(IHooks self, PoolKey memory key, IPoolManager.SwapParams memory params, bytes calldata hookData)
    internal
    returns (int256 amountToSwap, BeforeSwapDelta hookReturn, uint24 lpFeeOverride);

```

Copy

### afterSwap [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks\#afterswap "Direct link to heading")

calls afterSwap hook if permissioned and validates return value

```codeBlockLines_mRuA
function afterSwap(
    IHooks self,
    PoolKey memory key,
    IPoolManager.SwapParams memory params,
    BalanceDelta swapDelta,
    bytes calldata hookData,
    BeforeSwapDelta beforeSwapHookReturn
) internal returns (BalanceDelta, BalanceDelta);

```

Copy

### beforeDonate [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks\#beforedonate "Direct link to heading")

calls beforeDonate hook if permissioned and validates return value

```codeBlockLines_mRuA
function beforeDonate(IHooks self, PoolKey memory key, uint256 amount0, uint256 amount1, bytes calldata hookData)
    internal
    noSelfCall(self);

```

Copy

### afterDonate [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks\#afterdonate "Direct link to heading")

calls afterDonate hook if permissioned and validates return value

```codeBlockLines_mRuA
function afterDonate(IHooks self, PoolKey memory key, uint256 amount0, uint256 amount1, bytes calldata hookData)
    internal
    noSelfCall(self);

```

Copy

### hasPermission [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks\#haspermission "Direct link to heading")

```codeBlockLines_mRuA
function hasPermission(IHooks self, uint160 flag) internal pure returns (bool);

```

Copy

## Errors [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks\#errors "Direct link to heading")

### HookAddressNotValid [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks\#hookaddressnotvalid "Direct link to heading")

Thrown if the address will not lead to the specified hook calls being called

```codeBlockLines_mRuA
error HookAddressNotValid(address hooks);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `hooks` | `address` | The address of the hooks contract |

### InvalidHookResponse [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks\#invalidhookresponse "Direct link to heading")

Hook did not return its selector

```codeBlockLines_mRuA
error InvalidHookResponse();

```

Copy

### HookCallFailed [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks\#hookcallfailed "Direct link to heading")

Additional context for ERC-7751 wrapped error when a hook call fails

```codeBlockLines_mRuA
error HookCallFailed();

```

Copy

### HookDeltaExceedsSwapAmount [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks\#hookdeltaexceedsswapamount "Direct link to heading")

The hook's delta changed the swap from exactIn to exactOut or vice versa

```codeBlockLines_mRuA
error HookDeltaExceedsSwapAmount();

```

Copy

## Structs [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks\#structs "Direct link to heading")

### Permissions [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks\#permissions "Direct link to heading")

```codeBlockLines_mRuA
struct Permissions {
    bool beforeInitialize;
    bool afterInitialize;
    bool beforeAddLiquidity;
    bool afterAddLiquidity;
    bool beforeRemoveLiquidity;
    bool afterRemoveLiquidity;
    bool beforeSwap;
    bool afterSwap;
    bool beforeDonate;
    bool afterDonate;
    bool beforeSwapReturnDelta;
    bool afterSwapReturnDelta;
    bool afterAddLiquidityReturnDelta;
    bool afterRemoveLiquidityReturnDelta;
}

```

Copy

- [State Variables](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks#state-variables)
  - [ALL\_HOOK\_MASK](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks#all_hook_mask)
  - [BEFORE\_INITIALIZE\_FLAG](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks#before_initialize_flag)
  - [AFTER\_INITIALIZE\_FLAG](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks#after_initialize_flag)
  - [BEFORE\_ADD\_LIQUIDITY\_FLAG](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks#before_add_liquidity_flag)
  - [AFTER\_ADD\_LIQUIDITY\_FLAG](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks#after_add_liquidity_flag)
  - [BEFORE\_REMOVE\_LIQUIDITY\_FLAG](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks#before_remove_liquidity_flag)
  - [AFTER\_REMOVE\_LIQUIDITY\_FLAG](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks#after_remove_liquidity_flag)
  - [BEFORE\_SWAP\_FLAG](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks#before_swap_flag)
  - [AFTER\_SWAP\_FLAG](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks#after_swap_flag)
  - [BEFORE\_DONATE\_FLAG](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks#before_donate_flag)
  - [AFTER\_DONATE\_FLAG](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks#after_donate_flag)
  - [BEFORE\_SWAP\_RETURNS\_DELTA\_FLAG](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks#before_swap_returns_delta_flag)
  - [AFTER\_SWAP\_RETURNS\_DELTA\_FLAG](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks#after_swap_returns_delta_flag)
  - [AFTER\_ADD\_LIQUIDITY\_RETURNS\_DELTA\_FLAG](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks#after_add_liquidity_returns_delta_flag)
  - [AFTER\_REMOVE\_LIQUIDITY\_RETURNS\_DELTA\_FLAG](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks#after_remove_liquidity_returns_delta_flag)
- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks#functions)
  - [validateHookPermissions](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks#validatehookpermissions)
  - [isValidHookAddress](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks#isvalidhookaddress)
  - [callHook](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks#callhook)
  - [callHookWithReturnDelta](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks#callhookwithreturndelta)
  - [noSelfCall](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks#noselfcall)
  - [beforeInitialize](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks#beforeinitialize)
  - [afterInitialize](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks#afterinitialize)
  - [beforeModifyLiquidity](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks#beforemodifyliquidity)
  - [afterModifyLiquidity](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks#aftermodifyliquidity)
  - [beforeSwap](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks#beforeswap)
  - [afterSwap](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks#afterswap)
  - [beforeDonate](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks#beforedonate)
  - [afterDonate](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks#afterdonate)
  - [hasPermission](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks#haspermission)
- [Errors](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks#errors)
  - [HookAddressNotValid](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks#hookaddressnotvalid)
  - [InvalidHookResponse](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks#invalidhookresponse)
  - [HookCallFailed](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks#hookcallfailed)
  - [HookDeltaExceedsSwapAmount](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks#hookdeltaexceedsswapamount)
- [Structs](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks#structs)
  - [Permissions](https://docs.uniswap.org/contracts/v4/reference/core/libraries/Hooks#permissions)