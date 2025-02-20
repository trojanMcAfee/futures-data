[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Permit2Forwarder#)

On this page

# Permit2Forwarder

[Git Source](https://github.com/uniswap/v4-periphery/blob/3f295d8435e4f776ea2daeb96ce1bc6d63f33fc7/src/base/Permit2Forwarder.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

PermitForwarder allows permitting this contract as a spender on permit2

_This contract does not enforce the spender to be this contract, but that is the intended use case_

## State Variables [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Permit2Forwarder\#state-variables "Direct link to heading")

### permit2 [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Permit2Forwarder\#permit2 "Direct link to heading")

the Permit2 contract to forward approvals

```codeBlockLines_mRuA
IAllowanceTransfer public immutable permit2;

```

Copy

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Permit2Forwarder\#functions "Direct link to heading")

### constructor [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Permit2Forwarder\#constructor "Direct link to heading")

```codeBlockLines_mRuA
constructor(IAllowanceTransfer _permit2);

```

Copy

### permit [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Permit2Forwarder\#permit "Direct link to heading")

allows forwarding a single permit to permit2

_this function is payable to allow multicall with NATIVE based actions_

```codeBlockLines_mRuA
function permit(address owner, IAllowanceTransfer.PermitSingle calldata permitSingle, bytes calldata signature)
    external
    payable
    returns (bytes memory err);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `owner` | `address` | the owner of the tokens |
| `permitSingle` | `IAllowanceTransfer.PermitSingle` | the permit data |
| `signature` | `bytes` | the signature of the permit; abi.encodePacked(r, s, v) |

### permitBatch [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Permit2Forwarder\#permitbatch "Direct link to heading")

allows forwarding batch permits to permit2

_this function is payable to allow multicall with NATIVE based actions_

```codeBlockLines_mRuA
function permitBatch(address owner, IAllowanceTransfer.PermitBatch calldata _permitBatch, bytes calldata signature)
    external
    payable
    returns (bytes memory err);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `owner` | `address` | the owner of the tokens |
| `_permitBatch` | `IAllowanceTransfer.PermitBatch` | a batch of approvals |
| `signature` | `bytes` | the signature of the permit; abi.encodePacked(r, s, v) |

- [State Variables](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Permit2Forwarder#state-variables)
  - [permit2](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Permit2Forwarder#permit2)
- [Functions](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Permit2Forwarder#functions)
  - [constructor](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Permit2Forwarder#constructor)
  - [permit](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Permit2Forwarder#permit)
  - [permitBatch](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Permit2Forwarder#permitbatch)