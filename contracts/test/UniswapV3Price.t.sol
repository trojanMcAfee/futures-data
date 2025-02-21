// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {Test, console2} from "forge-std/Test.sol";
import {IUniswapV3Pool} from "@uniswap/v3-core/contracts/interfaces/IUniswapV3Pool.sol";

contract UniswapV3PriceTest is Test {
    IUniswapV3Pool public constant pool = IUniswapV3Pool(0x88e6A0c2dDD26FEEb64F039a2c41296FcB3f5640);
    
    function setUp() public {
        // Fork mainnet at specific block
        vm.createSelectFork(vm.rpcUrl("mainnet"), 21895733);
    }

    function testGetPrice() public view {
        (uint160 sqrtPriceX96,,,,,,) = pool.slot0();
        
        // Calculate ETH/USDC price = (1/p) * 10^12
        // Since we're doing integer arithmetic, we multiply by 10^12 first, then divide by p
        uint256 price = (1e12 * (1 << 192)) / (uint256(sqrtPriceX96) * uint256(sqrtPriceX96));
        
        console2.log("ETH/USDC Price:", price);
    }
} 