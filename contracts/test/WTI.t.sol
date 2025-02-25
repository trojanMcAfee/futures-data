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
import {IERC20} from "../src/interfaces/IERC20.sol";
import {INonfungiblePositionManager} from "../src/interfaces/INonfungiblePositionManager.sol";
import {WTILiquidityProvider} from "../src/WTILiquidityProvider.sol";

contract WTITest is Test {
    WTI public wti;
    address public deployer;
    
    // WTI/USD Chainlink Data Feed on Arbitrum
    address constant CHAINLINK_WTI_USD = 0x594b919AD828e693B935705c3F816221729E7AE8;

    // Get the NonFungiblePositionManager address (Uniswap V3 standard)
    address nonFungiblePositionManager = 0xC36442b4a4522E871399CD717aBDD847Ab11FE88;

    // Get the Uniswap factory and pool addresses
    IUniswapV3Factory factory = IUniswapV3Factory(0x1F98431c8aD98523631AE4a59f267346ea31F984);
    address USDC = 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48;
    uint24 fee = 500;
    

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
        // uint256 sqrtTarget = sqrt(targetPrice);
        // uint160 sqrtPriceX96 = uint160(FullMath.mulDiv(sqrtTarget, 1 << 96, 1e3));
        uint160 sqrtPriceX96 = 664832398952738400000000;
        
        // Log the initial sqrtPriceX96 value
        console.log("Initial sqrtPriceX96:", uint256(sqrtPriceX96));
        
        // Initialize the pool with the calculated sqrtPriceX96
        pool.initialize(sqrtPriceX96);
        vm.stopPrank();
        
        // Get the current price from the pool
        (uint160 currentSqrtPriceX96,,,,,,) = pool.slot0();
        
        // Calculate price from sqrtPriceX96 using FullMath for precision
        // For token0 = WTI (18 decimals) and token1 = USDC (6 decimals): 
        uint256 calculatedPrice = _calculateWTIprice(currentSqrtPriceX96);

        // Log the calculated price
        console.log("WTI price in USDC (with 6 decimals):", calculatedPrice);
        console.log("Expected price:", targetPrice);
        
        // Verify the price is within an acceptable range
        assertApproxEqAbs(calculatedPrice, targetPrice, targetPrice / 100); // Allow 1% deviation
    }

    function _calculateWTIprice(uint256 sqrtPriceX96) internal pure returns (uint256) {
        return FullMath.mulDiv(
            uint256(sqrtPriceX96) * uint256(sqrtPriceX96), 
            1e18,
            1 << 192
        );
    }

    function test_AddLiquidityToPool() public {
        // First create the pool
        test_CreateUniswapV3Pool();
        
        // Get the pool address and prepare for adding liquidity
        (address poolAddress, IUniswapV3Pool pool, address liquidityProvider) = _setupForLiquidity();
        
        // Calculate token amounts for 50/50 split
        (uint256 usdcAmount, uint256 wtiAmount) = _calculateLiquidityAmounts(pool);
        
        // Fund the liquidity provider with tokens
        _fundLiquidityProvider(liquidityProvider, usdcAmount, wtiAmount);
        
        // Add liquidity to the pool
        (uint256 tokenId, uint128 liquidity, uint256 amount0, uint256 amount1) = 
            _addLiquidityToPool(liquidityProvider, usdcAmount, wtiAmount);
        
        // Log the results
        _logPoolState(poolAddress, pool, tokenId, liquidity, amount0, amount1);
    }
    
    function _setupForLiquidity() private returns (address poolAddress, IUniswapV3Pool pool, address liquidityProvider) {
        // Get the pool address
        poolAddress = factory.getPool(address(wti), USDC, fee);
        pool = IUniswapV3Pool(poolAddress);
        
        // Create a new address for the liquidity provider
        uint256 liquidityProviderPrivateKey = uint256(keccak256(abi.encodePacked(block.timestamp, "LIQUIDITY_PROVIDER")));
        liquidityProvider = vm.addr(liquidityProviderPrivateKey);
        
        // Fund the liquidity provider with ETH
        vm.deal(liquidityProvider, 1 ether);
        
        return (poolAddress, pool, liquidityProvider);
    }
    
    function _calculateLiquidityAmounts(IUniswapV3Pool pool) private view returns (uint256 usdcAmount, uint256 wtiAmount) {
        // Get the current price to calculate the WTI/USDC ratio
        (uint160 currentSqrtPriceX96,,,,,,) = pool.slot0();
        uint256 wtiPrice = _calculateWTIprice(currentSqrtPriceX96);
        console.log("Current WTI price in USDC (with 6 decimals):", wtiPrice);
        
        // Define the USDC amount to add as liquidity
        usdcAmount = 30000 * 1e6; // 30,000 USDC with 6 decimals
        
        // Calculate the WTI amount for 50/50 split
        // For a 50/50 split at price p, we need: 
        // value_wti = value_usdc
        // amount_wti * p = amount_usdc
        // amount_wti = amount_usdc / p
        wtiAmount = (usdcAmount * 1e18) / wtiPrice; // Converting to 18 decimals
        console.log("WTI amount to add:", wtiAmount / 1e18, "WTI");
        
        return (usdcAmount, wtiAmount);
    }
    
    function _fundLiquidityProvider(address liquidityProvider, uint256 usdcAmount, uint256 wtiAmount) private {
        // Mint USDC to the liquidity provider
        vm.startPrank(deployer);
        // Deal USDC tokens to the liquidity provider
        deal(USDC, liquidityProvider, usdcAmount);
        
        // Transfer WTI tokens to the liquidity provider
        wti.transfer(liquidityProvider, wtiAmount);
        vm.stopPrank();
    }
    
    function _addLiquidityToPool(
        address liquidityProvider, 
        uint256 usdcAmount, 
        uint256 wtiAmount
    ) private returns (
        uint256 tokenId, 
        uint128 liquidity, 
        uint256 amount0, 
        uint256 amount1
    ) {
        // Deploy the WTILiquidityProvider contract
        vm.startPrank(liquidityProvider);
        
        WTILiquidityProvider liquidityProviderContract = _deployAndPrepareContract(
            liquidityProvider,
            usdcAmount,
            wtiAmount
        );
        
        // Get tick range for liquidity
        (int24 tickLower, int24 tickUpper) = _calculateTickRange();
        
        // Call the overloaded addLiquidity function with our custom tick range
        try liquidityProviderContract.addLiquidity(
            usdcAmount, 
            wtiAmount, 
            tickLower, 
            tickUpper
        ) returns (
            uint256 _tokenId, 
            uint128 _liquidity, 
            uint256 _amount0, 
            uint256 _amount1
        ) {
            tokenId = _tokenId;
            liquidity = _liquidity;
            amount0 = _amount0;
            amount1 = _amount1;
            
            _logAddLiquidityResults(tokenId, liquidity, amount0, amount1);
        } catch Error(string memory reason) {
            console.log("Failed to add liquidity with reason:", reason);
            revert(reason);
        } catch (bytes memory lowLevelData) {
            console.log("Failed to add liquidity with low level error");
            revert("Low level error");
        }
        
        vm.stopPrank();
        
        return (tokenId, liquidity, amount0, amount1);
    }
    
    function _deployAndPrepareContract(
        address liquidityProvider,
        uint256 usdcAmount,
        uint256 wtiAmount
    ) private returns (WTILiquidityProvider) {
        // Create the liquidity provider contract
        WTILiquidityProvider liquidityProviderContract = new WTILiquidityProvider(
            INonfungiblePositionManager(nonFungiblePositionManager),
            address(wti),
            USDC,
            fee
        );
        
        // Approve spending of tokens by the liquidity provider contract
        wti.approve(address(liquidityProviderContract), wtiAmount);
        IERC20(USDC).approve(address(liquidityProviderContract), usdcAmount);
        
        // Print debug info
        console.log("WTI token address:", address(wti));
        console.log("USDC token address:", USDC);
        console.log("WTI balance of provider:", wti.balanceOf(liquidityProvider) / 1e18);
        console.log("USDC balance of provider:", IERC20(USDC).balanceOf(liquidityProvider) / 1e6);
        
        return liquidityProviderContract;
    }
    
    function _calculateTickRange() private view returns (int24 tickLower, int24 tickUpper) {
        // Get the current price to calculate a reasonable price range
        address poolAddress = factory.getPool(address(wti), USDC, fee);
        IUniswapV3Pool pool = IUniswapV3Pool(poolAddress);
        (uint160 sqrtPriceX96, int24 currentTick,,,,,) = pool.slot0();
        
        // Instead of using a fixed range, let's make sure we're centered around the current tick
        int24 tickSpacing = pool.tickSpacing();
        
        // Calculate a tick range that includes the current price
        // Make sure the ticks are multiples of the tick spacing
        tickLower = ((currentTick - int24(100 * tickSpacing)) / tickSpacing) * tickSpacing;
        tickUpper = ((currentTick + int24(100 * tickSpacing)) / tickSpacing) * tickSpacing;
        
        console.log("Current tick:", currentTick);
        console.log("-----");
        console.logInt(tickLower);
        console.log("tickLower ^");
        console.logInt(tickUpper);
        console.log("tickUpper ^");
        console.log("-----");
        console.log("Tick spacing:", tickSpacing);
        
        return (tickLower, tickUpper);
    }
    
    // Helper function to log the results of adding liquidity
    function _logAddLiquidityResults(
        uint256 tokenId,
        uint128 liquidity,
        uint256 amount0,
        uint256 amount1
    ) private view {
        // Get pool token information
        address poolAddress = factory.getPool(address(wti), USDC, fee);
        IUniswapV3Pool pool = IUniswapV3Pool(poolAddress);
        
        console.log("Added liquidity with token ID:", tokenId);
        console.log("Liquidity amount:", uint256(liquidity));
        
        // WTI is always token0, USDC is always token1 in our setup
        console.log("Amount of WTI used (token0):", amount0 / 1e18, "WTI");
        console.log("Amount of USDC used (token1):", amount1 / 1e6, "USDC");
    }
    
    function _logPoolState(
        address poolAddress, 
        IUniswapV3Pool pool, 
        uint256 tokenId, 
        uint128 liquidity, 
        uint256 amount0, 
        uint256 amount1
    ) private view {
        // Get the pool's current state
        (uint160 updatedSqrtPriceX96,,,,,,) = pool.slot0();
        
        // Calculate the updated price
        uint256 updatedPrice = _calculateWTIprice(updatedSqrtPriceX96);
        
        console.log("Updated sqrtPriceX96:", uint256(updatedSqrtPriceX96));
        console.log("Updated WTI price in USDC:", updatedPrice, "USDC (6 decimals)");
        
        // Get token balances in the pool
        uint256 wtiBalance = IERC20(address(wti)).balanceOf(poolAddress);
        uint256 usdcBalance = IERC20(USDC).balanceOf(poolAddress);
        
        console.log("WTI in pool:", wtiBalance / 1e18, "WTI");
        console.log("USDC in pool:", usdcBalance / 1e6, "USDC");
    }

    //--------------------------------

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