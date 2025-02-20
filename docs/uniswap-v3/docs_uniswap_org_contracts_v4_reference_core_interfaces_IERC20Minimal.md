[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IERC20Minimal#)

On this page

# IERC20Minimal

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/interfaces/external/IERC20Minimal.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

Contains a subset of the full ERC20 interface that is used in Uniswap V3

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IERC20Minimal\#functions "Direct link to heading")

### balanceOf [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IERC20Minimal\#balanceof "Direct link to heading")

Returns an account's balance in the token

```codeBlockLines_mRuA
function balanceOf(address account) external view returns (uint256);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `account` | `address` | The account for which to look up the number of tokens it has, i.e. its balance |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `uint256` | The number of tokens held by the account |

### transfer [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IERC20Minimal\#transfer "Direct link to heading")

Transfers the amount of token from the `msg.sender` to the recipient

```codeBlockLines_mRuA
function transfer(address recipient, uint256 amount) external returns (bool);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `recipient` | `address` | The account that will receive the amount transferred |
| `amount` | `uint256` | The number of tokens to send from the sender to the recipient |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `bool` | Returns true for a successful transfer, false for an unsuccessful transfer |

### allowance [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IERC20Minimal\#allowance "Direct link to heading")

Returns the current allowance given to a spender by an owner

```codeBlockLines_mRuA
function allowance(address owner, address spender) external view returns (uint256);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `owner` | `address` | The account of the token owner |
| `spender` | `address` | The account of the token spender |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `uint256` | The current allowance granted by `owner` to `spender` |

### approve [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IERC20Minimal\#approve "Direct link to heading")

Sets the allowance of a spender from the `msg.sender` to the value `amount`

```codeBlockLines_mRuA
function approve(address spender, uint256 amount) external returns (bool);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `spender` | `address` | The account which will be allowed to spend a given amount of the owners tokens |
| `amount` | `uint256` | The amount of tokens allowed to be used by `spender` |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `bool` | Returns true for a successful approval, false for unsuccessful |

### transferFrom [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IERC20Minimal\#transferfrom "Direct link to heading")

Transfers `amount` tokens from `sender` to `recipient` up to the allowance given to the `msg.sender`

```codeBlockLines_mRuA
function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `sender` | `address` | The account from which the transfer will be initiated |
| `recipient` | `address` | The recipient of the transfer |
| `amount` | `uint256` | The amount of the transfer |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `bool` | Returns true for a successful transfer, false for unsuccessful |

## Events [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IERC20Minimal\#events "Direct link to heading")

### Transfer [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IERC20Minimal\#transfer-1 "Direct link to heading")

Event emitted when tokens are transferred from one address to another, either via `#transfer` or `#transferFrom`.

```codeBlockLines_mRuA
event Transfer(address indexed from, address indexed to, uint256 value);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `from` | `address` | The account from which the tokens were sent, i.e. the balance decreased |
| `to` | `address` | The account to which the tokens were sent, i.e. the balance increased |
| `value` | `uint256` | The amount of tokens that were transferred |

### Approval [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IERC20Minimal\#approval "Direct link to heading")

Event emitted when the approval amount for the spender of a given owner's tokens changes.

```codeBlockLines_mRuA
event Approval(address indexed owner, address indexed spender, uint256 value);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `owner` | `address` | The account that approved spending of its tokens |
| `spender` | `address` | The account for which the spending allowance was modified |
| `value` | `uint256` | The new allowance from the owner to the spender |

- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IERC20Minimal#functions)
  - [balanceOf](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IERC20Minimal#balanceof)
  - [transfer](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IERC20Minimal#transfer)
  - [allowance](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IERC20Minimal#allowance)
  - [approve](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IERC20Minimal#approve)
  - [transferFrom](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IERC20Minimal#transferfrom)
- [Events](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IERC20Minimal#events)
  - [Transfer](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IERC20Minimal#transfer-1)
  - [Approval](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IERC20Minimal#approval)