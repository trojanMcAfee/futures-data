[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IERC721Permit_v4#)

On this page

# IERC721Permit\_v4

[Git Source](https://github.com/uniswap/v4-periphery/blob/3f295d8435e4f776ea2daeb96ce1bc6d63f33fc7/src/interfaces/IERC721Permit_v4.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

Extension to ERC721 that includes a permit function for signature based approvals

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IERC721Permit_v4\#functions "Direct link to heading")

### permit [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IERC721Permit_v4\#permit "Direct link to heading")

Approve of a specific token ID for spending by spender via signature

_payable so it can be multicalled with NATIVE related actions_

```codeBlockLines_mRuA
function permit(address spender, uint256 tokenId, uint256 deadline, uint256 nonce, bytes calldata signature)
    external
    payable;

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `spender` | `address` | The account that is being approved |
| `tokenId` | `uint256` | The ID of the token that is being approved for spending |
| `deadline` | `uint256` | The deadline timestamp by which the call must be mined for the approve to work |
| `nonce` | `uint256` | a unique value, for an owner, to prevent replay attacks; an unordered nonce where the top 248 bits correspond to a word and the bottom 8 bits calculate the bit position of the word |
| `signature` | `bytes` | Concatenated data from a valid secp256k1 signature from the holder, i.e. abi.encodePacked(r, s, v) |

### permitForAll [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IERC721Permit_v4\#permitforall "Direct link to heading")

Set an operator with full permission to an owner's tokens via signature

_payable so it can be multicalled with NATIVE related actions_

```codeBlockLines_mRuA
function permitForAll(
    address owner,
    address operator,
    bool approved,
    uint256 deadline,
    uint256 nonce,
    bytes calldata signature
) external payable;

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `owner` | `address` | The address that is setting the operator |
| `operator` | `address` | The address that will be set as an operator for the owner |
| `approved` | `bool` | The permission to set on the operator |
| `deadline` | `uint256` | The deadline timestamp by which the call must be mined for the approve to work |
| `nonce` | `uint256` | a unique value, for an owner, to prevent replay attacks; an unordered nonce where the top 248 bits correspond to a word and the bottom 8 bits calculate the bit position of the word |
| `signature` | `bytes` | Concatenated data from a valid secp256k1 signature from the holder, i.e. abi.encodePacked(r, s, v) |

## Errors [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IERC721Permit_v4\#errors "Direct link to heading")

### SignatureDeadlineExpired [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IERC721Permit_v4\#signaturedeadlineexpired "Direct link to heading")

```codeBlockLines_mRuA
error SignatureDeadlineExpired();

```

Copy

### NoSelfPermit [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IERC721Permit_v4\#noselfpermit "Direct link to heading")

```codeBlockLines_mRuA
error NoSelfPermit();

```

Copy

### Unauthorized [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IERC721Permit_v4\#unauthorized "Direct link to heading")

```codeBlockLines_mRuA
error Unauthorized();

```

Copy

- [Functions](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IERC721Permit_v4#functions)
  - [permit](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IERC721Permit_v4#permit)
  - [permitForAll](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IERC721Permit_v4#permitforall)
- [Errors](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IERC721Permit_v4#errors)
  - [SignatureDeadlineExpired](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IERC721Permit_v4#signaturedeadlineexpired)
  - [NoSelfPermit](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IERC721Permit_v4#noselfpermit)
  - [Unauthorized](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IERC721Permit_v4#unauthorized)