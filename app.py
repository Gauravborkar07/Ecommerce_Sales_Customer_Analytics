import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="E-Commerce Sales Performance and Customer Behavior Analytics",
    layout="wide",
)

# ── Data loading ──────────────────────────────────────────────────────────────
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent / "ecommerce_customer_behavior_dataset_v2.csv"

@st.cache_data
def load_data(path) -> pd.DataFrame:
    df = pd.read_csv(path)
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df["Discount_Applied"] = df["Discount_Amount"] > 0
    return df

try:
    df = load_data(DATA_PATH)
except FileNotFoundError:
    st.error(
        f"Dataset file not found: **{DATA_PATH}**. "
        "Please place the CSV in the same directory as app.py and reload."
    )
    st.stop()
except Exception as exc:
    st.error(f"Failed to load dataset: {exc}")
    st.stop()

# ── Sidebar filters ────────────────────────────────────────────────────────────
st.sidebar.title("🔍 Filters")

date_min = df["Date"].min().date()
date_max = df["Date"].max().date()
date_range = st.sidebar.slider(
    "Date Range",
    min_value=date_min,
    max_value=date_max,
    value=(date_min, date_max),
)

categories = sorted(df["Product_Category"].dropna().unique().tolist())
sel_categories = st.sidebar.multiselect("Product Category", categories)

cities = sorted(df["City"].dropna().unique().tolist())
sel_cities = st.sidebar.multiselect("City", cities)

genders = sorted(df["Gender"].dropna().unique().tolist())
sel_genders = st.sidebar.multiselect("Gender", genders)

devices = sorted(df["Device_Type"].dropna().unique().tolist())
sel_devices = st.sidebar.multiselect("Device Type", devices)

payments = sorted(df["Payment_Method"].dropna().unique().tolist())
sel_payments = st.sidebar.multiselect("Payment Method", payments)

returning_option = st.sidebar.selectbox(
    "Returning Customer",
    ["All", "Returning Only", "New Only"],
)

# ── Apply filters ──────────────────────────────────────────────────────────────
filtered_df = df.copy()
filters_applied = 0

filtered_df = filtered_df[
    (filtered_df["Date"].dt.date >= date_range[0])
    & (filtered_df["Date"].dt.date <= date_range[1])
]
if date_range != (date_min, date_max):
    filters_applied += 1

if sel_categories:
    filtered_df = filtered_df[filtered_df["Product_Category"].isin(sel_categories)]
    filters_applied += 1

if sel_cities:
    filtered_df = filtered_df[filtered_df["City"].isin(sel_cities)]
    filters_applied += 1

if sel_genders:
    filtered_df = filtered_df[filtered_df["Gender"].isin(sel_genders)]
    filters_applied += 1

if sel_devices:
    filtered_df = filtered_df[filtered_df["Device_Type"].isin(sel_devices)]
    filters_applied += 1

if sel_payments:
    filtered_df = filtered_df[filtered_df["Payment_Method"].isin(sel_payments)]
    filters_applied += 1

if returning_option == "Returning Only":
    filtered_df = filtered_df[filtered_df["Is_Returning_Customer"] == True]
    filters_applied += 1
elif returning_option == "New Only":
    filtered_df = filtered_df[filtered_df["Is_Returning_Customer"] == False]
    filters_applied += 1

st.sidebar.markdown(f"**Filters Applied:** {filters_applied}")
st.sidebar.markdown(f"**Rows in view:** {len(filtered_df):,}")

# ── Page title ─────────────────────────────────────────────────────────────────
st.title("E-Commerce Sales Performance and Customer Behavior Analytics")

# ── Empty guard ────────────────────────────────────────────────────────────────
if filtered_df.empty:
    st.warning("⚠️ No data matches the selected filters. Please adjust your filters.")
    st.stop()

# ── Helper ─────────────────────────────────────────────────────────────────────
def fmt_currency(val: float) -> str:
    if val >= 1_000_000:
        return f"₹{val/1_000_000:.2f}M"
    if val >= 1_000:
        return f"₹{val/1_000:.1f}K"
    return f"₹{val:.2f}"

