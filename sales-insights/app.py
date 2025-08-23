import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales Insights", layout="wide")

# ---------------------------
# 🔹 Title with Author Branding
# ---------------------------
st.title("📊 Sales Insights Dashboard - by Prakash Mishra")

# ---------------------------
# 🔹 Sidebar Branding
# ---------------------------
st.sidebar.markdown("### 👨‍💻 Created by: **Prakash Mishra**")
st.sidebar.info("This dashboard provides insights into sales, profit, and trends.\n\n© 2025 Prakash Mishra")

# ---------------------------
# 🔹 Load dataset
# ---------------------------
df = pd.read_csv("sales-insights/data/Sample - Superstore.csv", encoding="cp1252")

# ---------------------------
# 🔹 Show first rows
# ---------------------------
st.subheader("Raw Data Preview")
st.dataframe(df.head(20))

# ---------------------------
# 🔹 Sales by Category
# ---------------------------
st.subheader("Sales by Category")
category_sales = df.groupby("Category")["Sales"].sum().reset_index()
fig1 = px.bar(category_sales, x="Category", y="Sales", title="Sales by Category")
st.plotly_chart(fig1, use_container_width=True)

# ---------------------------
# 🔹 Sales by Region
# ---------------------------
st.subheader("Sales by Region")
region_sales = df.groupby("Region")["Sales"].sum().reset_index()
fig2 = px.pie(region_sales, names="Region", values="Sales", title="Sales by Region")
st.plotly_chart(fig2, use_container_width=True)

# ---------------------------
# 🔹 Sales Trend over Time
# ---------------------------
st.subheader("Sales Trend Over Time")
df["Order Date"] = pd.to_datetime(df["Order Date"])
time_sales = df.groupby("Order Date")["Sales"].sum().reset_index()
fig3 = px.line(time_sales, x="Order Date", y="Sales", title="Sales Over Time")
st.plotly_chart(fig3, use_container_width=True)

# ---------------------------
# 🔹 Footer Branding (Non-removable credit)
# ---------------------------
st.markdown("---")
st.markdown("🔒 **Project Author: Prakash Mishra** | © 2025 All Rights Reserved")
