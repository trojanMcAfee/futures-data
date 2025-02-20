[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/ERC721PermitHash#)

On this page

# ERC721PermitHash

[Git Source](https://github.com/uniswap/v4-periphery/blob/3f295d8435e4f776ea2daeb96ce1bc6d63f33fc7/src/libraries/ERC721PermitHash.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

## State Variables [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/ERC721PermitHash\#state-variables "Direct link to heading")

### PERMIT\_TYPEHASH [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/ERC721PermitHash\#permit_typehash "Direct link to heading")

_Value is equal to keccak256("Permit(address spender,uint256 tokenId,uint256 nonce,uint256 deadline)");_

```codeBlockLines_mRuA
bytes32 constant PERMIT_TYPEHASH = 0x49ecf333e5b8c95c40fdafc95c1ad136e8914a8fb55e9dc8bb01eaa83a2df9ad;

```

Copy

### PERMIT\_FOR\_ALL\_TYPEHASH [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/ERC721PermitHash\#permit_for_all_typehash "Direct link to heading")

_Value is equal to keccak256("PermitForAll(address operator,bool approved,uint256 nonce,uint256 deadline)");_

```codeBlockLines_mRuA
bytes32 constant PERMIT_FOR_ALL_TYPEHASH = 0x6673cb397ee2a50b6b8401653d3638b4ac8b3db9c28aa6870ffceb7574ec2f76;

```

Copy

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/ERC721PermitHash\#functions "Direct link to heading")

### hashPermit [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/ERC721PermitHash\#hashpermit "Direct link to heading")

Hashes the data that will be signed for IERC721Permit\_v4.permit()

```codeBlockLines_mRuA
function hashPermit(address spender, uint256 tokenId, uint256 nonce, uint256 deadline)
    internal
    pure
    returns (bytes32 digest);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `spender` | `address` | The address which may spend the tokenId |
| `tokenId` | `uint256` | The tokenId of the owner, which may be spent by spender |
| `nonce` | `uint256` | A unique non-ordered value for each signature to prevent replay attacks |
| `deadline` | `uint256` | The time at which the signature expires |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `digest` | `bytes32` | The hash of the data to be signed; the equivalent to keccak256(abi.encode(PERMIT\_TYPEHASH, spender, tokenId, nonce, deadline)); |

### hashPermitForAll [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/ERC721PermitHash\#hashpermitforall "Direct link to heading")

Hashes the data that will be signed for IERC721Permit\_v4.permit()

```codeBlockLines_mRuA
function hashPermitForAll(address operator, bool approved, uint256 nonce, uint256 deadline)
    internal
    pure
    returns (bytes32 digest);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `operator` | `address` | The address which may spend any of the owner's tokenIds |
| `approved` | `bool` | true if the operator is to have full permission over the owner's tokenIds; false otherwise |
| `nonce` | `uint256` | A unique non-ordered value for each signature to prevent replay attacks |
| `deadline` | `uint256` | The time at which the signature expires |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `digest` | `bytes32` | The hash of the data to be signed; the equivalent to keccak256(abi.encode(PERMIT\_FOR\_ALL\_TYPEHASH, operator, approved, nonce, deadline)); |

- [State Variables](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/ERC721PermitHash#state-variables)
  - [PERMIT\_TYPEHASH](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/ERC721PermitHash#permit_typehash)
  - [PERMIT\_FOR\_ALL\_TYPEHASH](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/ERC721PermitHash#permit_for_all_typehash)
- [Functions](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/ERC721PermitHash#functions)
  - [hashPermit](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/ERC721PermitHash#hashpermit)
  - [hashPermitForAll](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/ERC721PermitHash#hashpermitforall)