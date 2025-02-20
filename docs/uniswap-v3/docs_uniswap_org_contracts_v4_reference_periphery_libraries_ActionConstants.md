[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/ActionConstants#)

On this page

# ActionConstants

[Git Source](https://github.com/uniswap/v4-periphery/blob/3f295d8435e4f776ea2daeb96ce1bc6d63f33fc7/src/libraries/ActionConstants.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

Common constants used in actions

_Constants are gas efficient alternatives to their literal values_

## State Variables [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/ActionConstants\#state-variables "Direct link to heading")

### OPEN\_DELTA [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/ActionConstants\#open_delta "Direct link to heading")

used to signal that an action should use the input value of the open delta on the pool manager
or of the balance that the contract holds

```codeBlockLines_mRuA
uint128 internal constant OPEN_DELTA = 0;

```

Copy

### CONTRACT\_BALANCE [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/ActionConstants\#contract_balance "Direct link to heading")

used to signal that an action should use the contract's entire balance of a currency
This value is equivalent to 1<<255, i.e. a singular 1 in the most significant bit.

```codeBlockLines_mRuA
uint256 internal constant CONTRACT_BALANCE = 0x8000000000000000000000000000000000000000000000000000000000000000;

```

Copy

### MSG\_SENDER [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/ActionConstants\#msg_sender "Direct link to heading")

used to signal that the recipient of an action should be the msgSender

```codeBlockLines_mRuA
address internal constant MSG_SENDER = address(1);

```

Copy

### ADDRESS\_THIS [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/ActionConstants\#address_this "Direct link to heading")

used to signal that the recipient of an action should be the address(this)

```codeBlockLines_mRuA
address internal constant ADDRESS_THIS = address(2);

```

Copy

- [State Variables](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/ActionConstants#state-variables)
  - [OPEN\_DELTA](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/ActionConstants#open_delta)
  - [CONTRACT\_BALANCE](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/ActionConstants#contract_balance)
  - [MSG\_SENDER](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/ActionConstants#msg_sender)
  - [ADDRESS\_THIS](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/ActionConstants#address_this)