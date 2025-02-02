// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {Script} from "forge-std/Script.sol";
import {console2} from "forge-std/console2.sol";

interface IRETH {
    function getExchangeRate() external view returns (uint256);
}

contract SimpleRateCheck is Script {
    IRETH public rETH;
    uint256 constant TARGET_BLOCK = 18957444; // Jan 1, 2024 00:00 UTC

    function setUp() public {
        console2.log("=== Setup Starting ===");
        rETH = IRETH(0xae78736Cd615f374D3085123A210448E74Fc6393);
        console2.log("=== Setup Complete ===");
    }

    function run() public {
        console2.log("=== Starting Simple Rate Check ===");
        
        // Create fork at specific block
        console2.log(string(abi.encodePacked("Creating fork at block ", vm.toString(TARGET_BLOCK))));
        vm.createSelectFork(
            "https://eth-mainnet.g.alchemy.com/v2/pdMXO8V_cevAZjdp6W-PJ8QSV3dd3rta",
            TARGET_BLOCK
        );
        
        // Get rate
        console2.log("Getting exchange rate...");
        uint256 rate = rETH.getExchangeRate();
        
        // Format and display rate
        uint256 whole = rate / 1e18;
        uint256 fraction = (rate % 1e18) / 1e14;
        string memory fractionStr = vm.toString(fraction);
        // Pad with leading zeros if needed
        while (bytes(fractionStr).length < 4) {
            fractionStr = string(abi.encodePacked("0", fractionStr));
        }
        
        console2.log(string(abi.encodePacked(
            "Exchange rate: ",
            vm.toString(whole),
            ".",
            fractionStr,
            " ETH per rETH"
        )));
        
        console2.log("=== Check Complete ===");
    }
} 