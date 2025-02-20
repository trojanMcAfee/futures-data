[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/periphery/base/ERC721Permit_v4#)

On this page

# ERC721Permit\_v4

[Git Source](https://github.com/uniswap/v4-periphery/blob/3f295d8435e4f776ea2daeb96ce1bc6d63f33fc7/src/base/ERC721Permit_v4.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:**
ERC721, [IERC721Permit\_v4](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IERC721Permit_v4), [EIP712\_v4](https://docs.uniswap.org/contracts/v4/reference/periphery/base/EIP712_v4), [UnorderedNonce](https://docs.uniswap.org/contracts/v4/reference/periphery/base/UnorderedNonce)

Nonfungible tokens that support an approve via signature, i.e. permit

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/ERC721Permit_v4\#functions "Direct link to heading")

### constructor [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/ERC721Permit_v4\#constructor "Direct link to heading")

Computes the nameHash and versionHash

```codeBlockLines_mRuA
constructor(string memory name_, string memory symbol_) ERC721(name_, symbol_) EIP712_v4(name_);

```

Copy

### checkSignatureDeadline [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/ERC721Permit_v4\#checksignaturedeadline "Direct link to heading")

Checks if the block's timestamp is before a signature's deadline

```codeBlockLines_mRuA
modifier checkSignatureDeadline(uint256 deadline);

```

Copy

### permit [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/ERC721Permit_v4\#permit "Direct link to heading")

Approve of a specific token ID for spending by spender via signature

_payable so it can be multicalled with NATIVE related actions_

```codeBlockLines_mRuA
function permit(address spender, uint256 tokenId, uint256 deadline, uint256 nonce, bytes calldata signature)
    external
    payable
    checkSignatureDeadline(deadline);

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

### permitForAll [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/ERC721Permit_v4\#permitforall "Direct link to heading")

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
) external payable checkSignatureDeadline(deadline);

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

### setApprovalForAll [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/ERC721Permit_v4\#setapprovalforall "Direct link to heading")

Enable or disable approval for a third party ("operator") to manage
all of `msg.sender`'s assets

_Emits the ApprovalForAll event. The contract MUST allow_
_multiple operators per owner._

_Override Solmate's ERC721 setApprovalForAll so setApprovalForAll() and permit() share the \_approveForAll method_

```codeBlockLines_mRuA
function setApprovalForAll(address operator, bool approved) public override;

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `operator` | `address` | Address to add to the set of authorized operators |
| `approved` | `bool` | True if the operator is approved, false to revoke approval |

### \_approveForAll [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/ERC721Permit_v4\#_approveforall "Direct link to heading")

```codeBlockLines_mRuA
function _approveForAll(address owner, address operator, bool approved) internal;

```

Copy

### approve [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/ERC721Permit_v4\#approve "Direct link to heading")

Change or reaffirm the approved address for an NFT

_override Solmate's ERC721 approve so approve() and permit() share the \_approve method_
_Passing a spender address of zero can be used to remove any outstanding approvals_
_Throws error unless `msg.sender` is the current NFT owner,_
_or an authorized operator of the current owner._

```codeBlockLines_mRuA
function approve(address spender, uint256 id) public override;

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `spender` | `address` | The new approved NFT controller |
| `id` | `uint256` | The tokenId of the NFT to approve |

### \_approve [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/ERC721Permit_v4\#_approve "Direct link to heading")

```codeBlockLines_mRuA
function _approve(address owner, address spender, uint256 id) internal;

```

Copy

### \_isApprovedOrOwner [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/ERC721Permit_v4\#_isapprovedorowner "Direct link to heading")

```codeBlockLines_mRuA
function _isApprovedOrOwner(address spender, uint256 tokenId) internal view returns (bool);

```

Copy

- [Functions](https://docs.uniswap.org/contracts/v4/reference/periphery/base/ERC721Permit_v4#functions)
  - [constructor](https://docs.uniswap.org/contracts/v4/reference/periphery/base/ERC721Permit_v4#constructor)
  - [checkSignatureDeadline](https://docs.uniswap.org/contracts/v4/reference/periphery/base/ERC721Permit_v4#checksignaturedeadline)
  - [permit](https://docs.uniswap.org/contracts/v4/reference/periphery/base/ERC721Permit_v4#permit)
  - [permitForAll](https://docs.uniswap.org/contracts/v4/reference/periphery/base/ERC721Permit_v4#permitforall)
  - [setApprovalForAll](https://docs.uniswap.org/contracts/v4/reference/periphery/base/ERC721Permit_v4#setapprovalforall)
  - [\_approveForAll](https://docs.uniswap.org/contracts/v4/reference/periphery/base/ERC721Permit_v4#_approveforall)
  - [approve](https://docs.uniswap.org/contracts/v4/reference/periphery/base/ERC721Permit_v4#approve)
  - [\_approve](https://docs.uniswap.org/contracts/v4/reference/periphery/base/ERC721Permit_v4#_approve)
  - [\_isApprovedOrOwner](https://docs.uniswap.org/contracts/v4/reference/periphery/base/ERC721Permit_v4#_isapprovedorowner)