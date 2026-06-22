import sys
import os

# Fix import issue
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

import streamlit as st
import pandas as pd
import plotly.express as px

from analytics.data_loader import load_data
from analytics.cleaning import clean_data
from analytics.kpi import calculate_kpis
from analytics.forecasting import monthly_sales_forecast
from ai.recommendation_engine import generate_recommendations

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI-Powered Enterprise Analytics Platform",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI-Powered Enterprise Analytics Platform")
st.markdown("Business Intelligence • Data Analytics • AI Insights")

# --------------------------------------------------
# Load Data
# --------------------------------------------------

df = load_data("data/raw/sales_data.csv")

clean_df, report = clean_data(df)
st.sidebar.header("🔍 Filters")

selected_region = st.sidebar.selectbox(
    "Region",
    ["All"] + sorted(clean_df["Region"].unique().tolist())
)

selected_category = st.sidebar.selectbox(
    "Category",
    ["All"] + sorted(clean_df["Category"].unique().tolist())
)

selected_segment = st.sidebar.selectbox(
    "Segment",
    ["All"] + sorted(clean_df["Segment"].unique().tolist())
)

filtered_df = clean_df.copy()

if selected_region != "All":
    filtered_df = filtered_df[
        filtered_df["Region"] == selected_region
    ]

if selected_category != "All":
    filtered_df = filtered_df[
        filtered_df["Category"] == selected_category
    ]

if selected_segment != "All":
    filtered_df = filtered_df[
        filtered_df["Segment"] == selected_segment
    ]
if filtered_df.empty:
    st.warning("No data available for selected filters.")
    st.stop()

kpis = calculate_kpis(filtered_df)
recommendations = generate_recommendations(kpis)

# --------------------------------------------------
# KPI Section
# --------------------------------------------------

st.subheader("📈 Business KPIs")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "💰 Total Revenue",
        f"${kpis['total_revenue']:,.2f}"
    )

with col2:
    st.metric(
        "📊 Total Profit",
        f"${kpis['total_profit']:,.2f}"
    )

with col3:
    st.metric(
        "🛒 Orders",
        kpis["total_orders"]
    )

with col4:
    st.metric(
        "👥 Customers",
        kpis["total_customers"]
    )

st.divider()

# --------------------------------------------------
# Monthly Sales Trend
# --------------------------------------------------

st.subheader("📈 Monthly Sales Trend")

forecast_df = monthly_sales_forecast(filtered_df.copy())

fig = px.line(
    forecast_df,
    x="Order Date",
    y="Sales",
    markers=True,
    title="Monthly Revenue Trend"
)

st.plotly_chart(fig, width="stretch")

st.divider()

# --------------------------------------------------
# Top Performers
# --------------------------------------------------

st.subheader("🏆 Top Performers")

col1, col2 = st.columns(2)

with col1:
    st.success(
        f"Top Product:\n\n{kpis['top_product']}"
    )

with col2:
    st.success(
        f"Top Customer:\n\n{kpis['top_customer']}"
    )

st.divider()

# --------------------------------------------------
# Revenue by Category
# --------------------------------------------------

st.subheader("📦 Revenue by Category")

category_sales = (
    filtered_df.groupby("Category")["Sales"]
    .sum()
    .reset_index()
)

fig_category = px.bar(
    category_sales,
    x="Category",
    y="Sales",
    title="Revenue by Category"
)

st.plotly_chart(fig_category, width="stretch")

# --------------------------------------------------
# Revenue by Region
# --------------------------------------------------

st.subheader("🌎 Revenue by Region")

region_sales = (
    filtered_df.groupby("Region")["Sales"]
    .sum()
    .reset_index()
)

fig_region = px.pie(
    region_sales,
    names="Region",
    values="Sales",
    title="Regional Revenue Distribution"
)

st.plotly_chart(fig_region, width="stretch")

# --------------------------------------------------
# Top 10 Products
# --------------------------------------------------

st.subheader("🔥 Top 10 Products")

top_products = (
    filtered_df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig_products = px.bar(
    top_products,
    x="Sales",
    y="Product Name",
    orientation="h",
    title="Top 10 Products by Revenue"
)

st.plotly_chart(fig_products, width="stretch")

# --------------------------------------------------
# Dataset Preview
# --------------------------------------------------

st.subheader("📄 Dataset Preview")
st.dataframe(
    filtered_df.head(20),
    width="stretch"
)
# --------------------------------------------------
# Export Data
# --------------------------------------------------

st.subheader("⬇️ Export Data")

csv = filtered_df.to_csv(index=False)

st.download_button(
    label="Download Filtered Dataset",
    data=csv,
    file_name="filtered_sales_data.csv",
    mime="text/csv"
)

# --------------------------------------------------
# Data Quality Report
# --------------------------------------------------

st.subheader("🧹 Data Quality Report")

st.json(report)
st.divider()

# --------------------------------------------------
# AI Recommendations
# --------------------------------------------------

st.subheader("🤖 AI Business Recommendations")

for rec in recommendations:
    st.info(rec)