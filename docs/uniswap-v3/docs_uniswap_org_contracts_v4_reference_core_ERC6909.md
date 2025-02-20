[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/ERC6909#)

On this page

# ERC6909

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/ERC6909.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:** [IERC6909Claims](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IERC6909Claims)

**Author:**
Solmate ( [https://github.com/transmissions11/solmate/blob/main/src/tokens/ERC6909.sol](https://github.com/transmissions11/solmate/blob/main/src/tokens/ERC6909.sol))

Minimalist and gas efficient standard ERC6909 implementation.

_Copied from the commit at 4b47a19038b798b4a33d9749d25e570443520647_

_This contract has been modified from the implementation at the above link._

## State Variables [​](https://docs.uniswap.org/contracts/v4/reference/core/ERC6909\#state-variables "Direct link to heading")

### isOperator [​](https://docs.uniswap.org/contracts/v4/reference/core/ERC6909\#isoperator "Direct link to heading")

```codeBlockLines_mRuA
mapping(address owner => mapping(address operator => bool isOperator)) public isOperator;

```

Copy

### balanceOf [​](https://docs.uniswap.org/contracts/v4/reference/core/ERC6909\#balanceof "Direct link to heading")

```codeBlockLines_mRuA
mapping(address owner => mapping(uint256 id => uint256 balance)) public balanceOf;

```

Copy

### allowance [​](https://docs.uniswap.org/contracts/v4/reference/core/ERC6909\#allowance "Direct link to heading")

```codeBlockLines_mRuA
mapping(address owner => mapping(address spender => mapping(uint256 id => uint256 amount))) public allowance;

```

Copy

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/ERC6909\#functions "Direct link to heading")

### transfer [​](https://docs.uniswap.org/contracts/v4/reference/core/ERC6909\#transfer "Direct link to heading")

```codeBlockLines_mRuA
function transfer(address receiver, uint256 id, uint256 amount) public virtual returns (bool);

```

Copy

### transferFrom [​](https://docs.uniswap.org/contracts/v4/reference/core/ERC6909\#transferfrom "Direct link to heading")

```codeBlockLines_mRuA
function transferFrom(address sender, address receiver, uint256 id, uint256 amount) public virtual returns (bool);

```

Copy

### approve [​](https://docs.uniswap.org/contracts/v4/reference/core/ERC6909\#approve "Direct link to heading")

```codeBlockLines_mRuA
function approve(address spender, uint256 id, uint256 amount) public virtual returns (bool);

```

Copy

### setOperator [​](https://docs.uniswap.org/contracts/v4/reference/core/ERC6909\#setoperator "Direct link to heading")

```codeBlockLines_mRuA
function setOperator(address operator, bool approved) public virtual returns (bool);

```

Copy

### supportsInterface [​](https://docs.uniswap.org/contracts/v4/reference/core/ERC6909\#supportsinterface "Direct link to heading")

```codeBlockLines_mRuA
function supportsInterface(bytes4 interfaceId) public view virtual returns (bool);

```

Copy

### \_mint [​](https://docs.uniswap.org/contracts/v4/reference/core/ERC6909\#_mint "Direct link to heading")

```codeBlockLines_mRuA
function _mint(address receiver, uint256 id, uint256 amount) internal virtual;

```

Copy

### \_burn [​](https://docs.uniswap.org/contracts/v4/reference/core/ERC6909\#_burn "Direct link to heading")

```codeBlockLines_mRuA
function _burn(address sender, uint256 id, uint256 amount) internal virtual;

```

Copy

- [State Variables](https://docs.uniswap.org/contracts/v4/reference/core/ERC6909#state-variables)
  - [isOperator](https://docs.uniswap.org/contracts/v4/reference/core/ERC6909#isoperator)
  - [balanceOf](https://docs.uniswap.org/contracts/v4/reference/core/ERC6909#balanceof)
  - [allowance](https://docs.uniswap.org/contracts/v4/reference/core/ERC6909#allowance)
- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/ERC6909#functions)
  - [transfer](https://docs.uniswap.org/contracts/v4/reference/core/ERC6909#transfer)
  - [transferFrom](https://docs.uniswap.org/contracts/v4/reference/core/ERC6909#transferfrom)
  - [approve](https://docs.uniswap.org/contracts/v4/reference/core/ERC6909#approve)
  - [setOperator](https://docs.uniswap.org/contracts/v4/reference/core/ERC6909#setoperator)
  - [supportsInterface](https://docs.uniswap.org/contracts/v4/reference/core/ERC6909#supportsinterface)
  - [\_mint](https://docs.uniswap.org/contracts/v4/reference/core/ERC6909#_mint)
  - [\_burn](https://docs.uniswap.org/contracts/v4/reference/core/ERC6909#_burn)