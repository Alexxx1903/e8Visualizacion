import streamlit as st
import pandas as pd
import plotly.express as px

# 1º Add a text explaining what we are going to do
st.title('Airbnb Analysis')
# 2º Explore and show the data
df = pd.read_csv("airbnb.csv")

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


## 5º Instead of table, do it in a plotly chart, in the hover include the price



## 6º Instead of Top 10, make it a choice for the user


## 7º Create a boxplot for the prices for Neighbourhood groups



## 8º Create a boxplot for the prices for neighbourhood after selecting one neighbourhood group


## 9º Create a map with all the listings in that neighbourhood


## 10º Create a new tab
