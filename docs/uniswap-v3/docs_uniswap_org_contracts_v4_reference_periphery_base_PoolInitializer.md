[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/periphery/base/PoolInitializer#)

On this page

# PoolInitializer

[Git Source](https://github.com/uniswap/v4-periphery/blob/3f295d8435e4f776ea2daeb96ce1bc6d63f33fc7/src/base/PoolInitializer.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:** [ImmutableState](https://docs.uniswap.org/contracts/v4/reference/periphery/base/ImmutableState)

Initializes a Uniswap v4 Pool

_Enables create pool + mint liquidity in a single transaction with multicall_

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/PoolInitializer\#functions "Direct link to heading")

### initializePool [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/PoolInitializer\#initializepool "Direct link to heading")

Initialize a Uniswap v4 Pool

```codeBlockLines_mRuA
function initializePool(PoolKey calldata key, uint160 sqrtPriceX96) external payable returns (int24);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `key` | `PoolKey` | the PoolKey of the pool to initialize |
| `sqrtPriceX96` | `uint160` | the initial sqrtPriceX96 of the pool |

- [Functions](https://docs.uniswap.org/contracts/v4/reference/periphery/base/PoolInitializer#functions)
  - [initializePool](https://docs.uniswap.org/contracts/v4/reference/periphery/base/PoolInitializer#initializepool)