import pandas as pd
df= pd.read_csv("data/raw/01_fund_master.csv")
print(df.columns)
print("shape:")
print(df.shape)

print("\nFund Houses:")
print(df["fund_house"].unique())

print("\nCount:")
print(df["fund_house"].nunique())

print("\nCategories:")
print(df["category"].unique())

print("\nSubcategories:")
print(df["sub_category"].unique())

print("\nRisk categories:")
print(df["risk_category"].unique())

print("\nAMFI codes:")
print(df["amfi_code"].head())
