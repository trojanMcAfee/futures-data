// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {Script, console2} from "forge-std/Script.sol";
import {UniswapV3RethPriceScript} from "./UniswapV3RethPrice.s.sol";
import {stdJson} from "forge-std/StdJson.sol";

contract MonthlyRethUniPricesScript is Script {
    using stdJson for string;

    function setUp() public {}

    function run() public {
        // Parse February blocks
        string[] memory blocks = new string[](29); // February 2024 has 29 days (leap year)
        blocks[0] = "19129889";  // Feb 1
        blocks[1] = "19137016";  // Feb 2
        blocks[2] = "19144139";  // Feb 3
        blocks[3] = "19151256";  // Feb 4
        blocks[4] = "19158367";  // Feb 5
        blocks[5] = "19165490";  // Feb 6
        blocks[6] = "19172615";  // Feb 7
        blocks[7] = "19179747";  // Feb 8
        blocks[8] = "19186867";  // Feb 9
        blocks[9] = "19194001";  // Feb 10
        blocks[10] = "19201123"; // Feb 11
        blocks[11] = "19208243"; // Feb 12
        blocks[12] = "19215378"; // Feb 13
        blocks[13] = "19222506"; // Feb 14
        blocks[14] = "19229625"; // Feb 15
        blocks[15] = "19236755"; // Feb 16
        blocks[16] = "19243885"; // Feb 17
        blocks[17] = "19250998"; // Feb 18
        blocks[18] = "19258094"; // Feb 19
        blocks[19] = "19265203"; // Feb 20
        blocks[20] = "19272341"; // Feb 21
        blocks[21] = "19279458"; // Feb 22
        blocks[22] = "19286583"; // Feb 23
        blocks[23] = "19293723"; // Feb 24
        blocks[24] = "19300884"; // Feb 25
        blocks[25] = "19308030"; // Feb 26
        blocks[26] = "19315170"; // Feb 27
        blocks[27] = "19322320"; // Feb 28
        blocks[28] = "19329465"; // Feb 29

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
            string memory outputPath = "/Users/dnyrm/Documents/defi/commodities framework/sample-data/data/reth_uni_february.json";
            vm.writeFile(outputPath, intermediateOutput);
        }
        
        console2.log("Data written to reth_uni_february.json");
    }
}

// Struct to match JSON data structure
struct MonthlyData {
    string timestamp;
    string block;
    string rate;
    string unix;
} 