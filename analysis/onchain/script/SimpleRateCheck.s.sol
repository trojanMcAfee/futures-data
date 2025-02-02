// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {Script} from "forge-std/Script.sol";
import {console2} from "forge-std/console2.sol";

interface IRETH {
    function getExchangeRate() external view returns (uint256);
}

contract SimpleRateCheck is Script {
    IRETH public rETH;
    
    // Constants for block calculation
    uint256 constant BLOCKS_PER_DAY = 7200; // ~12 second block time
    uint256 constant BASE_BLOCK = 18957444; // Jan 1, 2024 00:00 UTC
    uint256 constant DAYS_TO_CHECK = 31; // Full month of January
    uint256 constant DELAY_SECONDS = 2; // Delay between RPC calls
    string constant OUTPUT_FILE = "../../data/reth_prices.json";

    // Track success/failure stats
    uint256 public successCount;
    uint256 public failureCount;

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
            fractionStr
        ));
    }

    function tryGetRate(uint256 blockNumber) internal returns (bool success, uint256 rate) {
        try vm.createSelectFork(
            "https://eth-mainnet.g.alchemy.com/v2/pdMXO8V_cevAZjdp6W-PJ8QSV3dd3rta",
            blockNumber
        ) returns (uint256) {
            try rETH.getExchangeRate() returns (uint256 _rate) {
                return (true, _rate);
            } catch {
                console2.log("Failed to get exchange rate");
                return (false, 0);
            }
        } catch {
            console2.log("Failed to create fork");
            return (false, 0);
        }
    }

    function run() public {
        console2.log("=== Starting Rate Collection ===");
        console2.log(string(abi.encodePacked(
            "Will check ",
            vm.toString(DAYS_TO_CHECK),
            " days starting from block ",
            vm.toString(BASE_BLOCK)
        )));
        
        // Initialize JSON file
        vm.writeFile(OUTPUT_FILE, "[\n");
        bool isFirst = true;
        
        for (uint256 i = 0; i < DAYS_TO_CHECK; i++) {
            uint256 blockNumber = BASE_BLOCK + (i * BLOCKS_PER_DAY);
            uint256 timestamp = 1704067200 + (i * 86400); // Jan 1, 2024 00:00 UTC + days
            
            console2.log(string(abi.encodePacked(
                "\nDay ",
                vm.toString(i + 1),
                "/",
                vm.toString(DAYS_TO_CHECK),
                " (Block ",
                vm.toString(blockNumber),
                ")"
            )));
            
            (bool success, uint256 rate) = tryGetRate(blockNumber);
            
            if (success) {
                successCount++;
                string memory entry = string(abi.encodePacked(
                    isFirst ? "" : ",\n",
                    '  {"timestamp": "',
                    vm.toString(timestamp),
                    '", "block": "',
                    vm.toString(blockNumber),
                    '", "rate": "',
                    formatRate(rate),
                    '"}'
                ));
                vm.writeLine(OUTPUT_FILE, entry);
                isFirst = false;
                
                console2.log(string(abi.encodePacked(
                    "Success - Rate: ",
                    formatRate(rate),
                    " ETH per rETH"
                )));
            } else {
                failureCount++;
                console2.log("Failed to get rate for this block");
            }
            
            if (i < DAYS_TO_CHECK - 1) {
                console2.log(string(abi.encodePacked(
                    "Waiting ",
                    vm.toString(DELAY_SECONDS),
                    " seconds..."
                )));
                vm.sleep(DELAY_SECONDS * 1000);
            }
        }
        
        // Close JSON file
        vm.writeLine(OUTPUT_FILE, "\n]");
        
        console2.log("\n=== Collection Complete ===");
        console2.log(string(abi.encodePacked(
            "Successful collections: ",
            vm.toString(successCount),
            "/",
            vm.toString(DAYS_TO_CHECK)
        )));
        if (failureCount > 0) {
            console2.log(string(abi.encodePacked(
                "Failed collections: ",
                vm.toString(failureCount)
            )));
        }
    }
} 