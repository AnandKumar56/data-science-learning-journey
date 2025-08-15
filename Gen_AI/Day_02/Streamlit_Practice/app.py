import streamlit as st

st.write("My First Streamlit App")
st.title("Hello Everyone")
st.header("This is a header")

name =st.text("Enter a Name")
st.text_input("Enter Text")

st.title("This is 'button'")

if st.button("Click Me"):
    st.write("Hi there!")
else:
    st.write(f"Goodbye!")