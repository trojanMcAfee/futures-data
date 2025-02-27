// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import {ERC20} from "openzeppelin-contracts/contracts/token/ERC20/ERC20.sol";
import {Ownable} from "openzeppelin-contracts/contracts/access/Ownable.sol";

contract WTI is ERC20, Ownable {
    // Minimum amount of tokens that can be minted
    uint256 public constant MIN_MINT_AMOUNT = 100 * 10**18; // 100 tokens with 18 decimals
    
    constructor() ERC20("Crude Oil", "WTI") Ownable(msg.sender) {
        // Mint 1000 tokens to the contract deployer
        // Note: ERC20 uses 18 decimals by default, so we multiply by 1e18
        _mint(msg.sender, 1000 * 10**decimals());
    }
    
    /**
     * @notice Mints new WTI tokens to a specified address
     * @dev Only callable by the contract owner
     * @param to The address that will receive the minted tokens
     * @param amount The amount of tokens to mint (in wei)
     * @return Boolean indicating whether the operation succeeded
     */
    function mint(address to, uint256 amount) external onlyOwner returns (bool) {
        // Check that the recipient address is valid
        require(to != address(0), "WTI: cannot mint to the zero address");
        
        // Enforce minimum mint amount
        require(amount >= MIN_MINT_AMOUNT, "WTI: mint amount below minimum (100 tokens)");
        
        // Mint tokens to the specified address
        _mint(to, amount);
        
        return true;
    }
} 