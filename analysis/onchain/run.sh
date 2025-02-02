#!/bin/bash
forge clean && \
forge script script/RocketPoolPrices.s.sol:RocketPoolPrices \
  --fork-url "https://eth-mainnet.g.alchemy.com/v2/pdMXO8V_cevAZjdp6W-PJ8QSV3dd3rta" \
  -vvvv \
  --silent 