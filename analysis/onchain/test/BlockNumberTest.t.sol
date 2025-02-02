// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {Test} from "forge-std/Test.sol";

contract BlockNumberTest is Test {
    function setUp() public {
        // Fork Ethereum mainnet
        vm.createSelectFork("mainnet");
    }

    function test_GetBlockNumber() public {
        // Get and log the current block number
        uint256 blockNumber = block.number;
        emit log_named_uint("Current Block Number", blockNumber);
        
        // Basic assertion to ensure block number is greater than 0
        assertGt(blockNumber, 0);
    }
} 