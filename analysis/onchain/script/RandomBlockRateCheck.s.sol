// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {Script} from "forge-std/Script.sol";
import {console2} from "forge-std/console2.sol";

interface IRETH {
    function getExchangeRate() external view returns (uint256);
}

contract RandomBlockRateCheck is Script {
    IRETH public rocketTokenRETH;
    
    function setUp() public {
        console2.log("=== Setup Starting ===");
        rocketTokenRETH = IRETH(0xae78736Cd615f374D3085123A210448E74Fc6393);
        console2.log("=== Setup Complete ===");
    }

    function run() public {
        console2.log("=== Starting Random Block Rate Check ===");
        
        // Generate a random block number between 15000000 and current block
        // uint256 currentBlock = block.number;
        // uint256 randomBlock = uint256(keccak256(abi.encodePacked(block.timestamp))) % (currentBlock - 15000000) + 15000000;
        uint256 randomBlock = 20573272;
        
        console2.log(string.concat("Checking rate at block: ", vm.toString(randomBlock)));

        // Create fork and get rate
        vm.createSelectFork(
            "https://eth-mainnet.g.alchemy.com/v2/pdMXO8V_cevAZjdp6W-PJ8QSV3dd3rta",
            randomBlock
        );

        uint256 rawRate = rocketTokenRETH.getExchangeRate();
        
        console2.log(string.concat("Raw Rate: ", vm.toString(rawRate)));
        console2.log("=== Check Complete ===");
    }
} 