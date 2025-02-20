[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/test/MockERC6909Claims#)

On this page

# MockERC6909Claims

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/test/MockERC6909Claims.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:** [ERC6909Claims](https://docs.uniswap.org/contracts/v4/reference/core/ERC6909Claims)

Mock contract for testing ERC6909Claims

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/test/MockERC6909Claims\#functions "Direct link to heading")

### mint [​](https://docs.uniswap.org/contracts/v4/reference/core/test/MockERC6909Claims\#mint "Direct link to heading")

mocked mint logic

```codeBlockLines_mRuA
function mint(address to, uint256 id, uint256 amount) public;

```

Copy

### burn [​](https://docs.uniswap.org/contracts/v4/reference/core/test/MockERC6909Claims\#burn "Direct link to heading")

mocked burn logic

```codeBlockLines_mRuA
function burn(uint256 id, uint256 amount) public;

```

Copy

### burnFrom [​](https://docs.uniswap.org/contracts/v4/reference/core/test/MockERC6909Claims\#burnfrom "Direct link to heading")

mocked burn logic without checking sender allowance

```codeBlockLines_mRuA
function burnFrom(address from, uint256 id, uint256 amount) public;

```

Copy

- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/test/MockERC6909Claims#functions)
  - [mint](https://docs.uniswap.org/contracts/v4/reference/core/test/MockERC6909Claims#mint)
  - [burn](https://docs.uniswap.org/contracts/v4/reference/core/test/MockERC6909Claims#burn)
  - [burnFrom](https://docs.uniswap.org/contracts/v4/reference/core/test/MockERC6909Claims#burnfrom)