# ── Tabs ───────────────────────────────────────────────────────────────────────
tabs = st.tabs([
    "📊 Overview",
    "🏙️ City & Category",
    "👥 Customer Behaviour",
    "📦 Delivery & Ratings",
    "💰 Discount Analysis",
    "🎯 RFM Segments",
    "🤖 AI Insights",
    "📋 Data Table",
])

# ════════════════════════════════════════════════════════════
# TAB 1 — Overview
# ════════════════════════════════════════════════════════════
with tabs[0]:
    st.subheader("📊 Overview")

    total_revenue = filtered_df["Total_Amount"].sum()
    total_orders = len(filtered_df)
    unique_customers = filtered_df["Customer_ID"].nunique()
    aov = total_revenue / total_orders if total_orders else 0
    returning_rate = (
        filtered_df["Is_Returning_Customer"].mean() * 100
        if "Is_Returning_Customer" in filtered_df.columns
        else 0
    )
    avg_rating = (
        filtered_df["Customer_Rating"].mean()
        if "Customer_Rating" in filtered_df.columns
        else 0
    )

    k1, k2, k3, k4, k5, k6 = st.columns(6)
    k1.metric("💵 Total Revenue", fmt_currency(total_revenue))
    k2.metric("🛒 Total Orders", f"{total_orders:,}")
    k3.metric("👤 Unique Customers", f"{unique_customers:,}")
    k4.metric("📈 Avg Order Value", fmt_currency(aov))
    k5.metric("🔄 Returning Rate", f"{returning_rate:.1f}%")
    k6.metric("⭐ Avg Rating", f"{avg_rating:.2f}")

    st.markdown("---")

    col_a, col_b = st.columns(2)

    with col_a:
        monthly = (
            filtered_df.groupby(filtered_df["Date"].dt.to_period("M"))["Total_Amount"]
            .sum()
            .reset_index()
        )
        monthly["Date"] = monthly["Date"].astype(str)
        fig_monthly = px.line(
            monthly,
            x="Date",
            y="Total_Amount",
            title="Monthly Revenue Trend",
            labels={"Total_Amount": "Revenue (₹)", "Date": "Month"},
            markers=True,
        )
        fig_monthly.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig_monthly, width="stretch")
        st.caption("Total revenue aggregated by calendar month for the selected period.")

    with col_b:
        cat_rev = (
            filtered_df.groupby("Product_Category")["Total_Amount"]
            .sum()
            .sort_values(ascending=False)
            .reset_index()
        )
        fig_cat = px.bar(
            cat_rev,
            x="Product_Category",
            y="Total_Amount",
            title="Revenue by Product Category",
            labels={"Total_Amount": "Revenue (₹)", "Product_Category": "Category"},
            color="Product_Category",
        )
        st.plotly_chart(fig_cat, width="stretch")
        st.caption("Total revenue per product category.")

# ════════════════════════════════════════════════════════════
# TAB 2 — City & Category
# ════════════════════════════════════════════════════════════
with tabs[1]:
    st.subheader("🏙️ City & Category Analysis")

    city_rev = (
        filtered_df.groupby("City")["Total_Amount"]
        .sum()
        .sort_values()
        .reset_index()
    )
    fig_city = px.bar(
        city_rev,
        x="Total_Amount",
        y="City",
        orientation="h",
        title="Revenue by City",
        labels={"Total_Amount": "Revenue (₹)", "City": "City"},
        color="Total_Amount",
        color_continuous_scale="Blues",
    )
    st.plotly_chart(fig_city, width="stretch")
    st.caption("Horizontal bar chart showing total revenue contribution by city.")

    col_c, col_d = st.columns(2)

    with col_c:
        cat_rev2 = (
            filtered_df.groupby("Product_Category")["Total_Amount"]
            .sum()
            .sort_values(ascending=False)
            .reset_index()
        )
        fig_cat2 = px.bar(
            cat_rev2,
            x="Product_Category",
            y="Total_Amount",
            title="Revenue by Product Category",
            labels={"Total_Amount": "Revenue (₹)", "Product_Category": "Category"},
            color="Total_Amount",
            color_continuous_scale="Greens",
        )
        st.plotly_chart(fig_cat2, width="stretch")
        st.caption("Total revenue per category (filtered view).")

    with col_d:
        heatmap_data = (
            filtered_df.groupby(["City", "Product_Category"])["Total_Amount"]
            .sum()
            .reset_index()
        )
        heatmap_pivot = heatmap_data.pivot(
            index="City", columns="Product_Category", values="Total_Amount"
        ).fillna(0)
        fig_heat = px.imshow(
            heatmap_pivot,
            title="Revenue Heatmap: City × Category",
            labels={"color": "Revenue (₹)"},
            color_continuous_scale="YlOrRd",
            aspect="auto",
        )
        st.plotly_chart(fig_heat, width="stretch")
        st.caption("Heatmap of revenue for each city–category combination.")

