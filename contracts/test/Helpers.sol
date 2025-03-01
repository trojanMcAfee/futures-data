// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

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
import {ISwapRouter} from "../src/interfaces/ISwapRouter.sol";

contract Helpers is Test {
    // These variables need to be accessible by the helper functions
    WTI public wti;
    address public deployer;
    address public USDC;
    uint24 public fee;
    IUniswapV3Factory public factory;
    address public nonFungiblePositionManager;

    // Constructor to initialize the variables
    constructor(
        WTI _wti,
        address _deployer,
        address _USDC,
        uint24 _fee,
        IUniswapV3Factory _factory,
        address _nonFungiblePositionManager
    ) {
        wti = _wti;
        deployer = _deployer;
        USDC = _USDC;
        fee = _fee;
        factory = _factory;
        nonFungiblePositionManager = _nonFungiblePositionManager;
    }

    function calculateWTIprice(uint256 sqrtPriceX96) public pure returns (uint256) {
        return FullMath.mulDiv(
            uint256(sqrtPriceX96) * uint256(sqrtPriceX96), 
            1e18,
            1 << 192
        );
    }

    function setupForLiquidity() public returns (address poolAddress, IUniswapV3Pool pool, address liquidityProvider) {
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
    
    function calculateLiquidityAmounts(IUniswapV3Pool pool) public view returns (uint256 usdcAmount, uint256 wtiAmount) {
        // Get the current price to calculate the WTI/USDC ratio
        (uint160 currentSqrtPriceX96,,,,,,) = pool.slot0();
        uint256 wtiPrice = calculateWTIprice(currentSqrtPriceX96);
        
        // Define the USDC amount to add as liquidity
        usdcAmount = 30000 * 1e6; // 30,000 USDC with 6 decimals
        
        // Calculate the WTI amount for 50/50 split
        // For a 50/50 split at price p, we need: 
        // value_wti = value_usdc
        // amount_wti * p = amount_usdc
        // amount_wti = amount_usdc / p
        wtiAmount = (usdcAmount * 1e18) / wtiPrice; // Converting to 18 decimals
        
        return (usdcAmount, wtiAmount);
    }
    
    function fundLiquidityProvider(address liquidityProvider, uint256 usdcAmount, uint256 wtiAmount) public {
        // Mint USDC to the liquidity provider
        vm.startPrank(deployer);
        // Deal USDC tokens to the liquidity provider
        deal(USDC, liquidityProvider, usdcAmount);
        
        // Transfer WTI tokens to the liquidity provider
        wti.transfer(liquidityProvider, wtiAmount);
        vm.stopPrank();
    }
    
    function addLiquidityToPool(
        address liquidityProvider, 
        uint256 usdcAmount, 
        uint256 wtiAmount
    ) public returns (
        uint256 tokenId, 
        uint128 liquidity, 
        uint256 amount0, 
        uint256 amount1
    ) {
        // Deploy the WTILiquidityProvider contract
        vm.startPrank(liquidityProvider);
        
        WTILiquidityProvider liquidityProviderContract = deployAndPrepareContract(
            usdcAmount,
            wtiAmount
        );
        
        // Get tick range for liquidity
        (int24 tickLower, int24 tickUpper) = calculateTickRange();
        
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
            
            logAddLiquidityResults(amount0, amount1);
        } catch Error(string memory reason) {
            console.log("Failed to add liquidity with reason:", reason);
            revert(reason);
        } catch {
            console.log("Failed to add liquidity with low level error");
            revert("Low level error");
        }
        
        vm.stopPrank();
        
        return (tokenId, liquidity, amount0, amount1);
    }
    
    function deployAndPrepareContract(
        uint256 usdcAmount,
        uint256 wtiAmount
    ) public returns (WTILiquidityProvider) {
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
        
        return liquidityProviderContract;
    }
    
    function calculateTickRange() public view returns (int24 tickLower, int24 tickUpper) {
        // Get the current price to calculate a reasonable price range
        address poolAddress = factory.getPool(address(wti), USDC, fee);
        IUniswapV3Pool pool = IUniswapV3Pool(poolAddress);
        (, int24 currentTick,,,,,) = pool.slot0();
        
        // Instead of using a fixed range, let's make sure we're centered around the current tick
        int24 tickSpacing = pool.tickSpacing();
        
        // Calculate a tick range that includes the current price
        // Make sure the ticks are multiples of the tick spacing
        tickLower = ((currentTick - int24(100 * tickSpacing)) / tickSpacing) * tickSpacing;
        tickUpper = ((currentTick + int24(100 * tickSpacing)) / tickSpacing) * tickSpacing;
    
        return (tickLower, tickUpper);
    }
    
    // Helper function to log the results of adding liquidity
    function logAddLiquidityResults(
        uint256 amount0,
        uint256 amount1
    ) public view {
        // Get pool token information
        factory.getPool(address(wti), USDC, fee);
                
        // WTI is always token0, USDC is always token1 in our setup
        console.log("Amount of WTI used (token0):", amount0 / 1e18, "WTI");
        console.log("Amount of USDC used (token1):", amount1 / 1e6, "USDC");
    }
    
    function logPoolState(
        address poolAddress
    ) public view {        
        // Get token balances in the pool
        uint256 wtiBalance = IERC20(address(wti)).balanceOf(poolAddress);
        uint256 usdcBalance = IERC20(USDC).balanceOf(poolAddress);
        
        console.log("WTI in pool:", wtiBalance / 1e18, "WTI");
        console.log("USDC in pool:", usdcBalance / 1e6, "USDC");
    }

    /**
     * @dev Swap WTI tokens for USDC using Uniswap V3 SwapRouter
     * @param trader Address of the trader performing the swap
     * @param amountIn Amount of WTI tokens to swap
     * @return amountOut Amount of USDC tokens received
     */
    function swapWTIForUSDC(
        address trader,
        uint256 amountIn
    ) public returns (uint256 amountOut) {
        // Uniswap V3 SwapRouter address on Ethereum mainnet
        address swapRouter = 0xE592427A0AEce92De3Edee1F18E0157C05861564;
        
        // Start transaction as the trader
        vm.startPrank(trader);
        
        // Approve the router to spend WTI tokens
        wti.approve(swapRouter, amountIn);
        
        // Create the parameters for the swap
        ISwapRouter.ExactInputSingleParams memory params = ISwapRouter.ExactInputSingleParams({
            tokenIn: address(wti),
            tokenOut: USDC,
            fee: fee,
            recipient: trader,
            deadline: block.timestamp + 15 minutes,
            amountIn: amountIn,
            amountOutMinimum: 0, // No slippage protection for testing
            sqrtPriceLimitX96: 0 // No price limit
        });
        
        // Execute the swap
        try ISwapRouter(swapRouter).exactInputSingle(params) returns (uint256 _amountOut) {
            amountOut = _amountOut;
        } catch Error(string memory reason) {
            console.log("Failed to swap with reason:", reason);
            revert(reason);
        } catch {
            console.log("Failed to swap with low level error");
            revert("Low level error");
        }
        
        vm.stopPrank();
        
        return amountOut;
    }
    
    /**
     * @dev Log the WTI and USDC balances of an address
     * @param account Address to check balances for
     */
    function logTokenBalances(address account) public view {
        uint256 wtiBalance = wti.balanceOf(account);
        uint256 usdcBalance = IERC20(USDC).balanceOf(account);
        
        console.log("WTI balance:", wtiBalance / 1e18, "WTI");
        console.log("USDC balance:", usdcBalance / 1e6, "USDC");
    }

    // Helper function to calculate square root
    function sqrt(uint256 x) public pure returns (uint256 y) {
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
    
    /**
     * @dev Helper function to parse the output from the Python script
     * @param output String output from the Python script (format: "sqrtPriceX96,targetPrice")
     * @return sqrtPriceX96 The parsed sqrtPriceX96 value
     * @return targetPrice The parsed targetPrice value
     */
    function parseOutput(string memory output) public pure returns (uint160 sqrtPriceX96, uint256 targetPrice) {
        // Extract the final line which contains the comma-separated values
        bytes memory outputBytes = bytes(output);
        
        // Find the last line by starting from the end and looking for the last newline
        uint256 lastNewLinePos = outputBytes.length; // Start at the end
        for (int i = int(outputBytes.length) - 1; i >= 0; i--) {
            if (outputBytes[uint(i)] == bytes1('\n')) {
                lastNewLinePos = uint(i) + 1; // Position after the newline
                break;
            }
        }
        
        // Extract just the last line (which should be "sqrtPriceX96,targetPrice")
        string memory lastLine;
        if (lastNewLinePos < outputBytes.length) {
            lastLine = substring(output, lastNewLinePos, outputBytes.length - lastNewLinePos);
        } else {
            lastLine = output; // No newline found, use the entire output
        }
        
        console.log("Last line extracted:", lastLine);
        
        // Find the comma position in the last line
        uint256 commaPos;
        bytes memory lastLineBytes = bytes(lastLine);
        
        bool commaFound = false;
        for (uint i = 0; i < lastLineBytes.length; i++) {
            if (lastLineBytes[i] == bytes1(',')) {
                commaPos = i;
                commaFound = true;
                break;
            }
        }
        
        require(commaFound, "Invalid output format: comma not found");
        
        // Extract the substrings before and after the comma
        string memory sqrtPriceStr = substring(lastLine, 0, commaPos);
        string memory targetPriceStr = substring(lastLine, commaPos + 1, lastLineBytes.length - commaPos - 1);
        
        // Convert strings to integers
        sqrtPriceX96 = uint160(stringToUint(sqrtPriceStr));
        targetPrice = stringToUint(targetPriceStr);
    }
    
    /**
     * @dev Helper function to extract a substring
     * @param str The input string
     * @param startIndex The starting index (inclusive)
     * @param length The length of the substring
     * @return The extracted substring
     */
    function substring(string memory str, uint startIndex, uint length) public pure returns (string memory) {
        bytes memory strBytes = bytes(str);
        require(startIndex + length <= strBytes.length, "Out of bounds");
        
        bytes memory result = new bytes(length);
        for (uint i = 0; i < length; i++) {
            result[i] = strBytes[startIndex + i];
        }
        
        return string(result);
    }
    
    /**
     * @dev Helper function to convert a string to uint
     * @param s The input string
     * @return The parsed uint value
     */
    function stringToUint(string memory s) public pure returns (uint256) {
        bytes memory b = bytes(s);
        uint256 result = 0;
        
        for (uint i = 0; i < b.length; i++) {
            uint8 c = uint8(b[i]);
            if (c >= 48 && c <= 57) {
                // Check for overflow before multiplying by 10
                if (result > type(uint256).max / 10) {
                    // If we would overflow, return the max value
                    return type(uint256).max;
                }
                result = result * 10;
                
                // Check for overflow before adding the digit
                if (result > type(uint256).max - (c - 48)) {
                    // If we would overflow, return the max value
                    return type(uint256).max;
                }
                result = result + (c - 48);
            }
        }
        
        return result;
    }
} 