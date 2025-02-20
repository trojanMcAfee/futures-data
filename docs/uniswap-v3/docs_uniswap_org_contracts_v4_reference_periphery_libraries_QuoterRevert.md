[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/QuoterRevert#)

On this page

# QuoterRevert

[Git Source](https://github.com/uniswap/v4-periphery/blob/3f295d8435e4f776ea2daeb96ce1bc6d63f33fc7/src/libraries/QuoterRevert.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/QuoterRevert\#functions "Direct link to heading")

### revertQuote [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/QuoterRevert\#revertquote "Direct link to heading")

reverts, where the revert data is the provided bytes

_called when quoting, to record the quote amount in an error_

_QuoteSwap is used to differentiate this error from other errors thrown when simulating the swap_

```codeBlockLines_mRuA
function revertQuote(uint256 quoteAmount) internal pure;

```

Copy

### bubbleReason [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/QuoterRevert\#bubblereason "Direct link to heading")

reverts using the revertData as the reason

_to bubble up both the valid QuoteSwap(amount) error, or an alternative error thrown during simulation_

```codeBlockLines_mRuA
function bubbleReason(bytes memory revertData) internal pure;

```

Copy

### parseQuoteAmount [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/QuoterRevert\#parsequoteamount "Direct link to heading")

validates whether a revert reason is a valid swap quote or not
if valid, it decodes the quote to return. Otherwise it reverts.

```codeBlockLines_mRuA
function parseQuoteAmount(bytes memory reason) internal pure returns (uint256 quoteAmount);

```

Copy

## Errors [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/QuoterRevert\#errors "Direct link to heading")

### UnexpectedRevertBytes [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/QuoterRevert\#unexpectedrevertbytes "Direct link to heading")

error thrown when invalid revert bytes are thrown by the quote

```codeBlockLines_mRuA
error UnexpectedRevertBytes(bytes revertData);

```

Copy

### QuoteSwap [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/QuoterRevert\#quoteswap "Direct link to heading")

error thrown containing the quote as the data, to be caught and parsed later

```codeBlockLines_mRuA
error QuoteSwap(uint256 amount);

```

Copy

- [Functions](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/QuoterRevert#functions)
  - [revertQuote](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/QuoterRevert#revertquote)
  - [bubbleReason](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/QuoterRevert#bubblereason)
  - [parseQuoteAmount](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/QuoterRevert#parsequoteamount)
- [Errors](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/QuoterRevert#errors)
  - [UnexpectedRevertBytes](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/QuoterRevert#unexpectedrevertbytes)
  - [QuoteSwap](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/QuoterRevert#quoteswap)