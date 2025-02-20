[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/periphery/base/UnorderedNonce#)

On this page

# UnorderedNonce

[Git Source](https://github.com/uniswap/v4-periphery/blob/3f295d8435e4f776ea2daeb96ce1bc6d63f33fc7/src/base/UnorderedNonce.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

Contract state and methods for using unordered nonces in signatures

## State Variables [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/UnorderedNonce\#state-variables "Direct link to heading")

### nonces [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/UnorderedNonce\#nonces "Direct link to heading")

mapping of nonces consumed by each address, where a nonce is a single bit on the 256-bit bitmap

_word is at most type(uint248).max_

```codeBlockLines_mRuA
mapping(address owner => mapping(uint256 word => uint256 bitmap)) public nonces;

```

Copy

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/UnorderedNonce\#functions "Direct link to heading")

### \_useUnorderedNonce [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/UnorderedNonce\#_useunorderednonce "Direct link to heading")

Consume a nonce, reverting if it has already been used

```codeBlockLines_mRuA
function _useUnorderedNonce(address owner, uint256 nonce) internal;

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `owner` | `address` | address, the owner/signer of the nonce |
| `nonce` | `uint256` | uint256, the nonce to consume. The top 248 bits are the word, the bottom 8 bits indicate the bit position |

### revokeNonce [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/UnorderedNonce\#revokenonce "Direct link to heading")

Revoke a nonce by spending it, preventing it from being used again

_Used in cases where a valid nonce has not been broadcasted onchain, and the owner wants to revoke the validity of the nonce_

_payable so it can be multicalled with native-token related actions_

```codeBlockLines_mRuA
function revokeNonce(uint256 nonce) external payable;

```

Copy

## Errors [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/UnorderedNonce\#errors "Direct link to heading")

### NonceAlreadyUsed [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/UnorderedNonce\#noncealreadyused "Direct link to heading")

```codeBlockLines_mRuA
error NonceAlreadyUsed();

```

Copy

- [State Variables](https://docs.uniswap.org/contracts/v4/reference/periphery/base/UnorderedNonce#state-variables)
  - [nonces](https://docs.uniswap.org/contracts/v4/reference/periphery/base/UnorderedNonce#nonces)
- [Functions](https://docs.uniswap.org/contracts/v4/reference/periphery/base/UnorderedNonce#functions)
  - [\_useUnorderedNonce](https://docs.uniswap.org/contracts/v4/reference/periphery/base/UnorderedNonce#_useunorderednonce)
  - [revokeNonce](https://docs.uniswap.org/contracts/v4/reference/periphery/base/UnorderedNonce#revokenonce)
- [Errors](https://docs.uniswap.org/contracts/v4/reference/periphery/base/UnorderedNonce#errors)
  - [NonceAlreadyUsed](https://docs.uniswap.org/contracts/v4/reference/periphery/base/UnorderedNonce#noncealreadyused)