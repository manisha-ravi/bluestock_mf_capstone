import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")

# NAV Table
nav_df = pd.read_csv(
    "data/processed/clean_nav_history.csv"
)

nav_df.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

print("fact_nav loaded successfully!")

# Transactions Table
tx_df = pd.read_csv(
    "data/processed/clean_investor_transactions.csv"
)

tx_df.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

print("fact_transactions loaded successfully!")

# Performance Table
perf_df = pd.read_csv(
    "data/processed/clean_scheme_performance.csv"
)

perf_df.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print("fact_performance loaded successfully!")