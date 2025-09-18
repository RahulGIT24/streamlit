import streamlit as st
import pandas as pd

st.title('Chai Sales')

file=st.file_uploader('Upload Your CSV File',type=['csv'])

if file:
    df=pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(df)

if file:
    st.subheader("Summary Stats")
    st.write(df.describe())

if file:
    cities=df['City'].unique()
    selected_city=st.selectbox("Filter by cities",cities)
    filtered_data=df[df["City"]==selected_city]
    st.subheader("Filtered data")
    st.dataframe(filtered_data)