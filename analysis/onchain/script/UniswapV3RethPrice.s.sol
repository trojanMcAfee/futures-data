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
    string constant RPC_URL = "https://eth-mainnet.g.alchemy.com/v2/pdMXO8V_cevAZjdp6W-PJ8QSV3dd3rta";

    function setUp() public {}

    function getPrice(uint256 blockNumber) public returns (bool success, uint256 price) {
        // Set the block number
        vm.createSelectFork(RPC_URL, blockNumber);
        
        // Get the pool contract
        IUniswapV3Pool pool = IUniswapV3Pool(POOL_ADDRESS);
        
        try pool.slot0() returns (
            uint160 sqrtPriceX96,
            int24,
            uint16,
            uint16,
            uint16,
            uint8,
            bool
        ) {
            // Calculate price from sqrtPriceX96
            // Price = (sqrtPriceX96 / 2^96)^2
            // Since rETH is token0 and WETH is token1, this gives us rETH/WETH price
            price = (uint256(sqrtPriceX96) * uint256(sqrtPriceX96) * 1e18) >> (96 * 2);
            return (true, price);
        } catch {
            return (false, 0);
        }
    }

    function run() public {
        // This is kept for compatibility but we'll use getPrice instead
        (bool success, uint256 price) = getPrice(21775219);
        if (success) {
            console2.log("Block Number:", block.number);
            console2.log("rETH/WETH Price (18 decimals):", price);
        } else {
            console2.log("Failed to get price");
        }
    }
} 