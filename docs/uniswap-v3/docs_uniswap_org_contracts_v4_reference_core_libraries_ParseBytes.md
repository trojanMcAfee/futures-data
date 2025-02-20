[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/libraries/ParseBytes#)

On this page

# ParseBytes

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/libraries/ParseBytes.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

Parses bytes returned from hooks and the byte selector used to check return selectors from hooks.

_parseSelector also is used to parse the expected selector_
_For parsing hook returns, note that all hooks return either bytes4 or (bytes4, 32-byte-delta) or (bytes4, 32-byte-delta, uint24)._

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/ParseBytes\#functions "Direct link to heading")

### parseSelector [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/ParseBytes\#parseselector "Direct link to heading")

```codeBlockLines_mRuA
function parseSelector(bytes memory result) internal pure returns (bytes4 selector);

```

Copy

### parseFee [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/ParseBytes\#parsefee "Direct link to heading")

```codeBlockLines_mRuA
function parseFee(bytes memory result) internal pure returns (uint24 lpFee);

```

Copy

### parseReturnDelta [​](https://docs.uniswap.org/contracts/v4/reference/core/libraries/ParseBytes\#parsereturndelta "Direct link to heading")

```codeBlockLines_mRuA
function parseReturnDelta(bytes memory result) internal pure returns (int256 hookReturn);

```

Copy

- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/libraries/ParseBytes#functions)
  - [parseSelector](https://docs.uniswap.org/contracts/v4/reference/core/libraries/ParseBytes#parseselector)
  - [parseFee](https://docs.uniswap.org/contracts/v4/reference/core/libraries/ParseBytes#parsefee)
  - [parseReturnDelta](https://docs.uniswap.org/contracts/v4/reference/core/libraries/ParseBytes#parsereturndelta)