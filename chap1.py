import streamlit as st

st.title("Streamlit Tutorial Title")
st.subheader("Brewed with Streamlit")
st.text("Welcome to Streamlit")
st.write("Choose Your Fav. Coffee")

coffee = st.selectbox("Your fav coffee: ",["Cold Coffee","Black Coffee","Hot Coffee","Matcha"])

st.write(f"You selected {coffee}. Excellent Choice")

st.success("Your Coffee has been brewed")

