// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {Test} from "forge-std/Test.sol";

interface IRETH {
    function getExchangeRate() external view returns (uint256);
}

contract RocketPoolTest is Test {
    IRETH public rETH;

    function setUp() public {
        // Fork Ethereum mainnet
        vm.createSelectFork("mainnet");
        
        // Initialize rETH contract
        rETH = IRETH(0xae78736Cd615f374D3085123A210448E74Fc6393);
    }

    function test_GetExchangeRate() public {
        // Get the exchange rate
        uint256 exchangeRate = rETH.getExchangeRate();
        
        // Log the exchange rate (divide by 1e18 to get the actual rate)
        emit log_named_decimal_uint("rETH/ETH Exchange Rate", exchangeRate, 18);
        
        // Basic assertion to ensure exchange rate is not zero
        assertGt(exchangeRate, 0);
    }
} 