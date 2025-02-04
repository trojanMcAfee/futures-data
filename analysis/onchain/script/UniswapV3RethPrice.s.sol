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

contract UniswapV3RethPriceScript is Script {
    // rETH/WETH Uniswap v3 pool
    address constant POOL_ADDRESS = 0x553e9C493678d8606d6a5ba284643dB2110Df823;

    function setUp() public {}

    function run() public {
        // Set the block number
        vm.createSelectFork(vm.envString("MAINNET_RPC_URL"), 21775219);
        
        // Get the pool contract
        IUniswapV3Pool pool = IUniswapV3Pool(POOL_ADDRESS);
        
        // Get slot0 data
        (uint160 sqrtPriceX96,,,,,,) = pool.slot0();
        
        // Calculate price from sqrtPriceX96
        // Price = (sqrtPriceX96 / 2^96)^2
        // Since rETH is token0 and WETH is token1, this gives us rETH/WETH price
        uint256 price = (uint256(sqrtPriceX96) * uint256(sqrtPriceX96) * 1e18) >> (96 * 2);
        
        console2.log("Block Number:", block.number);
        console2.log("sqrtPriceX96:", sqrtPriceX96);
        console2.log("rETH/WETH Price (18 decimals):", price);
    }
} 