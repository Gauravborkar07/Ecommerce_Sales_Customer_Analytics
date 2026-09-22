# E-Commerce Sales Performance and Customer Behavior Analysis Using Data Analytics and AI

> An internship data analytics project that applies exploratory data analysis, KPI computation, customer behaviour analysis, RFM segmentation, and an AI-assisted insight framework to an e-commerce transactional dataset.

**Internship:** AICTE | IBM SkillsBuild Data Analytics with AI Internship 2026

**Organization:** BharatCares

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

This project performs a comprehensive data analytics study on an e-commerce transactional dataset covering approximately 15 months of customer orders from January 2023 to March 2024.

The analysis focuses on:

- Sales performance measurement across time, geography, and product category.
- Customer behaviour profiling using demographic, session, and device data.
- RFM (Recency, Frequency, Monetary) customer segmentation.
- Delivery performance and customer satisfaction evaluation.
- Discount impact and penetration analysis.
- AI-assisted insight generation for business decision-making.
- An interactive Streamlit dashboard for business stakeholders.

All findings and recommendations are derived from calculations performed on the provided dataset.

---

## Problem Statement

E-commerce businesses generate large volumes of transactional data but often lack a structured analytical framework to answer important business questions.

This project addresses the following questions:

- Which product categories and cities generate the highest revenue?
- What distinguishes high-value customers from low-value customers?
- How does delivery time relate to customer satisfaction?
- Which customers may be at risk of disengaging?
- Where should discounting strategies be focused?
- How can data-driven insights support business decisions?

The project builds an analytical framework to convert raw e-commerce data into meaningful and actionable business insights.

---

## Project Objectives

| No. | Objective |
|---|---|
| O1 | Measure and track core sales KPIs across time, geography, and product category |
| O2 | Analyse customer behaviour using session, device, payment, and demographic data |
| O3 | Evaluate delivery performance and its relationship with customer satisfaction |
| O4 | Identify discount usage patterns and their relationship with order value |
| O5 | Segment customers based on value and purchase behaviour using RFM analysis |
| O6 | Build an AI-assisted insight framework using Fact → Insight → Risk/Opportunity → Action |
| O7 | Develop an interactive Streamlit dashboard for business stakeholders |
| O8 | Prepare a structured internship project report in DOCX format |

---

## Project Goals

The key goals of this project are:

- Produce a clean and reproducible Jupyter Notebook.
- Compute more than 15 business KPIs directly from the dataset.
- Generate more than 55 charts and visualisations.
- Build a rule-based RFM customer segmentation model.
- Identify customer satisfaction risks related to delivery performance.
- Develop a Streamlit dashboard with interactive tabs and filters.
- Prepare a professional project report with charts and KPI tables.
- Provide data-grounded business insights and recommendations.

---

## Dataset Details

| Attribute | Detail |
|---|---|
| File Name | `ecommerce_customer_behavior_dataset_v2.csv` |
| Format | CSV |
| Records | 17,049 rows |
| Columns | 18 columns |
| Unique Customers | 5,000 |
| Unique Orders | 17,049 |
| Date Range | January 1, 2023 – March 25, 2024 |
| Missing Values | None |
| Duplicate Rows | None |
| Product Categories | 8 |
| Cities | 10 |

### Dataset Source

The dataset can be downloaded from the following Google Drive link:

