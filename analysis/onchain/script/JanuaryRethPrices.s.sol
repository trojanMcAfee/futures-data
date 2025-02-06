// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {Script, console2} from "forge-std/Script.sol";
import {UniswapV3RethPriceScript} from "./UniswapV3RethPrice.s.sol";
import {stdJson} from "forge-std/StdJson.sol";

contract JanuaryRethPricesScript is Script {
    using stdJson for string;

    function setUp() public {}

    function run() public {
        // Parse January blocks directly
        string[] memory blocks = new string[](31);
        blocks[0] = "18908895";  // Jan 1
        blocks[1] = "18916002";  // Jan 2
        blocks[2] = "18923124";  // Jan 3
        blocks[3] = "18930253";  // Jan 4
        blocks[4] = "18937381";  // Jan 5
        blocks[5] = "18944481";  // Jan 6
        blocks[6] = "18951539";  // Jan 7
        blocks[7] = "18958622";  // Jan 8
        blocks[8] = "18965711";  // Jan 9
        blocks[9] = "18972838";  // Jan 10
        blocks[10] = "18979978"; // Jan 11
        blocks[11] = "18987104"; // Jan 12
        blocks[12] = "18994254"; // Jan 13
        blocks[13] = "19001407"; // Jan 14
        blocks[14] = "19008565"; // Jan 15
        blocks[15] = "19015724"; // Jan 16
        blocks[16] = "19022890"; // Jan 17
        blocks[17] = "19030033"; // Jan 18
        blocks[18] = "19037186"; // Jan 19
        blocks[19] = "19044349"; // Jan 20
        blocks[20] = "19051515"; // Jan 21
        blocks[21] = "19058587"; // Jan 22
        blocks[22] = "19065671"; // Jan 23
        blocks[23] = "19072788"; // Jan 24
        blocks[24] = "19079929"; // Jan 25
        blocks[25] = "19087067"; // Jan 26
        blocks[26] = "19094208"; // Jan 27
        blocks[27] = "19101334"; // Jan 28
        blocks[28] = "19108472"; // Jan 29
        blocks[29] = "19115609"; // Jan 30
        blocks[30] = "19122760"; // Jan 31

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
            string memory outputPath = "/Users/dnyrm/Documents/defi/commodities framework/sample-data/data/reth_uni_january.json";
            vm.writeFile(outputPath, intermediateOutput);
        }
        
        console2.log("Data written to reth_uni_january.json");
    }
}

// Struct to match JSON data structure
struct JanuaryData {
    string timestamp;
    string block;
    string rate;
    string unix;
} 