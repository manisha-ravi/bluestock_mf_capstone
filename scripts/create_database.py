import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")

test_df = pd.DataFrame({
    "id": [1],
    "name": ["test"]
})

test_df.to_sql(
    "test_table",
    engine,
    if_exists="replace",
    index=False
)

print("Database and test table created successfully!")