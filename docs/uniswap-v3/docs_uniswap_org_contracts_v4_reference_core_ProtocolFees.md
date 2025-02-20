[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/ProtocolFees#)

On this page

# ProtocolFees

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/ProtocolFees.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

**Inherits:** [IProtocolFees](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IProtocolFees), Owned

Contract handling the setting and accrual of protocol fees

## State Variables [​](https://docs.uniswap.org/contracts/v4/reference/core/ProtocolFees\#state-variables "Direct link to heading")

### protocolFeesAccrued [​](https://docs.uniswap.org/contracts/v4/reference/core/ProtocolFees\#protocolfeesaccrued "Direct link to heading")

Given a currency address, returns the protocol fees accrued in that currency

```codeBlockLines_mRuA
mapping(Currency currency => uint256 amount) public protocolFeesAccrued;

```

Copy

### protocolFeeController [​](https://docs.uniswap.org/contracts/v4/reference/core/ProtocolFees\#protocolfeecontroller "Direct link to heading")

Returns the current protocol fee controller address

```codeBlockLines_mRuA
address public protocolFeeController;

```

Copy

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/ProtocolFees\#functions "Direct link to heading")

### constructor [​](https://docs.uniswap.org/contracts/v4/reference/core/ProtocolFees\#constructor "Direct link to heading")

```codeBlockLines_mRuA
constructor(address initialOwner) Owned(initialOwner);

```

Copy

### setProtocolFeeController [​](https://docs.uniswap.org/contracts/v4/reference/core/ProtocolFees\#setprotocolfeecontroller "Direct link to heading")

Sets the protocol fee controller

```codeBlockLines_mRuA
function setProtocolFeeController(address controller) external onlyOwner;

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `controller` | `address` | The new protocol fee controller |

### setProtocolFee [​](https://docs.uniswap.org/contracts/v4/reference/core/ProtocolFees\#setprotocolfee "Direct link to heading")

Sets the protocol fee for the given pool

```codeBlockLines_mRuA
function setProtocolFee(PoolKey memory key, uint24 newProtocolFee) external;

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `key` | `PoolKey` | The key of the pool to set a protocol fee for |
| `newProtocolFee` | `uint24` | The fee to set |

### collectProtocolFees [​](https://docs.uniswap.org/contracts/v4/reference/core/ProtocolFees\#collectprotocolfees "Direct link to heading")

Collects the protocol fees for a given recipient and currency, returning the amount collected

_This will revert if the contract is unlocked_

```codeBlockLines_mRuA
function collectProtocolFees(address recipient, Currency currency, uint256 amount)
    external
    returns (uint256 amountCollected);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `recipient` | `address` | The address to receive the protocol fees |
| `currency` | `Currency` | The currency to withdraw |
| `amount` | `uint256` | The amount of currency to withdraw |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `amountCollected` | `uint256` | The amount of currency successfully withdrawn |

### \_isUnlocked [​](https://docs.uniswap.org/contracts/v4/reference/core/ProtocolFees\#_isunlocked "Direct link to heading")

_abstract internal function to allow the ProtocolFees contract to access the lock_

```codeBlockLines_mRuA
function _isUnlocked() internal virtual returns (bool);

```

Copy

### \_getPool [​](https://docs.uniswap.org/contracts/v4/reference/core/ProtocolFees\#_getpool "Direct link to heading")

_abstract internal function to allow the ProtocolFees contract to access pool state_

_this is overridden in PoolManager.sol to give access to the \_pools mapping_

```codeBlockLines_mRuA
function _getPool(PoolId id) internal virtual returns (Pool.State storage);

```

Copy

### \_updateProtocolFees [​](https://docs.uniswap.org/contracts/v4/reference/core/ProtocolFees\#_updateprotocolfees "Direct link to heading")

```codeBlockLines_mRuA
function _updateProtocolFees(Currency currency, uint256 amount) internal;

```

Copy

- [State Variables](https://docs.uniswap.org/contracts/v4/reference/core/ProtocolFees#state-variables)
  - [protocolFeesAccrued](https://docs.uniswap.org/contracts/v4/reference/core/ProtocolFees#protocolfeesaccrued)
  - [protocolFeeController](https://docs.uniswap.org/contracts/v4/reference/core/ProtocolFees#protocolfeecontroller)
- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/ProtocolFees#functions)
  - [constructor](https://docs.uniswap.org/contracts/v4/reference/core/ProtocolFees#constructor)
  - [setProtocolFeeController](https://docs.uniswap.org/contracts/v4/reference/core/ProtocolFees#setprotocolfeecontroller)
  - [setProtocolFee](https://docs.uniswap.org/contracts/v4/reference/core/ProtocolFees#setprotocolfee)
  - [collectProtocolFees](https://docs.uniswap.org/contracts/v4/reference/core/ProtocolFees#collectprotocolfees)
  - [\_isUnlocked](https://docs.uniswap.org/contracts/v4/reference/core/ProtocolFees#_isunlocked)
  - [\_getPool](https://docs.uniswap.org/contracts/v4/reference/core/ProtocolFees#_getpool)
  - [\_updateProtocolFees](https://docs.uniswap.org/contracts/v4/reference/core/ProtocolFees#_updateprotocolfees)