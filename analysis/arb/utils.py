from __future__ import annotations
import os
import json
from datetime import datetime, timedelta, timezone
from typing import Tuple

def get_nav_price_for_date(nav_data: dict, target_date: datetime) -> float:
    """Get the NAV price for the day before the target date."""
    # Get previous business day's date
    prev_date = target_date - timedelta(days=1)
    while prev_date.weekday() > 4:  # Skip weekends
        prev_date = prev_date - timedelta(days=1)
    
    # Format date string as it appears in the JSON
    date_str = prev_date.strftime("%-m/%-d/%Y")
    
    # Find the price in the correct month
    month = prev_date.strftime("%B")
    month_data = nav_data.get(month, [])
    
    for entry in month_data:
        if entry["date"] == date_str:
            return float(entry["price"])
            
    raise ValueError(f"No NAV price found for date {date_str}")

def get_order_book_path(date: datetime) -> str:
    """Generate the path for the order book data file."""
    return f"data/uso/order-book/arcx-pillar-{date.strftime('%Y%m%d')}-full.mbo.dbn.zst"

def get_market_hours(date: datetime) -> Tuple[datetime, datetime]:
    """Get market open and close times (EST) for a given date."""
    # Convert date to UTC (market opens at 9:30 AM EST / 14:30 UTC)
    market_open = datetime(
        date.year, date.month, date.day, 
        14, 30, 0, 
        tzinfo=timezone.utc
    )
    market_close = datetime(
        date.year, date.month, date.day,
        20, 0, 0,  # 4:00 PM EST / 20:00 UTC
        tzinfo=timezone.utc
    )
    return market_open, market_close

def load_nav_data() -> dict:
    """Load the NAV prices from the JSON file."""
    nav_file_path = os.path.join(
        os.path.dirname(__file__), 
        '..', '..', 
        'data/uso/nav_prices.json'
    )
    with open(nav_file_path, 'r') as f:
        return json.load(f) 