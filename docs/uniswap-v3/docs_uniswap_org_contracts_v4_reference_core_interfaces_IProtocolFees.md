[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IProtocolFees#)

On this page

# IProtocolFees

[Git Source](https://github.com/uniswap/v4-core/blob/b619b6718e31aa5b4fa0286520c455ceb950276d/src/interfaces/IProtocolFees.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

Interface for all protocol-fee related functions in the pool manager

## Functions [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IProtocolFees\#functions "Direct link to heading")

### protocolFeesAccrued [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IProtocolFees\#protocolfeesaccrued "Direct link to heading")

Given a currency address, returns the protocol fees accrued in that currency

```codeBlockLines_mRuA
function protocolFeesAccrued(Currency currency) external view returns (uint256 amount);

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `currency` | `Currency` | The currency to check |

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `amount` | `uint256` | The amount of protocol fees accrued in the currency |

### setProtocolFee [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IProtocolFees\#setprotocolfee "Direct link to heading")

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

### setProtocolFeeController [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IProtocolFees\#setprotocolfeecontroller "Direct link to heading")

Sets the protocol fee controller

```codeBlockLines_mRuA
function setProtocolFeeController(address controller) external;

```

Copy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `controller` | `address` | The new protocol fee controller |

### collectProtocolFees [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IProtocolFees\#collectprotocolfees "Direct link to heading")

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

### protocolFeeController [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IProtocolFees\#protocolfeecontroller "Direct link to heading")

Returns the current protocol fee controller address

```codeBlockLines_mRuA
function protocolFeeController() external view returns (address);

```

Copy

**Returns**

| Name | Type | Description |
| --- | --- | --- |
| `<none>` | `address` | address The current protocol fee controller address |

## Events [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IProtocolFees\#events "Direct link to heading")

### ProtocolFeeControllerUpdated [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IProtocolFees\#protocolfeecontrollerupdated "Direct link to heading")

Emitted when the protocol fee controller address is updated in setProtocolFeeController.

```codeBlockLines_mRuA
event ProtocolFeeControllerUpdated(address indexed protocolFeeController);

```

Copy

### ProtocolFeeUpdated [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IProtocolFees\#protocolfeeupdated "Direct link to heading")

Emitted when the protocol fee is updated for a pool.

```codeBlockLines_mRuA
event ProtocolFeeUpdated(PoolId indexed id, uint24 protocolFee);

```

Copy

## Errors [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IProtocolFees\#errors "Direct link to heading")

### ProtocolFeeTooLarge [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IProtocolFees\#protocolfeetoolarge "Direct link to heading")

Thrown when protocol fee is set too high

```codeBlockLines_mRuA
error ProtocolFeeTooLarge(uint24 fee);

```

Copy

### InvalidCaller [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IProtocolFees\#invalidcaller "Direct link to heading")

Thrown when collectProtocolFees or setProtocolFee is not called by the controller.

```codeBlockLines_mRuA
error InvalidCaller();

```

Copy

### ProtocolFeeCurrencySynced [​](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IProtocolFees\#protocolfeecurrencysynced "Direct link to heading")

Thrown when collectProtocolFees is attempted on a token that is synced.

```codeBlockLines_mRuA
error ProtocolFeeCurrencySynced();

```

Copy

- [Functions](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IProtocolFees#functions)
  - [protocolFeesAccrued](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IProtocolFees#protocolfeesaccrued)
  - [setProtocolFee](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IProtocolFees#setprotocolfee)
  - [setProtocolFeeController](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IProtocolFees#setprotocolfeecontroller)
  - [collectProtocolFees](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IProtocolFees#collectprotocolfees)
  - [protocolFeeController](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IProtocolFees#protocolfeecontroller)
- [Events](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IProtocolFees#events)
  - [ProtocolFeeControllerUpdated](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IProtocolFees#protocolfeecontrollerupdated)
  - [ProtocolFeeUpdated](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IProtocolFees#protocolfeeupdated)
- [Errors](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IProtocolFees#errors)
  - [ProtocolFeeTooLarge](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IProtocolFees#protocolfeetoolarge)
  - [InvalidCaller](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IProtocolFees#invalidcaller)
  - [ProtocolFeeCurrencySynced](https://docs.uniswap.org/contracts/v4/reference/core/interfaces/IProtocolFees#protocolfeecurrencysynced)