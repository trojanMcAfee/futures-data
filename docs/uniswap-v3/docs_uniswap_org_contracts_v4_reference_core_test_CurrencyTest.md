[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/test/CurrencyTest#)

On this page

# CurrencyTest

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/test/CurrencyTest.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/test/CurrencyTest\#functions "Direct link to heading")

### transfer [​](https://docs.uniswap.org/contracts/v4/reference/core/test/CurrencyTest\#transfer "Direct link to heading")

```codeBlockLines_mRuA
function transfer(Currency currency, address to, uint256 amount) external;

```

Copy

### balanceOfSelf [​](https://docs.uniswap.org/contracts/v4/reference/core/test/CurrencyTest\#balanceofself "Direct link to heading")

```codeBlockLines_mRuA
function balanceOfSelf(Currency currency) external view returns (uint256);

```

Copy

### balanceOf [​](https://docs.uniswap.org/contracts/v4/reference/core/test/CurrencyTest\#balanceof "Direct link to heading")

```codeBlockLines_mRuA
function balanceOf(Currency currency, address owner) external view returns (uint256);

```

Copy

### isAddressZero [​](https://docs.uniswap.org/contracts/v4/reference/core/test/CurrencyTest\#isaddresszero "Direct link to heading")

```codeBlockLines_mRuA
function isAddressZero(Currency currency) external pure returns (bool);

```

Copy

### toId [​](https://docs.uniswap.org/contracts/v4/reference/core/test/CurrencyTest\#toid "Direct link to heading")

```codeBlockLines_mRuA
function toId(Currency currency) external pure returns (uint256);

```

Copy

### fromId [​](https://docs.uniswap.org/contracts/v4/reference/core/test/CurrencyTest\#fromid "Direct link to heading")

```codeBlockLines_mRuA
function fromId(uint256 id) external pure returns (Currency);

```

Copy

- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/test/CurrencyTest#functions)
  - [transfer](https://docs.uniswap.org/contracts/v4/reference/core/test/CurrencyTest#transfer)
  - [balanceOfSelf](https://docs.uniswap.org/contracts/v4/reference/core/test/CurrencyTest#balanceofself)
  - [balanceOf](https://docs.uniswap.org/contracts/v4/reference/core/test/CurrencyTest#balanceof)
  - [isAddressZero](https://docs.uniswap.org/contracts/v4/reference/core/test/CurrencyTest#isaddresszero)
  - [toId](https://docs.uniswap.org/contracts/v4/reference/core/test/CurrencyTest#toid)
  - [fromId](https://docs.uniswap.org/contracts/v4/reference/core/test/CurrencyTest#fromid)