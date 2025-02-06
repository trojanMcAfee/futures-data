// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {Script, console2} from "forge-std/Script.sol";
import {UniswapV3RethPriceScript} from "./UniswapV3RethPrice.s.sol";
import {stdJson} from "forge-std/StdJson.sol";

contract MonthlyRethUniPricesScript is Script {
    using stdJson for string;

    function setUp() public {}

    function run() public {
        // Parse March blocks
        string[] memory blocks = new string[](31); // March has 31 days
        blocks[0] = "19336607";  // Mar 1
        blocks[1] = "19343772";  // Mar 2
        blocks[2] = "19350920";  // Mar 3
        blocks[3] = "19358080";  // Mar 4
        blocks[4] = "19365247";  // Mar 5
        blocks[5] = "19372411";  // Mar 6
        blocks[6] = "19379574";  // Mar 7
        blocks[7] = "19386734";  // Mar 8
        blocks[8] = "19393822";  // Mar 9
        blocks[9] = "19400982";  // Mar 10
        blocks[10] = "19408134"; // Mar 11
        blocks[11] = "19415286"; // Mar 12
        blocks[12] = "19422439"; // Mar 13
        blocks[13] = "19429556"; // Mar 14
        blocks[14] = "19436645"; // Mar 15
        blocks[15] = "19443768"; // Mar 16
        blocks[16] = "19450870"; // Mar 17
        blocks[17] = "19457983"; // Mar 18
        blocks[18] = "19465096"; // Mar 19
        blocks[19] = "19472215"; // Mar 20
        blocks[20] = "19479341"; // Mar 21
        blocks[21] = "19486457"; // Mar 22
        blocks[22] = "19493591"; // Mar 23
        blocks[23] = "19500711"; // Mar 24
        blocks[24] = "19507816"; // Mar 25
        blocks[25] = "19514906"; // Mar 26
        blocks[26] = "19522003"; // Mar 27
        blocks[27] = "19528924"; // Mar 28
        blocks[28] = "19535952"; // Mar 29
        blocks[29] = "19543074"; // Mar 30
        blocks[30] = "19550183"; // Mar 31

        // Create output array
        string memory output = "[";
        
        UniswapV3RethPriceScript priceScript = new UniswapV3RethPriceScript();
        
        for (uint i = 0; i < blocks.length; i++) {
            console2.log("Processing block:", blocks[i]);
            uint256 blockNumber = vm.parseUint(blocks[i]);
            
            (bool success, uint256 price) = priceScript.getPrice(blockNumber);
            if (!success) {
                console2.log("Failed to process block:", blocks[i]);
                break;
            }
            
            // Create JSON object with raw 18 decimal price
            string memory jsonObject = string.concat(
                '{"uni_rate":"',
                vm.toString(price),
                '","block":"',
                blocks[i],
                '"}'
            );
            
            // Add to output array
            if (i > 0) {
                output = string.concat(output, ",");
            }
            output = string.concat(output, jsonObject);
            
            console2.log("Processed price:", price);
            
            // Write intermediate results to file
            string memory intermediateOutput = string.concat(output, "]");
            string memory outputPath = "/Users/dnyrm/Documents/defi/commodities framework/sample-data/data/reth_uni_march.json";
            vm.writeFile(outputPath, intermediateOutput);
        }
        
        console2.log("Data written to reth_uni_march.json");
    }
}

// Struct to match JSON data structure
struct MonthlyData {
    string timestamp;
    string block;
    string rate;
    string unix;
} 