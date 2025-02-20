[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IExtsload#)

On this page

# IExtsload

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/interfaces/IExtsload.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

Interface for functions to access any storage slot in a contract

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IExtsload\#functions "Direct link to heading")

### extsload [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IExtsload\#extsload "Direct link to heading")

Called by external contracts to access granular pool state

```codeBlockLines_mRuA
function extsload(bytes32 slot) external view returns (bytes32 value);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `slot` | `bytes32` | Key of slot to sload |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `value` | `bytes32` | The value of the slot as bytes32 |

### extsload [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IExtsload\#extsload-1 "Direct link to heading")

Called by external contracts to access granular pool state

```codeBlockLines_mRuA
function extsload(bytes32 startSlot, uint256 nSlots) external view returns (bytes32[] memory values);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `startSlot` | `bytes32` | Key of slot to start sloading from |
| `nSlots` | `uint256` | Number of slots to load into return value |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `values` | `bytes32[]` | List of loaded values. |

### extsload [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IExtsload\#extsload-2 "Direct link to heading")

Called by external contracts to access sparse pool state

```codeBlockLines_mRuA
function extsload(bytes32[] calldata slots) external view returns (bytes32[] memory values);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `slots` | `bytes32[]` | List of slots to SLOAD from. |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `values` | `bytes32[]` | List of loaded values. |

- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IExtsload#functions)
  - [extsload](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IExtsload#extsload)
  - [extsload](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IExtsload#extsload-1)
  - [extsload](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IExtsload#extsload-2)