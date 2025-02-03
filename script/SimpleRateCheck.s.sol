// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {Script} from "forge-std/Script.sol";
import {console2} from "forge-std/console2.sol";

interface IRETH {
    function getExchangeRate() external view returns (uint256);
}

contract SimpleRateCheck is Script {
    IRETH public rocketTokenRETH;
    
    // Constants for block calculation
    uint256 constant BLOCKS_PER_DAY = 7200; // ~12 second block time
    uint256 constant BASE_BLOCK = 19459444; // March 1, 2024
    uint256 constant BASE_TIMESTAMP = 1709251200; // March 1, 2024 00:00:00 UTC
    uint256 constant DAYS_TO_CHECK = 31;

    // Track success/failure stats
    uint256 public successCount;

    function formatDate(uint256 timestamp) internal pure returns (string memory) {
        // Convert timestamp to date components
        uint256 z = timestamp / 86400 + 719468;
        uint256 era = (z >= 0 ? z : z - 146096) / 146097;
        uint256 doe = z - era * 146097;
        uint256 yoe = (doe - doe/1460 + doe/36524 - doe/146096) / 365;
        uint256 y = yoe + era * 400;
        uint256 doy = doe - (365*yoe + yoe/4 - yoe/100);
        uint256 mp = (5*doy + 2)/153;
        uint256 d = doy - (153*mp + 2)/5 + 1;
        uint256 m = mp < 10 ? mp + 3 : mp - 9;
        y = y + (m <= 2 ? 1 : 0);

        return string.concat(
            vm.toString(y), "-03-",
            d < 10 ? string.concat("0", vm.toString(d)) : vm.toString(d)
        );
    }

    function run() public {
        console2.log("=== Setup Starting ===");
        vm.createSelectFork("https://eth-mainnet.g.alchemy.com/v2/pdMXO8V_cevAZjdp6W-PJ8QSV3dd3rta");
        rocketTokenRETH = IRETH(0xae78736Cd615f374D3085123A210448E74Fc6393);
        console2.log("=== Setup Complete ===");

        console2.log("=== Starting Rate Collection ===");
        console2.log("Will check March 2024 rates");

        string memory outputPath = "../../data/reth_prices_march.json";
        vm.writeFile(outputPath, "{\n  \"march\": [");

        successCount = 0;

        for (uint256 i = 0; i < DAYS_TO_CHECK; i++) {
            uint256 currentBlock = BASE_BLOCK + (i * BLOCKS_PER_DAY);
            uint256 currentTimestamp = BASE_TIMESTAMP + (i * 1 days);

            console2.log("\nDay %s/%s (Block %s)", i + 1, DAYS_TO_CHECK, currentBlock);
            
            vm.createSelectFork("https://eth-mainnet.g.alchemy.com/v2/pdMXO8V_cevAZjdp6W-PJ8QSV3dd3rta", currentBlock);
            
            uint256 rate = rocketTokenRETH.getExchangeRate();
            string memory dateStr = formatDate(currentTimestamp);
            
            if (i == 0) {
                vm.writeLine(outputPath, string.concat(
                    "\n    {\"timestamp\": \"", dateStr, "\", \"block\": \"",
                    vm.toString(currentBlock), "\", \"rate\": \"",
                    vm.toString(rate), "\"}"
                ));
            } else {
                vm.writeLine(outputPath, string.concat(
                    ",\n    {\"timestamp\": \"", dateStr, "\", \"block\": \"",
                    vm.toString(currentBlock), "\", \"rate\": \"",
                    vm.toString(rate), "\"}"
                ));
            }

            console2.log("Success - Raw Rate: %s", rate);
            successCount++;

            console2.log("Waiting 2 seconds...");
            vm.sleep(2000);
        }

        vm.writeLine(outputPath, "\n  ]\n}");

        console2.log("\n=== Collection Complete ===");
        console2.log("Successful collections: %s/%s", successCount, DAYS_TO_CHECK);
    }
} 