# ════════════════════════════════════════════════════════════
# TAB 3 — Customer Behaviour
# ════════════════════════════════════════════════════════════
with tabs[2]:
    st.subheader("👥 Customer Behaviour")

    col_e, col_f = st.columns(2)

    with col_e:
        ret_rev = (
            filtered_df.groupby("Is_Returning_Customer")["Total_Amount"]
            .sum()
            .reset_index()
        )
        ret_rev["Segment"] = ret_rev["Is_Returning_Customer"].map(
            {True: "Returning", False: "New", 1: "Returning", 0: "New"}
        )
        fig_ret = px.bar(
            ret_rev,
            x="Segment",
            y="Total_Amount",
            title="Revenue: Returning vs New Customers",
            labels={"Total_Amount": "Revenue (₹)", "Segment": "Customer Type"},
            color="Segment",
        )
        st.plotly_chart(fig_ret, width="stretch")
        st.caption("Revenue split between returning and new customers.")

    with col_f:
        if "Age" in filtered_df.columns:
            filtered_df2 = filtered_df.copy()
            filtered_df2["Age_Group"] = pd.cut(
                filtered_df2["Age"],
                bins=[17, 25, 35, 45, 55, 75],
                labels=["18-25", "26-35", "36-45", "46-55", "56-75"],
                right=True,
            )
            age_rev = (
                filtered_df2.groupby("Age_Group", observed=True)["Total_Amount"]
                .sum()
                .reset_index()
            )
            fig_age = px.bar(
                age_rev,
                x="Age_Group",
                y="Total_Amount",
                title="Revenue by Age Group",
                labels={"Total_Amount": "Revenue (₹)", "Age_Group": "Age Group"},
                color="Age_Group",
            )
            st.plotly_chart(fig_age, width="stretch")
            st.caption("Total revenue broken down by customer age group.")
        else:
            st.info("Age column not found in dataset.")

    col_g, col_h, col_i = st.columns(3)

    with col_g:
        gender_rev = (
            filtered_df.groupby("Gender")["Total_Amount"]
            .sum()
            .sort_values(ascending=False)
            .reset_index()
        )
        fig_gender = px.bar(
            gender_rev,
            x="Gender",
            y="Total_Amount",
            title="Revenue by Gender",
            labels={"Total_Amount": "Revenue (₹)"},
            color="Gender",
        )
        st.plotly_chart(fig_gender, width="stretch")

    with col_h:
        device_rev = (
            filtered_df.groupby("Device_Type")["Total_Amount"]
            .sum()
            .sort_values(ascending=False)
            .reset_index()
        )
        fig_device = px.bar(
            device_rev,
            x="Device_Type",
            y="Total_Amount",
            title="Revenue by Device Type",
            labels={"Total_Amount": "Revenue (₹)", "Device_Type": "Device"},
            color="Device_Type",
        )
        st.plotly_chart(fig_device, width="stretch")

    with col_i:
        pay_rev = (
            filtered_df.groupby("Payment_Method")["Total_Amount"]
            .sum()
            .sort_values(ascending=False)
            .reset_index()
        )
        fig_pay = px.bar(
            pay_rev,
            x="Payment_Method",
            y="Total_Amount",
            title="Revenue by Payment Method",
            labels={"Total_Amount": "Revenue (₹)", "Payment_Method": "Payment"},
            color="Payment_Method",
        )
        st.plotly_chart(fig_pay, width="stretch")

    st.caption("Gender, device type, and payment method revenue breakdowns.")

