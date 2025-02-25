// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

// Import only Test, no console
import "forge-std/console.sol";
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
        
        // Create pool with WTI and USDC
        address poolAddress = factory.createPool(address(wti), USDC, fee);
        IUniswapV3Pool pool = IUniswapV3Pool(poolAddress);
        
        // Verify token ordering (WTI is token0, USDC is token1)
        address token0 = pool.token0();
        address token1 = pool.token1();
        assertEq(token0, address(wti), "WTI should be token0");
        assertEq(token1, USDC, "USDC should be token1");
        
        // Target price: 70.415 USDC per WTI
        uint256 targetPrice = 70415000; // 70.415 * 1e6
        
        // Calculate sqrtPriceX96 for WTI as token0 and USDC as token1
        // sqrtPriceX96 = sqrt(targetPrice/1e6) * 2^96 = sqrt(targetPrice)/1e3 * 2^96
        uint256 sqrtTarget = sqrt(targetPrice);
        uint160 sqrtPriceX96 = uint160(FullMath.mulDiv(sqrtTarget, 1 << 96, 1e3));
        
        // Log the initial sqrtPriceX96 value
        console.log("Initial sqrtPriceX96:", uint256(sqrtPriceX96));
        
        // Initialize the pool with the calculated sqrtPriceX96
        pool.initialize(sqrtPriceX96);
        vm.stopPrank();
        
        // Get the current price from the pool
        (uint160 currentSqrtPriceX96,,,,,,) = pool.slot0();
        
        // Calculate price from sqrtPriceX96 using FullMath for precision
        // For token0 = WTI and token1 = USDC: price = (sqrtPriceX96^2 / 2^192) * 1e6
        uint256 calculatedPrice = FullMath.mulDiv(
            uint256(currentSqrtPriceX96) * uint256(currentSqrtPriceX96), 
            1e6, 
            1 << 192
        );
        
        // Log the calculated price
        console.log("WTI price in USDC (with 6 decimals):", calculatedPrice);
        console.log("Expected price:", targetPrice);
        
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