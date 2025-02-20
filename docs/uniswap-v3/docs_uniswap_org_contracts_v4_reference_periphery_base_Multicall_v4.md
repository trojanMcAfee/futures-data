[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Multicall_v4#)

On this page

# Multicall\_v4

[Git Source](https://github.com/uniswap/v4-periphery/blob/3f295d8435e4f776ea2daeb96ce1bc6d63f33fc7/src/base/Multicall_v4.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:** [IMulticall\_v4](https://docs.uniswap.org/contracts/v4/reference/periphery/interfaces/IMulticall_v4)

Enables calling multiple methods in a single call to the contract

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Multicall_v4\#functions "Direct link to heading")

### multicall [​](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Multicall_v4\#multicall "Direct link to heading")

Call multiple functions in the current contract and return the data from all of them if they all succeed

_The `msg.value` is passed onto all subcalls, even if a previous subcall has consumed the ether._
_Subcalls can instead use `address(this).value` to see the available ETH, and consume it using {value: x}._

```codeBlockLines_mRuA
function multicall(bytes[] calldata data) external payable returns (bytes[] memory results);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `data` | `bytes[]` | The encoded function data for each of the calls to make to this contract |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `results` | `bytes[]` | The results from each of the calls passed in via data |

- [Functions](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Multicall_v4#functions)
  - [multicall](https://docs.uniswap.org/contracts/v4/reference/periphery/base/Multicall_v4#multicall)