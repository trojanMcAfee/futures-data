// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {Script, console2} from "forge-std/Script.sol";
import {stdJson} from "forge-std/StdJson.sol";

interface IUniswapV3Pool {
    function slot0()
        external
        view
        returns (
            uint160 sqrtPriceX96,
            int24 tick,
            uint16 observationIndex,
            uint16 observationCardinality,
            uint16 observationCardinalityNext,
            uint8 feeProtocol,
            bool unlocked
        );
}

contract JanuaryRethPriceScript is Script {
    using stdJson for string;

    // rETH/WETH Uniswap v3 pool
    address constant POOL_ADDRESS = 0x553e9C493678d8606d6a5ba284643dB2110Df823;

    function setUp() public {}

    function run() public {
        string memory root = vm.projectRoot();
        string memory path = string.concat(root, "/../../data/reth_prices.json");
        string memory json = vm.readFile(path);

        // Get the number of entries in January
        uint256[] memory blocks = abi.decode(json.parseRaw(".january[*].block"), (uint256[]));
        
        // Create output JSON string
        string memory jsonOutput = "[";
        
        // Process each block
        for (uint i = 0; i < blocks.length; i++) {
            // Create fork at specific block
            vm.createSelectFork(vm.envString("MAINNET_RPC_URL"), blocks[i]);
            
            // Get the pool contract
            IUniswapV3Pool pool = IUniswapV3Pool(POOL_ADDRESS);
            
            // Get slot0 data
            (uint160 sqrtPriceX96,,,,,,) = pool.slot0();
            
            // Calculate price from sqrtPriceX96
            uint256 price = (uint256(sqrtPriceX96) * uint256(sqrtPriceX96) * 1e18) >> (96 * 2);
            
            // Convert price to string with 4 decimals
            string memory priceStr = uint256ToString(price);
            
            // Get original data
            string memory timestamp = abi.decode(json.parseRaw(string.concat(".january[", vm.toString(i), "].timestamp")), (string));
            string memory rate = abi.decode(json.parseRaw(string.concat(".january[", vm.toString(i), "].rate")), (string));
            string memory unix = abi.decode(json.parseRaw(string.concat(".january[", vm.toString(i), "].unix")), (string));
            
            // Create JSON object for this entry
            string memory entry = string.concat(
                '{',
                '"timestamp":"', timestamp, '",',
                '"block":"', vm.toString(blocks[i]), '",',
                '"rate":"', rate, '",',
                '"rate_spot":"', priceStr, '",',
                '"unix":"', unix, '"',
                '}'
            );
            
            // Add comma if not last element
            if (i < blocks.length - 1) {
                entry = string.concat(entry, ",");
            }
            
            // Add to output
            jsonOutput = string.concat(jsonOutput, entry);
            
            // Log the results
            console2.log("Block:", blocks[i]);
            console2.log("Original rate:", rate);
            console2.log("Calculated rate:", priceStr);
            console2.log("---");
        }
        
        // Close the array
        jsonOutput = string.concat(jsonOutput, "]");
        
        // Write the output to a file
        string memory outputPath = string.concat(root, "/../../data/january_rates.json");
        vm.writeFile(outputPath, jsonOutput);
        
        console2.log("Results written to january_rates.json");
    }

    function uint256ToString(uint256 value) internal pure returns (string memory) {
        // Convert to 4 decimal places
        value = value / 1e14; // Convert from 18 decimals to 4 decimals
        
        if (value == 0) return "0.0000";
        
        uint256 temp = value;
        uint256 digits;
        while (temp != 0) {
            digits++;
            temp /= 10;
        }
        
        bytes memory buffer = new bytes(digits + 5); // +5 for "0." and 4 decimals
        buffer[0] = "0";
        buffer[1] = ".";
        
        // Fill with leading zeros if needed
        uint256 leadingZeros = 4 - digits;
        for (uint256 i = 0; i < leadingZeros; i++) {
            buffer[i + 2] = "0";
        }
        
        temp = value;
        uint256 index = buffer.length;
        while (temp != 0) {
            index--;
            buffer[index] = bytes1(uint8(48 + temp % 10));
            temp /= 10;
        }
        
        return string(buffer);
    }
} 