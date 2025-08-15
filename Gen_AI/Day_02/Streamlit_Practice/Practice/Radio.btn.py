'''Radio Button Mood Selector

Ask the user to select their mood using st.radio()

Display a matching emoji based on selection.
Example:

Happy → 😀

Sad → 😢'''

import streamlit as st

# Radio Button Mood Selector
mood=st.radio("How are you feeling today?", 
              ('Happy', 'Sad'))

if mood == 'Happy':
    st.write("You are feeling happy! 😀")
elif mood == 'Sad':
    st.write("You are feeling sad! 😢")