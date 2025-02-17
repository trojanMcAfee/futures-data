"""
Main runner for NAV arbitrage simulations. This script:
- Loads simulation configurations from YAML
- Runs simulations for specified dates and delays
- Supports running single dates, ranges, or entire months
- Maintains backward compatibility with existing simulation structure
- Provides progress tracking and error handling
"""

from __future__ import annotations
import os
import sys
import yaml
from datetime import datetime
from typing import Optional, Dict, List, Union
from pathlib import Path
import click
from tqdm import tqdm
from dotenv import load_dotenv

# Add the project root to the Python path
project_root = os.path.join(os.path.dirname(__file__), '..', '..')
sys.path.append(project_root)

# Load environment variables from the root directory
dotenv_path = os.path.join(project_root, '.env')
load_dotenv(dotenv_path)

from analysis.arb.core.nav_spot_logic import run_daily_simulation
from analysis.arb.periphery.nav_spot_total import get_tracker, print_all_summaries

class SimulationConfig:
    def __init__(self, config_path: str):
        """Load and validate simulation configuration"""
        self.config_path = config_path
        self.config = self._load_config()
        
    def _load_config(self) -> Dict:
        """Load configuration from YAML file"""
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Configuration file not found: {self.config_path}")
            
        with open(self.config_path, 'r') as f:
            return yaml.safe_load(f)
    
    def get_delays(self) -> List[Dict[str, Union[int, str]]]:
        """Get configured delay settings"""
        return self.config.get('delays', [])
    
    def is_valid_delay(self, delay_ms: int) -> bool:
        """Check if a delay value is configured"""
        return any(d['delay_ms'] == delay_ms for d in self.get_delays())
    
    def get_dates_for_month(self, year_month: str) -> List[Dict[str, Union[str, int]]]:
        """Get simulation dates for a specific month"""
        return self.config.get('months', {}).get(year_month, {}).get('dates', [])
    
    def get_all_months(self) -> List[str]:
        """Get all configured months"""
        return list(self.config.get('months', {}).keys())
    
    def validate_config(self) -> List[str]:
        """Validate the configuration file and return any errors"""
        errors = []
        
        # Check delays section
        if not self.config.get('delays'):
            errors.append("No delays configured")
        else:
            for delay in self.get_delays():
                if 'delay_ms' not in delay:
                    errors.append(f"Missing delay_ms in delay config: {delay}")
                if 'name' not in delay:
                    errors.append(f"Missing name in delay config: {delay}")
        
        # Check months section
        if not self.config.get('months'):
            errors.append("No months configured")
        else:
            for month, month_data in self.config.get('months', {}).items():
                if not month_data.get('dates'):
                    errors.append(f"No dates configured for month {month}")
                else:
                    for date_config in month_data['dates']:
                        if 'simulation_date' not in date_config:
                            errors.append(f"Missing simulation_date in config for month {month}")
                        if 'nav_index' not in date_config:
                            errors.append(f"Missing nav_index in config for month {month}")
        
        return errors

def run_simulation_for_date(date_config: Dict[str, Union[str, int]], delay_ms: int) -> None:
    """Run simulation for a specific date and delay"""
    simulation_date = datetime.strptime(date_config['simulation_date'], '%Y-%m-%d')
    nav_index = date_config['nav_index']
    
    try:
        run_daily_simulation(simulation_date, nav_index, delay_ms=delay_ms)
    except Exception as e:
        print(f"\nError running simulation for {simulation_date.strftime('%Y-%m-%d')}: {str(e)}")

@click.group()
def cli():
    """NAV Arbitrage Simulation Runner
    
    This tool runs NAV arbitrage simulations based on configuration in config/simulations_config.yaml.
    
    Examples:
        \b
        # Show this help message
        python run_simulations.py
        
        # Run all simulations for all configured delays
        python run_simulations.py run
        
        # Run simulations for January 2024
        python run_simulations.py run --month 2024-01
        
        # Run simulation for a specific date with 12s delay
        python run_simulations.py run --date 2024-01-03 --delay 12000
        
        # Validate configuration file
        python run_simulations.py validate
    """
    pass

