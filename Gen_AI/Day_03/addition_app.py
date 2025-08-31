import streamlit as st

st.title("Addition Application")
a = st.number_input("Enter the Number1 :")
b = st.number_input("Enter the Number2 :")

if st.button('add'):
    c=a+b
    st.success(f"The Addition of {a} and {b} is {c}")