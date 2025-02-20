[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/test/NoDelegateCallTest#)

On this page

# NoDelegateCallTest

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/test/NoDelegateCallTest.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:** [NoDelegateCall](https://docs.uniswap.org/contracts/v4/reference/core/NoDelegateCall)

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/test/NoDelegateCallTest\#functions "Direct link to heading")

### canBeDelegateCalled [​](https://docs.uniswap.org/contracts/v4/reference/core/test/NoDelegateCallTest\#canbedelegatecalled "Direct link to heading")

```codeBlockLines_mRuA
function canBeDelegateCalled() public view returns (uint256);

```

Copy

### cannotBeDelegateCalled [​](https://docs.uniswap.org/contracts/v4/reference/core/test/NoDelegateCallTest\#cannotbedelegatecalled "Direct link to heading")

```codeBlockLines_mRuA
function cannotBeDelegateCalled() public view noDelegateCall returns (uint256);

```

Copy

### getGasCostOfCanBeDelegateCalled [​](https://docs.uniswap.org/contracts/v4/reference/core/test/NoDelegateCallTest\#getgascostofcanbedelegatecalled "Direct link to heading")

```codeBlockLines_mRuA
function getGasCostOfCanBeDelegateCalled() external view returns (uint256);

```

Copy

### getGasCostOfCannotBeDelegateCalled [​](https://docs.uniswap.org/contracts/v4/reference/core/test/NoDelegateCallTest\#getgascostofcannotbedelegatecalled "Direct link to heading")

```codeBlockLines_mRuA
function getGasCostOfCannotBeDelegateCalled() external view returns (uint256);

```

Copy

### callsIntoNoDelegateCallFunction [​](https://docs.uniswap.org/contracts/v4/reference/core/test/NoDelegateCallTest\#callsintonodelegatecallfunction "Direct link to heading")

```codeBlockLines_mRuA
function callsIntoNoDelegateCallFunction() external view;

```

Copy

### noDelegateCallPrivate [​](https://docs.uniswap.org/contracts/v4/reference/core/test/NoDelegateCallTest\#nodelegatecallprivate "Direct link to heading")

```codeBlockLines_mRuA
function noDelegateCallPrivate() private view noDelegateCall;

```

Copy

- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/test/NoDelegateCallTest#functions)
  - [canBeDelegateCalled](https://docs.uniswap.org/contracts/v4/reference/core/test/NoDelegateCallTest#canbedelegatecalled)
  - [cannotBeDelegateCalled](https://docs.uniswap.org/contracts/v4/reference/core/test/NoDelegateCallTest#cannotbedelegatecalled)
  - [getGasCostOfCanBeDelegateCalled](https://docs.uniswap.org/contracts/v4/reference/core/test/NoDelegateCallTest#getgascostofcanbedelegatecalled)
  - [getGasCostOfCannotBeDelegateCalled](https://docs.uniswap.org/contracts/v4/reference/core/test/NoDelegateCallTest#getgascostofcannotbedelegatecalled)
  - [callsIntoNoDelegateCallFunction](https://docs.uniswap.org/contracts/v4/reference/core/test/NoDelegateCallTest#callsintonodelegatecallfunction)
  - [noDelegateCallPrivate](https://docs.uniswap.org/contracts/v4/reference/core/test/NoDelegateCallTest#nodelegatecallprivate)