# layouts
import streamlit as st

st.title("Lets Understand Layouts")

col1,col2=st.columns(2)

with col1:
    st.header("Programming Languages")
    st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png',width=100)
    vote1 = st.button("Vote Python")

with col2:
    st.header("Programming Languages")
    st.image('https://upload.wikimedia.org/wikipedia/commons/1/18/ISO_C%2B%2B_Logo.svg',width=100)
    vote2 = st.button("Vote C++")

if vote1:
    st.success("Vote Registered for python")
elif vote2:
    st.success("Vote Registered for C++")

# sidebar
name=st.sidebar.text_input("Enter your name")

with st.expander("How to compile a file in java"):
    st.write("""
    1. Create a file with .java extension
    2. Add java code inside that file
    3. Open terminal in that folder where file reside
    4. Run javac filename.java
    5. Bytecode get generated with classname and along with .class extension
""")

st.markdown("### Markdown Heading")
st.markdown("> Boilerplate 1")