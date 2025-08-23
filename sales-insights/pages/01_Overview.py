import streamlit as st
import pandas as pd

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("sales-insights/data/Sample - Superstore.csv", encoding="latin1")

df = load_data()

st.title("📊 Sales Overview")

# Show dataset preview
st.subheader("Sample Data")
st.dataframe(df.head())

# KPIs
st.subheader("Key Metrics")
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
total_customers = df["Customer ID"].nunique()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Sales", f"${total_sales:,.0f}")
col2.metric("Total Profit", f"${total_profit:,.0f}")
col3.metric("Total Orders", total_orders)
col4.metric("Unique Customers", total_customers)

# Sales by Region
st.subheader("Sales by Region")
region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
st.bar_chart(region_sales)

# 🔥 Novelty Insight: Profitability Efficiency (Profit per Order)
st.subheader("🔥 Profitability Efficiency")
df["Profit_per_Order"] = df["Profit"] / df["Order ID"].map(df.groupby("Order ID")["Order ID"].count())
efficiency = df.groupby("Region")["Profit_per_Order"].mean().sort_values(ascending=False)
st.write("This metric shows **how much profit is generated per order**, which is a novel way to measure efficiency.")
st.bar_chart(efficiency)
