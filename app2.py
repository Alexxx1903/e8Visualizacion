import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")


## 1º Add a text which explain what we are going to do
st.title('AirBnb Analysis2')

## 2º Explore and show the data
df = pd.read_csv("C:/Users/aleja/Desktop/cristianismo/airbnb.csv")

## 3º Create a table with the name of the apartment, neighbourhood_group, neighbourhood, price and reviews_per_month


## 4º Represent the top 10 host with more airbnb hostings


## 5º Instead of table, do it in a plotly chart, in the hover include the price
## pip install plotly


## 6º Instead of Top 10, make it a choice for the user


## 7º Create a boxplot for the prices for Neighbourhood groups



## 8º Create a boxplot for the prices for neighbourhood after selecting one neighbourhood group


## 9º Create a map with all the listings in that neighbourhood


## 10º Create a new tab 