@cli.command()
@click.option('--config', default='config/simulations_config.yaml', help='Path to simulation configuration file')
@click.option('--month', help='Run simulations for specific month (YYYY-MM format)')
@click.option('--date', help='Run simulation for specific date (YYYY-MM-DD format)')
@click.option('--delay', type=int, help='Run simulation for specific delay in milliseconds')
def run(config: str, month: Optional[str] = None, date: Optional[str] = None, delay: Optional[int] = None):
    """Run NAV arbitrage simulations based on configuration
    
    Examples:
        \b
        # Run all simulations
        python run_simulations.py run
        
        # Run January simulations
        python run_simulations.py run --month 2024-01
        
        # Run specific date with 12s delay
        python run_simulations.py run --date 2024-01-03 --delay 12000
    """
    config_path = os.path.join(os.path.dirname(__file__), config)
    sim_config = SimulationConfig(config_path)
    
    # Validate configuration first
    errors = sim_config.validate_config()
    if errors:
        print("Configuration validation failed:")
        for error in errors:
            print(f"- {error}")
        return
    
    # Validate delay if specified
    if delay and not sim_config.is_valid_delay(delay):
        configured_delays = [d['delay_ms'] for d in sim_config.get_delays()]
        print(f"Error: Delay {delay}ms is not configured. Available delays: {configured_delays}")
        return
    
    # Determine which delays to run
    delays = [{'delay_ms': delay, 'name': f"{delay}ms"}] if delay else sim_config.get_delays()
    
    # Flag to track if we're running multiple dates
    running_multiple_dates = not date  # True if we're running a month or all months
    
    # Determine which dates to run
    if date:
        # Find the date in config
        for month_key in sim_config.get_all_months():
            dates = sim_config.get_dates_for_month(month_key)
            date_config = next((d for d in dates if d['simulation_date'] == date), None)
            if date_config:
                for delay_config in delays:
                    print(f"\nRunning simulation for {date} with {delay_config['name']} delay...")
                    run_simulation_for_date(date_config, delay_config['delay_ms'])
                break
        else:
            print(f"Date {date} not found in configuration")
            return
    else:
        # Run for specified month or all months
        months = [month] if month else sim_config.get_all_months()
        
        for month_key in months:
            dates = sim_config.get_dates_for_month(month_key)
            if not dates:
                print(f"No dates found for month {month_key}")
                continue
                
            print(f"\nProcessing {month_key}...")
            for delay_config in delays:
                print(f"\nRunning simulations with {delay_config['name']} delay...")
                for date_config in tqdm(dates, desc="Progress"):
                    run_simulation_for_date(date_config, delay_config['delay_ms'])
    
    # Only print summary if running multiple dates
    if running_multiple_dates:
        print("\nSimulations completed. Generating summary...")
        print_all_summaries()

@cli.command()
@click.option('--config', default='config/simulations_config.yaml', help='Path to simulation configuration file')
def validate(config: str):
    """Validate simulation configuration file
    
    This command checks:
    - File exists and is valid YAML
    - All required sections are present
    - All delays have required fields
    - All months have properly configured dates
    
    Example:
        python run_simulations.py validate
    """
    config_path = os.path.join(os.path.dirname(__file__), config)
    try:
        sim_config = SimulationConfig(config_path)
        errors = sim_config.validate_config()
        
        if errors:
            print("\nConfiguration validation failed:")
            for error in errors:
                print(f"- {error}")
            return
        
        print(f"\nConfiguration file {config} is valid")
        print("\nConfigured delays:")
        for delay in sim_config.get_delays():
            print(f"- {delay['name']} ({delay['delay_ms']}ms)")
        
        print("\nConfigured months:")
        for month in sim_config.get_all_months():
            dates = sim_config.get_dates_for_month(month)
            print(f"- {month}: {len(dates)} dates")
            
            # Show date details
            print("  Dates:")
            for date_config in dates:
                print(f"  - {date_config['simulation_date']} (NAV index: {date_config['nav_index']})")
    except Exception as e:
        print(f"Error validating configuration: {str(e)}")

if __name__ == "__main__":
    cli() 