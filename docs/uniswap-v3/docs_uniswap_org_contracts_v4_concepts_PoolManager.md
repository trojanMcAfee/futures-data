[Skip to main content](https://docs.uniswap.org/contracts/v4/concepts/PoolManager#)

On this page

In Uniswap v3, each liquidity pool was represented by a separate smart contract deployed through the Uniswapv3Factory contract. While this approach provided flexibility, it also led to increased gas costs for pool creation and multi-hop swaps.

Uniswap v4 addresses this issue by introducing the Singleton design pattern. The PoolManager contract now serves as a single entry point for all liquidity pools. Instead of deploying separate contracts for each pool, the pool state and logic are encapsulated within the PoolManager itself.

# Purpose

The primary purpose of the `PoolManager` is to:

- Efficiently manage liquidity pools
- Facilitate token swaps
- Reduce gas costs compared to the factory-based approach in Uniswap v3
- Enable extensibility through hooks

# Architecture

## Singleton Design [​](https://docs.uniswap.org/contracts/v4/concepts/PoolManager\#singleton-design "Direct link to heading")

- Uniswap v4 uses a Singleton design pattern for the `PoolManager`
- All pool state and logic are encapsulated within the `PoolManager` contract

## Locking Mechanism [​](https://docs.uniswap.org/contracts/v4/concepts/PoolManager\#locking-mechanism "Direct link to heading")

- The `PoolManager` uses a locking mechanism to allow for _flash accounting_ (also known as deferred balance accounting)
- When unlocked, the calling contract can perform various operations and zero-out outstanding balances before returning control to the `PoolManager` for final solvency checks

## Pool State [​](https://docs.uniswap.org/contracts/v4/concepts/PoolManager\#pool-state "Direct link to heading")

- The `Pool.State` struct contains information such as:
  - Current price
  - Liquidity
  - Tick bitmap
  - Fee growth
  - Position information

## Libraries [​](https://docs.uniswap.org/contracts/v4/concepts/PoolManager\#libraries "Direct link to heading")

- The pool logic is implemented using Solidity libraries to keep the `PoolManager` contract modular and gas-efficient
- These libraries are:
  - `Pool`: Contains core pool functionality, such as swaps and liquidity management
  - `Hooks`: Handles the execution of hook functions
  - `Position`: Manages liquidity positions within a pool

# Core Functionality

## Pool Creation [​](https://docs.uniswap.org/contracts/v4/concepts/PoolManager\#pool-creation "Direct link to heading")

- New pools are created by calling the `initialize` function on the `PoolManager`
- The pool creator specifies the token pair, fee tier, tick spacing, and optional hook contract address
- The `PoolManager` initializes the pool state and associates it with a unique `PoolId`

## Swaps [​](https://docs.uniswap.org/contracts/v4/concepts/PoolManager\#swaps "Direct link to heading")

- Swaps are initiated through the `swap` function on the `PoolManager`, typically via a swap router contract
- The `PoolManager` executes the following steps:
1. Checks if the pool is valid and initialized
2. Executes the `beforeSwap` hook, if applicable
3. Performs the actual swap, updating the pool state and charging fees
4. Executes the `afterSwap` hook, if applicable
5. Calculates the net token amounts owed to the user and the pool, represented by the `BalanceDelta` struct
- Swaps utilize flash accounting, where tokens are moved into the `PoolManager`, and only the final output tokens are withdrawn

## Liquidity Management [​](https://docs.uniswap.org/contracts/v4/concepts/PoolManager\#liquidity-management "Direct link to heading")

- Liquidity providers can add or remove liquidity using the `modifyLiquidity` function on the `PoolManager`. However, you wouldn't call this directly from your application, you would call this from a periphery contract to handle the locking & unlocking a particular pool.
- The `PoolManager` executes the following steps:
1. Checks if the pool is valid and initialized
2. Determines if the modification is an addition or removal of liquidity
3. Executes the appropriate `beforeAddLiquidity` or `beforeRemoveLiquidity` hook, if applicable
4. Performs the actual liquidity modification and updates the pool state
5. Emits the `ModifyLiquidity` event
6. Executes the appropriate `afterAddLiquidity` or `afterRemoveLiquidity` hook, if applicable
7. Calculates the balance delta and returns it to the caller

## Flash Accounting [​](https://docs.uniswap.org/contracts/v4/concepts/PoolManager\#flash-accounting "Direct link to heading")

- The `PoolManager` employs flash accounting to reduce gas costs and simplify multi-hop swaps
- Tokens are moved into the `PoolManager` contract, and all subsequent actions are performed within the contract's context
- Only the final output tokens are withdrawn from the `PoolManager` at the end of the transaction

# Transient Storage

- The `PoolManager` utilizes transient storage (EIP-1153) to store temporary data during complex operations
- Transient storage reduces gas costs by avoiding regular storage operations for data only needed within a single transaction

- [Singleton Design](https://docs.uniswap.org/contracts/v4/concepts/PoolManager#singleton-design)
- [Locking Mechanism](https://docs.uniswap.org/contracts/v4/concepts/PoolManager#locking-mechanism)
- [Pool State](https://docs.uniswap.org/contracts/v4/concepts/PoolManager#pool-state)
- [Libraries](https://docs.uniswap.org/contracts/v4/concepts/PoolManager#libraries)
- [Pool Creation](https://docs.uniswap.org/contracts/v4/concepts/PoolManager#pool-creation)
- [Swaps](https://docs.uniswap.org/contracts/v4/concepts/PoolManager#swaps)
- [Liquidity Management](https://docs.uniswap.org/contracts/v4/concepts/PoolManager#liquidity-management)
- [Flash Accounting](https://docs.uniswap.org/contracts/v4/concepts/PoolManager#flash-accounting)