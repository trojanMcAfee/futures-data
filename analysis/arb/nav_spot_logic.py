from __future__ import annotations
import os
import sys
from datetime import datetime
from typing import Optional, Dict

import databento as db
from dotenv import load_dotenv
from databento_dbn import FIXED_PRICE_SCALE

# Add the project root to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from main.construct_order_book import Market

from analysis.arb.nav_arb_simulation import NAVArbitrageSimulator
from analysis.arb.simulation_types import SimulationResults

class NAVSpotSimulation:
    def __init__(self, simulation_date: datetime, nav_price: float, initial_capital: float = 7_500_000, target_capital: Optional[float] = None):
        self.simulation_date = simulation_date
        self.nav_price = nav_price
        self.initial_capital = initial_capital
        self.target_capital = target_capital or initial_capital

    def run_simulation(self) -> SimulationResults:
        # Load environment variables
        load_dotenv()

        # Get the project root directory (3 levels up from this file)
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        
        # Construct the path to the order book data
        data_path = os.path.join(
            project_root,
            'data', 'uso', 'order-book',
            f"arcx-pillar-{self.simulation_date.strftime('%Y%m%d')}-full.mbo.dbn.zst"
        )

        print(f"\nUsing data from {data_path}\n")
        print("Processing order book and simulating NAV arbitrage...")
        print(f"Simulation date: {self.simulation_date.date()}")
        print(f"NAV Price: ${self.nav_price:.2f}\n")

        # Initialize market and simulator
        dbn_store = db.DBNStore.from_file(data_path)
        market = Market()
        simulator = NAVArbitrageSimulator(
            nav_price=self.nav_price,
            initial_capital=self.initial_capital,
            target_capital=self.target_capital
        )

        # Process messages and evaluate bids after market open
        total_messages = 0
        bids_evaluated = 0
        messages_after_open = 0

        # Convert market open time to nanoseconds since epoch
        market_open = int(datetime.strptime(
            f"{self.simulation_date.date()} 14:00:00",
            "%Y-%m-%d %H:%M:%S"
        ).timestamp() * 1e9)

        def process_message(msg):
            nonlocal total_messages, bids_evaluated, messages_after_open
            total_messages += 1
            
            # Check if it's after market open
            if msg.ts_recv >= market_open:
                messages_after_open += 1
                
                # Update the order book
                market.apply(msg)
                
                # Check for arbitrage opportunities on every message
                if msg.flags & db.RecordFlags.F_LAST:
                    # Get the best bid from the aggregated book
                    best_bid, _ = market.aggregated_bbo(msg.instrument_id)
                    
                    if best_bid:
                        bid_price = best_bid.price / FIXED_PRICE_SCALE
                        bid_size = best_bid.size
                        bids_evaluated += 1
                        
                        # Create a simulated quote message
                        class QuoteMsg:
                            def __init__(self, ts, bid_px, bid_sz):
                                self.ts = ts
                                self.bid_px = bid_px
                                self.bid_sz = bid_sz
                        
                        quote = QuoteMsg(
                            ts=datetime.fromtimestamp(msg.ts_recv / 1e9),
                            bid_px=bid_price,
                            bid_sz=bid_size
                        )
                        simulator.process_opportunity(quote)

        # Replay the messages
        dbn_store.replay(process_message)

        print(f"Processed {total_messages:,} total messages")
        print(f"Messages after market open: {messages_after_open:,}")
        print(f"Evaluated {bids_evaluated:,} bids after market open\n")

        return simulator.get_results() 