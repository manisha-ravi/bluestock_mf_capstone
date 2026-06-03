-- 1. Top 5 funds by AUM

SELECT *
FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;


-- 2. Average NAV

SELECT AVG(nav) AS average_nav
FROM fact_nav;


-- 3. Monthly Average NAV

SELECT
strftime('%Y-%m', date) AS month,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month;


-- 4. Transactions by Type

SELECT
transaction_type,
COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY transaction_type;


-- 5. Total Transaction Amount

SELECT
SUM(amount_inr) AS total_amount
FROM fact_transactions;


-- 6. Funds with Expense Ratio Below 1%

SELECT
amfi_code,
expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;


-- 7. Highest 1 Year Returns

SELECT
amfi_code,
return_1yr_pct
FROM fact_performance
ORDER BY return_1yr_pct DESC
LIMIT 5;


-- 8. Highest 3 Year Returns

SELECT
amfi_code,
return_3yr_pct
FROM fact_performance
ORDER BY return_3yr_pct DESC
LIMIT 5;


-- 9. Highest Sharpe Ratio

SELECT
amfi_code,
sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;


-- 10. Total Records in Each Table

SELECT COUNT(*) AS nav_records
FROM fact_nav;

SELECT COUNT(*) AS transaction_records
FROM fact_transactions;

SELECT COUNT(*) AS performance_records
FROM fact_performance;