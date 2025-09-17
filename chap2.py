import streamlit as st

st.title("Chai Maker App")

# widgets

if st.button("Make Coffee"):
    st.success("Button Clicked")

add_shots = st.checkbox("Add Shots")

if add_shots:
    st.success("Shots Added")

tea_types = st.radio("Pick your pizza base: ",["Maida","Wheat","Barley"])
st.write(tea_types)

languages=st.selectbox("Choose Languages: ",["C++","Python","Java"])

st.write(languages)

age = st.slider("Age ",0,50,4) # start,end,default value
st.write("Your age is ",age)

# User inputs
langs=st.number_input("How many languages do you know?",min_value=1,max_value=3)
st.write(f"Selected languages user know is ",langs)

name=st.text_input("Enter your name")
if name:
    st.write("Good Evening ",name)

dob=st.date_input("Enter your DOB")
if dob:
    st.write(dob)