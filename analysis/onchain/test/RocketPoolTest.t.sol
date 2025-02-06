// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {Test, console2} from "forge-std/Test.sol";
import {stdJson} from "forge-std/StdJson.sol";

interface IRETH {
    function getExchangeRate() external view returns (uint256);
}

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

contract RocketPoolTest is Test {
    IRETH public rETH;
    using stdJson for string;

    // rETH/WETH Uniswap v3 pool
    address constant POOL_ADDRESS = 0x553e9C493678d8606d6a5ba284643dB2110Df823;

    function setUp() public {
        // Fork Ethereum mainnet
        vm.createSelectFork("mainnet");
        
        // Initialize rETH contract
        rETH = IRETH(0xae78736Cd615f374D3085123A210448E74Fc6393);
    }

    function test_GetExchangeRate() public {
        // Get the exchange rate
        uint256 exchangeRate = rETH.getExchangeRate();
        
        // Log the exchange rate (divide by 1e18 to get the actual rate)
        emit log_named_decimal_uint("rETH/ETH Exchange Rate", exchangeRate, 18);
        
        // Basic assertion to ensure exchange rate is not zero
        assertGt(exchangeRate, 0);
    }

    function testJanuaryRethPrices() public {
        string memory root = vm.projectRoot();
        string memory path = string.concat(root, "/../../data/reth_prices.json");
        string memory json = vm.readFile(path);

        // Get the number of entries in January
        uint256[] memory blocks = abi.decode(json.parseRaw(".january[*].block"), (uint256[]));
        string[] memory rates = abi.decode(json.parseRaw(".january[*].rate"), (string[]));
        
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
            
            // Compare with expected rate
            assertEq(priceStr, rates[i], string.concat("Price mismatch at block ", vm.toString(blocks[i])));
            
            // Log the results
            console2.log("Block:", blocks[i]);
            console2.log("Expected rate:", rates[i]);
            console2.log("Calculated rate:", priceStr);
            console2.log("---");
        }
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