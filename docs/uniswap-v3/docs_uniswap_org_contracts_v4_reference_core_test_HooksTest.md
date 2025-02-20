[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/test/HooksTest#)

On this page

# HooksTest

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/test/HooksTest.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/test/HooksTest\#functions "Direct link to heading")

### validateHookPermissions [​](https://docs.uniswap.org/contracts/v4/reference/core/test/HooksTest\#validatehookpermissions "Direct link to heading")

```codeBlockLines_mRuA
function validateHookPermissions(address hookAddress, Hooks.Permissions calldata params) external pure;

```

Copy

### isValidHookAddress [​](https://docs.uniswap.org/contracts/v4/reference/core/test/HooksTest\#isvalidhookaddress "Direct link to heading")

```codeBlockLines_mRuA
function isValidHookAddress(address hookAddress, uint24 fee) external pure returns (bool);

```

Copy

### shouldCallBeforeInitialize [​](https://docs.uniswap.org/contracts/v4/reference/core/test/HooksTest\#shouldcallbeforeinitialize "Direct link to heading")

```codeBlockLines_mRuA
function shouldCallBeforeInitialize(address hookAddress) external pure returns (bool);

```

Copy

### shouldCallAfterInitialize [​](https://docs.uniswap.org/contracts/v4/reference/core/test/HooksTest\#shouldcallafterinitialize "Direct link to heading")

```codeBlockLines_mRuA
function shouldCallAfterInitialize(address hookAddress) external pure returns (bool);

```

Copy

### shouldCallBeforeSwap [​](https://docs.uniswap.org/contracts/v4/reference/core/test/HooksTest\#shouldcallbeforeswap "Direct link to heading")

```codeBlockLines_mRuA
function shouldCallBeforeSwap(address hookAddress) external pure returns (bool);

```

Copy

### shouldCallAfterSwap [​](https://docs.uniswap.org/contracts/v4/reference/core/test/HooksTest\#shouldcallafterswap "Direct link to heading")

```codeBlockLines_mRuA
function shouldCallAfterSwap(address hookAddress) external pure returns (bool);

```

Copy

### shouldCallBeforeAddLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/core/test/HooksTest\#shouldcallbeforeaddliquidity "Direct link to heading")

```codeBlockLines_mRuA
function shouldCallBeforeAddLiquidity(address hookAddress) external pure returns (bool);

```

Copy

### shouldCallAfterAddLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/core/test/HooksTest\#shouldcallafteraddliquidity "Direct link to heading")

```codeBlockLines_mRuA
function shouldCallAfterAddLiquidity(address hookAddress) external pure returns (bool);

```

Copy

### shouldCallBeforeRemoveLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/core/test/HooksTest\#shouldcallbeforeremoveliquidity "Direct link to heading")

```codeBlockLines_mRuA
function shouldCallBeforeRemoveLiquidity(address hookAddress) external pure returns (bool);

```

Copy

### shouldCallAfterRemoveLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/core/test/HooksTest\#shouldcallafterremoveliquidity "Direct link to heading")

```codeBlockLines_mRuA
function shouldCallAfterRemoveLiquidity(address hookAddress) external pure returns (bool);

```

Copy

### shouldCallBeforeDonate [​](https://docs.uniswap.org/contracts/v4/reference/core/test/HooksTest\#shouldcallbeforedonate "Direct link to heading")

```codeBlockLines_mRuA
function shouldCallBeforeDonate(address hookAddress) external pure returns (bool);

```

Copy

### shouldCallAfterDonate [​](https://docs.uniswap.org/contracts/v4/reference/core/test/HooksTest\#shouldcallafterdonate "Direct link to heading")

```codeBlockLines_mRuA
function shouldCallAfterDonate(address hookAddress) external pure returns (bool);

```

Copy

### getGasCostOfShouldCall [​](https://docs.uniswap.org/contracts/v4/reference/core/test/HooksTest\#getgascostofshouldcall "Direct link to heading")

```codeBlockLines_mRuA
function getGasCostOfShouldCall(address hookAddress) external view returns (uint256);

```

Copy

### getGasCostOfValidateHookAddress [​](https://docs.uniswap.org/contracts/v4/reference/core/test/HooksTest\#getgascostofvalidatehookaddress "Direct link to heading")

```codeBlockLines_mRuA
function getGasCostOfValidateHookAddress(address hookAddress, Hooks.Permissions calldata params)
    external
    view
    returns (uint256);

```

Copy

- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/test/HooksTest#functions)
  - [validateHookPermissions](https://docs.uniswap.org/contracts/v4/reference/core/test/HooksTest#validatehookpermissions)
  - [isValidHookAddress](https://docs.uniswap.org/contracts/v4/reference/core/test/HooksTest#isvalidhookaddress)
  - [shouldCallBeforeInitialize](https://docs.uniswap.org/contracts/v4/reference/core/test/HooksTest#shouldcallbeforeinitialize)
  - [shouldCallAfterInitialize](https://docs.uniswap.org/contracts/v4/reference/core/test/HooksTest#shouldcallafterinitialize)
  - [shouldCallBeforeSwap](https://docs.uniswap.org/contracts/v4/reference/core/test/HooksTest#shouldcallbeforeswap)
  - [shouldCallAfterSwap](https://docs.uniswap.org/contracts/v4/reference/core/test/HooksTest#shouldcallafterswap)
  - [shouldCallBeforeAddLiquidity](https://docs.uniswap.org/contracts/v4/reference/core/test/HooksTest#shouldcallbeforeaddliquidity)
  - [shouldCallAfterAddLiquidity](https://docs.uniswap.org/contracts/v4/reference/core/test/HooksTest#shouldcallafteraddliquidity)
  - [shouldCallBeforeRemoveLiquidity](https://docs.uniswap.org/contracts/v4/reference/core/test/HooksTest#shouldcallbeforeremoveliquidity)
  - [shouldCallAfterRemoveLiquidity](https://docs.uniswap.org/contracts/v4/reference/core/test/HooksTest#shouldcallafterremoveliquidity)
  - [shouldCallBeforeDonate](https://docs.uniswap.org/contracts/v4/reference/core/test/HooksTest#shouldcallbeforedonate)
  - [shouldCallAfterDonate](https://docs.uniswap.org/contracts/v4/reference/core/test/HooksTest#shouldcallafterdonate)
  - [getGasCostOfShouldCall](https://docs.uniswap.org/contracts/v4/reference/core/test/HooksTest#getgascostofshouldcall)
  - [getGasCostOfValidateHookAddress](https://docs.uniswap.org/contracts/v4/reference/core/test/HooksTest#getgascostofvalidatehookaddress)