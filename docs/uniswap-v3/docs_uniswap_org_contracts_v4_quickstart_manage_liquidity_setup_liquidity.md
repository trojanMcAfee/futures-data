[Skip to main content](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/setup-liquidity#)

On this page

# Setup

For users looking to interact with the canonical Uniswap v4 `PositionManager`, _v4-periphery_ is a required dependency

Currently, developing with Uniswap v4 _requires [foundry](https://book.getfoundry.sh/)_

## Quickstart [​](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/setup-liquidity\#quickstart "Direct link to heading")

_Use [v4-template](https://github.com/new?template_name=v4-template&template_owner=uniswapfoundation)_, which has pre-configured dependencies and tests for Uniswap v4

Clone the repository made from _v4-template_

```codeBlockLines_mRuA
git clone https://github.com/<your_username>/<your_repo>

```

Copy

Install dependencies

```codeBlockLines_mRuA
forge install

```

Copy

* * *

## Manual Setup [​](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/setup-liquidity\#manual-setup "Direct link to heading")

After cloning the repository, and installing foundry, developers can manually set up their Uniswap v4 environment:

1. Initialize a foundry project





```codeBlockLines_mRuA
forge init . --force

```

Copy

2. Install dependencies





```codeBlockLines_mRuA
forge install uniswap/v4-core
forge install uniswap/v4-periphery

```

Copy

3. Set the `remappings.txt` to:





```codeBlockLines_mRuA
@uniswap/v4-core/=lib/v4-core/
forge-gas-snapshot/=lib/v4-core/lib/forge-gas-snapshot/src/
forge-std/=lib/v4-core/lib/forge-std/src/
permit2/=lib/v4-periphery/lib/permit2/
solmate/=lib/v4-core/lib/solmate/
v4-periphery/=lib/v4-periphery/

```

Copy


- [Quickstart](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/setup-liquidity#quickstart)
- [Manual Setup](https://docs.uniswap.org/contracts/v4/quickstart/manage-liquidity/setup-liquidity#manual-setup)