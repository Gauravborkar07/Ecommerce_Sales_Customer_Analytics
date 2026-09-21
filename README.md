# E-Commerce Sales Performance and Customer Behavior Analysis Using Data Analytics and AI

> An internship data analytics project that applies exploratory data analysis, KPI computation,
> customer behaviour analysis, RFM segmentation, and an AI-assisted insight framework to an
> e-commerce transactional dataset.
>
> **Internship:** AICTE | IBM SkillsBuild Data Analytics with AI Internship 2026
> **Organization:** BharatCares

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Problem Statement](#problem-statement)
3. [Project Objectives](#project-objectives)
4. [Project Goals](#project-goals)
5. [Dataset Details](#dataset-details)
6. [Tools and Technologies](#tools-and-technologies)
7. [Methodology / Workflow](#methodology--workflow)
8. [Exploratory Data Analysis](#exploratory-data-analysis)
9. [Key Findings](#key-findings)
10. [Business Insights and Recommendations](#business-insights-and-recommendations)
11. [Setup Instructions](#setup-instructions)
12. [How to Run the Notebook](#how-to-run-the-notebook)
13. [How to Run the Dashboard](#how-to-run-the-dashboard)
14. [Project Folder Structure](#project-folder-structure)
15. [Chart References](#chart-references)
16. [Conclusion](#conclusion)
17. [Limitations and Future Scope](#limitations-and-future-scope)
18. [Author](#author)
19. [GitHub Repository](#github-repository)

---

## Project Overview

This project performs a comprehensive data analytics study on an e-commerce transactional
dataset covering **15 months** of customer orders (January 2023 – March 2024).

The analysis spans:
- Sales performance measurement across time, geography, and product category
- Customer behaviour profiling using demographics, session, and device data
- RFM (Recency, Frequency, Monetary) customer segmentation
- Delivery performance and customer satisfaction evaluation
- Discount impact and penetration analysis
- An AI-assisted insight framework converting findings into business actions
- An interactive Streamlit dashboard for business stakeholders

All findings and recommendations are derived exclusively from calculations on the actual dataset.
No results are invented or assumed prior to analysis.

---

## Problem Statement

E-commerce businesses generate large volumes of transactional data yet often lack a structured
analytical framework to answer critical questions:

- Which product categories and cities drive the most revenue?
- What distinguishes high-value customers from low-value ones?
- How does delivery time relate to customer satisfaction?
- Which customers are at risk of disengaging?
- Where should discounting strategy be focused?

This project builds that analytical framework from the ground up, ending with a set of
data-grounded, actionable business recommendations.

---

## Project Objectives

| # | Objective |
|---|---|
| O1 | Measure and track core sales KPIs across time, geography, and product category |
| O2 | Analyse customer behaviour using session, device, payment, and demographic data |
| O3 | Evaluate delivery performance and its relationship with customer satisfaction |
| O4 | Identify discount usage patterns and their relationship with order value |
| O5 | Segment customers by value and purchase behaviour using RFM analysis |
| O6 | Build an AI-assisted insight framework (Fact -> Insight -> Risk/Opportunity -> Action) |
| O7 | Deliver an interactive Streamlit dashboard for business stakeholders |
| O8 | Produce a structured internship project report in `.docx` format |

---

## Project Goals

- Produce a clean, reproducible Jupyter notebook covering the full analytics lifecycle
- Compute 15+ business KPIs directly from the dataset
- Generate 55+ charts and visualisations saved to `assets/`
- Build a rule-based RFM customer segmentation model (descriptive, not predictive)
- Identify satisfaction-risk orders and suggest actionable logistics improvements
- Deliver a Streamlit dashboard with 8 interactive tabs and 7 sidebar filters
- Submit a professional `.docx` project report with embedded charts and computed KPI tables

---

## Dataset Details

| Attribute | Detail |
|---|---|
| **File name** | `ecommerce_customer_behavior_dataset_v2.csv` |
| **Format** | CSV (comma-separated values) |
| **Records** | 17,049 rows |
| **Columns** | 18 columns |
| **Unique Customers** | 5,000 |
| **Unique Orders** | 17,049 |
| **Date Range** | January 1, 2023 – March 25, 2024 (~15 months) |
| **Missing Values** | None |
| **Duplicate Rows** | None |
| **Dataset Source** | Dataset source link: To be added. |

### Important Columns

| Column | Type | Description |
|---|---|---|
| `Order_ID` | string | Unique order identifier |
| `Customer_ID` | string | Unique customer identifier |
| `Date` | datetime | Order date |
| `Age` | integer | Customer age (18–75) |
| `Gender` | string | Female / Male / Other |
| `City` | string | 10 cities |
| `Product_Category` | string | 8 product categories |
| `Unit_Price` | float | Price per unit |
| `Quantity` | integer | Units ordered (1–5) |
| `Discount_Amount` | float | Discount applied |
| `Total_Amount` | float | Derived: (Unit_Price × Quantity) − Discount_Amount |
| `Payment_Method` | string | 5 payment methods |
| `Device_Type` | string | Mobile / Desktop / Tablet |
| `Session_Duration_Minutes` | integer | Session length on site (4–26 min) |
| `Pages_Viewed` | integer | Pages visited per session (1–18) |
| `Is_Returning_Customer` | boolean | True = returning customer |
| `Delivery_Time_Days` | integer | Days from order to delivery (1–25) |
| `Customer_Rating` | integer | Post-delivery rating (1–5) |

### Dataset Purpose

Used strictly for educational and internship analytics purposes.
No personally identifiable information is present.

### Dataset Access

> **Google Drive Download Link:**
> [https://drive.google.com/file/d/1xx3co8Mo7EDAGTvhiVA8CkgJ_vOmPfsI/view?usp=sharing](https://drive.google.com/file/d/1xx3co8Mo7EDAGTvhiVA8CkgJ_vOmPfsI/view?usp=sharing)
>
> If the above link is unavailable, the dataset file is included in this repository as:
> `ecommerce_customer_behavior_dataset_v2.csv`

---

## Tools and Technologies

| Tool / Library | Version | Purpose |
|---|---|---|
| Python | 3.10 / 3.11 | Core programming language |
| `pandas` | 2.2.2 | Data loading, manipulation, aggregation |
| `numpy` | 1.26.4 | Numerical operations |
| `matplotlib` | 3.8.4 | Base plotting and chart export |
| `seaborn` | 0.13.2 | Statistical visualisations |
| `plotly` | 5.22.0 | Interactive dashboard charts |
| `streamlit` | 1.35.0 | Interactive web dashboard |
| `scipy` | 1.13.0 | Pearson correlation and statistical tests |
| `python-docx` | 1.1.2 | `.docx` report generation |
| `openpyxl` | 3.1.2 | Excel export |
| `nbformat` | 5.10.4 | Jupyter notebook format |
| `ipykernel` | 6.29.4 | Jupyter kernel |
| Jupyter Notebook | — | Interactive analysis environment |

---

## Methodology / Workflow

```
1. Data Loading and Inspection
        |
2. Data Cleaning and Type Conversion
        |
3. Feature Engineering (11 derived features)
        |
4. Data Validation (15 assertion checks)
        |
5. KPI Computation (15 KPIs)
        |
6. Exploratory Data Analysis
   - Univariate Analysis
   - Bivariate Analysis
   - Multivariate Analysis
        |
7. Time-Series and Sales Trend Analysis
        |
8. Customer Behaviour Analysis
        |
9. RFM Customer Segmentation
        |
10. Delivery, Satisfaction and Discount Analysis
        |
11. AI-Assisted Insight Framework
        |
12. Streamlit Dashboard
        |
13. Project Report (.docx)
```

---

## Exploratory Data Analysis

The EDA is structured across three sub-sections in the notebook:

**Univariate Analysis (Section 3)**
- Distribution analysis for all 9 numerical variables with histograms, KDE plots, and boxplots
- Count distributions for all 5 categorical variables
- Key findings: `Total_Amount` and `Unit_Price` are heavily right-skewed (skew > 3.5); `Quantity` is uniformly distributed 1–5; 62% of orders have zero discount

**Bivariate / Multivariate Analysis (Section 4)**
- Pearson correlation heatmap across all numerical variables
- Scatter plots: `Total_Amount` vs `Unit_Price` (r=+0.87), `Session_Duration` (r=-0.009), `Pages_Viewed` (r=+0.009)
- Grouped bar charts: revenue by category × gender, device, payment method
- Delivery time vs customer rating analysis

**Time-Series Analysis (Section 5)**
- Monthly revenue trend, order count, AOV, and MoM growth across 15 months
- Quarterly comparison and yearly summary (2023 full, 2024 partial)
- Category-wise monthly revenue trends
- Returning vs new customer revenue over time

> **Correlation note:** All correlation findings are associations only — causation cannot be established.

---

## Key Findings

All findings below are computed directly from the dataset:

1. **Total Revenue:** 21,779,052.59 across 17,049 orders in 15 months
2. **Average Order Value (AOV):** 1,277.44 per order
3. **Returning customers:** 88.2% of orders and 88.1% of total revenue come from returning customers
4. **Top revenue category:** Electronics (10,481,898 — 48.1% of total revenue) despite ranking 6th in order count
5. **Top city by revenue:** Istanbul (5,646,596 — 25.9% of total revenue)
6. **Mobile dominance:** 56.0% of orders placed via Mobile; Desktop has the highest AOV (1,310.77)
7. **Discount penetration:** 38.0% of orders include a discount; AOV without discount (1,338) > with discount (1,178)
8. **Delivery:** Average delivery = 6.50 days; 13.2% of orders take >10 days
9. **Customer rating:** Average 3.90/5; 13.3% of orders rated 1 or 2 (low satisfaction)
10. **Satisfaction risk:** 316 orders (1.85%) combine delivery >10 days AND rating ≤2 — Istanbul (83), Ankara (47), Izmir (37) top the list
11. **RFM segments:** Champions (640, 12.8%) and Loyal Customers (966, 19.3%) account for 54.2% of total revenue; At-Risk customers = 778 (15.6%)
12. **Session behaviour:** Near-zero correlation between session duration / pages viewed and order value suggests session metrics alone do not predict spend

---

## Business Insights and Recommendations

> All recommendations are based on computed dataset results.
> They are analytical suggestions — not guaranteed outcomes.

| Tier | Area | Recommendation |
|---|---|---|
| 1 | Revenue Growth | Focus on Electronics and Istanbul — they contribute the highest revenue share. Investigate peak months (Jul, Dec 2023) for campaign timing. |
| 2 | Customer Retention | 88.2% returning customer rate is high. Build a formal loyalty programme for Champions and Loyal RFM segments to protect this advantage. |
| 3 | At-Risk Re-engagement | 778 At-Risk customers have not ordered recently despite past frequency. Run targeted win-back campaigns with personalised category offers. |
| 4 | Logistics Improvement | Istanbul, Ankara, and Izmir have the highest concentration of satisfaction-risk orders. Audit last-mile delivery partners in these cities. |
| 5 | Discounting Strategy | 38% discount penetration with no evidence of AOV uplift. Avoid blanket discounting; test targeted discounts for specific segments and measure conversion. |

---

## Setup Instructions

### 1. Install Python

Download Python 3.10 or 3.11 from [python.org](https://www.python.org/downloads/).

### 2. Clone or Download

```bash
git clone https://github.com/[your-username]/ECommerce-Sales-Customer-Analytics.git
cd ECommerce-Sales-Customer-Analytics
```

Or download the ZIP from GitHub and extract it.

### 3. Create a Virtual Environment (recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Place the Dataset

Ensure the dataset file is in the project root:

```
ECommerce-Sales-Customer-Analytics/
    ecommerce_customer_behavior_dataset_v2.csv
```

Download from Google Drive if needed:
[https://drive.google.com/file/d/1xx3co8Mo7EDAGTvhiVA8CkgJ_vOmPfsI/view?usp=sharing](https://drive.google.com/file/d/1xx3co8Mo7EDAGTvhiVA8CkgJ_vOmPfsI/view?usp=sharing)

---

## How to Run the Notebook

```bash
jupyter notebook analysis.ipynb
```

Run all cells from top to bottom in order. The notebook will:
- Load and preprocess the dataset
- Compute all 15 KPIs
- Generate and save all 55 charts to `assets/`
- Run all analysis sections (Sections 1–9)
- Generate `report/project_report.docx`

---

## How to Run the Dashboard

```bash
streamlit run app.py
```

The dashboard opens at `http://localhost:8501` and includes 8 interactive tabs:

| Tab | Contents |
|---|---|
| 📊 Overview | 6 KPI metric cards, monthly revenue trend, revenue by category |
| 🏙️ City & Category | Revenue by city, revenue by category, city × category heatmap |
| 👥 Customer Behaviour | Returning vs new, age group, gender, device, payment method |
| 📦 Delivery & Ratings | Delivery time histogram, avg delivery by city, rating distribution |
| 💰 Discount Analysis | Discount penetration, discount by category, AOV comparison |
| 🎯 RFM Segments | Descriptive RFM segmentation (Champions, Loyal, At-Risk, etc.) |
| 🤖 AI Insights | 5 dynamically computed insight cards from filtered data |
| 📋 Data Table | Filtered records table (up to 500 rows) |

**Sidebar filters:** Date range, Product Category, City, Gender, Device Type, Payment Method, Returning Customer status.

> The dashboard is educational and analytical. It does not claim predictive AI functionality.

---

## Project Folder Structure

```
ECommerce-Sales-Customer-Analytics/
|
|-- ecommerce_customer_behavior_dataset_v2.csv   <- original dataset
|
|-- analysis.ipynb                                <- main analysis notebook
|
|-- app.py                                        <- Streamlit interactive dashboard
|
|-- requirements.txt                              <- pinned library versions
|
|-- README.md                                     <- this file
|
|-- report/
|   +-- project_report.docx                      <- final internship report (.docx)
|
|-- assets/
|   +-- (55 chart PNG files auto-generated
|        by the notebook)
|
+-- .gitignore
```

---

## Chart References

Selected charts from `assets/` (all generated by `analysis.ipynb`):

| File | Section | Description |
|---|---|---|
| `eda_uni_customer_rating.png` | Section 3 | Customer rating distribution (1–5) |
| `eda_uni_total_amount.png` | Section 3 | Total Amount distribution (log scale) |
| `ts_monthly_revenue.png` | Section 5 | Monthly revenue trend (15 months) |
| `ts_mom_growth.png` | Section 5 | Month-over-month revenue growth |
| `eda_biv_correlation_heatmap.png` | Section 4 | Pearson correlation heatmap |
| `eda_biv_delivery_vs_rating.png` | Section 4 | Delivery time vs customer rating |
| `cb_age_group_revenue.png` | Section 6 | Revenue by age group |
| `rfm_segment_overview.png` | Section 7 | RFM segment distribution, revenue, and scatter |
| `del_delivery_distribution.png` | Section 8 | Delivery time distribution with buckets |
| `ai_risk_opportunity.png` | Section 9 | Risk and opportunity summary chart |

Full chart list: 55 files in `assets/`.

---

## Conclusion

This project successfully demonstrates the full data analytics lifecycle applied to an
e-commerce transactional dataset. Starting from raw CSV data, the analysis progressed through
data cleaning, feature engineering, KPI computation, EDA, customer segmentation, delivery
and satisfaction analysis, and an AI-assisted business insight framework.

Key outcomes:
- 15 business KPIs computed and tabulated
- 55 visualisations generated and saved
- 5 RFM customer segments identified (rule-based, descriptive)
- 316 satisfaction-risk orders identified and mapped by city and category
- 10 structured business insights produced with Fact -> Interpretation -> Action format
- An interactive 8-tab Streamlit dashboard delivered
- A professional 30+ page project report generated

All findings are grounded in actual computed results from the dataset.

---

## Limitations and Future Scope

### Limitations

- No product-level SKU data — analysis limited to 8 broad categories
- No cost or profit margin data — cannot extend to profitability analysis
- No customer acquisition channel data — marketing attribution not possible
- `Quantity` is capped at 5 — may reflect data generation constraints
- `Session_Duration_Minutes` and `Pages_Viewed` have narrow integer ranges
- `Gender: Other` has only 260 records — insufficient for reliable segment conclusions
- No returns, refunds, or cancellation data — satisfaction analysis is incomplete
- No time-of-day data — intraday patterns cannot be analysed
- 2024 data is partial (Jan 1 – Mar 25 only) — full-year comparisons not possible
- All correlation findings are associations only — causation cannot be established
- Dataset characteristics suggest possible synthetic generation

### Future Scope

- Integrate SKU-level product data for recommendation models
- Add return/refund data for complete satisfaction and churn modelling
- Connect to a live database for real-time dashboard refresh
- Extend RFM with predictive CLV modelling (BG/NBD model)
- Add geospatial visualisation with geocoded city coordinates
- Build automated weekly KPI report scheduler with email delivery
- Deploy Streamlit dashboard to cloud (Streamlit Community Cloud, AWS, or Azure)

---

## Author

**Author:** [Your Name]
**Internship:** AICTE | IBM SkillsBuild Data Analytics with AI Internship 2026
**Organization:** BharatCares

---

## GitHub Repository

**GitHub Repository:** [Add repository link after publishing]

> After pushing to GitHub, replace the placeholder above with your actual repository URL.

---

*This project was developed as part of an internship programme. All analysis is based
solely on the provided dataset. No external data sources were used.*
