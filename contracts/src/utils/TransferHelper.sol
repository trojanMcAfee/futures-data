// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import {IERC20} from "../interfaces/IERC20.sol";

/**
 * @title TransferHelper
 * @dev Helper functions for safely transferring ETH and ERC20 tokens
 */
library TransferHelper {
    /**
     * @notice Transfers tokens from the targeted address to the given destination
     * @param token The contract address of the token to be transferred
     * @param from The originating address from which the tokens will be transferred
     * @param to The destination address of the transfer
     * @param value The amount to be transferred
     */
    function safeTransferFrom(
        address token,
        address from,
        address to,
        uint256 value
    ) internal {
        (bool success, bytes memory data) =
            token.call(abi.encodeWithSelector(IERC20.transferFrom.selector, from, to, value));
        require(success && (data.length == 0 || abi.decode(data, (bool))), 'TransferHelper: TRANSFER_FROM_FAILED');
    }

    /**
     * @notice Transfers tokens from msg.sender to a recipient
     * @param token The contract address of the token which will be transferred
     * @param to The recipient of the transfer
     * @param value The value of the transfer
     */
    function safeTransfer(
        address token,
        address to,
        uint256 value
    ) internal {
        (bool success, bytes memory data) =
            token.call(abi.encodeWithSelector(IERC20.transfer.selector, to, value));
        require(success && (data.length == 0 || abi.decode(data, (bool))), 'TransferHelper: TRANSFER_FAILED');
    }

    /**
     * @notice Approves the stipulated contract to spend the given allowance in the given token
     * @param token The contract address of the token to be approved
     * @param to The target of the approval
     * @param value The amount of the given token the target will be allowed to spend
     */
    function safeApprove(
        address token,
        address to,
        uint256 value
    ) internal {
        (bool success, bytes memory data) =
            token.call(abi.encodeWithSelector(IERC20.approve.selector, to, value));
        require(success && (data.length == 0 || abi.decode(data, (bool))), 'TransferHelper: APPROVE_FAILED');
    }

    /**
     * @notice Transfers ETH to the recipient address
     * @param to The destination of the transfer
     * @param value The value to be transferred
     */
    function safeTransferETH(address to, uint256 value) internal {
        (bool success, ) = to.call{value: value}(new bytes(0));
        require(success, 'TransferHelper: ETH_TRANSFER_FAILED');
    }
} 