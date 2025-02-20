[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/test/NativeERC20#)

On this page

# NativeERC20

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/test/NativeERC20.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:**
Test

_This token contract simulates the ERC20 representation of a native token where on `transfer` and `transferFrom` the native balances are modified using a precompile_

## State Variables [​](https://docs.uniswap.org/contracts/v4/reference/core/test/NativeERC20\#state-variables "Direct link to heading")

### name [​](https://docs.uniswap.org/contracts/v4/reference/core/test/NativeERC20\#name "Direct link to heading")

```codeBlockLines_mRuA
string public name = "NativeERC20";

```

Copy

### symbol [​](https://docs.uniswap.org/contracts/v4/reference/core/test/NativeERC20\#symbol "Direct link to heading")

```codeBlockLines_mRuA
string public symbol = "NERC20";

```

Copy

### decimals [​](https://docs.uniswap.org/contracts/v4/reference/core/test/NativeERC20\#decimals "Direct link to heading")

```codeBlockLines_mRuA
uint8 public decimals = 18;

```

Copy

### allowance [​](https://docs.uniswap.org/contracts/v4/reference/core/test/NativeERC20\#allowance "Direct link to heading")

```codeBlockLines_mRuA
mapping(address => mapping(address => uint256)) public allowance;

```

Copy

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/test/NativeERC20\#functions "Direct link to heading")

### totalSupply [​](https://docs.uniswap.org/contracts/v4/reference/core/test/NativeERC20\#totalsupply "Direct link to heading")

```codeBlockLines_mRuA
function totalSupply() public view returns (uint256);

```

Copy

### approve [​](https://docs.uniswap.org/contracts/v4/reference/core/test/NativeERC20\#approve "Direct link to heading")

```codeBlockLines_mRuA
function approve(address guy, uint256 wad) public returns (bool);

```

Copy

### transfer [​](https://docs.uniswap.org/contracts/v4/reference/core/test/NativeERC20\#transfer "Direct link to heading")

```codeBlockLines_mRuA
function transfer(address dst, uint256 wad) public returns (bool);

```

Copy

### transferFrom [​](https://docs.uniswap.org/contracts/v4/reference/core/test/NativeERC20\#transferfrom "Direct link to heading")

```codeBlockLines_mRuA
function transferFrom(address src, address dst, uint256 wad) public returns (bool);

```

Copy

### balanceOf [​](https://docs.uniswap.org/contracts/v4/reference/core/test/NativeERC20\#balanceof "Direct link to heading")

```codeBlockLines_mRuA
function balanceOf(address account) external view returns (uint256);

```

Copy

## Events [​](https://docs.uniswap.org/contracts/v4/reference/core/test/NativeERC20\#events "Direct link to heading")

### Approval [​](https://docs.uniswap.org/contracts/v4/reference/core/test/NativeERC20\#approval "Direct link to heading")

```codeBlockLines_mRuA
event Approval(address indexed src, address indexed guy, uint256 wad);

```

Copy

### Transfer [​](https://docs.uniswap.org/contracts/v4/reference/core/test/NativeERC20\#transfer-1 "Direct link to heading")

```codeBlockLines_mRuA
event Transfer(address indexed src, address indexed dst, uint256 wad);

```

Copy

- [State Variables](https://docs.uniswap.org/contracts/v4/reference/core/test/NativeERC20#state-variables)
  - [name](https://docs.uniswap.org/contracts/v4/reference/core/test/NativeERC20#name)
  - [symbol](https://docs.uniswap.org/contracts/v4/reference/core/test/NativeERC20#symbol)
  - [decimals](https://docs.uniswap.org/contracts/v4/reference/core/test/NativeERC20#decimals)
  - [allowance](https://docs.uniswap.org/contracts/v4/reference/core/test/NativeERC20#allowance)
- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/test/NativeERC20#functions)
  - [totalSupply](https://docs.uniswap.org/contracts/v4/reference/core/test/NativeERC20#totalsupply)
  - [approve](https://docs.uniswap.org/contracts/v4/reference/core/test/NativeERC20#approve)
  - [transfer](https://docs.uniswap.org/contracts/v4/reference/core/test/NativeERC20#transfer)
  - [transferFrom](https://docs.uniswap.org/contracts/v4/reference/core/test/NativeERC20#transferfrom)
  - [balanceOf](https://docs.uniswap.org/contracts/v4/reference/core/test/NativeERC20#balanceof)
- [Events](https://docs.uniswap.org/contracts/v4/reference/core/test/NativeERC20#events)
  - [Approval](https://docs.uniswap.org/contracts/v4/reference/core/test/NativeERC20#approval)
  - [Transfer](https://docs.uniswap.org/contracts/v4/reference/core/test/NativeERC20#transfer-1)