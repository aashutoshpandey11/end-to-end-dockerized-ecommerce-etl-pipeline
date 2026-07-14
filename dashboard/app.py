import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="E-Commerce ETL Dashboard",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# Database Connection
# -----------------------------
@st.cache_resource
def get_engine():
    return create_engine(
        "postgresql://postgres:postgresql@localhost:5433/ecommerce_db"
    )

engine = get_engine()

@st.cache_data
def load_data():
    return pd.read_sql(
        "SELECT * FROM public.products",
        engine
    )

df = load_data()


# -----------------------------
# Sidebar Filters
# -----------------------------
st.sidebar.header("🔍 Filters")

# Search Box
search = st.sidebar.text_input("Search Product")

# Category Filter
categories = sorted(df["category"].unique())

selected_category = st.sidebar.selectbox(
    "Category",
    ["All"] + categories
)

# Price Range Filter
min_price = float(df["product_price"].min())
max_price = float(df["product_price"].max())

price_range = st.sidebar.slider(
    "Price Range",
    min_price,
    max_price,
    (min_price, max_price)
)

# Rating Filter
rating = st.sidebar.slider(
    "Minimum Rating",
    0.0,
    5.0,
    0.0,
    0.1
)

# Refresh Button
if st.sidebar.button("🔄 Refresh"):
    load_data.clear()
    st.success("Data refreshed!")
    st.rerun()

# -----------------------------
# Apply Filters
# -----------------------------
filtered_df = df.copy()


# Search
if search:
    filtered_df = filtered_df[
        filtered_df["title"].str.contains(
            search,
            case=False,
            na=False
        )
    ]

# Category
if selected_category != "All":
    filtered_df = filtered_df[
        filtered_df["category"] == selected_category
    ]

# Price
filtered_df = filtered_df[
    (filtered_df["product_price"] >= price_range[0]) &
    (filtered_df["product_price"] <= price_range[1])
]

# Rating
filtered_df = filtered_df[
    filtered_df["rating"] >= rating
]

# -----------------------------
# No Data Check
# -----------------------------
if filtered_df.empty:
    st.warning("⚠️ No products match the selected filters.")
    st.stop()


# -----------------------------
# Dashboard Title
# -----------------------------
st.title("📊 Cloud-Based Automated E-Commerce ETL Dashboard")
st.markdown("### Real-Time Analytics from PostgreSQL")

st.divider()

# -----------------------------
# KPI Calculations
# -----------------------------
total_products = len(filtered_df)

total_categories = filtered_df["category"].nunique()

average_price = filtered_df["product_price"].mean()

average_rating = filtered_df["rating"].mean()

highest_price = filtered_df["product_price"].max()

lowest_price = filtered_df["product_price"].min()

#----------------------------
#KPI Cards - Row 1
#----------------------------
col1, col2, col3 = st.columns(3)

col1.metric(
    "🛍 Total Products",
    total_products
)

col2.metric(
    "📂 Categories",
    total_categories
)

col3.metric(
    "⭐ Average Rating",
    f"{average_rating:.2f}"
)

# -----------------------------
# KPI Cards - Row 2
# -----------------------------
col4, col5, col6 = st.columns(3)

col4.metric(
    "💲 Average Price",
    f"${average_price:.2f}"
)

col5.metric(
    "📈 Highest Price",
    f"${highest_price:.2f}"
)

col6.metric(
    "📉 Lowest Price",
    f"${lowest_price:.2f}"
)

st.divider()



# =====================================================
# Database Statistics
# =====================================================

st.subheader("🗄️ Database Statistics")

stat1, stat2, stat3, stat4 = st.columns(4)

# Total Records
stat1.metric(
    "📦 Total Records",
    len(df)
)

# Total Columns
stat2.metric(
    "📑 Total Columns",
    len(df.columns)
)

# Missing Values
stat3.metric(
    "⚠️ Missing Values",
    int(df.isnull().sum().sum())
)

# Memory Usage
memory_usage = df.memory_usage(deep=True).sum() / 1024

stat4.metric(
    "💾 Memory Usage",
    f"{memory_usage:.2f} KB"
)

st.divider()


# =====================================================
# Data Quality Report
# =====================================================

st.subheader("📋 Data Quality Report")

quality_col1, quality_col2 = st.columns(2)

# -----------------------------
# Left Side - Dataset Information
# -----------------------------
with quality_col1:

    st.markdown("### 📊 Dataset Summary")

    summary_df = pd.DataFrame({
        "Metric": [
            "Rows",
            "Columns",
            "Duplicate Rows",
            "Missing Values"
        ],
        "Value": [
            len(df),
            len(df.columns),
            df.duplicated().sum(),
            df.isnull().sum().sum()
        ]
    })

    st.dataframe(
        summary_df,
        use_container_width=True,
        hide_index=True
    )

# -----------------------------
# Right Side - Missing Values
# -----------------------------
with quality_col2:

    st.markdown("### ⚠️ Missing Values by Column")

    missing_df = pd.DataFrame({
        "Column": df.columns,
        "Missing Values": df.isnull().sum().values
    })

    st.dataframe(
        missing_df,
        use_container_width=True,
        hide_index=True
    )

st.divider()


# =====================================================
# Charts
# =====================================================

