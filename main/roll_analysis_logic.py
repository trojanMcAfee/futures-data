#!/usr/bin/env python3

import json
import pandas as pd
from datetime import datetime

def analyze_month_rolls(month_name, month_number, data_path='data/output.json', verbose=True):
    """Core analysis logic for both traditional and alternative rolling strategies.
    
    Args:
        month_name (str): Name of the month to analyze
        month_number (int): Number of the month (1-12)
        data_path (str): Path to the data file
        verbose (bool): If True, prints detailed analysis. If False, prints only summary.
    """
    
    # Position parameters
    CONTRACTS = 100
    BARRELS_PER_CONTRACT = 1000
    
    # Read and prepare data
    with open(data_path, 'r') as f:
        data = json.load(f)
    
    df = pd.DataFrame(data)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['date'] = df['timestamp'].dt.strftime('%Y-%m-%d')
    
    # Create pivot table
    pivot_df = df.pivot(index='date', columns='symbol', 
                        values=['volume', 'close'])
    pivot_df.columns = [f"{col[0]}_{col[1]}" for col in pivot_df.columns]
    
    # Get month data
    month_data = pivot_df[pivot_df.index.str.startswith(f'2024-{str(month_number).zfill(2)}')]
    
    results = {
        'daily_data': [],
        'backwardation_days': [],
        'traditional_roll': None,
        'alternative_strategy': None
    }
    
    # Part 1: Traditional Roll Analysis
    if verbose:
        print(f"\nPart 1: {month_name} 2024 Traditional Roll Analysis")
        print("=" * (len(month_name) + 31))
        print("                     Volume                    Close")
        print("Date           CL.n.0      CL.n.1      CL.n.0   CL.n.1   Spread   Structure")
        print("-" * 85)
    
    for idx, row in month_data.iterrows():
        spread = row['close_CL.n.1'] - row['close_CL.n.0']
        structure = "Backwardation" if spread < 0 else "Contango"
        
        daily_data = {
            'date': idx,
            'spread': spread,
            'structure': structure,
            'close_n0': row['close_CL.n.0'],
            'close_n1': row['close_CL.n.1']
        }
        results['daily_data'].append(daily_data)
        
        if spread < 0:
            results['backwardation_days'].append((idx, spread, row))
        
        if verbose:
            print(f"{idx}  {int(row['volume_CL.n.0']):9,d}  {int(row['volume_CL.n.1']):9,d}  "
                  f"  {row['close_CL.n.0']:6.2f}  {row['close_CL.n.1']:6.2f}  {spread:6.2f}   {structure}")
    
    # Traditional Roll Analysis
    roll_period = month_data[(month_data['volume_CL.n.1'] > month_data['volume_CL.n.0'])]
    if not roll_period.empty:
        roll_day = roll_period.index[0]
        sell_price = roll_period.loc[roll_day, 'close_CL.n.0']
        buy_price = roll_period.loc[roll_day, 'close_CL.n.1']
        
        sell_value = CONTRACTS * BARRELS_PER_CONTRACT * sell_price
        buy_value = CONTRACTS * BARRELS_PER_CONTRACT * buy_price
        roll_pnl = sell_value - buy_value
        
        results['traditional_roll'] = {
            'date': roll_day,
            'sell_price': sell_price,
            'buy_price': buy_price,
            'pnl': roll_pnl,
            'structure': "Backwardation" if (buy_price - sell_price) < 0 else "Contango"
        }
        
        if verbose:
            print("\nTraditional Roll Analysis")
            print("========================")
            print(f"Roll Date: {roll_day}")
            print(f"Selling {CONTRACTS:,d} contracts at ${sell_price:.2f} = ${sell_value:,.2f}")
            print(f"Buying {CONTRACTS:,d} contracts at ${buy_price:.2f} = ${buy_value:,.2f}")
            print(f"Roll P&L: ${roll_pnl:,.2f}")
            print(f"Market Structure: {results['traditional_roll']['structure']}")
    
    # Part 2: Alternative Rolling Strategy
    if verbose:
        print("\n\nPart 2: Alternative Rolling Strategy (Backwardation-based)")
        print("====================================================")
    
    # Filter days until the 19th
    backwardation_days = [(d, s, r) for d, s, r in results['backwardation_days'] 
                          if datetime.strptime(d, '%Y-%m-%d').day <= 19]
    
    if backwardation_days:
        contracts_per_day = CONTRACTS / len(backwardation_days)
        contracts_per_day = round(contracts_per_day)
        remaining_contracts = CONTRACTS
        
        # Initialize position value based on the current price of CL.n.0
        position_value = CONTRACTS * BARRELS_PER_CONTRACT * month_data.iloc[0]['close_CL.n.0']
        
        if verbose:
            print("\nRolling Schedule:")
            print("================")
        
        alternative_rolls = []
        
        for i, (day, spread, row) in enumerate(backwardation_days):
            if i == len(backwardation_days) - 1:
                contracts_to_roll = remaining_contracts
            else:
                contracts_to_roll = min(contracts_per_day, remaining_contracts)
            
            if contracts_to_roll > 0:
                sell_price = row['close_CL.n.0']
                buy_price = row['close_CL.n.1']
                
                # Calculate the change in position value from this mini-roll
                contracts_not_rolled = CONTRACTS - contracts_to_roll
                position_value = (contracts_not_rolled * BARRELS_PER_CONTRACT * sell_price +  # Value of non-rolled contracts
                                contracts_to_roll * BARRELS_PER_CONTRACT * buy_price)         # Value of rolled contracts
                
                alternative_rolls.append({
                    'date': day,
                    'contracts': contracts_to_roll,
                    'sell_price': sell_price,
                    'buy_price': buy_price,
                    'position_value': position_value,
                    'spread': spread
                })
                
                if verbose:
                    print(f"\nDate: {day}")
                    print(f"Rolling {contracts_to_roll:,d} contracts")
                    print(f"Selling at ${sell_price:.2f}")
                    print(f"Buying at ${buy_price:.2f}")
                    print(f"New Position Value: ${position_value:,.2f}")
                    print(f"Spread: ${spread:.2f}")
                
                remaining_contracts -= contracts_to_roll
        
        results['alternative_strategy'] = {
            'rolls': alternative_rolls,
            'final_position_value': position_value,
            'initial_price': month_data.iloc[0]['close_CL.n.0'],  # Initial price at start of month
            'final_price': alternative_rolls[-1]['buy_price'] if alternative_rolls else None  # Final price after last roll
        }
        
        if verbose:
            print("\nAlternative Strategy Summary")
            print("==========================")
        print(f"Position Value for {month_name}: ${position_value:,.2f}")
        
        if results['traditional_roll'] and verbose:
            trad_value = CONTRACTS * BARRELS_PER_CONTRACT * results['traditional_roll']['buy_price']
            print(f"\nComparison with Traditional Roll:")
            print(f"Traditional Position Value: ${trad_value:,.2f}")
            print(f"Alternative Position Value: ${position_value:,.2f}")
            print(f"Difference: ${position_value - trad_value:,.2f}")
            print(f"Value Difference: {((position_value - trad_value) / trad_value * 100):.2f}%")
    else:
        if verbose:
            print("\nNo backwardation days found before the 19th. Strategy could not be executed.")
        results['alternative_strategy'] = None
    
    return results 