[Download E-Commerce Customer Behavior Dataset](https://drive.google.com/file/d/1xx3co8Mo7EDAGTvhiVA8CkgJ_vOmPfsI/view?usp=sharing)

The dataset file is also included in this repository:

```text
ecommerce_customer_behavior_dataset_v2.csv
```

### Important Columns

| Column | Type | Description |
|---|---|---|
| `Order_ID` | String | Unique order identifier |
| `Customer_ID` | String | Unique customer identifier |
| `Date` | Datetime | Order date |
| `Age` | Integer | Customer age |
| `Gender` | String | Customer gender |
| `City` | String | Customer city |
| `Product_Category` | String | Product category |
| `Unit_Price` | Float | Price per unit |
| `Quantity` | Integer | Number of units ordered |
| `Discount_Amount` | Float | Discount applied to the order |
| `Total_Amount` | Float | Final order amount |
| `Payment_Method` | String | Payment method used |
| `Device_Type` | String | Mobile, Desktop, or Tablet |
| `Session_Duration_Minutes` | Integer | Session duration on the website |
| `Pages_Viewed` | Integer | Number of pages viewed |
| `Is_Returning_Customer` | Boolean | Indicates whether the customer is returning |
| `Delivery_Time_Days` | Integer | Delivery duration in days |
| `Customer_Rating` | Integer | Customer rating from 1 to 5 |

### Dataset Purpose

The dataset is used strictly for educational and internship analytics purposes.

No personally identifiable information is included in the dataset.

---

## Tools and Technologies

| Tool / Library | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data loading, cleaning, and manipulation |
| NumPy | Numerical operations |
| Matplotlib | Data visualisation and chart generation |
| Seaborn | Statistical visualisation |
| Plotly | Interactive charts |
| Streamlit | Interactive web dashboard |
| SciPy | Correlation and statistical analysis |
| Python-docx | DOCX report generation |
| OpenPyXL | Excel file handling |
| Nbformat | Jupyter Notebook format handling |
| IPykernel | Jupyter execution kernel |
| Jupyter Notebook | Interactive analysis environment |
| Git and GitHub | Version control and project hosting |

---

## Methodology / Workflow

The project followed the complete data analytics lifecycle:

```text
1. Data Loading and Inspection
            ↓
2. Data Cleaning and Type Conversion
            ↓
3. Feature Engineering
            ↓
4. Data Validation
            ↓
5. KPI Computation
            ↓
6. Exploratory Data Analysis
            ↓
7. Time-Series and Sales Trend Analysis
            ↓
8. Customer Behaviour Analysis
            ↓
9. RFM Customer Segmentation
            ↓
10. Delivery, Satisfaction and Discount Analysis
            ↓
11. AI-Assisted Insight Framework
            ↓
12. Streamlit Dashboard Development
            ↓
13. Project Report Preparation
```

### Main Analytical Activities

- Data cleaning and preprocessing.
- Feature engineering.
- KPI calculation.
- Univariate analysis.
- Bivariate analysis.
- Multivariate analysis.
- Time-series analysis.
- Customer segmentation.
- Delivery and rating analysis.
- Discount analysis.
- Business insight generation.
- Interactive dashboard development.

---

## Exploratory Data Analysis

The exploratory data analysis was divided into multiple sections.

### 1. Univariate Analysis

The following analyses were performed:

- Distribution of numerical variables.
- Histograms and KDE plots.
- Boxplots for outlier analysis.
- Count distributions for categorical variables.
- Analysis of order value and unit price.
- Quantity and discount distribution analysis.

### 2. Bivariate and Multivariate Analysis

The following relationships were studied:

- Correlation between numerical variables.
- Total amount versus unit price.
- Total amount versus session duration.
- Total amount versus pages viewed.
- Revenue by product category and gender.
- Revenue by device type.
- Revenue by payment method.
- Delivery time versus customer rating.

### 3. Time-Series Analysis

The following time-based analyses were performed:

- Monthly revenue trend.
- Monthly order count.
- Average Order Value trend.
- Month-over-month revenue growth.
- Quarterly performance comparison.
- Yearly summary.
- Category-wise monthly revenue trends.
- Returning versus new customer revenue over time.

> Correlation findings represent associations only. Correlation does not establish causation.

---

## Key Findings

The following findings were calculated from the dataset:

| Metric | Result |
|---|---:|
| Total Revenue | 21,779,052.59 |
| Average Order Value | 1,277.44 |
| Returning Customer Orders | 88.2% |
| Returning Customer Revenue | 88.1% |
| Top Revenue Category | Electronics |
| Top Revenue City | Istanbul |
| Mobile Order Share | 56.0% |
| Average Delivery Time | 6.50 days |
| Average Customer Rating | 3.90 / 5 |
| Low-Rating Orders | 13.3% |
| Satisfaction-Risk Orders | 316 |
| At-Risk Customers | 778 |

### Major Observations

1. Total revenue was approximately 21.78 million across 17,049 orders.
2. The average order value was approximately 1,277.44.
3. Returning customers contributed a significant share of orders and revenue.
4. Electronics was the highest revenue-generating product category.
5. Istanbul was the highest revenue-generating city.
6. Mobile devices accounted for the highest share of orders.
7. Desktop users recorded the highest average order value.
8. Orders with discounts had a lower average order value than orders without discounts.
9. Average delivery time was approximately 6.50 days.
10. A measurable percentage of orders received low customer ratings.
11. RFM segmentation identified Champions, Loyal Customers, At-Risk Customers, and other customer groups.
12. Session duration and pages viewed showed very weak relationships with order value.

---

## Business Insights and Recommendations

All recommendations are based on the calculated dataset results.

| Area | Recommendation |
|---|---|
| Revenue Growth | Focus on high-performing categories such as Electronics and high-revenue cities such as Istanbul |
| Customer Retention | Introduce loyalty programmes and personalised offers for returning customers |
| At-Risk Re-engagement | Run targeted win-back campaigns for At-Risk RFM customer segments |
| Logistics Improvement | Review delivery operations in cities with higher satisfaction-risk orders |
| Discount Strategy | Avoid blanket discounting and test targeted offers for specific customer segments |
| Customer Satisfaction | Monitor low ratings and investigate delivery or product-related issues |
| Inventory Planning | Maintain adequate stock for high-demand categories |
| Average Order Value | Use product bundling, cross-selling, and upselling strategies |
| Customer Segmentation | Use RFM segments to personalise marketing campaigns |
| Data-Driven Decisions | Regularly monitor KPIs through the analytics dashboard |

> These recommendations are analytical suggestions and do not guarantee specific business outcomes.

---

## Setup Instructions

### 1. Install Python

Install Python 3.10 or Python 3.11 from:

[https://www.python.org/downloads/](https://www.python.org/downloads/)

### 2. Clone the Repository

```bash
git clone https://github.com/Gauravborkar07/Ecommerce_Sales_Customer_Analytics.git
```

### 3. Navigate to the Project Folder

```bash
cd Ecommerce_Sales_Customer_Analytics
```

### 4. Create a Virtual Environment

For Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

For macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Place the Dataset

Make sure the dataset is available in the project root directory:

```text
ecommerce_customer_behavior_dataset_v2.csv
```

---

## How to Run the Notebook

Start Jupyter Notebook using:

```bash
jupyter notebook
```

Then open the following notebook:

```text
GauravBorkar_EcommerceSalesCustomerAnalytics.ipynb
```

Run all cells sequentially from top to bottom.

The notebook performs the following activities:

- Loads the dataset.
- Cleans and preprocesses the data.
- Computes business KPIs.
- Performs exploratory data analysis.
- Generates charts and visualisations.
- Performs RFM segmentation.
- Analyses delivery, ratings, and discounts.
- Generates business insights.

---

## How to Run the Dashboard

The project includes an interactive Streamlit dashboard.

Run the following command:

```bash
streamlit run app.py
```

The dashboard will open in a browser at:

```text
http://localhost:8501
```

### Dashboard Tabs

| Tab | Contents |
|---|---|
| Overview | KPI cards, monthly revenue trend, and category revenue |
| City & Category | Revenue by city, category, and heatmap |
| Customer Behaviour | Returning customers, age group, gender, device, and payment analysis |
| Delivery & Ratings | Delivery distribution, city-wise delivery, and ratings |
| Discount Analysis | Discount penetration and average order value comparison |
| RFM Segments | Customer segmentation using RFM analysis |
| AI Insights | Dynamically generated insight cards |
| Data Table | Filtered dataset records |

### Dashboard Filters

The dashboard includes filters for:

- Date range.
- Product category.
- City.
- Gender.
- Device type.
- Payment method.
- Returning customer status.

> The dashboard is educational and analytical. It does not claim predictive AI functionality.

---

## Project Folder Structure

```text
Ecommerce_Sales_Customer_Analytics/
│
├── ecommerce_customer_behavior_dataset_v2.csv
├── GauravBorkar_EcommerceSalesCustomerAnalytics.ipynb
├── app.py
├── requirements.txt
├── README.md
├── GauravBorkar_ProjectReport.docx
│
├── report/
│   └── project_report.docx
│
├── assets/
│   └── chart PNG files
│
└── .gitignore
```

---

## Chart References

Selected charts generated during the analysis include:

| Chart File | Description |
|---|---|
| `eda_uni_customer_rating.png` | Customer rating distribution |
| `eda_uni_total_amount.png` | Total amount distribution |
| `ts_monthly_revenue.png` | Monthly revenue trend |
| `ts_mom_growth.png` | Month-over-month revenue growth |
| `eda_biv_correlation_heatmap.png` | Pearson correlation heatmap |
| `eda_biv_delivery_vs_rating.png` | Delivery time versus customer rating |
| `cb_age_group_revenue.png` | Revenue by age group |
| `rfm_segment_overview.png` | RFM segment distribution and revenue |
| `del_delivery_distribution.png` | Delivery time distribution |
| `ai_risk_opportunity.png` | Risk and opportunity summary |

The project contains more than 55 charts and visualisations saved in the `assets/` directory.

---

## Conclusion

This project demonstrates the complete data analytics lifecycle applied to an e-commerce transactional dataset.

The analysis covers:

- Data cleaning.
- Feature engineering.
- KPI computation.
- Exploratory data analysis.
- Sales trend analysis.
- Customer behaviour analysis.
- RFM customer segmentation.
- Delivery and satisfaction analysis.
- Discount analysis.
- AI-assisted business insights.
- Interactive dashboard development.

### Key Outcomes

- Business KPIs were computed and analysed.
- More than 55 visualisations were generated.
- Customer segments were identified using RFM analysis.
- Satisfaction-risk orders were identified.
- Business recommendations were developed from actual dataset results.
- An interactive Streamlit dashboard was created.
- A professional project report was prepared.

All findings are based on the provided dataset and the performed analysis.

---

## Limitations and Future Scope

### Limitations

- The dataset contains only broad product categories and no SKU-level information.
- Cost and profit margin data are not available.
- Customer acquisition channel data is not included.
- Quantity values are limited to a range of 1 to 5.
- Session duration and pages viewed have narrow ranges.
- Some demographic groups have limited records.
- Returns, refunds, and cancellation data are not available.
- Time-of-day analysis cannot be performed.
- The 2024 data covers only a partial year.
- Correlation analysis cannot establish causation.
- The dataset may contain synthetic data characteristics.

### Future Scope

Future improvements may include:

- SKU-level product recommendation systems.
- Sales forecasting.
- Customer churn prediction.
- Customer lifetime value modelling.
- Return and refund analysis.
- Real-time dashboard integration.
- Live database connectivity.
- Geospatial analysis using city coordinates.
- Automated weekly KPI reports.
- Cloud deployment using Streamlit Community Cloud, AWS, or Azure.

---

## Author

**Gaurav Ghanshyam Borkar**

**Institution:** Suryodaya College of Engineering and Technology

**Internship:** AICTE | IBM SkillsBuild Data Analytics with AI Internship 2026

**Organization:** BharatCares

---

## GitHub Repository

[View Project on GitHub](https://github.com/Gauravborkar07/Ecommerce_Sales_Customer_Analytics)

---

## Acknowledgement

I would like to express my gratitude to AICTE, IBM SkillsBuild, BharatCares, and all the mentors and instructors involved in the Data Analytics with AI Internship 2026 for providing valuable learning resources and practical project experience.

---

*This project was developed as part of an internship programme. All analysis is based on the provided dataset.*