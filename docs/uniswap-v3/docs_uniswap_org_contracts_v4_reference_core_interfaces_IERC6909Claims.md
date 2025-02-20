[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IERC6909Claims#)

On this page

# IERC6909Claims

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/interfaces/external/IERC6909Claims.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

Interface for claims over a contract balance, wrapped as a ERC6909

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IERC6909Claims\#functions "Direct link to heading")

### balanceOf [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IERC6909Claims\#balanceof "Direct link to heading")

Owner balance of an id.

```codeBlockLines_mRuA
function balanceOf(address owner, uint256 id) external view returns (uint256 amount);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `owner` | `address` | The address of the owner. |
| `id` | `uint256` | The id of the token. |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `amount` | `uint256` | The balance of the token. |

### allowance [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IERC6909Claims\#allowance "Direct link to heading")

Spender allowance of an id.

```codeBlockLines_mRuA
function allowance(address owner, address spender, uint256 id) external view returns (uint256 amount);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `owner` | `address` | The address of the owner. |
| `spender` | `address` | The address of the spender. |
| `id` | `uint256` | The id of the token. |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `amount` | `uint256` | The allowance of the token. |

### isOperator [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IERC6909Claims\#isoperator "Direct link to heading")

Checks if a spender is approved by an owner as an operator

```codeBlockLines_mRuA
function isOperator(address owner, address spender) external view returns (bool approved);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `owner` | `address` | The address of the owner. |
| `spender` | `address` | The address of the spender. |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `approved` | `bool` | The approval status. |

### transfer [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IERC6909Claims\#transfer "Direct link to heading")

Transfers an amount of an id from the caller to a receiver.

```codeBlockLines_mRuA
function transfer(address receiver, uint256 id, uint256 amount) external returns (bool);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `receiver` | `address` | The address of the receiver. |
| `id` | `uint256` | The id of the token. |
| `amount` | `uint256` | The amount of the token. |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `bool` | bool True, always, unless the function reverts |

### transferFrom [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IERC6909Claims\#transferfrom "Direct link to heading")

Transfers an amount of an id from a sender to a receiver.

```codeBlockLines_mRuA
function transferFrom(address sender, address receiver, uint256 id, uint256 amount) external returns (bool);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `sender` | `address` | The address of the sender. |
| `receiver` | `address` | The address of the receiver. |
| `id` | `uint256` | The id of the token. |
| `amount` | `uint256` | The amount of the token. |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `bool` | bool True, always, unless the function reverts |

### approve [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IERC6909Claims\#approve "Direct link to heading")

Approves an amount of an id to a spender.

```codeBlockLines_mRuA
function approve(address spender, uint256 id, uint256 amount) external returns (bool);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `spender` | `address` | The address of the spender. |
| `id` | `uint256` | The id of the token. |
| `amount` | `uint256` | The amount of the token. |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `bool` | bool True, always |

### setOperator [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IERC6909Claims\#setoperator "Direct link to heading")

Sets or removes an operator for the caller.

```codeBlockLines_mRuA
function setOperator(address operator, bool approved) external returns (bool);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `operator` | `address` | The address of the operator. |
| `approved` | `bool` | The approval status. |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `bool` | bool True, always |

## Events [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IERC6909Claims\#events "Direct link to heading")

### OperatorSet [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IERC6909Claims\#operatorset "Direct link to heading")

```codeBlockLines_mRuA
event OperatorSet(address indexed owner, address indexed operator, bool approved);

```

Copy

### Approval [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IERC6909Claims\#approval "Direct link to heading")

```codeBlockLines_mRuA
event Approval(address indexed owner, address indexed spender, uint256 indexed id, uint256 amount);

```

Copy

### Transfer [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IERC6909Claims\#transfer-1 "Direct link to heading")

```codeBlockLines_mRuA
event Transfer(address caller, address indexed from, address indexed to, uint256 indexed id, uint256 amount);

```

Copy

- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IERC6909Claims#functions)
  - [balanceOf](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IERC6909Claims#balanceof)
  - [allowance](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IERC6909Claims#allowance)
  - [isOperator](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IERC6909Claims#isoperator)
  - [transfer](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IERC6909Claims#transfer)
  - [transferFrom](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IERC6909Claims#transferfrom)
  - [approve](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IERC6909Claims#approve)
  - [setOperator](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IERC6909Claims#setoperator)
- [Events](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IERC6909Claims#events)
  - [OperatorSet](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IERC6909Claims#operatorset)
  - [Approval](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IERC6909Claims#approval)
  - [Transfer](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IERC6909Claims#transfer-1)