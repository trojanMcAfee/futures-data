// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

// Import only Test, no console
import {Test} from "forge-std/Test.sol";
import {WTI} from "../src/WTI.sol";
import {AggregatorV3Interface} from "../src/interfaces/AggregatorV3Interface.sol";
import {IUniswapV3Pool} from "../src/interfaces/IUniswapV3Pool.sol";
import {IUniswapV3Factory} from "../src/interfaces/IUniswapV3.sol";
import {FullMath} from "../lib/v3-core/contracts/libraries/FullMath.sol";

contract WTITest is Test {
    WTI public wti;
    address public deployer;
    
    // WTI/USD Chainlink Data Feed on Arbitrum
    address constant CHAINLINK_WTI_USD = 0x594b919AD828e693B935705c3F816221729E7AE8;
    
    function setUp() public {
        // Create a new account for the deployer
        uint256 deployerPrivateKey = uint256(keccak256(abi.encodePacked(block.timestamp, "WTI_DEPLOYER")));
        deployer = vm.addr(deployerPrivateKey);
        
        // Fund the deployer with some ETH
        vm.deal(deployer, 1 ether);
        
        // Deploy WTI contract as the deployer
        vm.startPrank(deployer);
        wti = new WTI();
        vm.stopPrank();
    }

    function test_InitialBalance() public view {
        // Test that the deployer received 1000 tokens
        uint256 expectedBalance = 1000 * 10**wti.decimals();
        assertEq(wti.balanceOf(deployer), expectedBalance, "Deployer should have 1000 WTI tokens");
        
        // Remove console logging
    }

    function test_TokenMetadata() public view {
        // Test token name and symbol
        assertEq(wti.name(), "Crude Oil", "Token name should be 'Crude Oil'");
        assertEq(wti.symbol(), "WTI", "Token symbol should be 'WTI'");
        assertEq(wti.decimals(), 18, "Token should have 18 decimals");
    }

    function test_ChainlinkWTIPrice() public {
        // Fork Arbitrum at specific block
        vm.createSelectFork(vm.envString("ARBITRUM_RPC_URL"), 309442764);
        
        // Get the Chainlink price feed
        AggregatorV3Interface priceFeed = AggregatorV3Interface(CHAINLINK_WTI_USD);
        
        // Get the latest price data
        (
            uint80 roundId,
            int256 price,,
            uint256 updatedAt,
            uint80 answeredInRound
        ) = priceFeed.latestRoundData();
        
        // Get decimals to format the price correctly
        uint8 decimals = priceFeed.decimals();
        
        // Remove console logging
        
        // Make sure we got a valid price
        require(price > 0, "Invalid price");
        require(updatedAt > 0, "Round not complete");
        require(answeredInRound >= roundId, "Stale price");
    }

    function test_CreateUniswapV3Pool() public {
        // Fork Ethereum mainnet at a recent block
        vm.createSelectFork(vm.envString("MAINNET_RPC_URL"));
        
        // Import required interfaces
        IUniswapV3Factory factory = IUniswapV3Factory(0x1F98431c8aD98523631AE4a59f267346ea31F984);
        
        // USDC address on Ethereum mainnet
        address USDC = 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48;
        
        // Create pool with 0.05% fee
        uint24 fee = 500;
        
        // Deploy WTI token again on the forked network
        vm.startPrank(deployer);
        wti = new WTI();
        
        // Ensure WTI has some initial liquidity
        require(wti.balanceOf(deployer) > 0, "No WTI balance");
        
        // Create pool - note that the order doesn't matter for creation, Uniswap will sort them
        address poolAddress = factory.createPool(address(wti), USDC, fee);
        IUniswapV3Pool pool = IUniswapV3Pool(poolAddress);
        
        // Get token ordering
        address token0 = pool.token0();
        address token1 = pool.token1();
        
        // Store values in variables for debugging later
        bool isUsdcToken0 = token0 == USDC;
        
        // Target price: 70.415 USDC per WTI
        uint256 targetPrice = 70415000; // 70.415 * 1e6
        
        // Calculate sqrtPriceX96 based on token ordering
        uint160 sqrtPriceX96;
        
        if (isUsdcToken0) {
            // USDC is token0, WTI is token1
            // Price = USDC/WTI = 1/70.415
            // Adjust for decimals: 10^(18-6) = 10^12
            
            // Calculate price = 1/70.415 * 10^12
            uint256 price = FullMath.mulDiv(1e12, 1e6, targetPrice);
            
            // Calculate sqrt(price) * 2^96
            uint256 sqrtPrice = sqrt(price);
            sqrtPriceX96 = uint160(FullMath.mulDiv(sqrtPrice, 1 << 96, 1e6));
        } else {
            // WTI is token0 and USDC is token1.
            // The pool encodes sqrtPriceX96 = sqrt(USDC per WTI) * 2^96.
            // Our target price is 70.415 USDC/WTI but targetPrice is 70415000 (with 6 decimals).
            // Thus, USDC per WTI = targetPrice/1e6. We want:
            //    (sqrtPriceX96/2^96)^2 = targetPrice/1e6.
            // Taking square roots, we desire:
            //    sqrtPriceX96 = sqrt(targetPrice/1e6) * 2^96.
            // Since targetPrice is scaled by 1e6, we compute:
            //    sqrt(targetPrice/1e6) = sqrt(targetPrice) / 1e3   (because sqrt(1e6)=1e3).
            //
            // Thus, set:
            uint256 sqrtTarget = sqrt(targetPrice); // e.g., sqrt(70415000) ≈ 8392.
            sqrtPriceX96 = uint160(FullMath.mulDiv(sqrtTarget, 1 << 96, 1e3));
        }
        
        // Initialize the pool with the calculated sqrtPriceX96
        pool.initialize(sqrtPriceX96);
        vm.stopPrank();
        
        // Get the current price from the pool
        (uint160 currentSqrtPriceX96,,,,,,) = pool.slot0();
        
        // Debug info
        emit log_named_uint("Token0 is USDC", isUsdcToken0 ? 1 : 0);
        emit log_named_uint("sqrtPriceX96", uint256(currentSqrtPriceX96));
        emit log_named_address("Token0", token0);
        emit log_named_address("Token1", token1);
        
        // Calculate price from sqrtPriceX96 using FullMath for precision
        uint256 calculatedPrice;
        
        if (isUsdcToken0) {
            // If USDC is token0, price of WTI in USDC = 1/(sqrtPrice^2/2^192) * 10^12
            uint256 sqrtPriceSq = FullMath.mulDiv(uint256(currentSqrtPriceX96), uint256(currentSqrtPriceX96), 1);
            uint256 Q192 = 1 << 192;
            calculatedPrice = FullMath.mulDiv(FullMath.mulDiv(Q192, 1e12, sqrtPriceSq), 1, 1);
        } else {
            // For token0 = WTI and token1 = USDC, the pool's encoded price is:
            //    USDC per WTI = (sqrtPriceX96 / 2^96)^2.
            // We then scale by 1e6 (USDC decimals) to get calculatedPrice.
            // So set:
            calculatedPrice = FullMath.mulDiv(uint256(currentSqrtPriceX96) * uint256(currentSqrtPriceX96), 1e6, 1 << 192);
        }
        
        emit log_named_uint("Calculated price (in USDC decimals)", calculatedPrice);
        emit log_named_uint("Expected price", targetPrice);
        
        // Verify the price is within an acceptable range
        assertApproxEqAbs(calculatedPrice, targetPrice, targetPrice / 100); // Allow 1% deviation
    }

    // Helper function to calculate square root
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
} 