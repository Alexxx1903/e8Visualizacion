import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Alejandro's Airbnb Analysis")
def load_data():
    df = pd.read_csv("airbnb.csv") 
    df = df.rename(columns={"room_type": "listing_type", "neighbourhood": "neighborhood"})
    df.dropna(subset=["price"], inplace=True)
    return df

df = load_data()

st.sidebar.header("Airbnb Filters")
listing_types = st.sidebar.multiselect("Select the listing types", df["listing_type"].unique(), default=df["listing_type"].unique())
neighborhoods = st.sidebar.multiselect("Select the neighborhoods", df["neighborhood"].unique(), default=df["neighborhood"].unique())
filtered_df = df[(df["listing_type"].isin(listing_types)) & (df["neighborhood"].isin(neighborhoods))]


analysis, simu = st.tabs(["Analysis", "Simulator for extra points"])
with analysis:
    col1, col2 = st.columns(2)
    with col1:
        fig1 = px.box(filtered_df, x="listing_type", y="minimum_nights", title="Minimum nights by listing type",color_discrete_sequence=["#FF5733", "#33FF57", "#3357FF"])
        st.plotly_chart(fig1)
    with col2:
        fig2 = px.box(filtered_df, x="listing_type", y="price", title="Price by listing type")
        st.plotly_chart(fig2)
    
    top_reviews = filtered_df.groupby(["neighborhood", "listing_type"]).agg({"reviews_per_month": "sum"}).reset_index()
    fig3 = px.bar(top_reviews, x="neighborhood", y="reviews_per_month", color="listing_type", title="Most reviewed apartments per month by neighborhood")
    st.plotly_chart(fig3)
    fig4 = px.box(filtered_df, x="listing_type", y="reviews_per_month", title="Reviews per Month by Listing Type")
    st.plotly_chart(fig4)
    fig5 = px.scatter(filtered_df, x="availability_365", y="price", color="listing_type", title="Availability vs Price")
    st.plotly_chart(fig5)

with simu:
    st.header("Price Simulator")
    selected_neighborhood = st.selectbox("Select a neighborhood", df["neighborhood"].unique())
    selected_type = st.selectbox("Select listing type", df["listing_type"].unique())
    num_nights = st.slider("Number of nights", 1, 30, 2)
    similar_listings = df[(df["neighborhood"] == selected_neighborhood) & (df["listing_type"] == selected_type) & (df["minimum_nights"] >= num_nights)]
    price_range = (similar_listings["price"].quantile(0.25), similar_listings["price"].quantile(0.75))
    
    st.write(f"Recommended price range: ${price_range[0]:.1f} - ${price_range[1]:.1f}")


secondaryBackgroundColor = "#333333"


