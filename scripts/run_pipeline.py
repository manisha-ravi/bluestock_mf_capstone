"""
Master ETL Pipeline Runner
Runs the complete Bluestock Mutual Fund ETL workflow.
"""

import subprocess
import sys

scripts = [
    "scripts/data_ingestion.py",
    "scripts/data_cleaning.py",
    "scripts/create_database.py",
    "scripts/load_data.py"
]

for script in scripts:
    print(f"\nRunning {script}...")
    subprocess.run([sys.executable, script], check=True)

print("\nETL Pipeline Completed Successfully!")