import pandas as pd

# Load datasets
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

# Unique AMFI codes
fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

# Missing codes
missing_codes = fund_codes - nav_codes

print("Fund Master Codes:", len(fund_codes))
print("NAV History Codes:", len(nav_codes))
print("Missing Codes:", len(missing_codes))

if len(missing_codes) == 0:
    print("\nAll AMFI codes are present in NAV history")
else:
    print("\nMissing AMFI Codes:")
    print(missing_codes)