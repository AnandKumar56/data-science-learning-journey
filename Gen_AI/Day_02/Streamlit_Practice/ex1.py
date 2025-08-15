import streamlit as st

st.write("My First Streamlit App")
st.title("Hello World")
st.header("This is a header")
st.text("Enter a Name")
st.text_input("Enter Text")
a=st.number_input("Enter a Number")
st.button("Click Me")
st.selectbox("What Do You want to Select", ['Add','Subtract'])
st.checkbox("What Do You want to Check", ['Add','Subtract'])
st.radio("What Do You want to Radio", ['Add','Subtract'])
