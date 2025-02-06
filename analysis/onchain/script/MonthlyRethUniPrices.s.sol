// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {Script, console2} from "forge-std/Script.sol";
import {UniswapV3RethPriceScript} from "./UniswapV3RethPrice.s.sol";
import {stdJson} from "forge-std/StdJson.sol";


/**
 * Script for pulling the rETH/WETH Uniswap v3 pool price for each day of a month
 */
contract MonthlyRethUniPricesScript is Script {
    using stdJson for string;

    function setUp() public {}

    function run() public {
        // Parse December blocks
        string[] memory blocks = new string[](31); // December has 31 days
        blocks[0] = "21303934";  // Dec 1
        blocks[1] = "21311106";  // Dec 2
        blocks[2] = "21318260";  // Dec 3
        blocks[3] = "21325416";  // Dec 4
        blocks[4] = "21332579";  // Dec 5
        blocks[5] = "21339733";  // Dec 6
        blocks[6] = "21346895";  // Dec 7
        blocks[7] = "21354048";  // Dec 8
        blocks[8] = "21361218";  // Dec 9
        blocks[9] = "21368390";  // Dec 10
        blocks[10] = "21375546"; // Dec 11
        blocks[11] = "21382703"; // Dec 12
        blocks[12] = "21389869"; // Dec 13
        blocks[13] = "21397031"; // Dec 14
        blocks[14] = "21404197"; // Dec 15
        blocks[15] = "21411357"; // Dec 16
        blocks[16] = "21418530"; // Dec 17
        blocks[17] = "21425700"; // Dec 18
        blocks[18] = "21432853"; // Dec 19
        blocks[19] = "21440010"; // Dec 20
        blocks[20] = "21447176"; // Dec 21
        blocks[21] = "21454315"; // Dec 22
        blocks[22] = "21461472"; // Dec 23
        blocks[23] = "21468618"; // Dec 24
        blocks[24] = "21475765"; // Dec 25
        blocks[25] = "21482925"; // Dec 26
        blocks[26] = "21490078"; // Dec 27
        blocks[27] = "21497236"; // Dec 28
        blocks[28] = "21504402"; // Dec 29
        blocks[29] = "21511572"; // Dec 30
        blocks[30] = "21518735"; // Dec 31

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
            string memory outputPath = "/Users/dnyrm/Documents/defi/commodities framework/sample-data/data/reth_uni_december.json";
            vm.writeFile(outputPath, intermediateOutput);
        }
        
        console2.log("Data written to reth_uni_december.json");
    }
}

// Struct to match JSON data structure
struct MonthlyData {
    string timestamp;
    string block;
    string rate;
    string unix;
} 