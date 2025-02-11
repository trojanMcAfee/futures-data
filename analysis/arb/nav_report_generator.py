from __future__ import annotations
from analysis.arb.simulation_types import SimulationResults

def generate_report(results: SimulationResults) -> None:
    """Generate a report from the simulation results."""
    print("\n=== NAV Arbitrage Simulation Results ===")
    print(f"Start Time: {results.start_time}")
    print(f"End Time: {results.end_time}")
    print(f"Total Investment: ${results.total_investment:,.2f}")
    print(f"Total Profit: ${results.total_profit:,.2f}")
    
    # Calculate ROI only if there was any investment
    if results.total_investment > 0:
        roi = (results.total_profit / results.total_investment * 100)
        print(f"Overall ROI: {roi:.2f}%")
    else:
        print("Overall ROI: N/A (no trades executed)")
    
    print(f"Number of Trades: {len(results.trades):,}")
    
    if results.trades:
        print("\nTrade Details:")
        for trade in results.trades[:5]:  # Show first 5 trades
            print(f"  {trade.timestamp}: {trade.shares:,} shares @ ${trade.bid_price:.2f} (NAV: ${trade.nav_price:.2f})")
        
        if len(results.trades) > 5:
            print("  ...")
            for trade in results.trades[-5:]:  # Show last 5 trades
                print(f"  {trade.timestamp}: {trade.shares:,} shares @ ${trade.bid_price:.2f} (NAV: ${trade.nav_price:.2f})")
    else:
        print("\nNo trades were executed during this simulation.") 