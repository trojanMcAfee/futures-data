// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {Script} from "forge-std/Script.sol";
import {console2} from "forge-std/console2.sol";

interface IRETH {
    function getExchangeRate() external view returns (uint256);
}

/**
 Pulls the July NAV price from rETH using blocks from reth_prices.json
 */
contract SimpleRateCheck is Script {
    IRETH public rocketTokenRETH;
    string constant OUTPUT_FILE = "/Users/dnyrm/Documents/defi/commodities framework/sample-data/data/reth_july.json";
    uint256 constant DAYS_IN_MONTH = 31;

    function setUp() public {
        console2.log("=== Setup Starting ===");
        rocketTokenRETH = IRETH(0xae78736Cd615f374D3085123A210448E74Fc6393);
        console2.log("=== Setup Complete ===");
    }

    function run() public {
        console2.log("=== Starting Rate Collection ===");
        console2.log("Will check July 2024 rates\n");

        string[] memory blocks = new string[](DAYS_IN_MONTH);
        string[] memory rates = new string[](DAYS_IN_MONTH);

        // Read blocks from reth_prices.json
        string memory jsonPath = "/Users/dnyrm/Documents/defi/commodities framework/sample-data/data/reth_prices.json";
        string memory json = vm.readFile(jsonPath);
        
        for (uint i = 0; i < DAYS_IN_MONTH; i++) {
            // Get block number for this day using the full path
            string memory blockPath = string.concat(".july[", vm.toString(i), "].block");
            string memory blockStr = abi.decode(vm.parseJson(json, blockPath), (string));
            uint256 blockNum = vm.parseUint(blockStr);
            
            // Create fork and get rate
            vm.createSelectFork(
                "https://eth-mainnet.g.alchemy.com/v2/pdMXO8V_cevAZjdp6W-PJ8QSV3dd3rta",
                blockNum
            );
            uint256 rawRate = rocketTokenRETH.getExchangeRate();
            
            console2.log(string.concat("Day ", vm.toString(i + 1), "/", vm.toString(DAYS_IN_MONTH)));
            console2.log(string.concat("  Block: ", blockStr));
            console2.log(string.concat("  Raw Rate: ", vm.toString(rawRate), "\n"));

            blocks[i] = blockStr;
            rates[i] = vm.toString(rawRate);

            vm.sleep(2 seconds);
        }

        console2.log("=== Collection Complete ===");
        console2.log(string.concat("  Successful collections: ", vm.toString(DAYS_IN_MONTH), "/", vm.toString(DAYS_IN_MONTH)));

        // Build JSON output
        string memory jsonStr = "[\n";
        for (uint i = 0; i < DAYS_IN_MONTH; i++) {
            jsonStr = string.concat(
                jsonStr,
                '  {\n    "block": "',
                blocks[i],
                '",\n    "rate": "',
                rates[i],
                '"\n  }'
            );
            if (i < DAYS_IN_MONTH - 1) {
                jsonStr = string.concat(jsonStr, ",\n");
            } else {
                jsonStr = string.concat(jsonStr, "\n");
            }
        }
        jsonStr = string.concat(jsonStr, "]\n");

        vm.writeFile(OUTPUT_FILE, jsonStr);
    }
} 