import streamlit as st
import pandas as pd
import plotly.express as px

# 1º Add a text explaining what we are going to do
st.title('Airbnb Analysis')
# 2º Explore and show the data
df = pd.read_csv('airbnb.csv')

st.sidebar.title("Sidebar Navigation")

# Create Sidebar Tabs using Radio Buttons
sidebar_tab = st.sidebar.radio("Choose a tab:", ["Filters", "Settings"])

if sidebar_tab == "Filters":
    st.sidebar.subheader("Filter Options")
    neighborhoods = st.sidebar.multiselect("Select Neighborhoods", ["Centro", "Latina", "Salamanca"])
    room_types = st.sidebar.multiselect("Select Room Types", ["Entire home/apt", "Private room", "Shared room"])

elif sidebar_tab == "Settings":
    st.sidebar.subheader("App Settings")
    dark_mode = st.sidebar.toggle("Enable Dark Mode")
    notifications = st.sidebar.checkbox("Enable Notifications")

