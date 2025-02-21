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
        uint256 price = (1e12 * (1 << 192)) / (uint256(sqrtPriceX96) * uint256(sqrtPriceX96));
        
        console2.log("ETH/USDC Price:", price);
    }

    function testPrice75() public pure {
        // For price = 75 USDC/ETH
        // p = 1/75 ETH/USDC
        // sqrtPriceX96 = sqrt((1/75) * 2^192)
        uint160 sqrtPriceX96 = 1771845835885348651472;
        
        uint256 price = (1e12 * (1 << 192)) / (uint256(sqrtPriceX96) * uint256(sqrtPriceX96));
        
        console2.log("sqrtPriceX96:", sqrtPriceX96);
        console2.log("Expected price: 75");
        console2.log("Calculated price:", price);
        
        require(price == 75, "Price should be 75");
    }

    function sqrt(uint256 x) private pure returns (uint256 y) {
        if (x == 0) return 0;
        
        // Using the Babylonian method for square root
        // Start with x as initial estimate
        y = x;
        uint256 z = (y + (x / y)) >> 1;
        
        // Keep improving the estimate until we converge
        while (z < y) {
            y = z;
            z = (y + (x / y)) >> 1;
        }
    }

    function testPriceCalculationSteps() public pure {
        // Let's verify our current understanding first
        uint160 currentSqrtPriceX96 = 1516523207171707839981635735553771;
        uint256 currentPrice = (1e12 * (1 << 192)) / (uint256(currentSqrtPriceX96) * uint256(currentSqrtPriceX96));
        console2.log("Current sqrtPriceX96:", currentSqrtPriceX96);
        console2.log("Gives price:", currentPrice);

        // Now let's calculate backwards from price = 75
        uint256 targetPrice = 75;
        
        // We want: sqrtPriceX96 = √((2^192) / 75)
        uint256 numerator = 1 << 192;
        uint256 denominator = targetPrice;
        
        // First divide, then take square root
        uint256 priceRatio = numerator / denominator;
        uint256 sqrtPriceX96Result = sqrt(priceRatio);
        
        console2.log("Calculated sqrtPriceX96:", sqrtPriceX96Result);
        
        // Verify our result gives the correct price
        uint256 verifyPrice = (1e18 * (1 << 192)) / (sqrtPriceX96Result * sqrtPriceX96Result);
        console2.log("Verification price:", verifyPrice);
    }
} 