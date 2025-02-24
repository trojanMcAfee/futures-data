// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {Test, console2} from "forge-std/Test.sol";
import {IUniswapV3Pool} from "@uniswap/v3-core/contracts/interfaces/IUniswapV3Pool.sol";
import {TickMath} from "@uniswap/v3-core/contracts/libraries/TickMath.sol";
import {TickBitmap} from "@uniswap/v3-core/contracts/libraries/TickBitmap.sol";
import {SqrtPriceMath} from "@uniswap/v3-core/contracts/libraries/SqrtPriceMath.sol";


interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}

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

    function test_CalculateSqrtPriceFromTick() public view {
        // Get current tick and sqrtPriceX96 from pool
        (uint160 actualSqrtPriceX96, int24 tick,,,,,) = pool.slot0();
        
        // Calculate sqrtPriceX96 from tick using Uniswap's TickMath library
        uint160 calculatedSqrtPriceX96 = TickMath.getSqrtRatioAtTick(tick);
        
        console2.log("Tick:", tick);
        console2.log("Actual sqrtPriceX96:", actualSqrtPriceX96);
        console2.log("Calculated sqrtPriceX96:", calculatedSqrtPriceX96);
        
        // They should be exactly equal
        require(actualSqrtPriceX96 == calculatedSqrtPriceX96, "SqrtPrice calculation mismatch");
    }
    

    function testCalculateSqrtPriceFromTick() public view {
        // Get current tick and sqrtPriceX96 from pool
        (uint160 actualSqrtPriceX96, int24 actualTick,,,,,) = pool.slot0();
        
        // Calculate sqrtPriceX96 from tick using Uniswap's TickMath library
        uint160 calculatedSqrtPriceX96 = TickMath.getSqrtRatioAtTick(actualTick);
        
        // Calculate tick from our calculated sqrtPriceX96
        int24 calculatedTick = TickMath.getTickAtSqrtRatio(calculatedSqrtPriceX96);
        
        console2.log("Actual tick:", actualTick);
        console2.log("Calculated tick:", calculatedTick);
        console2.log("Actual sqrtPriceX96:", actualSqrtPriceX96);
        console2.log("Calculated sqrtPriceX96:", calculatedSqrtPriceX96);
        
        // The ticks should match exactly
        require(actualTick == calculatedTick, "Tick calculation mismatch");
        
        // The sqrtPriceX96 values should be very close (within 0.01%)
        uint256 diff = actualSqrtPriceX96 > calculatedSqrtPriceX96 ? 
            actualSqrtPriceX96 - calculatedSqrtPriceX96 : 
            calculatedSqrtPriceX96 - actualSqrtPriceX96;
        
        require(diff * 10000 < actualSqrtPriceX96, "SqrtPrice difference too large");
    }


    function test_getLiquidity() public view {
        uint128 liquidity = pool.liquidity();
        console2.log("Liquidity:", liquidity);
    }


    function test_getCurrentLiquidityAmounts() public view {
        // Get current price and liquidity
        (uint160 sqrtPriceX96, int24 tick,,,,,) = pool.slot0();
        uint128 liquidity = pool.liquidity();
        
        // Calculate amounts at current price
        uint256 amount0 = SqrtPriceMath.getAmount0Delta(
            sqrtPriceX96,      // current sqrt price
            TickMath.getSqrtRatioAtTick(TickMath.MAX_TICK), // upper bound
            liquidity,
            false // roundUp
        );
        
        uint256 amount1 = SqrtPriceMath.getAmount1Delta(
            TickMath.getSqrtRatioAtTick(TickMath.MIN_TICK), // lower bound
            sqrtPriceX96,     // current sqrt price
            liquidity,
            false // roundUp
        );
        
        // USDC has 6 decimals, WETH has 18 decimals
        console2.log("Current tick:", tick);
        console2.log("Liquidity:", liquidity);
        console2.log("USDC amount:", amount0 / 1e6, "USDC");
        console2.log("WETH amount:", amount1 / 1e18, "WETH");
    }


    function test_getBalances() public view {
        IERC20 USDC = IERC20(pool.token0());
        uint256 balance = USDC.balanceOf(address(pool));
        console2.log("USDC balance:", balance / 1e6, "USDC");

        IERC20 WETH = IERC20(pool.token1());
        balance = WETH.balanceOf(address(pool));
        console2.log("WETH balance:", balance / 1e18, "WETH");
    }

    function test_calculateRequiredAmountsForPrice75() public view {
        // Current pool state
        (uint160 currentSqrtPriceX96, int24 currentTick,,,,,) = pool.slot0();
        uint128 currentLiquidity = pool.liquidity();
        
        console2.log("Current state:");
        console2.log("sqrtPriceX96:", currentSqrtPriceX96);
        console2.log("tick:", currentTick);
        console2.log("liquidity:", currentLiquidity);
        
        // Calculate target sqrtPriceX96 for price = 75 USDC/ETH
        // For price of 75 USDC/ETH, we need sqrtP = sqrt(1/75) * 2^96
        // This is equivalent to sqrt(2^192/75)
        uint256 targetPrice = 75;
        uint256 numerator = 1 << 192;
        uint256 denominator = targetPrice;
        uint256 priceRatio = numerator / denominator;
        uint160 targetSqrtPriceX96 = uint160(sqrt(priceRatio));
        
        console2.log("\nTarget state:");
        console2.log("Target sqrtPriceX96:", targetSqrtPriceX96);
        
        // Calculate the tick for this price
        int24 targetTick = TickMath.getTickAtSqrtRatio(targetSqrtPriceX96);
        console2.log("Target tick:", targetTick);
        
        // Get the exact sqrtPriceX96 for this tick to ensure it's valid
        uint160 exactSqrtPriceX96 = TickMath.getSqrtRatioAtTick(targetTick);
        console2.log("Exact sqrtPriceX96:", TickMath.getSqrtRatioAtTick(targetTick));
        
        // Calculate token amounts using smaller ranges to avoid overflow
        // Instead of using MIN_TICK to MAX_TICK, use a smaller range around the target tick
        // int24 lowerTick = targetTick - 10; // 10 ticks below target
        // int24 upperTick = targetTick + 10; // 10 ticks above target
        
        // uint160 lowerSqrtPriceX96 = TickMath.getSqrtRatioAtTick(lowerTick);
        // uint160 upperSqrtPriceX96 = TickMath.getSqrtRatioAtTick(upperTick);
        
        uint256 amount0 = SqrtPriceMath.getAmount0Delta(
            exactSqrtPriceX96,
            TickMath.getSqrtRatioAtTick(targetTick + 10),
            currentLiquidity,
            false // roundUp
        );
        
        uint256 amount1 = SqrtPriceMath.getAmount1Delta(
            TickMath.getSqrtRatioAtTick(targetTick - 10),
            exactSqrtPriceX96,
            currentLiquidity,
            false // roundUp
        );
        
        console2.log("USDC amount needed:", amount0 / 1e6, "USDC");
        console2.log("WETH amount needed:", amount1 / 1e18, "WETH");
        
        // Verify the resulting price using the same calculation as testGetPrice()
        uint256 verificationPrice = (1e12 * (1 << 192)) / (uint256(exactSqrtPriceX96) * uint256(exactSqrtPriceX96));
        console2.log("\nVerification:");
        console2.log("Resulting price:", verificationPrice, "USDC/ETH");
    }
} 