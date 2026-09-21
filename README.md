# E-Commerce Sales Performance and Customer Behavior Analysis Using Data Analytics and AI

> An internship data analytics project that applies exploratory data analysis, KPI computation,
> customer behaviour analysis, and an AI-assisted insight framework to a real-structure
> e-commerce transactional dataset.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Business Problem Statement](#business-problem-statement)
3. [Project Objectives](#project-objectives)
4. [Dataset Information](#dataset-information)
5. [Key Analytical Areas](#key-analytical-areas)
6. [Technologies and Libraries](#technologies-and-libraries)
7. [Project Folder Structure](#project-folder-structure)
8. [Setup Instructions](#setup-instructions)
9. [How to Use the Project](#how-to-use-the-project)
10. [Expected Outputs](#expected-outputs)
11. [Limitations](#limitations)
12. [Future Scope](#future-scope)
13. [Author](#author)
14. [GitHub Repository](#github-repository)

---

## Project Overview

This project performs a comprehensive data analytics study on an e-commerce transactional
dataset covering 15 months of customer orders (January 2023 – March 2024). The analysis
spans sales performance measurement, product category and city-level breakdowns, customer
behaviour profiling, delivery and satisfaction evaluation, discount impact assessment, and
an AI-assisted business insight framework that converts computed findings into actionable
recommendations.

The project follows the full data analytics lifecycle:

```
Data Loading → Cleaning & Preprocessing → KPI Computation →
Exploratory Data Analysis → Customer Behaviour Analysis →
Sales & Product Analysis → Delivery & Satisfaction Analysis →
AI Insight Framework → Streamlit Dashboard → Project Report (.docx)
```

All findings and recommendations are derived exclusively from calculations performed on
the actual dataset. No results are invented or assumed prior to analysis.

---

## Business Problem Statement

Despite having thousands of orders from thousands of customers, e-commerce businesses
often lack a structured analytical framework to answer critical operational questions:

- Which product categories and cities drive the most revenue?
- What distinguishes high-value customers from low-value ones?
- How does delivery time relate to customer satisfaction?
- Where should discounting strategy be focused?
- Which customer segments are at risk of churning?

This project builds that analytical framework from the ground up using the available
transactional dataset, ending with a set of data-grounded, actionable business
recommendations.

---

## Project Objectives

| # | Objective |
|---|---|
| O1 | Measure and track core sales KPIs across time, geography, and product category |
| O2 | Analyse customer behaviour using session, device, payment, and demographic data |
| O3 | Evaluate delivery performance and its relationship with customer satisfaction |
| O4 | Identify discount usage patterns and their relationship with order value |
| O5 | Segment customers by value and purchase behaviour using RFM analysis |
| O6 | Build an AI-assisted insight framework (Fact → Insight → Risk/Opportunity → Action) |
| O7 | Deliver an interactive Streamlit dashboard for business stakeholders |
| O8 | Produce a structured internship project report in `.docx` format |

---

## Dataset Information

| Attribute | Detail |
|---|---|
| **Filename** | `ecommerce_customer_behavior_dataset_v2.csv` |
| **Records** | 17,049 rows |
| **Columns** | 18 columns |
| **Unique Customers** | 5,000 |
| **Unique Orders** | 17,049 |
| **Date Range** | January 1, 2023 – March 25, 2024 (≈15 months) |
| **Missing Values** | None |
| **Duplicate Rows** | None |
| **Dataset Source** | Dataset source link: To be added. |

### Columns Available

| Column | Type | Description |
|---|---|---|
| `Order_ID` | string | Unique order identifier |
| `Customer_ID` | string | Unique customer identifier |
| `Date` | string → datetime | Order date |
| `Age` | integer | Customer age (18–75) |
| `Gender` | string | Female / Male / Other |
| `City` | string | 10 cities |
| `Product_Category` | string | 8 product categories |
| `Unit_Price` | float | Price per unit |
| `Quantity` | integer | Units ordered (1–5) |
| `Discount_Amount` | float | Discount applied in currency |
| `Total_Amount` | float | Derived: (Unit_Price × Quantity) − Discount_Amount |
| `Payment_Method` | string | 5 payment methods |
| `Device_Type` | string | Mobile / Desktop / Tablet |
| `Session_Duration_Minutes` | integer | Session length on site |
| `Pages_Viewed` | integer | Pages visited per session |
| `Is_Returning_Customer` | boolean | True = returning customer |
| `Delivery_Time_Days` | integer | Days from order to delivery |
| `Customer_Rating` | integer | Post-delivery rating (1–5) |

> **Educational use notice:** This dataset is used strictly for educational and
> internship analytics purposes. No personally identifiable information is present.

---

## Key Analytical Areas

### 1. Sales Performance
- Total revenue, total orders, average order value (AOV)
- Monthly revenue trend and month-over-month growth
- Quarterly revenue comparison

### 2. Product Category Analysis
- Revenue, order volume, AOV, and average rating per category
- Discount penetration and average discount rate by category
- Delivery time distribution by category

### 3. City-Wise Analysis
- Revenue and order count per city (horizontal bar charts)
- Average delivery time and average customer rating per city
- City × Category revenue heatmap

### 4. Customer Behaviour
- Age group and gender analysis
- Session duration and pages viewed patterns
- Device type and payment method preferences
- Correlation between session behaviour and order value

### 5. Returning vs New Customers
- Revenue and order count split
- AOV comparison: returning vs new
- Category and device preferences by customer type

### 6. Delivery and Customer Satisfaction
- Delivery time distribution and city/category averages
- Customer rating distribution (1–5)
- Correlation analysis: delivery time vs customer rating
- Risk identification: high delivery time + low rating orders

### 7. Discount Analysis
- Discount penetration rate overall and by category
- Average order value with vs without discount
- Discount rate by age group and gender

### 8. AI-Assisted Business Insights
- Structured framework: **Fact → Insight → Risk/Opportunity → Recommended Action**
- All insight cards computed from actual dataset results
- Configurable thresholds — no hardcoded or invented conclusions

---

## Technologies and Libraries

| Library | Version | Purpose |
|---|---|---|
| `pandas` | 2.2.2 | Data loading, manipulation, groupby, pivot tables |
| `numpy` | 1.26.4 | Numerical operations and log transforms |
| `matplotlib` | 3.8.4 | Base plotting and chart export |
| `seaborn` | 0.13.2 | Statistical visualisations (heatmaps, boxplots) |
| `plotly` | 5.22.0 | Interactive charts for Streamlit dashboard |
| `streamlit` | 1.35.0 | Interactive web dashboard |
| `scipy` | 1.13.0 | Pearson correlation and statistical tests |
| `python-docx` | 1.1.2 | Programmatic `.docx` report generation |
| `openpyxl` | 3.1.2 | Excel export of KPI tables |
| `nbformat` | 5.10.4 | Jupyter notebook format support |
| `ipykernel` | 6.29.4 | Jupyter kernel |
| `scikit-learn` | 1.4.2 | *(Optional — ML section only; commented out by default)* |

> **Python version:** 3.10 or 3.11 recommended.

---

## Project Folder Structure

```
E-Commerce_Sales_Customer_Analytics/
│
├── ecommerce_customer_behavior_dataset_v2.csv   ← original dataset
│
├── analysis.ipynb                                ← main code file (single notebook)
│
├── app.py                                        ← Streamlit interactive dashboard
│
├── requirements.txt                              ← pinned library versions
│
├── README.md                                     ← this file
│
├── report/
│   └── project_report.docx                      ← final internship report
│
├── assets/
│   └── (chart images exported by notebook,      ← auto-generated
│       embedded in project_report.docx)
│
└── .gitignore                                    ← excludes cache, checkpoints, envs
```

---

## Setup Instructions

### Step 1 — Install Python

Download and install **Python 3.10 or 3.11** from [python.org](https://www.python.org/downloads/).
Verify your installation:

```bash
python --version
```

### Step 2 — Clone or Download the Repository

```bash
git clone https://github.com/[your-username]/[repository-name].git
cd E-Commerce_Sales_Customer_Analytics
```

Or download the ZIP and extract it to your working directory.

### Step 3 — Create a Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 4 — Install Dependencies

```bash
pip install -r requirements.txt
```

> To enable the optional ML section, open `requirements.txt`, uncomment
> `scikit-learn==1.4.2`, and re-run the install command.

### Step 5 — Place the Dataset

Ensure the dataset file is in the project root:

```
E-Commerce_Sales_Customer_Analytics/
└── ecommerce_customer_behavior_dataset_v2.csv
```

### Step 6 — Launch the Jupyter Notebook

```bash
jupyter notebook analysis.ipynb
```

Run all cells from top to bottom in order. The notebook will:
- Load and preprocess the dataset
- Compute all KPIs
- Generate and save all charts to `assets/`
- Run all analysis sections
- Generate `report/project_report.docx`

### Step 7 — Run the Streamlit Dashboard

A fully functional interactive dashboard is provided at `app.py` in the project root.

**Installation (if not already done):**

```bash
pip install -r requirements.txt
```

**Run the dashboard:**

```bash
streamlit run app.py
```

The dashboard will open automatically in your browser at `http://localhost:8501`.

**Expected file location:** `e:\Ecommerce_Sales_Customer_Analytics\app.py`

**Main dashboard features:**

| Tab | Contents |
|---|---|
| 📊 Overview | 6 KPI metric cards, monthly revenue trend, revenue by category |
| 🏙️ City & Category | Revenue by city, revenue by category, city×category heatmap |
| 👥 Customer Behaviour | Returning vs new, age group, gender, device type, payment method |
| 📦 Delivery & Ratings | Delivery time histogram, avg delivery by city, rating distribution |
| 💰 Discount Analysis | Discount penetration, discount by category, AOV comparison |
| 🎯 RFM Segments | Descriptive RFM segmentation (Champions, Loyal, At-Risk, etc.) |
| 🤖 AI Insights | 5 dynamically computed insight cards from filtered data |
| 📋 Data Table | Filtered records table (up to 500 rows) |

**Sidebar filters available:** Date range · Product Category · City · Gender · Device Type · Payment Method · Returning Customer status

> **Note:** The dashboard is educational and analytical. It does not claim predictive AI functionality.

---

## How to Use the Project

1. **Run `analysis.ipynb` from top to bottom** — each section is clearly labelled and
   self-contained. No manual configuration is needed beyond placing the dataset file
   in the correct location.

2. **Review KPI output tables** printed at the end of Section 2.

3. **Inspect EDA charts** displayed inline in the notebook and saved to `assets/`.

4. **Read AI insight cards** in Section 9 — each card shows the computed fact,
   derived insight, risk/opportunity classification, and recommended action.

5. **Open `report/project_report.docx`** for the full formatted internship report
   with all sections, tables, and embedded charts.

6. **Launch the Streamlit dashboard** (Step 7 above) for an interactive view of
   all KPIs, charts, and insights with sidebar filters.

---

## Expected Outputs

| Output | Description |
|---|---|
| **KPI Summary Tables** | KPI summary tables with computed values and formulas |
| **EDA Charts** | Univariate, bivariate, time-series, and multivariate visualisations |
| **RFM Customer Segments** | Rule-based segmentation: Champions, Loyal, At-Risk, etc. |
| **AI Insight Cards** | Fact → Insight → Risk/Opportunity → Action, one per key finding |
| **Business Recommendations** | Tiered (Revenue / Retention / Operations / Channel / Discounting) |
| **assets/ PNG files** | Chart images saved for use in the report |
| **report/project_report.docx** | Full structured internship report |
| **Streamlit Dashboard** | Streamlit dashboard, if implemented. |

---

## Limitations

- No product-level SKU data — analysis is limited to 8 broad product categories.
- No cost or profit margin data — revenue analysis cannot extend to profitability.
- No customer acquisition channel data — marketing attribution is not possible.
- `Quantity` is capped at 5 — may reflect data generation constraints rather than real behaviour.
- `Session_Duration_Minutes` and `Pages_Viewed` have a narrow integer range.
- `Gender: Other` has only 260 records — insufficient for reliable segment-level conclusions.
- No returns, refunds, or cancellation data — satisfaction analysis is incomplete.
- No time-of-day data — intraday purchase patterns cannot be analysed.
- All correlation findings are associations only — causation cannot be established from this dataset.

---

## Future Scope

- Integrate SKU-level product data to enable product recommendation models.
- Add return/refund data for a complete customer satisfaction and churn model.
- Connect to a live database for real-time dashboard refresh.
- Incorporate marketing channel and campaign spend data for attribution analysis.
- Extend RFM segmentation with predictive Customer Lifetime Value (CLV) modelling.
- Add geospatial visualisation with geocoded city coordinates.
- Build an automated weekly KPI report scheduler with email delivery.
- Deploy the Streamlit dashboard to a cloud platform (Streamlit Community Cloud, AWS, or Azure).

---

## Author

**Author:** [Your Name]

---

## GitHub Repository

**GitHub Repository:** [Add repository link after publishing]

> After pushing to GitHub, replace the placeholder above with your actual repository URL,
> for example: `https://github.com/your-username/ecommerce-sales-analytics`

---

*This project was developed as part of an internship programme. All analysis is based
solely on the provided dataset. No external data sources were used.*
