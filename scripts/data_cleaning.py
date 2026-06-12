# import pandas as pd

# print("Day 2 Data Cleaning Started")

# # ---------------Load dataset
# nav_df = pd.read_csv("data/raw/02_nav_history.csv")

# print("\nOriginal Shape:")
# print(nav_df.shape)

# # Convert date column
# nav_df["date"] = pd.to_datetime(nav_df["date"])

# print("\nDate converted successfully")

# # Sort values
# nav_df = nav_df.sort_values(
#     by=["amfi_code", "date"]
# )

# print("Data sorted")

# # Remove duplicates
# before = len(nav_df)

# nav_df = nav_df.drop_duplicates()

# after = len(nav_df)

# print("\nDuplicates Removed:")
# print(before - after)

# # Check missing values
# print("\nMissing Values:")
# print(nav_df.isnull().sum())

# # Forward fill NAV values if any missing

# nav_df["nav"] = nav_df["nav"].ffill()

# print("\nForward Fill Applied")

# # Check for invalid NAV values

# invalid_nav = nav_df[nav_df["nav"] <= 0]

# print("\nInvalid NAV Records:")
# print(len(invalid_nav))

# # Save cleaned dataset

# nav_df.to_csv(
#     "data/processed/clean_nav_history.csv",
#     index=False
# )

# print("\nClean NAV file saved successfully!")
# #----------------------

# import pandas as pd

# tx_df = pd.read_csv(
#     "data/raw/08_investor_transactions.csv"
# )

# tx_df.to_csv(
#     "data/processed/clean_investor_transactions.csv",
#     index=False
# )

# print("Clean transactions file saved!")
# # Convert transaction date

# tx_df["transaction_date"] = pd.to_datetime(
#     tx_df["transaction_date"]
# )

# print("\nDate conversion successful")

# # Check missing values

# print("\nMissing Values:")
# print(tx_df.isnull().sum())

# # Check duplicate rows

# duplicates = tx_df.duplicated().sum()

# print("\nDuplicate Rows:")
# print(duplicates)

# # Remove duplicates

# tx_df = tx_df.drop_duplicates()

# # Validate amount > 0

# invalid_amounts = tx_df[
#     tx_df["amount_inr"] <= 0
# ]

# print("\nInvalid Amount Records:")
# print(len(invalid_amounts))

# # Validate KYC values

# valid_kyc = ["Verified", "Pending"]

# invalid_kyc = tx_df[
#     ~tx_df["kyc_status"].isin(valid_kyc)
# ]

# print("\nInvalid KYC Records:")
# print(len(invalid_kyc))

# print("\nDataset Shape:")
# print(tx_df.shape)

# print("\nFirst 5 Rows:")
# print(tx_df.head())

# print("\nColumns:")
# print(tx_df.columns)

# print("\nTransaction Types:")
# print(tx_df["transaction_type"].unique())

# print("\nKYC Status:")
# print(tx_df["kyc_status"].unique())

# import pandas as pd

# perf_df = pd.read_csv(
#     "data/raw/07_scheme_performance.csv"
# )

# print("Dataset Shape:")
# print(perf_df.shape)

# # Convert return columns to numeric

# return_cols = [
#     "return_1yr_pct",
#     "return_3yr_pct",
#     "return_5yr_pct",
#     "benchmark_3yr_pct",
#     "alpha",
#     "beta",
#     "sharpe_ratio",
#     "sortino_ratio",
#     "std_dev_ann_pct",
#     "max_drawdown_pct",
#     "expense_ratio_pct"
# ]

# for col in return_cols:
#     perf_df[col] = pd.to_numeric(
#         perf_df[col],
#         errors="coerce"
#     )

# print("\nNumeric conversion completed")

# # Check missing values

# print("\nMissing Values:")
# print(perf_df.isnull().sum())

# # Negative Sharpe Ratios

# negative_sharpe = perf_df[
#     perf_df["sharpe_ratio"] < 0
# ]

# print("\nNegative Sharpe Ratios:")
# print(len(negative_sharpe))

# # Expense Ratio Validation

# invalid_expense = perf_df[
#     (perf_df["expense_ratio_pct"] < 0.1)
#     |
#     (perf_df["expense_ratio_pct"] > 2.5)
# ]

# print("\nInvalid Expense Ratios:")
# print(len(invalid_expense))

# # Remove duplicates

# perf_df = perf_df.drop_duplicates()

# # Save cleaned file

# perf_df.to_csv(
#     "data/processed/clean_scheme_performance.csv",
#     index=False
# )

# print("\nClean performance file saved!")

import pandas as pd

files = {
    "01_fund_master.csv": "clean_fund_master.csv",
    "03_aum_by_fund_house.csv": "clean_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv": "clean_monthly_sip_inflows.csv",
    "05_category_inflows.csv": "clean_category_inflows.csv",
    "06_industry_folio_count.csv": "clean_industry_folio_count.csv",
    "09_portfolio_holdings.csv": "clean_portfolio_holdings.csv",
    "10_benchmark_indices.csv": "clean_benchmark_indices.csv"
}

for raw_file, clean_file in files.items():

    df = pd.read_csv(f"data/raw/{raw_file}")

    print(f"\nProcessing: {raw_file}")

    print("Original Rows:", len(df))

    # Remove duplicate rows
    df = df.drop_duplicates()

    print("Rows After Cleaning:", len(df))

    # Save cleaned file
    df.to_csv(
        f"data/processed/{clean_file}",
        index=False
    )

    print(f"Saved: {clean_file}")

print("\nAll remaining datasets cleaned successfully!")