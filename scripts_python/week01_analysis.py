import pandas as pd
import numpy as np
import sqlite3
from pathlib import Path

RAW = Path("./data/app_metrics.csv")
DB = Path("./data/app_metrics.db")

def load_data(filepath, dtypes=None):
    df = pd.read_csv(filepath, dtype=dtypes)
    print("✅ Data loaded")
    return df

df = load_data(RAW) 


avg_minutes_pandas = df["minutes_per_user"].mean()
print(avg_minutes_pandas)
var_active_users_pandas = df["active_users"].var()
print(var_active_users_pandas)
std_active_users_pandas = df["active_users"].std()
print(std_active_users_pandas)

std_minutes_pandas = df["minutes_per_user"].std()
print(std_minutes_pandas)