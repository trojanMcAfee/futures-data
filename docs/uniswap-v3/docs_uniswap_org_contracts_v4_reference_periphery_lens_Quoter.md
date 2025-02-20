[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/periphery/lens/Quoter#)

On this page

# Quoter

[Git Source](https://github.com/uniswap/v4-periphery/blob/3f295d8435e4f776ea2daeb96ce1bc6d63f33fc7/src/lens/Quoter.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:** [IQuoter](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IQuoter), [BaseV4Quoter](https://docs.uniswap.org/contracts/v4/reference/periphery/base/BaseV4Quoter)

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/periphery/lens/Quoter\#functions "Direct link to heading")

### constructor [​](https://docs.uniswap.org/contracts/v4/reference/periphery/lens/Quoter\#constructor "Direct link to heading")

```codeBlockLines_mRuA
constructor(IPoolManager _poolManager) BaseV4Quoter(_poolManager);

```

Copy

### quoteExactInputSingle [​](https://docs.uniswap.org/contracts/v4/reference/periphery/lens/Quoter\#quoteexactinputsingle "Direct link to heading")

Returns the delta amounts for a given exact input swap of a single pool

```codeBlockLines_mRuA
function quoteExactInputSingle(QuoteExactSingleParams memory params)
    external
    returns (uint256 amountOut, uint256 gasEstimate);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `params` | `QuoteExactSingleParams` | The params for the quote, encoded as `QuoteExactSingleParams` poolKey The key for identifying a V4 pool zeroForOne If the swap is from currency0 to currency1 exactAmount The desired input amount hookData arbitrary hookData to pass into the associated hooks |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `amountOut` | `uint256` | The output quote for the exactIn swap |
| `gasEstimate` | `uint256` | Estimated gas units used for the swap |

### quoteExactInput [​](https://docs.uniswap.org/contracts/v4/reference/periphery/lens/Quoter\#quoteexactinput "Direct link to heading")

Returns the delta amounts along the swap path for a given exact input swap

```codeBlockLines_mRuA
function quoteExactInput(QuoteExactParams memory params) external returns (uint256 amountOut, uint256 gasEstimate);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `params` | `QuoteExactParams` | the params for the quote, encoded as 'QuoteExactParams' currencyIn The input currency of the swap path The path of the swap encoded as PathKeys that contains currency, fee, tickSpacing, and hook info exactAmount The desired input amount |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `amountOut` | `uint256` | The output quote for the exactIn swap |
| `gasEstimate` | `uint256` | Estimated gas units used for the swap |

### quoteExactOutputSingle [​](https://docs.uniswap.org/contracts/v4/reference/periphery/lens/Quoter\#quoteexactoutputsingle "Direct link to heading")

Returns the delta amounts for a given exact output swap of a single pool

```codeBlockLines_mRuA
function quoteExactOutputSingle(QuoteExactSingleParams memory params)
    external
    returns (uint256 amountIn, uint256 gasEstimate);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `params` | `QuoteExactSingleParams` | The params for the quote, encoded as `QuoteExactSingleParams` poolKey The key for identifying a V4 pool zeroForOne If the swap is from currency0 to currency1 exactAmount The desired output amount hookData arbitrary hookData to pass into the associated hooks |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `amountIn` | `uint256` | The input quote for the exactOut swap |
| `gasEstimate` | `uint256` | Estimated gas units used for the swap |

### quoteExactOutput [​](https://docs.uniswap.org/contracts/v4/reference/periphery/lens/Quoter\#quoteexactoutput "Direct link to heading")

Returns the delta amounts along the swap path for a given exact output swap

```codeBlockLines_mRuA
function quoteExactOutput(QuoteExactParams memory params) external returns (uint256 amountIn, uint256 gasEstimate);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `params` | `QuoteExactParams` | the params for the quote, encoded as 'QuoteExactParams' currencyOut The output currency of the swap path The path of the swap encoded as PathKeys that contains currency, fee, tickSpacing, and hook info exactAmount The desired output amount |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `amountIn` | `uint256` | The input quote for the exactOut swap |
| `gasEstimate` | `uint256` | Estimated gas units used for the swap |

### \_quoteExactInput [​](https://docs.uniswap.org/contracts/v4/reference/periphery/lens/Quoter\#_quoteexactinput "Direct link to heading")

_external function called within the \_unlockCallback, to simulate an exact input swap, then revert with the result_

```codeBlockLines_mRuA
function _quoteExactInput(QuoteExactParams calldata params) external selfOnly returns (bytes memory);

```

Copy

### \_quoteExactInputSingle [​](https://docs.uniswap.org/contracts/v4/reference/periphery/lens/Quoter\#_quoteexactinputsingle "Direct link to heading")

_external function called within the \_unlockCallback, to simulate a single-hop exact input swap, then revert with the result_

```codeBlockLines_mRuA
function _quoteExactInputSingle(QuoteExactSingleParams calldata params) external selfOnly returns (bytes memory);

```

Copy

### \_quoteExactOutput [​](https://docs.uniswap.org/contracts/v4/reference/periphery/lens/Quoter\#_quoteexactoutput "Direct link to heading")

_external function called within the \_unlockCallback, to simulate an exact output swap, then revert with the result_

```codeBlockLines_mRuA
function _quoteExactOutput(QuoteExactParams calldata params) external selfOnly returns (bytes memory);

```

Copy

### \_quoteExactOutputSingle [​](https://docs.uniswap.org/contracts/v4/reference/periphery/lens/Quoter\#_quoteexactoutputsingle "Direct link to heading")

_external function called within the \_unlockCallback, to simulate a single-hop exact output swap, then revert with the result_

```codeBlockLines_mRuA
function _quoteExactOutputSingle(QuoteExactSingleParams calldata params) external selfOnly returns (bytes memory);

```

Copy

- [Functions](https://docs.uniswap.org/contracts/v4/reference/periphery/lens/Quoter#functions)
  - [constructor](https://docs.uniswap.org/contracts/v4/reference/periphery/lens/Quoter#constructor)
  - [quoteExactInputSingle](https://docs.uniswap.org/contracts/v4/reference/periphery/lens/Quoter#quoteexactinputsingle)
  - [quoteExactInput](https://docs.uniswap.org/contracts/v4/reference/periphery/lens/Quoter#quoteexactinput)
  - [quoteExactOutputSingle](https://docs.uniswap.org/contracts/v4/reference/periphery/lens/Quoter#quoteexactoutputsingle)
  - [quoteExactOutput](https://docs.uniswap.org/contracts/v4/reference/periphery/lens/Quoter#quoteexactoutput)
  - [\_quoteExactInput](https://docs.uniswap.org/contracts/v4/reference/periphery/lens/Quoter#_quoteexactinput)
  - [\_quoteExactInputSingle](https://docs.uniswap.org/contracts/v4/reference/periphery/lens/Quoter#_quoteexactinputsingle)
  - [\_quoteExactOutput](https://docs.uniswap.org/contracts/v4/reference/periphery/lens/Quoter#_quoteexactoutput)
  - [\_quoteExactOutputSingle](https://docs.uniswap.org/contracts/v4/reference/periphery/lens/Quoter#_quoteexactoutputsingle)