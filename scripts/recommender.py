from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]

perf = pd.read_csv(
    BASE_DIR / "data" / "processed" / "clean_scheme_performance.csv"
)

risk = input("Enter Risk Appetite (Low/Moderate/High): ")

funds = perf[
    perf["risk_grade"]
    .str.lower()
    .str.contains(risk.lower())
]

top3 = funds.sort_values(
    "sharpe_ratio",
    ascending=False
).head(3)

print(top3[
    [
        "scheme_name",
        "risk_grade",
        "sharpe_ratio",
        "return_3yr_pct"
    ]
])