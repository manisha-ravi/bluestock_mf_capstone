# Bluestock Fintech – Mutual Fund Analytics Platform

> **Capstone Project | Data Analytics Internship | June 2026**  
> Intern: Manisha Ravikumar | Company: Bluestock Fintech Pvt. Ltd.

End-to-End Data Engineering, ETL Pipeline & Interactive Dashboard for the Indian Mutual Fund Industry.

---

## 📊 Project Overview

This platform ingests publicly available mutual fund data from AMFI India and mfapi.in, transforms it through a Python/Pandas ETL pipeline, stores it in a normalised SQLite database, performs comprehensive EDA and risk analytics, and presents insights via a 4-page interactive Power BI dashboard.

| Metric | Value |
|--------|-------|
| Schemes covered | 40 real AMFI schemes |
| NAV history rows | ~46,000 (Jan 2022 – May 2026) |
| Investor transactions | ~32,000 rows |
| Industry AUM tracked | Rs. 81 Lakh Crore |
| SIP inflow ATH | Rs. 31,002 Crore (Dec 2025) |

---

## 🗂️ Repository Structure

```
bluestock_mf_capstone/
├── data/
│   ├── raw/                   ← Original CSV files + mfapi.in live NAV fetches
│   ├── processed/             ← 10 cleaned CSVs
│   └── db/                    ← bluestock_mf.db (SQLite) — add to .gitignore if > 100MB
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda_analysis.ipynb
│   ├── 04_performance_analytics.ipynb
│   └── 05_advanced_analytics.ipynb
├── scripts/
│   ├── etl_pipeline.py        ← Master ETL script (run this first)
│   ├── live_nav_fetch.py      ← Fetches live NAV from mfapi.in
│   ├── compute_metrics.py     ← Sharpe, Sortino, Alpha, Beta, VaR
│   └── recommender.py         ← Fund recommender by risk grade
├── sql/
│   ├── schema.sql             ← CREATE TABLE statements
│   └── queries.sql            ← 10 analytical SQL queries
├── dashboard/
│   └── bluestock_mf_dashboard.pbix   ← Power BI dashboard
├── reports/
│   ├── Final_Report.pdf
│   └── Bluestock_MF_Presentation.pptx
└── README.md
```

---

## ⚙️ Setup Instructions

### Prerequisites
- Python 3.10+
- Power BI Desktop (latest) for the dashboard
- Git

### 1. Clone the repository
```bash
git clone https://github.com/manisha-ravi/bluestock_mf_capstone.git
cd bluestock_mf_capstone
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

**requirements.txt contents:**
```
pandas>=2.0
numpy>=1.24
matplotlib>=3.7
seaborn>=0.12
plotly>=5.0
sqlalchemy>=2.0
scipy>=1.10
requests>=2.30
jupyter
```

### 3. Run the ETL pipeline
```bash
python scripts/etl_pipeline.py
```
This will:
- Load all 10 CSV datasets from `data/raw/`
- Clean and validate each dataset
- Create `bluestock_mf.db` in `data/db/`
- Load all tables into SQLite

### 4. Fetch live NAV data (optional)
```bash
python scripts/live_nav_fetch.py
```
Fetches current NAV for 5 selected schemes from `api.mfapi.in` and saves to `data/raw/`.

### 5. Run notebooks in order
Open Jupyter Lab and run notebooks `01` through `05` in sequence:
```bash
jupyter lab
```

### 6. Open the dashboard
- Open Power BI Desktop
- File → Open → `dashboard/bluestock_mf_dashboard.pbix`
- Refresh data connections if prompted

---

## 📁 Data Sources

| Source | URL | Data Type |
|--------|-----|-----------|
| AMFI India | amfiindia.com | NAV, AUM, Folio, SIP |
| mfapi.in | api.mfapi.in/mf/{code} | Historical NAV (JSON) |
| NSE India | nseindia.com/reports | Nifty 50/100 Index |
| BSE India | bseindia.com | BSE SmallCap Index |

> ⚠️ Add `*.db` to `.gitignore` to avoid uploading large database files. Upload `schema.sql` + `queries.sql` instead.

---

## 📈 Key Results

| Fund | 3yr CAGR | Sharpe | Alpha vs Nifty100 | Score/100 |
|------|----------|--------|-------------------|-----------|
| ICICI Pru Bluechip | 18.2% | 1.51 | +2.8% | 85 |
| SBI Bluechip | 17.8% | 1.42 | +2.1% | 82 |
| Mirae Asset Large Cap | 17.1% | 1.38 | +2.0% | 79 |

**Top EDA Finding:** SIP inflows grew 3× from Rs.11,000 Cr (Jan 2022) to Rs.31,002 Cr (Dec 2025). The 26–35 age group drives 38% of all investor transactions.

---

## 📋 Deliverables

| # | Deliverable | Weight | Status |
|---|-------------|--------|--------|
| D1 | ETL Pipeline Script | 15% | ✅ Complete |
| D2 | SQLite Database | 10% | ✅ Complete |
| D3 | EDA Notebook | 15% | ✅ Complete |
| D4 | Performance Metrics | 15% | ✅ Complete |
| D5 | Interactive Dashboard | 20% | ✅ Complete |
| D6 | Advanced Analytics | 10% | ✅ Complete |
| D7 | Final Report + Slides | 15% | ✅ Complete |

---

## ⚠️ Disclaimer

All data is sourced from publicly available information published by AMFI India, NSE, BSE and open APIs (mfapi.in). This project is for educational purposes only and does not constitute financial advice. Mutual Fund investments are subject to market risks.

---

## 👩‍💻 Author

**Manisha Ravikumar**  
Data Analytics Intern | Bluestock Fintech Pvt. Ltd.  
LinkedIn: [linkedin.com/in/manisha-ravikumar](https://linkedin.com/in/manisha-ravikumar)  
GitHub: [github.com/manisha-ravi](https://github.com/manisha-ravi)
