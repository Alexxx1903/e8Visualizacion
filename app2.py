import streamlit as st
import pandas as pd
import plotly.express as px

# Load Data (Hardcoded CSV File)
st.title("Pablo Gil-Antuñano's Airbnb Dashboard")
file_path = "airbnb.csv"  # Ensure this file is in the correct directory
df = pd.read_csv(file_path)

# Data Cleaning
df = df.dropna(subset=['room_type', 'neighbourhood', 'price', 'reviews_per_month'])

# Sidebar Navigation
st.sidebar.title("Sidebar Navigation")
sidebar_tab = st.sidebar.radio("Choose a tab:", ["Filters", "Settings"])

if sidebar_tab == "Filters":
    st.sidebar.header("Filters")
    neighborhoods = st.sidebar.multiselect("Select Neighborhoods", df['neighbourhood'].unique(), default=df['neighbourhood'].unique())
    room_types = st.sidebar.multiselect("Select Room Types", df['room_type'].unique(), default=df['room_type'].unique())
    df_filtered = df[(df['neighbourhood'].isin(neighborhoods)) & (df['room_type'].isin(room_types))]

elif sidebar_tab == "Settings":
    st.sidebar.header("Settings")
    dark_mode = st.sidebar.toggle("Enable Dark Mode")
    notifications = st.sidebar.checkbox("Enable Notifications")
    df_filtered = df  # Keep unfiltered dataset for now

# Tabs
tab1, tab2 = st.tabs(["Listing Analysis", "Review Trends"])

# Tab 1: Listing Analysis
with tab1:
    st.header("Listing Type vs. Number of People")
    fig1 = px.box(df_filtered, x='room_type', y='minimum_nights', color='room_type', title="Minimum Nights by Listing Type")
    st.plotly_chart(fig1)

    st.header("Price Distribution by Listing Type")
    fig2 = px.box(df_filtered, x='room_type', y='price', color='room_type', title="Price Distribution by Listing Type")
    st.plotly_chart(fig2)

# Tab 2: Review Trends
with tab2:
    st.header("Top Reviewed Apartments by Neighborhood")
    top_reviews = df_filtered.groupby(['neighbourhood', 'name'])['reviews_per_month'].max().reset_index()
    fig3 = px.bar(top_reviews, x='neighbourhood', y='reviews_per_month', color='name', title="Top Apartments by Reviews per Month")
    st.plotly_chart(fig3)
