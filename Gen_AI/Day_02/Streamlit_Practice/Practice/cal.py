'''Number Input & Simple Math

Ask for two numbers and display:

Their sum

Their product
Goal: Practice st.number_input() and basic calculations.'''

import streamlit as st

num1=st.number_input("Enter First Number:")
num2=st.number_input("Enter Second Number:")

st.write(f"Sum of {num1} and {num2} is: {int(num1) + int(num2)}")