chart1, chart2 = st.columns(2)

# -----------------------------
# Chart 1
# -----------------------------
with chart1:

    st.subheader("📦 Products by Category")

    category_count = (
        filtered_df
        .groupby("category")
        .size()
        .reset_index(name="Total Products")
    )

    fig_category = px.bar(
        category_count,
        x="category",
        y="Total Products",
        color="category",
        text="Total Products",
        title="Products Available in Each Category"
    )

    fig_category.update_traces(
        textposition="outside"
    )

    fig_category.update_layout(
        showlegend=False,
        height=450
    )

    st.plotly_chart(
        fig_category,
        use_container_width=True
    )

# -----------------------------
# Chart 2
# -----------------------------
with chart2:

    st.subheader("💰 Average Price by Category")

    avg_price = (
        filtered_df
        .groupby("category")["product_price"]
        .mean()
        .reset_index()
    )

    fig_price = px.bar(
        avg_price,
        x="category",
        y="product_price",
        color="category",
        text_auto=".2f",
        title="Average Product Price"
    )

    fig_price.update_layout(
        showlegend=False,
        height=450,
        yaxis_title="Average Price ($)"
    )

    st.plotly_chart(
        fig_price,
        use_container_width=True
    )

st.divider()

# =====================================================
# Charts - Row 2
# =====================================================

chart3, chart4 = st.columns(2)

# =====================================================
# Category Distribution (Pie Chart)
# =====================================================
with chart3:

    st.subheader("🥧 Category Distribution")

    category_share = (
        filtered_df
        .groupby("category")
        .size()
        .reset_index(name="Products")
    )

    fig_pie = px.pie(
        category_share,
        names="category",
        values="Products",
        title="Product Share by Category",
        hole=0.45
    )

    fig_pie.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )

    fig_pie.update_layout(
        height=500
    )

    st.plotly_chart(
        fig_pie,
        use_container_width=True
    )

# =====================================================
# Rating Distribution (Histogram)
# =====================================================
with chart4:

    st.subheader("⭐ Rating Distribution")

    fig_rating = px.histogram(
        filtered_df,
        x="rating",
        nbins=10,
        title="Distribution of Product Ratings",
        color_discrete_sequence=["orange"]
    )

    fig_rating.update_layout(
        xaxis_title="Rating",
        yaxis_title="Number of Products",
        height=500
    )

    st.plotly_chart(
        fig_rating,
        use_container_width=True
    )

st.divider()


# =====================================================
# Charts - Row 3
# =====================================================

chart5, chart6 = st.columns(2)

# =====================================================
# Price vs Rating
# =====================================================

with chart5:

    st.subheader("📈 Price vs Rating")

    fig_scatter = px.scatter(
        filtered_df,
        x="product_price",
        y="rating",
        color="category",
        hover_name="title",
        size="rating",
        title="Relationship Between Price and Rating"
    )

    fig_scatter.update_layout(
        height=500
    )

    st.plotly_chart(
        fig_scatter,
        use_container_width=True
    )



# =====================================================
# Top 10 Most Expensive Products
# =====================================================

with chart6:

    st.subheader("🏆 Top 10 Most Expensive Products")

    top10 = (
        filtered_df
        .sort_values(
            by="product_price",
            ascending=False
        )
        .head(10)
    )

    fig_top = px.bar(
        top10,
        x="product_price",
        y="title",
        orientation="h",
        color="product_price",
        title="Top 10 Expensive Products"
    )

    fig_top.update_layout(
        height=500,
        yaxis={
            "categoryorder": "total ascending"
        }
    )

    st.plotly_chart(
        fig_top,
        use_container_width=True
    )

st.divider()

# =====================================================
# Category Summary
# =====================================================

st.subheader("📋 Category Summary")

summary = (
    filtered_df
    .groupby("category")
    .agg(
        Total_Products=("title", "count"),
        Average_Price=("product_price", "mean"),
        Average_Rating=("rating", "mean"),
        Maximum_Price=("product_price", "max"),
        Minimum_Price=("product_price", "min")
    )
    .reset_index()
)

summary["Average_Price"] = summary["Average_Price"].round(2)
summary["Average_Rating"] = summary["Average_Rating"].round(2)

st.dataframe(
    summary,
    use_container_width=True
)

st.divider()


# -----------------------------
# Download Button
# -----------------------------
st.download_button(
    label="📥 Download Filtered Data",
    data=filtered_df.to_csv(index=False),
    file_name="filtered_products.csv",
    mime="text/csv"
)

# -----------------------------
# Interactive Product Explore
# -----------------------------
st.subheader("📦 Product Explore")

st.write(f"Showing **{len(filtered_df)}** product(s).")

# Select columns to display
selected_columns = st.multiselect(
    "Select Columns to Display",
    options=filtered_df.columns.tolist(),
    default=filtered_df.columns.tolist()
)

# Display selected columns
if selected_columns:

    st.dataframe(
        filtered_df[selected_columns],
        use_container_width=True,
        hide_index=True
    )

else:

    st.warning("Please select at least one column.")


# =====================================================
# Dashboard Footer
# =====================================================

st.caption(
    "Built with using Streamlit, PostgreSQL, Docker, SQLAlchemy and Plotly"
)