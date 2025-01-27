#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main.roll_analysis_logic import analyze_month_rolls

if __name__ == "__main__":
    analyze_month_rolls("March", 3) 