# ════════════════════════════════════════════════════════════
# TAB 4 — Delivery & Ratings
# ════════════════════════════════════════════════════════════
with tabs[3]:
    st.subheader("📦 Delivery & Ratings")

    col_j, col_k = st.columns(2)

    with col_j:
        if "Delivery_Time_Days" in filtered_df.columns:
            fig_deliv = px.histogram(
                filtered_df,
                x="Delivery_Time_Days",
                nbins=20,
                title="Distribution of Delivery Time (Days)",
                labels={"Delivery_Time_Days": "Delivery Days", "count": "Orders"},
                color_discrete_sequence=["#3b82d4"],
            )
            st.plotly_chart(fig_deliv, width="stretch")
            st.caption("Histogram of order delivery times across the filtered dataset.")
        else:
            st.info("Delivery_Time_Days column not found.")

    with col_k:
        if "Delivery_Time_Days" in filtered_df.columns:
            city_deliv = (
                filtered_df.groupby("City")["Delivery_Time_Days"]
                .mean()
                .sort_values()
                .reset_index()
            )
            fig_city_deliv = px.bar(
                city_deliv,
                x="Delivery_Time_Days",
                y="City",
                orientation="h",
                title="Avg Delivery Time by City",
                labels={"Delivery_Time_Days": "Avg Days", "City": "City"},
                color="Delivery_Time_Days",
                color_continuous_scale="Reds",
            )
            st.plotly_chart(fig_city_deliv, width="stretch")
            st.caption("Average delivery time per city.")

    col_l, col_m = st.columns(2)

    with col_l:
        if "Customer_Rating" in filtered_df.columns:
            rating_dist = (
                filtered_df["Customer_Rating"]
                .value_counts()
                .sort_index()
                .reset_index()
            )
            rating_dist.columns = ["Rating", "Count"]
            fig_rating = px.bar(
                rating_dist,
                x="Rating",
                y="Count",
                title="Customer Rating Distribution",
                labels={"Rating": "Rating (1–5)", "Count": "Number of Orders"},
                color="Rating",
                color_continuous_scale="Viridis",
            )
            st.plotly_chart(fig_rating, width="stretch")
            st.caption("Distribution of customer ratings across all orders.")

    with col_m:
        if "Customer_Rating" in filtered_df.columns:
            cat_rating = (
                filtered_df.groupby("Product_Category")["Customer_Rating"]
                .mean()
                .sort_values(ascending=False)
                .reset_index()
            )
            fig_cat_rating = px.bar(
                cat_rating,
                x="Product_Category",
                y="Customer_Rating",
                title="Avg Customer Rating by Category",
                labels={
                    "Customer_Rating": "Avg Rating",
                    "Product_Category": "Category",
                },
                color="Customer_Rating",
                color_continuous_scale="RdYlGn",
            )
            st.plotly_chart(fig_cat_rating, width="stretch")
            st.caption("Average rating customers gave for each product category.")

