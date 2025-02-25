// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import {Test, console2} from "forge-std/Test.sol";
import {WTI} from "../src/WTI.sol";
import {AggregatorV3Interface} from "../src/interfaces/AggregatorV3Interface.sol";
import {IUniswapV3Factory, IUniswapV3Pool} from "../src/interfaces/IUniswapV3.sol";

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
        
        // Log the deployer's address and balance
        console2.log("Deployer address:", deployer);
        console2.log("WTI balance:", wti.balanceOf(deployer));
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
        
        // Log all the relevant information
        console2.log("WTI/USD Price Feed Data:");
        console2.log("Round ID:", roundId);
        console2.log("Price (raw):", uint256(price));
        console2.log("Price (USD):", uint256(price) / 10**decimals);
        console2.log("Last Updated:", updatedAt);
        
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
        
        // Create pool with USDC as token0 (lower address) and WTI as token1
        address poolAddress = factory.createPool(USDC, address(wti), fee);
        IUniswapV3Pool pool = IUniswapV3Pool(poolAddress);
        
        // Calculate initial sqrtPriceX96 for price of 70.415 USDC/WTI
        // To correctly set the price, we need to account for the decimal difference
        // USDC (token0) has 6 decimals, WTI (token1) has 18 decimals
        
        // Target price: 70.415 USDC per WTI
        uint256 targetPrice = 70415000; // 70.415 * 1e6
        
        // In Uniswap V3, sqrtPriceX96 is calculated as sqrt(price) * 2^96
        // where price = price1/price0 adjusted for decimals
        
        // For a price of 70.415 USDC per WTI:
        // 1. Calculate price1/price0 = 1/70.415 = 0.0142 (approximately)
        // 2. Adjust for decimal difference: 0.0142 * 10^(6-18) = 0.0142 * 10^(-12)
        
        // Calculate sqrtPriceX96 properly
        uint256 price = (1e18 * 1e6) / targetPrice; // WTI/USDC price in Q128.128
        uint256 sqrtPriceX96Raw = sqrt((price << 96) * 1e6) << 48;
        uint160 sqrtPriceX96 = uint160(sqrtPriceX96Raw / 1e12);
        
        // Initialize pool with calculated sqrtPriceX96
        pool.initialize(sqrtPriceX96);
        vm.stopPrank();
        
        // Get current price from pool
        (uint160 currentSqrtPriceX96,,,,,,) = pool.slot0();
        
        // Calculate and verify price using the formula from the docs
        // Price = (1 / (sqrtPrice^2 / 2^192)) * 10^(decimals1 - decimals0)
        // where decimals1 = 18 (WTI) and decimals0 = 6 (USDC)
        uint256 base = 1 << 192; // 2^192
        uint256 denominator = uint256(currentSqrtPriceX96) * uint256(currentSqrtPriceX96);
        uint256 price_adjusted = (base * 1e6) / denominator;
        
        // Convert to USDC decimals for comparison
        uint256 scaledPrice = price_adjusted * 1e6 / 1e12;
        
        // Log results
        console2.log("Pool address:", poolAddress);
        console2.log("WTI/USDC Price (raw):", price_adjusted);
        console2.log("WTI/USDC Price (adjusted):", price_adjusted / 1e12);
        console2.log("WTI/USDC Price (scaled 6 decimals):", scaledPrice);
        
        // Verify price is close to 70.415 (allowing for some rounding error)
        assertApproxEqAbs(scaledPrice, 70415000, 1000); // Allow for 0.001 USDC deviation
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