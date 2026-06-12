import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")

datasets = {
    "dim_fund": "data/processed/clean_fund_master.csv",
    "fact_nav": "data/processed/clean_nav_history.csv",
    "fact_aum": "data/processed/clean_aum_by_fund_house.csv",
    "fact_sip_inflows": "data/processed/clean_monthly_sip_inflows.csv",
    "fact_category_inflows": "data/processed/clean_category_inflows.csv",
    "fact_folio_count": "data/processed/clean_industry_folio_count.csv",
    "fact_performance": "data/processed/clean_scheme_performance.csv",
    "fact_transactions": "data/processed/clean_investor_transactions.csv",
    "fact_portfolio": "data/processed/clean_portfolio_holdings.csv",
    "fact_benchmark": "data/processed/clean_benchmark_indices.csv"
}

for table_name, file_path in datasets.items():

    print(f"\nLoading {table_name}...")

    df = pd.read_csv(file_path)

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"{table_name} loaded successfully!")
    print(f"Rows: {len(df)}")

print("\nAll datasets loaded successfully!")