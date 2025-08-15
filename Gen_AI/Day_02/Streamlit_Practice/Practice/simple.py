'''Simple Text Input & Display

Take a user’s name as input and display:
"Hello, <name>! Welcome to Streamlit."
Goal: Learn st.text_input() and dynamically display values.'''

import streamlit as st

username = st.text_input("Enter your name:")

st.write(f"Hello, {username}! Welcome to Streamlit.")