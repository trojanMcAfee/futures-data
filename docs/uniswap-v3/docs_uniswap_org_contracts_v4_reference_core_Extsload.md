[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/Extsload#)

On this page

# Extsload

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/Extsload.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:** [IExtsload](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IExtsload)

Enables public storage access for efficient state retrieval by external contracts.
[https://eips.ethereum.org/EIPS/eip-2330#rationale](https://eips.ethereum.org/EIPS/eip-2330#rationale)

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/Extsload\#functions "Direct link to heading")

### extsload [​](https://docs.uniswap.org/contracts/v4/reference/core/Extsload\#extsload-1 "Direct link to heading")

Called by external contracts to access granular pool state

```codeBlockLines_mRuA
function extsload(bytes32 slot) external view returns (bytes32);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `slot` | `bytes32` | Key of slot to sload |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `bytes32` | value The value of the slot as bytes32 |

### extsload [​](https://docs.uniswap.org/contracts/v4/reference/core/Extsload\#extsload-2 "Direct link to heading")

Called by external contracts to access granular pool state

```codeBlockLines_mRuA
function extsload(bytes32 startSlot, uint256 nSlots) external view returns (bytes32[] memory);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `startSlot` | `bytes32` |  |
| `nSlots` | `uint256` |  |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `bytes32[]` | value The value of the slot as bytes32 |

### extsload [​](https://docs.uniswap.org/contracts/v4/reference/core/Extsload\#extsload-3 "Direct link to heading")

Called by external contracts to access granular pool state

```codeBlockLines_mRuA
function extsload(bytes32[] calldata slots) external view returns (bytes32[] memory);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `slots` | `bytes32[]` |  |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `bytes32[]` | value The value of the slot as bytes32 |

- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/Extsload#functions)
  - [extsload](https://docs.uniswap.org/contracts/v4/reference/core/Extsload#extsload-1)
  - [extsload](https://docs.uniswap.org/contracts/v4/reference/core/Extsload#extsload-2)
  - [extsload](https://docs.uniswap.org/contracts/v4/reference/core/Extsload#extsload-3)