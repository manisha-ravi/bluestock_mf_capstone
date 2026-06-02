import pandas as pd
import glob
files=glob.glob("data/raw/*.csv")
print(f"Found {len(files)} CSV files")
for file in files:
    print("\n"+ "=" *60)
    print("FILE:", file)
    df= pd.read_csv(file)

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 rows:")
    print(df.head())

    print("\nMissing values:")
    print(df.isnull().sum())

# ==================================
# DATA QUALITY SUMMARY
# ==================================

# 01_fund_master.csv
# No anomalies found.

# 02_nav_history.csv
# No anomalies found.

# 03_aum_by_fund_house.csv
# No anomalies found.

# 04_monthly_sip_inflows.csv
# yoy_growth_pct contains 12 missing values.
# Likely expected because YoY growth cannot be calculated for initial periods.

# 05_category_inflows.csv
# No anomalies found.

# 06_industry_folio_count.csv
# No anomalies found.

# 07_scheme_performance.csv
# No anomalies found.

# 08_investor_transactions.csv
# No anomalies found.

# 09_portfolio_holdings.csv
# No anomalies found.

# 10_benchmark_indices.csv
# No anomalies found. 
