[Skip to main content](https://docs.uniswap.org/contracts/v4/overview#)

On this page

# Uniswap v4

Uniswap v4 inherits all of the capital efficiency gains of Uniswap v3, but provides flexibility via _hooks_ and gas optimizations across the entire lifecycle.

For additional information, see the [Uniswap v4 whitepaper](https://app.uniswap.org/whitepaper-v4.pdf)

## Hooks [​](https://docs.uniswap.org/contracts/v4/overview\#hooks "Direct link to heading")

Developers can attach solidity logic to the _swap lifecycle_ through Hooks. The logic is executed before and/or after major operations such as
pool creation, liquidity addition and removal, swapping, and donations. Hooks are deployed contracts, and are called by the Uniswap v4 PoolManager,
for permissionless execution.

The flexibility of hooks can enable:

- Limit orders
- Custom oracles
- Fee management
- Automated liquidity management

## Dynamic Fees [​](https://docs.uniswap.org/contracts/v4/overview\#dynamic-fees "Direct link to heading")

Uniswap v4 supports dynamic fees, allowing pools to adjust their fees up or down. While other AMMs may have hard-coded logic for dynamic fees,
v4 provides no opinionated calculation of the fee. The frequency of _liquidity fee_ updates is also flexible and determined by the developer. Fee updates can
occur on every swap, every block, or on an arbitrary schedule (weekly, monthly, yearly, etc).

Dynamic fees open up the design space for fee optimization, value redistribution, and research.

## Singleton Design [​](https://docs.uniswap.org/contracts/v4/overview\#singleton-design "Direct link to heading")

Architecturally, all pool state and operations are managed by a single contract -- `PoolManager.sol`. The singleton design provides major gas
savings. For example, creating a pool is now a state update instead of the deployment of a new contract. Swapping through multiple pools no longer requires
transferring tokens for intermediate pools.

## Flash Accounting [​](https://docs.uniswap.org/contracts/v4/overview\#flash-accounting "Direct link to heading")

By leveraging EIP-1153 Transient Storage, v4 provides an optimization referred to as _flash accounting_. Swapping, liquidity modification, and donations
incur _balance changes_, i.e. tokens to be sent in and tokens to be taken out. With _flash accounting_ these balance changes are efficiently recorded in transient storage and
netted against each other. This system allows users to only pay the final balance change, without the need for resolving intermediate balance changes.

## Native ETH [​](https://docs.uniswap.org/contracts/v4/overview\#native-eth "Direct link to heading")

Uniswap v4 supports native token assets (Ether), without the need to wrap/unwrap the native token to Wrapped Ether (WETH9).

## Custom Accounting [​](https://docs.uniswap.org/contracts/v4/overview\#custom-accounting "Direct link to heading")

The flexibility of custom accounting allows developers to alter token amounts for swaps and liquidity modifications. The feature opens up the design
space for hooks to charge fees or forgo the underlying concentrated liquidity model.

Example use-cases:

- Custom curves, opt-out of the concentrated liquidity curve in favor of an entirely independent pricing mechanism
- Hook swap fees, charge and collect fees on swaps
- Liquidity withdrawal fees, penalize and/or redistribute fee revenue

- [Hooks](https://docs.uniswap.org/contracts/v4/overview#hooks)
- [Dynamic Fees](https://docs.uniswap.org/contracts/v4/overview#dynamic-fees)
- [Singleton Design](https://docs.uniswap.org/contracts/v4/overview#singleton-design)
- [Flash Accounting](https://docs.uniswap.org/contracts/v4/overview#flash-accounting)
- [Native ETH](https://docs.uniswap.org/contracts/v4/overview#native-eth)
- [Custom Accounting](https://docs.uniswap.org/contracts/v4/overview#custom-accounting)