[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IPositionDescriptor#)

On this page

# IPositionDescriptor

[Git Source](https://github.com/uniswap/v4-periphery/blob/3f295d8435e4f776ea2daeb96ce1bc6d63f33fc7/src/interfaces/IPositionDescriptor.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IPositionDescriptor\#functions "Direct link to heading")

### tokenURI [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IPositionDescriptor\#tokenuri "Direct link to heading")

Produces the URI describing a particular token ID

_Note this URI may be a data: URI with the JSON contents directly inlined_

```codeBlockLines_mRuA
function tokenURI(IPositionManager positionManager, uint256 tokenId) external view returns (string memory);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `positionManager` | `IPositionManager` | The position manager for which to describe the token |
| `tokenId` | `uint256` | The ID of the token for which to produce a description, which may not be valid |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `string` | The URI of the ERC721-compliant metadata |

- [Functions](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IPositionDescriptor#functions)
  - [tokenURI](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IPositionDescriptor#tokenuri)