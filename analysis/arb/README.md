# NAV Arbitrage Simulation Runner

This directory contains tools for running NAV (Net Asset Value) arbitrage simulations based on configurations defined in `config/simulations_config.yaml`.

## Overview

The NAV Arbitrage Simulation Runner allows you to simulate arbitrage opportunities between NAV and spot prices across different time periods and delay settings. The tool supports running simulations for specific dates, entire months, or custom date ranges.

## Usage

The main entry point is the `arbitrage.py` script in the project root, which forwards all arguments to `analysis/arb/run_simulations.py`.

### Basic Commands

```bash
# Show help message and available commands
python arbitrage.py

# Run all simulations for all configured delays
python arbitrage.py run

# Run simulations for a specific month
python arbitrage.py run --month 2024-01

# Run simulation for a specific date with a specific delay (in milliseconds)
python arbitrage.py run --date 2024-01-03 --delay 12000

# Validate the configuration file
python arbitrage.py validate
```

### Command Options

- `run`: Run NAV arbitrage simulations based on configuration
- `validate`: Validate the simulation configuration file

### Parameters

- `--config`: Path to simulation configuration file (default: `config/simulations_config.yaml`)
- `--month`: Run simulations for specific month (YYYY-MM format)
- `--date`: Run simulation for specific date (YYYY-MM-DD format)
- `--delay`: Run simulation for specific delay in milliseconds

## Directory Structure

- `core/`: Core simulation logic and algorithms
- `periphery/`: Supporting modules and utilities
- `config/`: Configuration files for simulations
- `results/`: Output directory for simulation results
- `run_simulations.py`: Main simulation runner script

## Configuration

Simulations are configured in `config/simulations_config.yaml`, which defines:

- Available delay settings
- Date ranges for simulations
- Other simulation parameters

Use the `validate` command to check your configuration file for errors before running simulations.

## Examples

```bash
# Run all simulations for January 2024
python arbitrage.py run --month 2024-01

# Run simulation for January 3, 2024 with 12-second delay
python arbitrage.py run --date 2024-01-03 --delay 12000
``` 