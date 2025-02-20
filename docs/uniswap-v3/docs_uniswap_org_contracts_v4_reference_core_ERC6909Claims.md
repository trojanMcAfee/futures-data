[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/ERC6909Claims#)

On this page

# ERC6909Claims

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/ERC6909Claims.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:** [ERC6909](https://docs.uniswap.org/contracts/v4/reference/core/ERC6909)

ERC6909Claims inherits ERC6909 and implements an internal burnFrom function

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/ERC6909Claims\#functions "Direct link to heading")

### \_burnFrom [​](https://docs.uniswap.org/contracts/v4/reference/core/ERC6909Claims\#_burnfrom "Direct link to heading")

Burn `amount` tokens of token type `id` from `from`.

_if sender is not `from` they must be an operator or have sufficient allowance._

```codeBlockLines_mRuA
function _burnFrom(address from, uint256 id, uint256 amount) internal;

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `from` | `address` | The address to burn tokens from. |
| `id` | `uint256` | The currency to burn. |
| `amount` | `uint256` | The amount to burn. |

- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/ERC6909Claims#functions)
  - [\_burnFrom](https://docs.uniswap.org/contracts/v4/reference/core/ERC6909Claims#_burnfrom)