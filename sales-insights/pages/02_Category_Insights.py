import streamlit as st
import pandas as pd

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("sales-insights/data/Sample - Superstore.csv", encoding="latin1")

df = load_data()

st.title("📦 Category Insights")

# Sales by Category
st.subheader("Sales by Category")
category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
st.bar_chart(category_sales)

# Profit by Sub-Category
st.subheader("Profit by Sub-Category")
subcategory_profit = df.groupby("Sub-Category")["Profit"].sum().sort_values(ascending=False)
st.bar_chart(subcategory_profit)

# 🔥 Novelty Insight: High-Risk Categories (Loss-Making Subcategories)
st.subheader("⚠️ High-Risk Categories")
loss_subcats = df.groupby("Sub-Category")["Profit"].sum()
loss_subcats = loss_subcats[loss_subcats < 0].sort_values()
if not loss_subcats.empty:
    st.write("These subcategories consistently make a **loss** and are high-risk for the business:")
    st.bar_chart(loss_subcats)
else:
    st.write("No categories are running in loss! ✅")

# 🔥 Novelty Insight: Profit-to-Sales Ratio (Efficiency by Sub-Category)
st.subheader("💡 Profit-to-Sales Ratio (Unique Insight)")
ratio = (df.groupby("Sub-Category")["Profit"].sum() / df.groupby("Sub-Category")["Sales"].sum()).sort_values(ascending=False)
st.write("This ratio shows **how much profit is generated for every dollar of sales**.")
st.bar_chart(ratio)
