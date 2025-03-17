import streamlit as st
import pandas as pd
import plotly.express as px

# 1º Add a text explaining what we are going to do
st.title('Airbnb Analysisssss')
# 2º Explore and show the data
df = pd.read_csv('airbnb.csv')

# 3º Create a table with selected columns
df_select = df[['name', 'neighbourhood_group', 'neighbourhood', 'price', 'reviews_per_month']]


st.dataframe(
    df_select.head(),
    column_config={
        'name': 'Apartment Name',
        'price': st.column_config.NumberColumn(
            label='Price ($)',
            format='%.2f'
        ),
        'reviews_per_month': st.column_config.ProgressColumn(
            label='Notas por mes',
            format='%d'  
        )
    }
)

# 4º Represent the top 10 hosts with the most Airbnb listings
fig = px.box(df_select, x='neighbourhood', y='price', title="Price Distribution by Neighbourhood")
st.plotly_chart(fig)


# Sidebar Filters
st.sidebar.header("Filters")
neighborhoods = st.sidebar.multiselect("Select Neighborhoods", df['neighbourhood'].unique(), default=df['neighbourhood'].unique())
room_types = st.sidebar.multiselect("Select Room Types", df['room_type'].unique(), default=df['room_type'].unique())

# Apply Filters
df_filtered = df[(df['neighbourhood'].isin(neighborhoods)) & (df['room_type'].isin(room_types))]

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


## 9º Create a map with all the listings in that neighbourhood


## 10º Create a new tab
