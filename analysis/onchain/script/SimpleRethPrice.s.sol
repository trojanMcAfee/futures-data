// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {Script, console2} from "forge-std/Script.sol";

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

/**
 * Script for querying the rETH/WETH Uniswap v3 pool for a specific block
 */
contract SimpleRethPriceScript is Script {
    // rETH/WETH Uniswap v3 pool
    address constant POOL_ADDRESS = 0x553e9C493678d8606d6a5ba284643dB2110Df823;
    
    // Replace this with your desired block number
    uint256 constant BLOCK_NUMBER = 21475765; // <-- Replace this value

    function setUp() public {}

    function run() public {
        // Create fork at specific block
        vm.createSelectFork(vm.envString("MAINNET_RPC_URL"), BLOCK_NUMBER);
        
        // Get the pool contract
        IUniswapV3Pool pool = IUniswapV3Pool(POOL_ADDRESS);
        
        // Get slot0 data
        (uint160 sqrtPriceX96,,,,,,) = pool.slot0();
        
        // Calculate price from sqrtPriceX96
        uint256 price = (uint256(sqrtPriceX96) * uint256(sqrtPriceX96) * 1e18) >> (96 * 2);
        
        uint256 readablePrice = price;
        
        // Log results
        console2.log("Block:", BLOCK_NUMBER);
        console2.log("rETH/WETH Price:", readablePrice / 1e4);
    }
} 