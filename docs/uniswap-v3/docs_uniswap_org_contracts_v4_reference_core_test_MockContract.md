[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/test/MockContract#)

On this page

# MockContract

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/test/MockContract.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:**
Proxy

Mock contract that tracks the number of calls to various functions by selector

_allows for proxying to an implementation contract_
_if real logic or return values are needed_

## State Variables [​](https://docs.uniswap.org/contracts/v4/reference/core/test/MockContract\#state-variables "Direct link to heading")

### calls [​](https://docs.uniswap.org/contracts/v4/reference/core/test/MockContract\#calls "Direct link to heading")

```codeBlockLines_mRuA
mapping(bytes32 => uint256) public calls;

```

Copy

### callParams [​](https://docs.uniswap.org/contracts/v4/reference/core/test/MockContract\#callparams "Direct link to heading")

```codeBlockLines_mRuA
mapping(bytes32 => mapping(bytes => uint256)) public callParams;

```

Copy

### impl [​](https://docs.uniswap.org/contracts/v4/reference/core/test/MockContract\#impl "Direct link to heading")

If set, delegatecall to implementation after tracking call

```codeBlockLines_mRuA
address internal impl;

```

Copy

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/test/MockContract\#functions "Direct link to heading")

### timesCalledSelector [​](https://docs.uniswap.org/contracts/v4/reference/core/test/MockContract\#timescalledselector "Direct link to heading")

```codeBlockLines_mRuA
function timesCalledSelector(bytes32 selector) public view returns (uint256);

```

Copy

### timesCalled [​](https://docs.uniswap.org/contracts/v4/reference/core/test/MockContract\#timescalled "Direct link to heading")

```codeBlockLines_mRuA
function timesCalled(string calldata fnSig) public view returns (uint256);

```

Copy

### calledWithSelector [​](https://docs.uniswap.org/contracts/v4/reference/core/test/MockContract\#calledwithselector "Direct link to heading")

```codeBlockLines_mRuA
function calledWithSelector(bytes32 selector, bytes calldata params) public view returns (bool);

```

Copy

### calledWith [​](https://docs.uniswap.org/contracts/v4/reference/core/test/MockContract\#calledwith "Direct link to heading")

```codeBlockLines_mRuA
function calledWith(string calldata fnSig, bytes calldata params) public view returns (bool);

```

Copy

### \_implementation [​](https://docs.uniswap.org/contracts/v4/reference/core/test/MockContract\#_implementation "Direct link to heading")

exposes implementation contract address

```codeBlockLines_mRuA
function _implementation() internal view override returns (address);

```

Copy

### setImplementation [​](https://docs.uniswap.org/contracts/v4/reference/core/test/MockContract\#setimplementation "Direct link to heading")

```codeBlockLines_mRuA
function setImplementation(address _impl) external;

```

Copy

### \_beforeFallback [​](https://docs.uniswap.org/contracts/v4/reference/core/test/MockContract\#_beforefallback "Direct link to heading")

Captures calls by selector

```codeBlockLines_mRuA
function _beforeFallback() internal;

```

Copy

### \_fallback [​](https://docs.uniswap.org/contracts/v4/reference/core/test/MockContract\#_fallback "Direct link to heading")

```codeBlockLines_mRuA
function _fallback() internal override;

```

Copy

### receive [​](https://docs.uniswap.org/contracts/v4/reference/core/test/MockContract\#receive "Direct link to heading")

```codeBlockLines_mRuA
receive() external payable;

```

Copy

- [State Variables](https://docs.uniswap.org/contracts/v4/reference/core/test/MockContract#state-variables)
  - [calls](https://docs.uniswap.org/contracts/v4/reference/core/test/MockContract#calls)
  - [callParams](https://docs.uniswap.org/contracts/v4/reference/core/test/MockContract#callparams)
  - [impl](https://docs.uniswap.org/contracts/v4/reference/core/test/MockContract#impl)
- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/test/MockContract#functions)
  - [timesCalledSelector](https://docs.uniswap.org/contracts/v4/reference/core/test/MockContract#timescalledselector)
  - [timesCalled](https://docs.uniswap.org/contracts/v4/reference/core/test/MockContract#timescalled)
  - [calledWithSelector](https://docs.uniswap.org/contracts/v4/reference/core/test/MockContract#calledwithselector)
  - [calledWith](https://docs.uniswap.org/contracts/v4/reference/core/test/MockContract#calledwith)
  - [\_implementation](https://docs.uniswap.org/contracts/v4/reference/core/test/MockContract#_implementation)
  - [setImplementation](https://docs.uniswap.org/contracts/v4/reference/core/test/MockContract#setimplementation)
  - [\_beforeFallback](https://docs.uniswap.org/contracts/v4/reference/core/test/MockContract#_beforefallback)
  - [\_fallback](https://docs.uniswap.org/contracts/v4/reference/core/test/MockContract#_fallback)
  - [receive](https://docs.uniswap.org/contracts/v4/reference/core/test/MockContract#receive)