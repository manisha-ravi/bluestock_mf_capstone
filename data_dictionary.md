# Data Dictionary

## Table: fact_nav

### amfi_code

* Data Type: INTEGER
* Description: Unique mutual fund identifier assigned by AMFI.
* Source: 02_nav_history.csv

### date

* Data Type: DATE
* Description: NAV reporting date.
* Source: 02_nav_history.csv

### nav

* Data Type: REAL
* Description: Net Asset Value of the mutual fund on a specific date.
* Source: 02_nav_history.csv

## Table: fact_transactions

### investor_id

* Data Type: TEXT
* Description: Unique investor identifier.
* Source: 08_investor_transactions.csv

### transaction_date

* Data Type: DATE
* Description: Date of investment transaction.
* Source: 08_investor_transactions.csv

### amfi_code

* Data Type: INTEGER
* Description: Mutual fund identifier.
* Source: 08_investor_transactions.csv

### transaction_type

* Data Type: TEXT
* Description: Type of transaction (SIP, Lumpsum, Redemption).
* Source: 08_investor_transactions.csv

### amount_inr

* Data Type: REAL
* Description: Transaction amount in Indian Rupees.
* Source: 08_investor_transactions.csv

### kyc_status

* Data Type: TEXT
* Description: Investor KYC verification status.
* Source: 08_investor_transactions.csv

## Table: fact_performance

### amfi_code

* Data Type: INTEGER
* Description: Mutual fund identifier.
* Source: 07_scheme_performance.csv

### return_1yr_pct

* Data Type: REAL
* Description: One-year return percentage.
* Source: 07_scheme_performance.csv

### return_3yr_pct

* Data Type: REAL
* Description: Three-year return percentage.
* Source: 07_scheme_performance.csv

### return_5yr_pct

* Data Type: REAL
* Description: Five-year return percentage.
* Source: 07_scheme_performance.csv

### sharpe_ratio

* Data Type: REAL
* Description: Risk-adjusted return measure.
* Source: 07_scheme_performance.csv

### expense_ratio_pct

* Data Type: REAL
* Description: Annual fund expense ratio percentage.
* Source: 07_scheme_performance.csv
