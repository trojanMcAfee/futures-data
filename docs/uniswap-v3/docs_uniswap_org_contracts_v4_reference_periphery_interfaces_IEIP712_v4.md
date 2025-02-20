[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IEIP712_v4#)

On this page

# IEIP712\_v4

[Git Source](https://github.com/uniswap/v4-periphery/blob/3f295d8435e4f776ea2daeb96ce1bc6d63f33fc7/src/interfaces/IEIP712_v4.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

This interface is used for an EIP712 implementation

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IEIP712_v4\#functions "Direct link to heading")

### DOMAIN\_SEPARATOR [​](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IEIP712_v4\#domain_separator "Direct link to heading")

Returns the domain separator for the current chain.

```codeBlockLines_mRuA
function DOMAIN_SEPARATOR() external view returns (bytes32);

```

Copy

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `bytes32` | bytes32 The domain separator |

- [Functions](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IEIP712_v4#functions)
  - [DOMAIN\_SEPARATOR](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IEIP712_v4#domain_separator)