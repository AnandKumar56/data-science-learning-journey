import google.generativeai as genai
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

# place your .env file here
Gemini_api_key=os.getenv("GEMINI_API_KEY")
from PIL import Image

uploaded_file=st.file_uploader("Upload an image file",type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    img = Image.open(uploaded_file)

# View the uploaded image
    st.image(img, caption='Uploaded Image')

# Configure API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

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