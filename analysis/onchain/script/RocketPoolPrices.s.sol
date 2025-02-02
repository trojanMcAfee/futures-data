// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {Script} from "forge-std/Script.sol";
import {console2} from "forge-std/console2.sol";

interface IRETH {
    function getExchangeRate() external view returns (uint256);
}

contract RocketPoolPrices is Script {
    constructor() {
        console2.log("=== Constructor Called ===");
    }

    IRETH public rETH;
    string constant RPC_URL = "https://eth-mainnet.g.alchemy.com/v2/pdMXO8V_cevAZjdp6W-PJ8QSV3dd3rta";
    
    // Constants for block calculation
    uint256 constant SECONDS_PER_DAY = 86400;
    uint256 constant BLOCKS_PER_DAY = 7200; // ~12 second block time
    uint256 constant BASE_BLOCK = 18957444; // Jan 1, 2024 00:00 UTC
    uint256 constant BASE_TIMESTAMP = 1704067200;
    uint256 constant DAYS_TO_COLLECT = 60; // Start with 60 days as a test
    uint256 constant COOLDOWN_DELAY = 5; // 5 second delay between iterations

    error RateCollectionFailed(string date);

    function setUp() public {
        console2.log("=== Setup Starting ===");
        // Initialize rETH contract
        rETH = IRETH(0xae78736Cd615f374D3085123A210448E74Fc6393);
        console2.log("=== Setup Complete ===");
    }

    function formatDate(uint256 timestamp) internal pure returns (string memory) {
        (uint256 year, uint256 month, uint256 day) = timestampToDate(timestamp);
        return string(
            abi.encodePacked(
                vm.toString(year), "-",
                month < 10 ? "0" : "", vm.toString(month), "-",
                day < 10 ? "0" : "", vm.toString(day)
            )
        );
    }

    function timestampToDate(uint256 timestamp) internal pure returns (uint256 year, uint256 month, uint256 day) {
        uint256 z = timestamp / SECONDS_PER_DAY + 719468;
        uint256 era = (z >= 0 ? z : z - 146096) / 146097;
        uint256 doe = z - era * 146097;
        uint256 yoe = (doe - doe/1460 + doe/36524 - doe/146096) / 365;
        uint256 doy = doe - (365*yoe + yoe/4 - yoe/100);
        uint256 mp = (5*doy + 2)/153;
        
        day = doy - (153*mp + 2)/5 + 1;
        month = mp < 10 ? mp + 3 : mp - 9;
        year = yoe + era * 400 + (month <= 2 ? 1 : 0);
    }

    function formatRate(uint256 rate) internal pure returns (string memory) {
        string memory rateStr = vm.toString(rate / 1e14);
        return string(
            abi.encodePacked(
                substring(rateStr, 0, bytes(rateStr).length - 4),
                ".",
                substring(rateStr, bytes(rateStr).length - 4, bytes(rateStr).length)
            )
        );
    }

    function substring(string memory str, uint256 startIndex, uint256 endIndex) internal pure returns (string memory) {
        bytes memory strBytes = bytes(str);
        bytes memory result = new bytes(endIndex - startIndex);
        for (uint256 i = startIndex; i < endIndex; i++) {
            result[i - startIndex] = strBytes[i];
        }
        return string(result);
    }

    function run() public {
        console2.log("=== Starting rETH Rate Collection ===");
        console2.log(string(
            abi.encodePacked(
                "Target: ",
                vm.toString(DAYS_TO_COLLECT),
                " days, with ",
                vm.toString(COOLDOWN_DELAY),
                " second cooldown between requests"
            )
        ));
        console2.log("=====================================");

        // Create initial fork
        console2.log("Creating initial fork...");
        vm.createSelectFork(RPC_URL);
        console2.log("Fork created successfully");
        
        // Create the JSON file
        console2.log("Creating output file...");
        vm.writeFile("../../data/reth_prices.json", "[");
        bool isFirst = true;
        uint256 successCount = 0;
        uint256 failureCount = 0;
        
        uint256 currentTimestamp = BASE_TIMESTAMP;
        for (uint256 dayCount = 0; dayCount < DAYS_TO_COLLECT; dayCount++) {
            console2.log("-----------------------------------");
            string memory dateStr = formatDate(currentTimestamp);
            uint256 blockNumber = BASE_BLOCK + (dayCount * BLOCKS_PER_DAY);
            
            // Log start of iteration
            console2.log(string(
                abi.encodePacked(
                    "Processing day ",
                    vm.toString(dayCount + 1),
                    "/",
                    vm.toString(DAYS_TO_COLLECT),
                    ": ",
                    dateStr
                )
            ));
            console2.log(string(
                abi.encodePacked(
                    "Target block: ",
                    vm.toString(blockNumber)
                )
            ));

            uint256 rate;
            bool success = false;

            console2.log("Rolling fork to target block...");
            try vm.rollFork(blockNumber) {
                console2.log("Fork rolled successfully, getting exchange rate...");
                rate = rETH.getExchangeRate();
                success = true;
                successCount++;
                console2.log(string(
                    abi.encodePacked(
                        "Exchange rate retrieved: ",
                        formatRate(rate),
                        " ETH per rETH"
                    )
                ));
            } catch Error(string memory reason) {
                console2.log(string(abi.encodePacked("Error: ", reason)));
                failureCount++;
            } catch {
                console2.log("Unknown error occurred");
                failureCount++;
            }

            if (success) {
                // Create JSON object
                string memory jsonObject = string(
                    abi.encodePacked(
                        isFirst ? "" : ",",
                        '{',
                        '"date": "', dateStr, '",',
                        '"price": "', formatRate(rate), '"',
                        '}'
                    )
                );
                
                // Write to file
                console2.log("Writing result to file...");
                vm.writeLine("../../data/reth_prices.json", jsonObject);
                isFirst = false;
            }

            // Move to next day
            currentTimestamp += SECONDS_PER_DAY;

            // Add cooldown delay between iterations
            if (dayCount < DAYS_TO_COLLECT - 1) {
                console2.log(string(
                    abi.encodePacked(
                        "Cooling down for ",
                        vm.toString(COOLDOWN_DELAY),
                        " seconds before next request..."
                    )
                ));
                vm.warp(block.timestamp + COOLDOWN_DELAY);
                vm.sleep(COOLDOWN_DELAY * 1000); // Convert to milliseconds
            }
        }

        // Close JSON array
        console2.log("-----------------------------------");
        console2.log("Writing final closing bracket...");
        vm.writeLine("../../data/reth_prices.json", "]");
        
        console2.log("=== Collection Complete ===");
        console2.log(string(
            abi.encodePacked(
                "Successful requests: ",
                vm.toString(successCount),
                "/",
                vm.toString(DAYS_TO_COLLECT)
            )
        ));
        if (failureCount > 0) {
            console2.log(string(
                abi.encodePacked(
                    "Failed requests: ",
                    vm.toString(failureCount)
                )
            ));
        }
        console2.log("=========================");
    }
} 