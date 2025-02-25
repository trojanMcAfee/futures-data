// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import {IERC20} from "./interfaces/IERC20.sol";
import {IUniswapV3Pool} from "./interfaces/IUniswapV3Pool.sol";
import {IUniswapV3Factory} from "./interfaces/IUniswapV3.sol";
import {TickMath} from "../lib/v3-core/contracts/libraries/TickMath.sol";
import {FullMath} from "../lib/v3-core/contracts/libraries/FullMath.sol";
import {ISwapRouter} from "./interfaces/ISwapRouter.sol";
import {INonfungiblePositionManager} from "./interfaces/INonfungiblePositionManager.sol";
import {TransferHelper} from "./utils/TransferHelper.sol";
import "forge-std/console.sol";

/**
 * @title WTILiquidityProvider
 * @dev Contract to manage liquidity provision for WTI/USDC pool on Uniswap V3
 */
contract WTILiquidityProvider {
    // Uniswap V3 Position Manager
    INonfungiblePositionManager public immutable nonfungiblePositionManager;
    
    // Token addresses
    address public immutable wtiToken;
    address public immutable usdcToken;
    
    // Pool fee
    uint24 public immutable poolFee;
    
    // Last minted position ID
    uint256 public lastPositionId;
    
    /**
     * @dev Represents a liquidity position
     */
    struct Position {
        address owner;
        uint128 liquidity;
        address token0;
        address token1;
    }
    
    // Mapping of tokenId to Position
    mapping(uint256 => Position) public positions;
    
    /**
     * @dev Constructor
     * @param _nonfungiblePositionManager NFT position manager address
     * @param _wtiToken WTI token address
     * @param _usdcToken USDC token address
     * @param _poolFee Pool fee (500 = 0.05%)
     */
    constructor(
        INonfungiblePositionManager _nonfungiblePositionManager,
        address _wtiToken,
        address _usdcToken,
        uint24 _poolFee
    ) {
        nonfungiblePositionManager = _nonfungiblePositionManager;
        wtiToken = _wtiToken;
        usdcToken = _usdcToken;
        poolFee = _poolFee;
    }
    
    /**
     * @dev Add liquidity to the WTI/USDC pool
     * @param amountUSDC Amount of USDC to add as liquidity
     * @param amountWTI Amount of WTI to add as liquidity
     * @return tokenId The NFT position token ID
     * @return liquidity The amount of liquidity added
     * @return amount0 The amount of token0 used
     * @return amount1 The amount of token1 used
     */
    function addLiquidity(
        uint256 amountUSDC,
        uint256 amountWTI
    ) external returns (
        uint256 tokenId,
        uint128 liquidity,
        uint256 amount0,
        uint256 amount1
    ) {
        return addLiquidity(amountUSDC, amountWTI, TickMath.MIN_TICK, TickMath.MAX_TICK);
    }
    
    /**
     * @dev Add liquidity to the WTI/USDC pool with custom tick range
     * @param amountUSDC Amount of USDC to add as liquidity
     * @param amountWTI Amount of WTI to add as liquidity
     * @param tickLower Lower tick bound
     * @param tickUpper Upper tick bound
     * @return tokenId The NFT position token ID
     * @return liquidity The amount of liquidity added
     * @return amount0 The amount of token0 used
     * @return amount1 The amount of token1 used
     */
    function addLiquidity(
        uint256 amountUSDC,
        uint256 amountWTI,
        int24 tickLower,
        int24 tickUpper
    ) public returns (
        uint256 tokenId,
        uint128 liquidity,
        uint256 amount0,
        uint256 amount1
    ) {
        // Transfer tokens to this contract
        TransferHelper.safeTransferFrom(wtiToken, msg.sender, address(this), amountWTI);
        TransferHelper.safeTransferFrom(usdcToken, msg.sender, address(this), amountUSDC);
        
        // Approve the position manager to spend the tokens
        TransferHelper.safeApprove(wtiToken, address(nonfungiblePositionManager), amountWTI);
        TransferHelper.safeApprove(usdcToken, address(nonfungiblePositionManager), amountUSDC);
        
        // Debug logging
        console.log("Adding liquidity:");
        console.log("WTI amount:", amountWTI / 1e18);
        console.log("USDC amount:", amountUSDC / 1e6);
        console.log("-----");
        console.logInt(tickLower);
        console.log("tickLower ^");
        console.logInt(tickUpper);
        console.log("tickUpper ^");
        console.log("-----");
        
        // Create the parameters for minting a position
        // WTI is always token0, USDC is always token1 in our setup
        INonfungiblePositionManager.MintParams memory params =
            INonfungiblePositionManager.MintParams({
                token0: wtiToken,
                token1: usdcToken,
                fee: poolFee,
                tickLower: tickLower,
                tickUpper: tickUpper,
                amount0Desired: amountWTI,
                amount1Desired: amountUSDC,
                amount0Min: 0, // Accept any amount
                amount1Min: 0, // Accept any amount
                recipient: address(this),
                deadline: block.timestamp + 15 minutes
            });

        // Mint the position
        (tokenId, liquidity, amount0, amount1) = nonfungiblePositionManager.mint(params);
        
        // Debug logging for amounts after minting
        console.log("After mint - WTI used (amount0):", amount0 / 1e18);
        console.log("After mint - USDC used (amount1):", amount1 / 1e6);
        
        // Save position information
        positions[tokenId] = Position({
            owner: msg.sender,
            liquidity: liquidity,
            token0: wtiToken,
            token1: usdcToken
        });
        
        // Update the last position ID
        lastPositionId = tokenId;
        
        // Refund any leftover tokens to msg.sender
        if (amountWTI > amount0) {
            uint256 refundAmount = amountWTI - amount0;
            TransferHelper.safeTransfer(wtiToken, msg.sender, refundAmount);
        }
        
        if (amountUSDC > amount1) {
            uint256 refundAmount = amountUSDC - amount1;
            TransferHelper.safeTransfer(usdcToken, msg.sender, refundAmount);
        }
        
        return (tokenId, liquidity, amount0, amount1);
    }
    
    /**
     * @dev Save the position information
     * @param _tokenId The NFT position token ID
     * @param _owner The position owner
     */
    function _savePosition(uint256 _tokenId, address _owner) internal {
        (
            ,
            ,
            address token0,
            address token1,
            ,
            ,
            ,
            uint128 liquidity,
            ,
            ,
            ,
        ) = nonfungiblePositionManager.positions(_tokenId);
        
        positions[_tokenId] = Position({
            owner: _owner,
            liquidity: liquidity,
            token0: token0,
            token1: token1
        });
    }
    
    /**
     * @dev Get liquidity for a position
     * @param _tokenId The NFT position token ID
     * @return liquidity The position's liquidity
     */
    function getPositionLiquidity(uint256 _tokenId) external view returns (uint128 liquidity) {
        (
            ,
            ,
            ,
            ,
            ,
            ,
            ,
            liquidity,
            ,
            ,
            ,
        ) = nonfungiblePositionManager.positions(_tokenId);
        return liquidity;
    }
    
    /**
     * @dev ERC721 receiver function to handle position NFT transfers
     */
    function onERC721Received(
        address operator,
        address,
        uint256 tokenId,
        bytes calldata
    ) external returns (bytes4) {
        _savePosition(tokenId, operator);
        return this.onERC721Received.selector;
    }
} 