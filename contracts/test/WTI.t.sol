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
import {WTIPoolCreator} from "../src/WTIPoolCreator.sol";
import {Helpers} from "./Helpers.sol";


contract WTITest is Test {
    WTI public wti;
    address public deployer;
    Helpers public helpers;
    
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
        
        // Initialize the helpers contract
        helpers = new Helpers(
            wti,
            deployer,
            USDC,
            fee,
            factory,
            nonFungiblePositionManager
        );
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
        
        // Reinitialize helpers with the new WTI instance
        helpers = new Helpers(
            wti,
            deployer,
            USDC,
            fee,
            factory,
            nonFungiblePositionManager
        );
        
        // Ensure WTI has some initial liquidity
        require(wti.balanceOf(deployer) > 0, "No WTI balance");
        
        // Target price: 70.415 USDC per WTI
        uint256 targetPrice = 70415000; // 70.415 * 1e6
        uint160 sqrtPriceX96 = 664832398952738400000000;
        
        // Create the WTIPoolCreator instance
        WTIPoolCreator poolCreator = new WTIPoolCreator(
            address(wti),
            USDC,
            address(factory),
            fee,
            targetPrice,
            sqrtPriceX96
        );
        
        // Create and initialize the pool
        address poolAddress = poolCreator.createAndInitializePool();
        IUniswapV3Pool pool = IUniswapV3Pool(poolAddress);
        vm.stopPrank();
        
        // Get the current price from the pool
        (uint160 currentSqrtPriceX96,,,,,,) = pool.slot0();
        
        // Calculate price from sqrtPriceX96 using FullMath for precision
        uint256 calculatedPrice = helpers.calculateWTIprice(currentSqrtPriceX96);
        
        // Verify the price is within an acceptable range
        assertApproxEqAbs(calculatedPrice, targetPrice, targetPrice / 100); // Allow 1% deviation
        
        console.log('--------------------------------');
    }

    function test_CreateRealWTIPool() public {
        // Fork Ethereum mainnet at a recent block
        vm.createSelectFork(vm.envString("MAINNET_RPC_URL"));
        
        // Deploy WTI token again on the forked network
        vm.startPrank(deployer);
        wti = new WTI();
        
        // Reinitialize helpers with the new WTI instance
        helpers = new Helpers(
            wti,
            deployer,
            USDC,
            fee,
            factory,
            nonFungiblePositionManager
        );
        
        // Ensure WTI has some initial liquidity
        require(wti.balanceOf(deployer) > 0, "No WTI balance");
        
        // Use vm.ffi() to call the Python script and get dynamic values
        string[] memory inputs = new string[](2);
        inputs[0] = "python";
        inputs[1] = "../ibkr/sqrtprice_calculator.py";
        
        // Call the Python script and get its output
        bytes memory result = vm.ffi(inputs);
        string memory output = string(result);
        
        // Parse the output to get sqrtPriceX96 and targetPrice using helpers
        (uint160 sqrtPriceX96, uint256 targetPrice) = helpers.parseOutput(output);
        
        // Create the WTIPoolCreator instance
        WTIPoolCreator poolCreator = new WTIPoolCreator(
            address(wti),
            USDC,
            address(factory),
            fee,
            targetPrice,
            sqrtPriceX96
        );
        
        // Create and initialize the pool
        address poolAddress = poolCreator.createAndInitializePool();
        IUniswapV3Pool pool = IUniswapV3Pool(poolAddress);
        vm.stopPrank();
        
        // Get the current price from the pool
        (uint160 currentSqrtPriceX96,,,,,,) = pool.slot0();
        
        // Calculate price from sqrtPriceX96 using FullMath for precision
        uint256 calculatedPrice = helpers.calculateWTIprice(currentSqrtPriceX96);
        
        // Verify the price is within an acceptable range
        assertApproxEqAbs(calculatedPrice, targetPrice, targetPrice / 100); // Allow 1% deviation
        
        console.log('--------------------------------');
    }
    
    function test_AddRealLiquidityWTI() public {
        // First create the pool with real WTI price
        test_CreateRealWTIPool();
        
        // Get the pool address and prepare for adding liquidity
        (address poolAddress, IUniswapV3Pool pool, address liquidityProvider) = helpers.setupForLiquidity();
        
        // Calculate token amounts for 50/50 split with 200,000 USDC
        uint256 usdcLiquidityAmount = 200000 * 1e6; // 200,000 USDC with 6 decimals
        (uint256 usdcAmount, uint256 wtiAmount) = helpers.calculateLiquidityAmounts(pool, usdcLiquidityAmount);
        
        // Since we need more WTI tokens, mint additional tokens to the deployer if needed
        vm.startPrank(deployer);
        uint256 currentWtiBalance = wti.balanceOf(deployer);
        if (currentWtiBalance < wtiAmount) {
            // For testing purposes, we'll just mint more tokens to the deployer
            // In a real scenario, this would be handled differently
            vm.stopPrank();
            // Get WTI contract owner
            address owner = deployer; // Assuming deployer is the owner
            vm.startPrank(owner);
            // Mint additional tokens to cover the required amount
            wti.mint(deployer, wtiAmount - currentWtiBalance);
            vm.stopPrank();
            vm.startPrank(deployer);
        }
        vm.stopPrank();
        
        // Fund the liquidity provider with tokens
        helpers.fundLiquidityProvider(liquidityProvider, usdcAmount, wtiAmount);
        
        // Add liquidity to the pool
        helpers.addLiquidityToPool(liquidityProvider, usdcAmount, wtiAmount);
        
        // Log the results
        helpers.logPoolState(poolAddress);
        
        console.log('--------------------------------');
        console.log('Added Real Liquidity to WTI/USDC Pool');
        console.log('USDC Amount:', usdcAmount / 1e6, 'USDC');
        console.log('WTI Amount:', wtiAmount / 1e18, 'WTI');
        console.log('--------------------------------');
    }

    function test_AddLiquidityToPool() public {
        // First create the pool
        test_CreateUniswapV3Pool();
        
        // Get the pool address and prepare for adding liquidity
        (address poolAddress, IUniswapV3Pool pool, address liquidityProvider) = helpers.setupForLiquidity();
        
        // Calculate token amounts for 50/50 split with 30,000 USDC
        uint256 usdcLiquidityAmount = 30000 * 1e6; // 30,000 USDC with 6 decimals
        (uint256 usdcAmount, uint256 wtiAmount) = helpers.calculateLiquidityAmounts(pool, usdcLiquidityAmount);
        
        // Fund the liquidity provider with tokens
        helpers.fundLiquidityProvider(liquidityProvider, usdcAmount, wtiAmount);
        
        // Add liquidity to the pool
        helpers.addLiquidityToPool(liquidityProvider, usdcAmount, wtiAmount);
        
        // Log the results
        helpers.logPoolState(poolAddress);

        console.log('--------------------------------');
        console.log('--------------------------------');
    }
    
    function test_SwapWTIForUSDC() public {
        // First add liquidity to the pool
        test_AddLiquidityToPool();
        
        // Get the pool address and pool instance
        address poolAddress = factory.getPool(address(wti), USDC, fee);
        IUniswapV3Pool pool = IUniswapV3Pool(poolAddress);
        
        // Amount of WTI to swap (10 WTI)
        uint256 amountIn = 85 * 10**wti.decimals();
        
        // Log the deployer's token balances before the swap
        console.log("Deployer token balances before swap:");
        console.log('Amount of WTI to swap:', amountIn / 1e18);
        helpers.logTokenBalances(deployer);
        
        // Log the pool state before the swap
        console.log('');
        console.log("Pool state before swap:");
        helpers.logPoolState(poolAddress);

        console.log('');
        console.log('--- SWAP ---');
        console.log('');
        
        // Execute the swap
        vm.startPrank(deployer);
        uint256 amountOut = helpers.swapWTIForUSDC(deployer, amountIn);
        vm.stopPrank();
        
        // Log the amount of USDC received
        console.log("USDC received from swap:", amountOut, "USDC (6 decimals)");
        console.log('USDC received formatted: ', amountOut / 1e6, 'USDC');
        
        // Log the new sqrtPriceX96 value and price
        (uint160 newSqrtPriceX96,,,,,,) = pool.slot0();
        uint256 newPrice = helpers.calculateWTIprice(newSqrtPriceX96);
        console.log("New sqrtPriceX96:", uint256(newSqrtPriceX96));
        console.log("New WTI price in USDC:", newPrice, "USDC (6 decimals)");
        console.log('New WTI price formatted: ', newPrice / 1e6, 'USDC');
        
        // Log the pool state after the swap
        console.log('');
        console.log("Pool state after swap:");
        helpers.logPoolState(poolAddress);
        
        // Log the deployer's token balances after the swap
        console.log('');
        console.log("Deployer token balances after swap:");
        helpers.logTokenBalances(deployer);
    }
} 