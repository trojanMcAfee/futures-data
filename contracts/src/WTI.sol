// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import {ERC20} from "openzeppelin-contracts/contracts/token/ERC20/ERC20.sol";

contract WTI is ERC20 {
    constructor() ERC20("Crude Oil", "WTI") {
        // Mint 1000 tokens to the contract deployer
        // Note: ERC20 uses 18 decimals by default, so we multiply by 1e18
        _mint(msg.sender, 1000 * 10**decimals());
    }
} 