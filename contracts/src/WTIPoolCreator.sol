// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import {IERC20} from "./interfaces/IERC20.sol";
import {IUniswapV3Pool} from "./interfaces/IUniswapV3Pool.sol";
import {IUniswapV3Factory} from "./interfaces/IUniswapV3.sol";
import {FullMath} from "../lib/v3-core/contracts/libraries/FullMath.sol";
import "forge-std/console.sol";

/**
 * @title WTIPoolCreator
 * @dev Contract to create and initialize a Uniswap V3 pool for WTI/USDC
 */
contract WTIPoolCreator {
    // Token addresses
    address public immutable wtiToken;
    address public immutable usdcToken;
    
    // Pool parameters
    uint24 public immutable poolFee;
    uint256 public immutable targetPrice;
    uint160 public immutable initialSqrtPriceX96;
    
    // Factory address
    IUniswapV3Factory public immutable factory;
    
    // Pool address after creation
    address public poolAddress;
    IUniswapV3Pool public pool;
    
    /**
     * @dev Constructor to set up the pool creator
     * @param _wtiToken Address of the WTI token
     * @param _usdcToken Address of the USDC token
     * @param _factory Address of the Uniswap V3 factory
     * @param _fee Pool fee tier (500 = 0.05%)
     * @param _targetPrice Target price of WTI in USDC (with USDC decimals)
     * @param _initialSqrtPriceX96 Initial sqrt price for the pool
     */
    constructor(
        address _wtiToken,
        address _usdcToken, 
        address _factory,
        uint24 _fee,
        uint256 _targetPrice,
        uint160 _initialSqrtPriceX96
    ) {
        wtiToken = _wtiToken;
        usdcToken = _usdcToken;
        factory = IUniswapV3Factory(_factory);
        poolFee = _fee;
        targetPrice = _targetPrice;
        initialSqrtPriceX96 = _initialSqrtPriceX96;
    }
    
    /**
     * @dev Creates and initializes a Uniswap V3 pool
     * @return address The address of the created pool
     */
    function createAndInitializePool() external returns (address) {
        // Create pool with WTI and USDC
        poolAddress = factory.createPool(wtiToken, usdcToken, poolFee);
        pool = IUniswapV3Pool(poolAddress);
        
        // Verify token ordering
        address token0 = pool.token0();
        address token1 = pool.token1();
        
        require(token0 == wtiToken, "WTI should be token0");
        require(token1 == usdcToken, "USDC should be token1");
        
        // Log the initial sqrtPriceX96 value
        console.log("Initial sqrtPriceX96:", uint256(initialSqrtPriceX96));
        
        // Initialize the pool with the calculated sqrtPriceX96
        pool.initialize(initialSqrtPriceX96);
        
        // Get the current price from the pool
        (uint160 currentSqrtPriceX96,,,,,,) = pool.slot0();
        
        // Calculate and log the price
        uint256 calculatedPrice = calculateWTIprice(currentSqrtPriceX96);
        console.log("WTI price in USDC (with 6 decimals):", calculatedPrice);
        
        // Verify the price is close to the target
        require(
            calculatedPrice > targetPrice * 99 / 100 && 
            calculatedPrice < targetPrice * 101 / 100, 
            "Price significantly differs from target"
        );
        
        return poolAddress;
    }
    
    /**
     * @dev Calculate the WTI price in USDC from sqrtPriceX96
     * @param sqrtPriceX96 The square root price from the pool
     * @return The price of WTI in USDC with 6 decimals
     */
    function calculateWTIprice(uint256 sqrtPriceX96) public pure returns (uint256) {
        return FullMath.mulDiv(
            uint256(sqrtPriceX96) * uint256(sqrtPriceX96), 
            1e18,
            1 << 192
        );
    }
} 