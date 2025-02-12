from __future__ import annotations
import os
import json

def load_nav_data() -> dict:
    """Load the NAV prices from the JSON file."""
    nav_file_path = os.path.join(
        os.path.dirname(__file__), 
        '..', '..', 
        'data/uso/nav_prices.json'
    )
    with open(nav_file_path, 'r') as f:
        return json.load(f) 