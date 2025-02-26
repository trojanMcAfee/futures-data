#!/usr/bin/env python
"""
Alias for the NAV arbitrage simulation runner.
This script forwards all arguments to analysis/arb/run_simulations.py
"""

import sys
import os
import subprocess

def main():
    # Get the absolute path to the run_simulations.py script
    script_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'analysis', 'arb', 'run_simulations.py'
    )
    
    # Forward all arguments to the script
    cmd = [sys.executable, script_path] + sys.argv[1:]
    
    # Execute the command
    subprocess.run(cmd)

if __name__ == "__main__":
    main() 