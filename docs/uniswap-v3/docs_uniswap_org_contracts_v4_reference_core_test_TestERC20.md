[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/test/TestERC20#)

On this page

# TestERC20

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/test/TestERC20.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:** [IERC20Minimal](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IERC20Minimal)

## State Variables [​](https://docs.uniswap.org/contracts/v4/reference/core/test/TestERC20\#state-variables "Direct link to heading")

### balanceOf [​](https://docs.uniswap.org/contracts/v4/reference/core/test/TestERC20\#balanceof "Direct link to heading")

```codeBlockLines_mRuA
mapping(address => uint256) public override balanceOf;

```

Copy

### allowance [​](https://docs.uniswap.org/contracts/v4/reference/core/test/TestERC20\#allowance "Direct link to heading")

```codeBlockLines_mRuA
mapping(address => mapping(address => uint256)) public override allowance;

```

Copy

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/test/TestERC20\#functions "Direct link to heading")

### constructor [​](https://docs.uniswap.org/contracts/v4/reference/core/test/TestERC20\#constructor "Direct link to heading")

```codeBlockLines_mRuA
constructor(uint256 amountToMint);

```

Copy

### mint [​](https://docs.uniswap.org/contracts/v4/reference/core/test/TestERC20\#mint "Direct link to heading")

```codeBlockLines_mRuA
function mint(address to, uint256 amount) public;

```

Copy

### transfer [​](https://docs.uniswap.org/contracts/v4/reference/core/test/TestERC20\#transfer "Direct link to heading")

```codeBlockLines_mRuA
function transfer(address recipient, uint256 amount) external override returns (bool);

```

Copy

### approve [​](https://docs.uniswap.org/contracts/v4/reference/core/test/TestERC20\#approve "Direct link to heading")

```codeBlockLines_mRuA
function approve(address spender, uint256 amount) external override returns (bool);

```

Copy

### transferFrom [​](https://docs.uniswap.org/contracts/v4/reference/core/test/TestERC20\#transferfrom "Direct link to heading")

```codeBlockLines_mRuA
function transferFrom(address sender, address recipient, uint256 amount) external override returns (bool);

```

Copy

- [State Variables](https://docs.uniswap.org/contracts/v4/reference/core/test/TestERC20#state-variables)
  - [balanceOf](https://docs.uniswap.org/contracts/v4/reference/core/test/TestERC20#balanceof)
  - [allowance](https://docs.uniswap.org/contracts/v4/reference/core/test/TestERC20#allowance)
- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/test/TestERC20#functions)
  - [constructor](https://docs.uniswap.org/contracts/v4/reference/core/test/TestERC20#constructor)
  - [mint](https://docs.uniswap.org/contracts/v4/reference/core/test/TestERC20#mint)
  - [transfer](https://docs.uniswap.org/contracts/v4/reference/core/test/TestERC20#transfer)
  - [approve](https://docs.uniswap.org/contracts/v4/reference/core/test/TestERC20#approve)
  - [transferFrom](https://docs.uniswap.org/contracts/v4/reference/core/test/TestERC20#transferfrom)