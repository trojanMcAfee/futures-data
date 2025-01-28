import json
import pandas as pd
from pathlib import Path

def load_data(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def get_futures_data(data_path=None):
    if data_path is None:
        # Get the path relative to this script's location
        script_dir = Path(__file__).resolve().parent.parent
        futures_data_path = script_dir / "data" / "output.json"
    else:
        futures_data_path = Path(data_path)
    
    if not futures_data_path.exists():
        print("Error: output.json not found.")
        return None
    
    data = load_data(futures_data_path)
    df = pd.DataFrame(data)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['date'] = df['timestamp'].dt.strftime('%Y-%m-%d')
    
    pivot_df = df.pivot(index='date', columns='symbol', 
                       values=['volume', 'close'])
    pivot_df.columns = [f"{col[0]}_{col[1]}" for col in pivot_df.columns]
    pivot_df = pivot_df.sort_index()
    pivot_df.index = pd.to_datetime(pivot_df.index)
    
    # Group by month to handle contract rolls properly
    monthly_groups = pivot_df.groupby(pivot_df.index.strftime('%Y-%m'))
    
    futures_data = []
    
    for month, month_data in monthly_groups:
        current_contract = 'front'  # Reset contract at start of each month
        roll_happened = False
        
        for date, row in month_data.iterrows():
            if pd.isna(row['volume_CL.n.0']) or pd.isna(row['volume_CL.n.1']):
                continue
            
            # Check for roll condition
            roll_event = False
            if not roll_happened and current_contract == 'front':
                if row['volume_CL.n.1'] > row['volume_CL.n.0']:
                    roll_event = True
                    roll_happened = True
                    current_contract = 'next'
            
            price = row['close_CL.n.0'] if current_contract == 'front' else row['close_CL.n.1']
            volume_front = row['volume_CL.n.0']
            volume_next = row['volume_CL.n.1']
            
            futures_data.append({
                'date': date,
                'price': price,
                'volume_front': volume_front,
                'volume_next': volume_next,
                'roll_event': roll_event
            })
    
    df_futures = pd.DataFrame(futures_data)
    if not df_futures.empty:
        df_futures = df_futures.sort_values('date')
        df_futures['daily_change'] = df_futures['price'].pct_change() * 100
    
    return df_futures 