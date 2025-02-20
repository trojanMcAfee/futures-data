[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks#)

On this page

# MockHooks

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/test/MockHooks.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:** [IHooks](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IHooks)

## State Variables [​](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks\#state-variables "Direct link to heading")

### beforeInitializeData [​](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks\#beforeinitializedata "Direct link to heading")

```codeBlockLines_mRuA
bytes public beforeInitializeData;

```

Copy

### afterInitializeData [​](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks\#afterinitializedata "Direct link to heading")

```codeBlockLines_mRuA
bytes public afterInitializeData;

```

Copy

### beforeAddLiquidityData [​](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks\#beforeaddliquiditydata "Direct link to heading")

```codeBlockLines_mRuA
bytes public beforeAddLiquidityData;

```

Copy

### afterAddLiquidityData [​](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks\#afteraddliquiditydata "Direct link to heading")

```codeBlockLines_mRuA
bytes public afterAddLiquidityData;

```

Copy

### beforeRemoveLiquidityData [​](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks\#beforeremoveliquiditydata "Direct link to heading")

```codeBlockLines_mRuA
bytes public beforeRemoveLiquidityData;

```

Copy

### afterRemoveLiquidityData [​](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks\#afterremoveliquiditydata "Direct link to heading")

```codeBlockLines_mRuA
bytes public afterRemoveLiquidityData;

```

Copy

### beforeSwapData [​](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks\#beforeswapdata "Direct link to heading")

```codeBlockLines_mRuA
bytes public beforeSwapData;

```

Copy

### afterSwapData [​](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks\#afterswapdata "Direct link to heading")

```codeBlockLines_mRuA
bytes public afterSwapData;

```

Copy

### beforeDonateData [​](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks\#beforedonatedata "Direct link to heading")

```codeBlockLines_mRuA
bytes public beforeDonateData;

```

Copy

### afterDonateData [​](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks\#afterdonatedata "Direct link to heading")

```codeBlockLines_mRuA
bytes public afterDonateData;

```

Copy

### returnValues [​](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks\#returnvalues "Direct link to heading")

```codeBlockLines_mRuA
mapping(bytes4 => bytes4) public returnValues;

```

Copy

### lpFees [​](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks\#lpfees "Direct link to heading")

```codeBlockLines_mRuA
mapping(PoolId => uint16) public lpFees;

```

Copy

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks\#functions "Direct link to heading")

### beforeInitialize [​](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks\#beforeinitialize "Direct link to heading")

```codeBlockLines_mRuA
function beforeInitialize(address, PoolKey calldata, uint160) external override returns (bytes4);

```

Copy

### afterInitialize [​](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks\#afterinitialize "Direct link to heading")

```codeBlockLines_mRuA
function afterInitialize(address, PoolKey calldata, uint160, int24) external override returns (bytes4);

```

Copy

### beforeAddLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks\#beforeaddliquidity "Direct link to heading")

```codeBlockLines_mRuA
function beforeAddLiquidity(
    address,
    PoolKey calldata,
    IPoolManager.ModifyLiquidityParams calldata,
    bytes calldata hookData
) external override returns (bytes4);

```

Copy

### afterAddLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks\#afteraddliquidity "Direct link to heading")

```codeBlockLines_mRuA
function afterAddLiquidity(
    address,
    PoolKey calldata,
    IPoolManager.ModifyLiquidityParams calldata,
    BalanceDelta,
    BalanceDelta,
    bytes calldata hookData
) external override returns (bytes4, BalanceDelta);

```

Copy

### beforeRemoveLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks\#beforeremoveliquidity "Direct link to heading")

```codeBlockLines_mRuA
function beforeRemoveLiquidity(
    address,
    PoolKey calldata,
    IPoolManager.ModifyLiquidityParams calldata,
    bytes calldata hookData
) external override returns (bytes4);

```

Copy

### afterRemoveLiquidity [​](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks\#afterremoveliquidity "Direct link to heading")

```codeBlockLines_mRuA
function afterRemoveLiquidity(
    address,
    PoolKey calldata,
    IPoolManager.ModifyLiquidityParams calldata,
    BalanceDelta,
    BalanceDelta,
    bytes calldata hookData
) external override returns (bytes4, BalanceDelta);

```

Copy

### beforeSwap [​](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks\#beforeswap "Direct link to heading")

```codeBlockLines_mRuA
function beforeSwap(address, PoolKey calldata, IPoolManager.SwapParams calldata, bytes calldata hookData)
    external
    override
    returns (bytes4, BeforeSwapDelta, uint24);

```

Copy

### afterSwap [​](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks\#afterswap "Direct link to heading")

```codeBlockLines_mRuA
function afterSwap(address, PoolKey calldata, IPoolManager.SwapParams calldata, BalanceDelta, bytes calldata hookData)
    external
    override
    returns (bytes4, int128);

```

Copy

### beforeDonate [​](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks\#beforedonate "Direct link to heading")

```codeBlockLines_mRuA
function beforeDonate(address, PoolKey calldata, uint256, uint256, bytes calldata hookData)
    external
    override
    returns (bytes4);

```

Copy

### afterDonate [​](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks\#afterdonate "Direct link to heading")

```codeBlockLines_mRuA
function afterDonate(address, PoolKey calldata, uint256, uint256, bytes calldata hookData)
    external
    override
    returns (bytes4);

```

Copy

### setReturnValue [​](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks\#setreturnvalue "Direct link to heading")

```codeBlockLines_mRuA
function setReturnValue(bytes4 key, bytes4 value) external;

```

Copy

### setlpFee [​](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks\#setlpfee "Direct link to heading")

```codeBlockLines_mRuA
function setlpFee(PoolKey calldata key, uint16 value) external;

```

Copy

- [State Variables](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks#state-variables)
  - [beforeInitializeData](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks#beforeinitializedata)
  - [afterInitializeData](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks#afterinitializedata)
  - [beforeAddLiquidityData](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks#beforeaddliquiditydata)
  - [afterAddLiquidityData](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks#afteraddliquiditydata)
  - [beforeRemoveLiquidityData](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks#beforeremoveliquiditydata)
  - [afterRemoveLiquidityData](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks#afterremoveliquiditydata)
  - [beforeSwapData](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks#beforeswapdata)
  - [afterSwapData](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks#afterswapdata)
  - [beforeDonateData](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks#beforedonatedata)
  - [afterDonateData](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks#afterdonatedata)
  - [returnValues](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks#returnvalues)
  - [lpFees](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks#lpfees)
- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks#functions)
  - [beforeInitialize](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks#beforeinitialize)
  - [afterInitialize](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks#afterinitialize)
  - [beforeAddLiquidity](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks#beforeaddliquidity)
  - [afterAddLiquidity](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks#afteraddliquidity)
  - [beforeRemoveLiquidity](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks#beforeremoveliquidity)
  - [afterRemoveLiquidity](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks#afterremoveliquidity)
  - [beforeSwap](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks#beforeswap)
  - [afterSwap](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks#afterswap)
  - [beforeDonate](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks#beforedonate)
  - [afterDonate](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks#afterdonate)
  - [setReturnValue](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks#setreturnvalue)
  - [setlpFee](https://docs.uniswap.org/contracts/v4/reference/core/test/MockHooks#setlpfee)