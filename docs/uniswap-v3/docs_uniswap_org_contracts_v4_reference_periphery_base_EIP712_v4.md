[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/periphery/base/EIP712_v4#)

On this page

# EIP712\_v4

[Git Source](https://github.com/uniswap/v4-periphery/blob/3f295d8435e4f776ea2daeb96ce1bc6d63f33fc7/src/base/EIP712_v4.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:** [IEIP712\_v4](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IEIP712_v4)

Generic EIP712 implementation

_Maintains cross-chain replay protection in the event of a fork_

_Should not be delegatecall'd because DOMAIN\_SEPARATOR returns the cached hash and does not recompute with the delegatecallers address_

_Reference: [https://github.com/Uniswap/permit2/blob/3f17e8db813189a03950dc7fc8382524a095c053/src/EIP712.sol](https://github.com/Uniswap/permit2/blob/3f17e8db813189a03950dc7fc8382524a095c053/src/EIP712.sol)_

_Reference: [https://github.com/OpenZeppelin/openzeppelin-contracts/blob/7bd2b2aaf68c21277097166a9a51eb72ae239b34/contracts/utils/cryptography/EIP712.sol](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/7bd2b2aaf68c21277097166a9a51eb72ae239b34/contracts/utils/cryptography/EIP712.sol)_

## State Variables [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/EIP712_v4\#state-variables "Direct link to heading")

### \_CACHED\_DOMAIN\_SEPARATOR [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/EIP712_v4\#_cached_domain_separator "Direct link to heading")

```codeBlockLines_mRuA
bytes32 private immutable _CACHED_DOMAIN_SEPARATOR;

```

Copy

### \_CACHED\_CHAIN\_ID [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/EIP712_v4\#_cached_chain_id "Direct link to heading")

```codeBlockLines_mRuA
uint256 private immutable _CACHED_CHAIN_ID;

```

Copy

### \_HASHED\_NAME [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/EIP712_v4\#_hashed_name "Direct link to heading")

```codeBlockLines_mRuA
bytes32 private immutable _HASHED_NAME;

```

Copy

### \_TYPE\_HASH [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/EIP712_v4\#_type_hash "Direct link to heading")

```codeBlockLines_mRuA
bytes32 private constant _TYPE_HASH = keccak256("EIP712Domain(string name,uint256 chainId,address verifyingContract)");

```

Copy

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/EIP712_v4\#functions "Direct link to heading")

### constructor [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/EIP712_v4\#constructor "Direct link to heading")

```codeBlockLines_mRuA
constructor(string memory name);

```

Copy

### DOMAIN\_SEPARATOR [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/EIP712_v4\#domain_separator "Direct link to heading")

Returns the domain separator for the current chain.

```codeBlockLines_mRuA
function DOMAIN_SEPARATOR() public view returns (bytes32);

```

Copy

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `bytes32` | bytes32 The domain separator |

### \_buildDomainSeparator [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/EIP712_v4\#_builddomainseparator "Direct link to heading")

Builds a domain separator using the current chainId and contract address.

```codeBlockLines_mRuA
function _buildDomainSeparator() private view returns (bytes32);

```

Copy

### \_hashTypedData [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/EIP712_v4\#_hashtypeddata "Direct link to heading")

Creates an EIP-712 typed data hash

```codeBlockLines_mRuA
function _hashTypedData(bytes32 dataHash) internal view returns (bytes32 digest);

```

Copy

- [State Variables](https://docs.uniswap.org/contracts/v4/reference/periphery/base/EIP712_v4#state-variables)
  - [\_CACHED\_DOMAIN\_SEPARATOR](https://docs.uniswap.org/contracts/v4/reference/periphery/base/EIP712_v4#_cached_domain_separator)
  - [\_CACHED\_CHAIN\_ID](https://docs.uniswap.org/contracts/v4/reference/periphery/base/EIP712_v4#_cached_chain_id)
  - [\_HASHED\_NAME](https://docs.uniswap.org/contracts/v4/reference/periphery/base/EIP712_v4#_hashed_name)
  - [\_TYPE\_HASH](https://docs.uniswap.org/contracts/v4/reference/periphery/base/EIP712_v4#_type_hash)
- [Functions](https://docs.uniswap.org/contracts/v4/reference/periphery/base/EIP712_v4#functions)
  - [constructor](https://docs.uniswap.org/contracts/v4/reference/periphery/base/EIP712_v4#constructor)
  - [DOMAIN\_SEPARATOR](https://docs.uniswap.org/contracts/v4/reference/periphery/base/EIP712_v4#domain_separator)
  - [\_buildDomainSeparator](https://docs.uniswap.org/contracts/v4/reference/periphery/base/EIP712_v4#_builddomainseparator)
  - [\_hashTypedData](https://docs.uniswap.org/contracts/v4/reference/periphery/base/EIP712_v4#_hashtypeddata)