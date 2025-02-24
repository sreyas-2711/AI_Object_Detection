import numpy as np
import altair as alt
import pandas as pd
import streamlit as st
import groqtest
import time
a = 0
st.header('Object-image identification')

uploaded_file = st.camera_input("Capture an Image")
timestamp = time.strftime("%Y%m%d_%H%M%S")  
image_path = f"captured_image_{timestamp}.jpg"
if uploaded_file is not None:
    # Save the image to a specified path
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getvalue())
    st.success("Image saved successfully!")

col1, col2, col3, col4 = st.columns(4)
if "output" not in st.session_state:
    st.session_state.output = ""
def reset():
    st.session_state.output = ""

with col1:
     if st.button('Experiments'):
          a = 1
with col2:
     if st.button('Quiz and questions.'):
          a = 2
with col3:
     if st.button("Reset"):
           reset()

if a == 1:
     st.write(groqtest.get_groq_response(image_path))
if a == 2:
     st.write(groqtest.get_groq_quiz(image_path))
