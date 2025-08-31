import google.generativeai as genai
import streamlit as st
from PIL import Image

uploaded_file=st.file_uploader("Upload an image file",type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    img = Image.open(uploaded_file)

# View the uploaded image
    st.image(img, caption='Uploaded Image')

# Configure API key
genai.configure(api_key="AIzaSyA8OBB4ifoqznOX_2F1T_HorTW9DmY_4Gw")

# Create model instance
model = genai.GenerativeModel("gemini-2.5-flash")

st.header("Image Anaytics App")

# Give Your Prompt here
user_input = st.text_input("Enter your prompt here:")

# Generate response
if st.button("Generate Response"):
    img=Image.open(uploaded_file)
    model= genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content([user_input,img])
    st.markdown(response.text)