# ════════════════════════════════════════════════════════════
# TAB 5 — Discount Analysis
# ════════════════════════════════════════════════════════════
with tabs[4]:
    st.subheader("💰 Discount Analysis")

    if "Discount_Applied" not in filtered_df.columns:
        st.warning("Discount_Applied column not found in dataset.")
    else:
        disc_counts = filtered_df["Discount_Applied"].value_counts().reset_index()
        disc_counts.columns = ["Discount_Applied", "Count"]
        disc_counts["Label"] = disc_counts["Discount_Applied"].map(
            {True: "Discounted", False: "Full Price"}
        ).fillna(disc_counts["Discount_Applied"].astype(str))

        col_n, col_o = st.columns(2)

        with col_n:
            fig_disc_pie = px.pie(
                disc_counts,
                names="Label",
                values="Count",
                title="Overall Discount Penetration",
                color_discrete_sequence=["#3b82d4", "#e5e7eb"],
            )
            st.plotly_chart(fig_disc_pie, width="stretch")
            st.caption("Share of orders that received a discount vs. full-price orders.")

        with col_o:
            disc_cat = (
                filtered_df.groupby("Product_Category")["Discount_Applied"]
                .mean()
                .mul(100)
                .sort_values(ascending=False)
                .reset_index()
            )
            disc_cat.columns = ["Product_Category", "Discount_Rate"]
            fig_disc_cat = px.bar(
                disc_cat,
                x="Product_Category",
                y="Discount_Rate",
                title="Discount Penetration Rate by Category (%)",
                labels={
                    "Discount_Rate": "Discount Rate (%)",
                    "Product_Category": "Category",
                },
                color="Discount_Rate",
                color_continuous_scale="Oranges",
            )
            st.plotly_chart(fig_disc_cat, width="stretch")
            st.caption("Percentage of orders with a discount applied per category.")

        aov_disc = (
            filtered_df.groupby("Discount_Applied")["Total_Amount"]
            .mean()
            .reset_index()
        )
        aov_disc["Label"] = aov_disc["Discount_Applied"].map(
            {True: "Discounted", False: "Full Price"}
        ).fillna(aov_disc["Discount_Applied"].astype(str))
        fig_aov_disc = px.bar(
            aov_disc,
            x="Label",
            y="Total_Amount",
            title="Average Order Value: Discounted vs Full Price",
            labels={"Total_Amount": "Avg Order Value (₹)", "Label": "Order Type"},
            color="Label",
            color_discrete_sequence=["#3b82d4", "#7c5cd8"],
        )
        st.plotly_chart(fig_aov_disc, width="stretch")
        st.caption("Comparison of average order value for discounted vs full-price orders.")

