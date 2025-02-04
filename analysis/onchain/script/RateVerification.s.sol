// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {Script} from "forge-std/Script.sol";
import {console2} from "forge-std/console2.sol";

interface IRETH {
    function getExchangeRate() external view returns (uint256);
}

contract RateVerification is Script {
    IRETH constant rocketTokenRETH = IRETH(0xae78736Cd615f374D3085123A210448E74Fc6393);
    uint256 constant TARGET_RATE = 1108864467208237612;
    
    function run() public {
        // June 2, 2024
        vm.createSelectFork("https://eth-mainnet.g.alchemy.com/v2/pdMXO8V_cevAZjdp6W-PJ8QSV3dd3rta", 20107444);
        uint256 rate1 = rocketTokenRETH.getExchangeRate();
        console2.log("2024-06-02 Rate:", rate1);
        console2.log("Matches expected?", rate1 == TARGET_RATE);
        
        // June 3, 2024
        vm.createSelectFork("https://eth-mainnet.g.alchemy.com/v2/pdMXO8V_cevAZjdp6W-PJ8QSV3dd3rta", 20114644);
        uint256 rate2 = rocketTokenRETH.getExchangeRate();
        console2.log("2024-06-03 Rate:", rate2);
        console2.log("Matches expected?", rate2 == TARGET_RATE);
        
        // June 4, 2024
        vm.createSelectFork("https://eth-mainnet.g.alchemy.com/v2/pdMXO8V_cevAZjdp6W-PJ8QSV3dd3rta", 20121844);
        uint256 rate3 = rocketTokenRETH.getExchangeRate();
        console2.log("2024-06-04 Rate:", rate3);
        console2.log("Matches expected?", rate3 == TARGET_RATE);
    }
} 