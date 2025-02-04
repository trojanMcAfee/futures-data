// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {Script} from "forge-std/Script.sol";
import {console2} from "forge-std/console2.sol";

interface IRETH {
    function getExchangeRate() external view returns (uint256);
}

contract SimpleRateCheck is Script {
    IRETH public rocketTokenRETH;
    
    // Constants for block calculation
    uint256 constant BLOCKS_PER_DAY = 7200; // ~12 second block time
    uint256 constant BASE_BLOCK = 19103444; // February 1, 2024
    uint256 constant BASE_TIMESTAMP = 1706745600; // February 1, 2024 00:00:00 UTC
    uint256 constant DAYS_TO_CHECK = 29; // February 2024 has 29 days (leap year)
    string constant OUTPUT_FILE = "../../data/reth_prices_february.json";

    // Track success/failure stats
    uint256 public successCount;
    uint256 public failureCount;

    function setUp() public {
        console2.log("=== Setup Starting ===");
        rocketTokenRETH = IRETH(0xae78736Cd615f374D3085123A210448E74Fc6393);
        console2.log("=== Setup Complete ===");
    }

    function formatRate(uint256 rate) internal pure returns (string memory) {
        uint256 whole = rate / 1e18;
        uint256 fraction = (rate % 1e18) / 1e15;
        string memory fractionStr = vm.toString(fraction);
        // Pad with leading zeros if needed
        while (bytes(fractionStr).length < 3) {
            fractionStr = string(abi.encodePacked("0", fractionStr));
        }
        return string(abi.encodePacked(
            vm.toString(whole),
            ".",
            fractionStr
        ));
    }

    function formatDate(uint256 timestamp) internal pure returns (string memory) {
        // Convert timestamp to date components
        uint256 z = timestamp / 86400 + 719468;
        uint256 era = (z >= 0 ? z : z - 146096) / 146097;
        uint256 doe = z - era * 146097;
        uint256 yoe = (doe - doe/1460 + doe/36524 - doe/146096) / 365;
        uint256 y = yoe + era * 400;
        uint256 doy = doe - (365*yoe + yoe/4 - yoe/100);
        uint256 mp = (5*doy + 2)/153;
        uint256 d = doy - (153*mp + 2)/5 + 1;
        uint256 m = mp < 10 ? mp + 3 : mp - 9;
        y = y + (m <= 2 ? 1 : 0);

        return string.concat(
            vm.toString(y), "-02-",  // Changed to February
            d < 10 ? string.concat("0", vm.toString(d)) : vm.toString(d)
        );
    }

    function tryGetRate(uint256 blockNumber) internal returns (bool success, uint256 rate) {
        try vm.createSelectFork(
            "https://eth-mainnet.g.alchemy.com/v2/pdMXO8V_cevAZjdp6W-PJ8QSV3dd3rta",
            blockNumber
        ) returns (uint256) {
            try rocketTokenRETH.getExchangeRate() returns (uint256 _rate) {
                return (true, _rate);
            } catch {
                console2.log("Failed to get exchange rate");
                return (false, 0);
            }
        } catch {
            console2.log("Failed to create fork");
            return (false, 0);
        }
    }

    function run() public {
        vm.createSelectFork("https://eth-mainnet.g.alchemy.com/v2/pdMXO8V_cevAZjdp6W-PJ8QSV3dd3rta", BASE_BLOCK);
        console2.log("=== Setup Starting ===");
        console2.log("=== Setup Complete ===");

        console2.log("=== Starting Rate Collection ===");
        console2.log("Will check February 2024 rates\n");

        string[] memory timestamps = new string[](DAYS_TO_CHECK);
        string[] memory blocks = new string[](DAYS_TO_CHECK);
        string[] memory rates = new string[](DAYS_TO_CHECK);

        for (uint i = 0; i < DAYS_TO_CHECK; i++) {
            uint currentBlock = BASE_BLOCK + (i * BLOCKS_PER_DAY);
            vm.rollFork(currentBlock);

            console2.log(string.concat("Day ", vm.toString(i + 1), "/", vm.toString(DAYS_TO_CHECK), " (Block ", vm.toString(currentBlock), ")"));
            
            uint rawRate = rocketTokenRETH.getExchangeRate();
            string memory rateStr = vm.toString(rawRate);  // Store raw rate as string
            
            console2.log(string.concat("  Success - Raw Rate: ", rateStr));
            console2.log("  Waiting 2 seconds...\n");

            timestamps[i] = formatDate(BASE_TIMESTAMP + (i * 1 days));
            blocks[i] = vm.toString(currentBlock);
            rates[i] = rateStr;

            vm.sleep(2 seconds);
        }

        console2.log("=== Collection Complete ===");
        console2.log(string.concat("  Successful collections: ", vm.toString(DAYS_TO_CHECK), "/", vm.toString(DAYS_TO_CHECK)));

        string memory jsonStr = '{\n  "february": [\n';  // Changed to February
        for (uint i = 0; i < DAYS_TO_CHECK; i++) {
            jsonStr = string.concat(
                jsonStr,
                '    {"timestamp": "',
                timestamps[i],
                '", "block": "',
                blocks[i],
                '", "rate": "',
                rates[i],
                '"}'
            );
            if (i < DAYS_TO_CHECK - 1) {
                jsonStr = string.concat(jsonStr, '\n,\n');
            } else {
                jsonStr = string.concat(jsonStr, '\n\n');
            }
        }
        jsonStr = string.concat(jsonStr, '  ]\n}\n');

        vm.writeFile(OUTPUT_FILE, jsonStr);
    }
} 