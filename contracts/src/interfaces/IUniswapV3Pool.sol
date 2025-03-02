// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;


interface IUniswapV3Pool {
    function token0() external view returns (address);
    function token1() external view returns (address);
    function slot0() external view returns (uint160 sqrtPriceX96, int24 tick, uint16 observationIndex, uint16 observationCardinality, uint16 observationCardinalityNext, uint8 feeProtocol, bool unlocked);
    function initialize(uint160 sqrtPriceX96) external;
    function tickSpacing() external view returns (int24);
}