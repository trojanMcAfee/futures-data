// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {Script} from "forge-std/Script.sol";
import {console2} from "forge-std/console2.sol";

interface IRETH {
    function getExchangeRate() external view returns (uint256);
}

contract SimpleRateCheck is Script {
    IRETH public rETH;
    uint256 constant BLOCK_JAN_1 = 18957444; // Jan 1, 2024 00:00 UTC
    uint256 constant BLOCK_JAN_2 = 18964644; // Jan 2, 2024 00:00 UTC

    function setUp() public {
        console2.log("=== Setup Starting ===");
        rETH = IRETH(0xae78736Cd615f374D3085123A210448E74Fc6393);
        console2.log("=== Setup Complete ===");
    }

    function formatRate(uint256 rate) internal pure returns (string memory) {
        uint256 whole = rate / 1e18;
        uint256 fraction = (rate % 1e18) / 1e14;
        string memory fractionStr = vm.toString(fraction);
        // Pad with leading zeros if needed
        while (bytes(fractionStr).length < 4) {
            fractionStr = string(abi.encodePacked("0", fractionStr));
        }
        return string(abi.encodePacked(
            vm.toString(whole),
            ".",
            fractionStr,
            " ETH per rETH"
        ));
    }

    function checkRate(uint256 blockNumber) internal {
        console2.log(string(abi.encodePacked("Creating fork at block ", vm.toString(blockNumber))));
        vm.createSelectFork(
            "https://eth-mainnet.g.alchemy.com/v2/pdMXO8V_cevAZjdp6W-PJ8QSV3dd3rta",
            blockNumber
        );
        
        console2.log("Getting exchange rate...");
        uint256 rate = rETH.getExchangeRate();
        console2.log(string(abi.encodePacked(
            "Exchange rate at block ",
            vm.toString(blockNumber),
            ": ",
            formatRate(rate)
        )));
    }

    function run() public {
        console2.log("=== Starting Simple Rate Check ===");
        
        console2.log("Checking January 1st, 2024...");
        checkRate(BLOCK_JAN_1);
        
        console2.log("\nChecking January 2nd, 2024...");
        checkRate(BLOCK_JAN_2);
        
        console2.log("=== Check Complete ===");
    }
} 