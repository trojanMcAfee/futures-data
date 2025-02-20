[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/errors/#)

On this page

# Custom Error Selectors

These are custom error selectors for Uniswap v4 contracts.

## IPoolManager.sol [​](https://docs.uniswap.org/contracts/v4/reference/errors/\#ipoolmanagersol "Direct link to heading")

| Error Selector | Hex Value |
| --- | --- |
| `IPoolManager.CurrencyNotSettled.selector` | `0x5212cba1` |
| `IPoolManager.PoolNotInitialized.selector` | `0x486aa307` |
| `IPoolManager.AlreadyUnlocked.selector` | `0x5090d6c6` |
| `IPoolManager.ManagerLocked.selector` | `0x54e3ca0d` |
| `IPoolManager.TickSpacingTooLarge.selector` | `0xb02b5dc2` |
| `IPoolManager.TickSpacingTooSmall.selector` | `0x16fe7696` |
| `IPoolManager.CurrenciesOutOfOrderOrEqual.selector` | `0xeaa6c6eb` |
| `IPoolManager.UnauthorizedDynamicLPFeeUpdate.selector` | `0x30d21641` |
| `IPoolManager.SwapAmountCannotBeZero.selector` | `0xbe8b8507` |
| `IPoolManager.NonZeroNativeValue.selector` | `0x19d245cf` |

## Hooks.sol [​](https://docs.uniswap.org/contracts/v4/reference/errors/\#hookssol "Direct link to heading")

| Error Selector | Hex Value |
| --- | --- |
| `Hooks.HookAddressNotValid.selector` | `0xe65af6a0` |
| `Hooks.InvalidHookResponse.selector` | `0x1e048e1d` |
| `Hooks.FailedHookCall.selector` | `0x36bc48c5` |
| `Hooks.HookDeltaExceedsSwapAmount.selector` | `0xfa0b71d6` |

## Pool.sol [​](https://docs.uniswap.org/contracts/v4/reference/errors/\#poolsol "Direct link to heading")

| Error Selector | Hex Value |
| --- | --- |
| `Pool.TicksMisordered.selector` | `0xc4433ed5` |
| `Pool.TickLowerOutOfBounds.selector` | `0xd5e2f7ab` |
| `Pool.TickUpperOutOfBounds.selector` | `0x1ad777f8` |
| `Pool.TickLiquidityOverflow.selector` | `0xb8e3c385` |
| `Pool.TickNotInitialized.selector` | `0x82a774d3` |
| `Pool.PoolAlreadyInitialized.selector` | `0x7983c051` |
| `Pool.PoolNotInitialized.selector` | `0x486aa307` |
| `Pool.PriceLimitAlreadyExceeded.selector` | `0x7c9c6e8f` |
| `Pool.PriceLimitOutOfBounds.selector` | `0x9e4d7cc7` |
| `Pool.NoLiquidityToReceiveFees.selector` | `0xa74f97ab` |
| `Pool.InvalidFeeForExactOut.selector` | `0x96206246` |

## IProtocolFees.sol [​](https://docs.uniswap.org/contracts/v4/reference/errors/\#iprotocolfeessol "Direct link to heading")

| Error Selector | Hex Value |
| --- | --- |
| `IProtocolFees.ProtocolFeeCannotBeFetched.selector` | `0x1ee49702` |
| `IProtocolFees.InvalidProtocolFee.selector` | `0xba97f838` |
| `IProtocolFees.InvalidCaller.selector` | `0x48f5c3ed` |

## LPFeeLibrary.sol [​](https://docs.uniswap.org/contracts/v4/reference/errors/\#lpfeelibrarysol "Direct link to heading")

| Error Selector | Hex Value |
| --- | --- |
| `LPFeeLibrary.FeeTooLarge.selector` | `0xfc5bee12` |

## Position.sol [​](https://docs.uniswap.org/contracts/v4/reference/errors/\#positionsol "Direct link to heading")

| Error Selector | Hex Value |
| --- | --- |
| `Position.CannotUpdateEmptyPosition.selector` | `0xaefeb924` |

## Reserves.sol [​](https://docs.uniswap.org/contracts/v4/reference/errors/\#reservessol "Direct link to heading")

| Error Selector | Hex Value |
| --- | --- |
| `Reserves.ReservesMustBeSynced.selector` | `0x8774be48` |

## SqrtPriceMath.sol [​](https://docs.uniswap.org/contracts/v4/reference/errors/\#sqrtpricemathsol "Direct link to heading")

| Error Selector | Hex Value |
| --- | --- |
| `SqrtPriceMath.InvalidPriceOrLiquidity.selector` | `0x4f2461b8` |
| `SqrtPriceMath.InvalidPrice.selector` | `0x00bfc921` |
| `SqrtPriceMath.NotEnoughLiquidity.selector` | `0x4323a555` |
| `SqrtPriceMath.PriceOverflow.selector` | `0xf5c787f1` |

## TickBitmap.sol [​](https://docs.uniswap.org/contracts/v4/reference/errors/\#tickbitmapsol "Direct link to heading")

| Error Selector | Hex Value |
| --- | --- |
| `TickBitmap.TickMisaligned.selector` | `0xd4d8f3e6` |

## TickMath.sol [​](https://docs.uniswap.org/contracts/v4/reference/errors/\#tickmathsol "Direct link to heading")

| Error Selector | Hex Value |
| --- | --- |
| `TickMath.InvalidTick.selector` | `0xce8ef7fc` |
| `TickMath.InvalidSqrtPrice.selector` | `0x31efafe8` |

- [IPoolManager.sol](https://docs.uniswap.org/contracts/v4/reference/errors/#ipoolmanagersol)
- [Hooks.sol](https://docs.uniswap.org/contracts/v4/reference/errors/#hookssol)
- [Pool.sol](https://docs.uniswap.org/contracts/v4/reference/errors/#poolsol)
- [IProtocolFees.sol](https://docs.uniswap.org/contracts/v4/reference/errors/#iprotocolfeessol)
- [LPFeeLibrary.sol](https://docs.uniswap.org/contracts/v4/reference/errors/#lpfeelibrarysol)
- [Position.sol](https://docs.uniswap.org/contracts/v4/reference/errors/#positionsol)
- [Reserves.sol](https://docs.uniswap.org/contracts/v4/reference/errors/#reservessol)
- [SqrtPriceMath.sol](https://docs.uniswap.org/contracts/v4/reference/errors/#sqrtpricemathsol)
- [TickBitmap.sol](https://docs.uniswap.org/contracts/v4/reference/errors/#tickbitmapsol)
- [TickMath.sol](https://docs.uniswap.org/contracts/v4/reference/errors/#tickmathsol)