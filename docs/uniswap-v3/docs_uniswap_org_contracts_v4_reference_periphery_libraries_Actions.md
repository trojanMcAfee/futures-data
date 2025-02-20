[Skip to main content](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions#)

On this page

# Actions

[Git Source](https://github.com/uniswap/v4-periphery/blob/3f295d8435e4f776ea2daeb96ce1bc6d63f33fc7/src/libraries/Actions.sol) \- Generated with [forge doc](https://book.getfoundry.sh/reference/forge/forge-doc)

Library to define different pool actions.

_These are suggested common commands, however additional commands should be defined as required_

## State Variables [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions\#state-variables "Direct link to heading")

### INCREASE\_LIQUIDITY [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions\#increase_liquidity "Direct link to heading")

```codeBlockLines_mRuA
uint256 constant INCREASE_LIQUIDITY = 0x00;

```

Copy

### DECREASE\_LIQUIDITY [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions\#decrease_liquidity "Direct link to heading")

```codeBlockLines_mRuA
uint256 constant DECREASE_LIQUIDITY = 0x01;

```

Copy

### MINT\_POSITION [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions\#mint_position "Direct link to heading")

```codeBlockLines_mRuA
uint256 constant MINT_POSITION = 0x02;

```

Copy

### BURN\_POSITION [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions\#burn_position "Direct link to heading")

```codeBlockLines_mRuA
uint256 constant BURN_POSITION = 0x03;

```

Copy

### SWAP\_EXACT\_IN\_SINGLE [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions\#swap_exact_in_single "Direct link to heading")

```codeBlockLines_mRuA
uint256 constant SWAP_EXACT_IN_SINGLE = 0x04;

```

Copy

### SWAP\_EXACT\_IN [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions\#swap_exact_in "Direct link to heading")

```codeBlockLines_mRuA
uint256 constant SWAP_EXACT_IN = 0x05;

```

Copy

### SWAP\_EXACT\_OUT\_SINGLE [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions\#swap_exact_out_single "Direct link to heading")

```codeBlockLines_mRuA
uint256 constant SWAP_EXACT_OUT_SINGLE = 0x06;

```

Copy

### SWAP\_EXACT\_OUT [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions\#swap_exact_out "Direct link to heading")

```codeBlockLines_mRuA
uint256 constant SWAP_EXACT_OUT = 0x07;

```

Copy

### DONATE [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions\#donate "Direct link to heading")

```codeBlockLines_mRuA
uint256 constant DONATE = 0x08;

```

Copy

### SETTLE [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions\#settle "Direct link to heading")

```codeBlockLines_mRuA
uint256 constant SETTLE = 0x09;

```

Copy

### SETTLE\_ALL [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions\#settle_all "Direct link to heading")

```codeBlockLines_mRuA
uint256 constant SETTLE_ALL = 0x10;

```

Copy

### SETTLE\_PAIR [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions\#settle_pair "Direct link to heading")

```codeBlockLines_mRuA
uint256 constant SETTLE_PAIR = 0x11;

```

Copy

### TAKE [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions\#take "Direct link to heading")

```codeBlockLines_mRuA
uint256 constant TAKE = 0x12;

```

Copy

### TAKE\_ALL [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions\#take_all "Direct link to heading")

```codeBlockLines_mRuA
uint256 constant TAKE_ALL = 0x13;

```

Copy

### TAKE\_PORTION [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions\#take_portion "Direct link to heading")

```codeBlockLines_mRuA
uint256 constant TAKE_PORTION = 0x14;

```

Copy

### TAKE\_PAIR [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions\#take_pair "Direct link to heading")

```codeBlockLines_mRuA
uint256 constant TAKE_PAIR = 0x15;

```

Copy

### SETTLE\_TAKE\_PAIR [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions\#settle_take_pair "Direct link to heading")

```codeBlockLines_mRuA
uint256 constant SETTLE_TAKE_PAIR = 0x16;

```

Copy

### CLOSE\_CURRENCY [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions\#close_currency "Direct link to heading")

```codeBlockLines_mRuA
uint256 constant CLOSE_CURRENCY = 0x17;

```

Copy

### CLEAR\_OR\_TAKE [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions\#clear_or_take "Direct link to heading")

```codeBlockLines_mRuA
uint256 constant CLEAR_OR_TAKE = 0x18;

```

Copy

### SWEEP [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions\#sweep "Direct link to heading")

```codeBlockLines_mRuA
uint256 constant SWEEP = 0x19;

```

Copy

### WRAP [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions\#wrap "Direct link to heading")

```codeBlockLines_mRuA
uint256 constant WRAP = 0x20;

```

Copy

### UNWRAP [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions\#unwrap "Direct link to heading")

```codeBlockLines_mRuA
uint256 constant UNWRAP = 0x21;

```

Copy

### MINT\_6909 [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions\#mint_6909 "Direct link to heading")

```codeBlockLines_mRuA
uint256 constant MINT_6909 = 0x22;

```

Copy

### BURN\_6909 [​](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions\#burn_6909 "Direct link to heading")

```codeBlockLines_mRuA
uint256 constant BURN_6909 = 0x23;

```

Copy

- [State Variables](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions#state-variables)
  - [INCREASE\_LIQUIDITY](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions#increase_liquidity)
  - [DECREASE\_LIQUIDITY](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions#decrease_liquidity)
  - [MINT\_POSITION](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions#mint_position)
  - [BURN\_POSITION](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions#burn_position)
  - [SWAP\_EXACT\_IN\_SINGLE](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions#swap_exact_in_single)
  - [SWAP\_EXACT\_IN](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions#swap_exact_in)
  - [SWAP\_EXACT\_OUT\_SINGLE](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions#swap_exact_out_single)
  - [SWAP\_EXACT\_OUT](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions#swap_exact_out)
  - [DONATE](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions#donate)
  - [SETTLE](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions#settle)
  - [SETTLE\_ALL](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions#settle_all)
  - [SETTLE\_PAIR](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions#settle_pair)
  - [TAKE](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions#take)
  - [TAKE\_ALL](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions#take_all)
  - [TAKE\_PORTION](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions#take_portion)
  - [TAKE\_PAIR](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions#take_pair)
  - [SETTLE\_TAKE\_PAIR](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions#settle_take_pair)
  - [CLOSE\_CURRENCY](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions#close_currency)
  - [CLEAR\_OR\_TAKE](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions#clear_or_take)
  - [SWEEP](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions#sweep)
  - [WRAP](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions#wrap)
  - [UNWRAP](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions#unwrap)
  - [MINT\_6909](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions#mint_6909)
  - [BURN\_6909](https://docs.uniswap.org/contracts/v4/reference/periphery/libraries/Actions#burn_6909)