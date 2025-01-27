#!/usr/bin/env python3

from datetime import datetime
import pandas as pd

# 2024 CL Futures Calendar
data = {
    'Contract': [
        'CLG24 (February 2024)',
        'CLH24 (March 2024)',
        'CLJ24 (April 2024)',
        'CLK24 (May 2024)',
        'CLM24 (June 2024)',
        'CLN24 (July 2024)',
        'CLQ24 (August 2024)',
        'CLU24 (September 2024)',
        'CLV24 (October 2024)',
        'CLX24 (November 2024)',
        'CLZ24 (December 2024)',
        'CLF25 (January 2025)'
    ],
    'Last Trading Day': [
        'January 22, 2024',
        'February 20, 2024',
        'March 20, 2024',
        'April 22, 2024',
        'May 21, 2024',
        'June 20, 2024',
        'July 22, 2024',
        'August 20, 2024',
        'September 20, 2024',
        'October 22, 2024',
        'November 20, 2024',
        'December 20, 2024'
    ],
    'Typical Roll Period Starts': [
        'January 8-12, 2024',
        'February 6-9, 2024',
        'March 6-8, 2024',
        'April 8-12, 2024',
        'May 7-10, 2024',
        'June 6-10, 2024',
        'July 8-12, 2024',
        'August 6-9, 2024',
        'September 6-10, 2024',
        'October 8-11, 2024',
        'November 6-8, 2024',
        'December 6-10, 2024'
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display settings
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

print("\nCME Crude Oil (CL) Futures 2024 Calendar")
print("----------------------------------------")
print(df)

print("\nKey Points:")
print("1. Contracts expire around the 20th of the month before delivery")
print("2. Roll period typically starts 10-14 days before expiration")
print("3. Most volume shifts to the next contract during roll period")
print("4. The 'front month' (CL.n.0) refers to the nearest expiring contract")
print("5. Contract symbols use letters: F(Jan) G(Feb) H(Mar) J(Apr) K(May) M(Jun)")
print("                                 N(Jul) Q(Aug) U(Sep) V(Oct) X(Nov) Z(Dec)") 