# ════════════════════════════════════════════════════════════
# TAB 6 — RFM Segments
# ════════════════════════════════════════════════════════════
with tabs[5]:
    st.subheader("🎯 RFM Segments")
    st.info(
        "ℹ️ Rule-based descriptive segmentation only — not a predictive model."
    )

    ref_date = filtered_df["Date"].max()
    rfm = (
        filtered_df.groupby("Customer_ID")
        .agg(
            Recency=("Date", lambda x: (ref_date - x.max()).days),
            Frequency=("Customer_ID", "count"),
            Monetary=("Total_Amount", "sum"),
        )
        .reset_index()
    )

    def safe_qcut(series, q, labels):
        try:
            return pd.qcut(series, q=q, labels=labels, duplicates="drop")
        except Exception:
            try:
                return pd.qcut(series.rank(method="first"), q=q, labels=labels)
            except Exception:
                return pd.Series([labels[len(labels) // 2]] * len(series), index=series.index)

    rfm["R_Score"] = safe_qcut(rfm["Recency"], 5, [5, 4, 3, 2, 1])
    rfm["F_Score"] = safe_qcut(rfm["Frequency"], 5, [1, 2, 3, 4, 5])
    rfm["M_Score"] = safe_qcut(rfm["Monetary"], 5, [1, 2, 3, 4, 5])

    rfm["R_Score"] = pd.to_numeric(rfm["R_Score"], errors="coerce").fillna(3).astype(int)
    rfm["F_Score"] = pd.to_numeric(rfm["F_Score"], errors="coerce").fillna(3).astype(int)
    rfm["M_Score"] = pd.to_numeric(rfm["M_Score"], errors="coerce").fillna(3).astype(int)

    def assign_segment(row):
        r, f = row["R_Score"], row["F_Score"]
        if r == 5 and f >= 4:
            return "Champions"
        elif f >= 4 and r >= 3:
            return "Loyal Customers"
        elif r >= 4 and f <= 3:
            return "Potential Loyalists"
        elif r <= 2 and f >= 3:
            return "At Risk"
        else:
            return "Others"

    rfm["Segment"] = rfm.apply(assign_segment, axis=1)

    seg_counts = rfm["Segment"].value_counts().reset_index()
    seg_counts.columns = ["Segment", "Count"]

    rfm["Revenue"] = rfm["Monetary"]
    seg_revenue = rfm.groupby("Segment")["Revenue"].sum().reset_index()

    col_p, col_q = st.columns(2)

    with col_p:
        fig_seg_cnt = px.bar(
            seg_counts,
            x="Segment",
            y="Count",
            title="Customer Count by RFM Segment",
            labels={"Count": "Customers", "Segment": "Segment"},
            color="Segment",
        )
        st.plotly_chart(fig_seg_cnt, width="stretch")
        st.caption("Number of customers in each RFM segment.")

    with col_q:
        fig_seg_rev = px.bar(
            seg_revenue,
            x="Segment",
            y="Revenue",
            title="Revenue by RFM Segment",
            labels={"Revenue": "Revenue (₹)", "Segment": "Segment"},
            color="Segment",
        )
        st.plotly_chart(fig_seg_rev, width="stretch")
        st.caption("Total revenue contributed by each RFM segment.")

# ════════════════════════════════════════════════════════════
# TAB 7 — AI Insights
# ════════════════════════════════════════════════════════════
with tabs[6]:
    st.subheader("🤖 AI-Assisted Analytical Insights")
    st.caption(
        "These insights are computed from the filtered dataset. "
        "They are analytical observations, not AI predictions."
    )
    st.markdown("---")

    # Compute insight values from filtered_df
    _ret_rate = filtered_df["Is_Returning_Customer"].mean() * 100 if "Is_Returning_Customer" in filtered_df.columns else 0
    _avg_rating = filtered_df["Customer_Rating"].mean() if "Customer_Rating" in filtered_df.columns else 0
    _avg_delivery = filtered_df["Delivery_Time_Days"].mean() if "Delivery_Time_Days" in filtered_df.columns else 0
    _disc_pct = filtered_df["Discount_Applied"].mean() * 100 if "Discount_Applied" in filtered_df.columns else 0

    _top_cat = (
        filtered_df.groupby("Product_Category")["Total_Amount"].sum().idxmax()
        if not filtered_df.empty else "N/A"
    )
    _top_cat_rev = (
        filtered_df.groupby("Product_Category")["Total_Amount"].sum().max()
        if not filtered_df.empty else 0
    )
    _top_cat_share = (
        _top_cat_rev / filtered_df["Total_Amount"].sum() * 100
        if filtered_df["Total_Amount"].sum() > 0 else 0
    )
    _top_city = (
        filtered_df.groupby("City")["Total_Amount"].sum().idxmax()
        if not filtered_df.empty else "N/A"
    )
    _top_city_aov = (
        filtered_df[filtered_df["City"] == _top_city]["Total_Amount"].mean()
        if not filtered_df.empty and _top_city in filtered_df["City"].values
        else 0
    )

    # Insight 1 — Returning customer rate
    if _ret_rate >= 60:
        st.success(
            f"**💡 Strong Customer Loyalty** \n\n"
            f"**Fact:** {_ret_rate:.1f}% of orders in the selected period are from returning customers. \n\n"
            f"**Interpretation:** A high retention rate signals that customers find value in repeat purchases. \n\n"
            f"**Suggested Action:** Invest in loyalty reward programmes to sustain and grow this cohort."
        )
    elif _ret_rate >= 40:
        st.info(
            f"**💡 Moderate Customer Retention** \n\n"
            f"**Fact:** {_ret_rate:.1f}% of orders come from returning customers. \n\n"
            f"**Interpretation:** Retention is at a moderate level; roughly half of sales depend on new acquisition. \n\n"
            f"**Suggested Action:** Introduce post-purchase email nurture flows and personalised recommendations."
        )
    else:
        st.warning(
            f"**⚠️ Low Returning Customer Rate** \n\n"
            f"**Fact:** Only {_ret_rate:.1f}% of orders are from returning customers. \n\n"
            f"**Interpretation:** The business is heavily reliant on new customer acquisition, which is costly. \n\n"
            f"**Suggested Action:** Prioritise retention strategies — loyalty points, personalised discounts, or re-engagement campaigns."
        )

    # Insight 2 — Average rating
    if _avg_rating >= 4.0:
        st.success(
            f"**⭐ High Customer Satisfaction** \n\n"
            f"**Fact:** The average customer rating across the selected data is {_avg_rating:.2f} / 5. \n\n"
            f"**Interpretation:** Customers are highly satisfied with their experience. \n\n"
            f"**Suggested Action:** Leverage positive sentiment in marketing and encourage reviews on external platforms."
        )
    elif _avg_rating >= 3.0:
        st.info(
            f"**⭐ Average Customer Satisfaction** \n\n"
            f"**Fact:** Average customer rating is {_avg_rating:.2f} / 5. \n\n"
            f"**Interpretation:** Satisfaction is acceptable but there is meaningful room for improvement. \n\n"
            f"**Suggested Action:** Identify the lowest-rated categories or cities and investigate root causes."
        )
    else:
        st.warning(
            f"**⚠️ Below-Average Customer Ratings** \n\n"
            f"**Fact:** Average rating is only {_avg_rating:.2f} / 5. \n\n"
            f"**Interpretation:** A significant portion of customers are dissatisfied. \n\n"
            f"**Suggested Action:** Conduct customer surveys; review fulfilment quality and product descriptions."
        )

    # Insight 3 — Delivery time
    if _avg_delivery > 0:
        if _avg_delivery <= 3:
            st.success(
                f"**🚚 Fast Delivery Performance** \n\n"
                f"**Fact:** Average delivery time is {_avg_delivery:.1f} days. \n\n"
                f"**Interpretation:** Delivery speed is a competitive advantage in the current selection. \n\n"
                f"**Suggested Action:** Highlight fast delivery in product listings and advertisements."
            )
        elif _avg_delivery <= 6:
            st.info(
                f"**🚚 Standard Delivery Times** \n\n"
                f"**Fact:** Average delivery time is {_avg_delivery:.1f} days. \n\n"
                f"**Interpretation:** Delivery is within standard industry range but may not be a differentiator. \n\n"
                f"**Suggested Action:** Explore last-mile partnerships to reduce delivery time in high-volume cities."
            )
        else:
            st.warning(
                f"**⚠️ Slow Delivery Times Detected** \n\n"
                f"**Fact:** Average delivery time is {_avg_delivery:.1f} days. \n\n"
                f"**Interpretation:** Longer delivery times may increase cart abandonment and reduce ratings. \n\n"
                f"**Suggested Action:** Audit fulfilment centres and carrier contracts; consider regional warehousing."
            )

    # Insight 4 — Discount penetration
    if _disc_pct >= 50:
        st.warning(
            f"**💸 High Discount Dependency** \n\n"
            f"**Fact:** {_disc_pct:.1f}% of orders received a discount. \n\n"
            f"**Interpretation:** More than half of orders are discount-driven, which may compress margins. \n\n"
            f"**Suggested Action:** Test reducing discount frequency on top-performing categories to protect margin."
        )
    else:
        st.info(
            f"**💸 Controlled Discount Usage** \n\n"
            f"**Fact:** {_disc_pct:.1f}% of orders received a discount. \n\n"
            f"**Interpretation:** Discount penetration is relatively contained; pricing power appears healthy. \n\n"
            f"**Suggested Action:** Use targeted discounts for at-risk customer segments rather than broad promotions."
        )

    # Insight 5 — Top category
    st.success(
        f"**🏆 Top Revenue Driver: {_top_cat}** \n\n"
        f"**Fact:** *{_top_cat}* generates {fmt_currency(_top_cat_rev)} in revenue, "
        f"representing {_top_cat_share:.1f}% of total revenue in this view. "
        f"The highest-revenue city is **{_top_city}** with an average order value of {fmt_currency(_top_city_aov)}. \n\n"
        f"**Interpretation:** Concentration in a single category and city can signal both strength and risk. \n\n"
        f"**Suggested Action:** Diversify marketing investment across under-performing categories "
        f"while protecting the leading segment's supply chain."
    )

# ════════════════════════════════════════════════════════════
# TAB 8 — Data Table
# ════════════════════════════════════════════════════════════
with tabs[7]:
    st.subheader("📋 Filtered Data Table")
    max_rows = 500
    display_df = filtered_df.head(max_rows)
    st.dataframe(display_df, width="stretch")
    st.caption(
        f"Showing {len(display_df):,} of {len(filtered_df):,} filtered rows "
        f"(display capped at {max_rows:,} rows)."
    )
