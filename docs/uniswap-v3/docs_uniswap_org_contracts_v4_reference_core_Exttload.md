[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/Exttload#)

On this page

# Exttload

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/Exttload.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:** [IExttload](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IExttload)

Enables public transient storage access for efficient state retrieval by external contracts.
[https://eips.ethereum.org/EIPS/eip-2330#rationale](https://eips.ethereum.org/EIPS/eip-2330#rationale)

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/Exttload\#functions "Direct link to heading")

### exttload [​](https://docs.uniswap.org/contracts/v4/reference/core/Exttload\#exttload-1 "Direct link to heading")

Called by external contracts to access transient storage of the contract

```codeBlockLines_mRuA
function exttload(bytes32 slot) external view returns (bytes32);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `slot` | `bytes32` | Key of slot to tload |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `bytes32` | value The value of the slot as bytes32 |

### exttload [​](https://docs.uniswap.org/contracts/v4/reference/core/Exttload\#exttload-2 "Direct link to heading")

Called by external contracts to access transient storage of the contract

```codeBlockLines_mRuA
function exttload(bytes32[] calldata slots) external view returns (bytes32[] memory);

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

- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/Exttload#functions)
  - [exttload](https://docs.uniswap.org/contracts/v4/reference/core/Exttload#exttload-1)
  - [exttload](https://docs.uniswap.org/contracts/v4/reference/core/Exttload#exttload-2)