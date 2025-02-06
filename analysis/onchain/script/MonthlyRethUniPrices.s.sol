// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {Script, console2} from "forge-std/Script.sol";
import {UniswapV3RethPriceScript} from "./UniswapV3RethPrice.s.sol";
import {stdJson} from "forge-std/StdJson.sol";

contract MonthlyRethUniPricesScript is Script {
    using stdJson for string;

    function setUp() public {}

    function run() public {
        // Parse May blocks
        string[] memory blocks = new string[](31); // May has 31 days
        blocks[0] = "19771560";  // May 1
        blocks[1] = "19778726";  // May 2
        blocks[2] = "19785870";  // May 3
        blocks[3] = "19793023";  // May 4
        blocks[4] = "19800180";  // May 5
        blocks[5] = "19807331";  // May 6
        blocks[6] = "19814478";  // May 7
        blocks[7] = "19821624";  // May 8
        blocks[8] = "19828771";  // May 9
        blocks[9] = "19835923";  // May 10
        blocks[10] = "19843076"; // May 11
        blocks[11] = "19850230"; // May 12
        blocks[12] = "19857379"; // May 13
        blocks[13] = "19864534"; // May 14
        blocks[14] = "19871653"; // May 15
        blocks[15] = "19878821"; // May 16
        blocks[16] = "19885977"; // May 17
        blocks[17] = "19893122"; // May 18
        blocks[18] = "19900268"; // May 19
        blocks[19] = "19907420"; // May 20
        blocks[20] = "19914565"; // May 21
        blocks[21] = "19921720"; // May 22
        blocks[22] = "19928862"; // May 23
        blocks[23] = "19936019"; // May 24
        blocks[24] = "19943177"; // May 25
        blocks[25] = "19950330"; // May 26
        blocks[26] = "19957490"; // May 27
        blocks[27] = "19964644"; // May 28
        blocks[28] = "19971801"; // May 29
        blocks[29] = "19978947"; // May 30
        blocks[30] = "19986093"; // May 31

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
            string memory outputPath = "/Users/dnyrm/Documents/defi/commodities framework/sample-data/data/reth_uni_may.json";
            vm.writeFile(outputPath, intermediateOutput);
        }
        
        console2.log("Data written to reth_uni_may.json");
    }
}

// Struct to match JSON data structure
struct MonthlyData {
    string timestamp;
    string block;
    string rate;
    string unix;
} 