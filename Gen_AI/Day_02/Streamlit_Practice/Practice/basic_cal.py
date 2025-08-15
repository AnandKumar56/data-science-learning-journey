'''Number Input & Simple Math

Ask for two numbers and display:

Their sum

Their product
Goal: Practice st.number_input() and basic calculations.'''

import streamlit as st

# Number Input & Simple Math
number1=st.number_input("Enter First Number:")
number2=st.number_input("Enter Second Number:")

st.write(f"Sum of {number1} and {number2} is : {int(number1) + int(number2)}")
st.write(f"Product of {number1} and {number2} is : {int(number1) * int(number2)}")