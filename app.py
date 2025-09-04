# streamlit_app.py
import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
import os

# --------------------------
# Load the trained model
# --------------------------
MODEL_PATH = "scene_classification_final.keras"
model = load_model(MODEL_PATH)

# Scene categories
class_names = ['buildings', 'forest', 'glacier', 'mountain', 'sea', 'street']

# Scene colors for dynamic header
scene_colors = {
    'buildings': '#FFD700',  # gold
    'forest': '#228B22',     # forest green
    'glacier': '#00BFFF',    # deep sky blue
    'mountain': '#A0522D',   # sienna
    'sea': '#1E90FF',        # dodger blue
    'street': '#808080'      # gray
}

# --------------------------
# Streamlit UI
# --------------------------
st.set_page_config(page_title="Scene Classification App", layout="wide")
st.title("🌄 Scene Classification App 🏙️")

st.markdown("""
Welcome! This app classifies images into **6 types of scenes**.  

**Supported scene categories:**  
- Buildings 🏢  
- Forest 🌲  
- Glacier 🏔️  
- Mountain ⛰️  
- Sea 🌊  
- Street 🛣️  

**Instructions:**  
- Upload a clear image of **one of these scenes**.  
- Make sure the scene is **mostly visible**, not too cluttered.  
- Supported formats: jpg, jpeg, png.  
""")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg","jpeg","png"])

if uploaded_file is not None:
    # Load the image
    img = Image.open(uploaded_file).convert('RGB')
    st.image(img, caption='Uploaded Image', use_container_width=True)
    
    # Preprocess the image
    IMG_HEIGHT = 150
    IMG_WIDTH = 150
    img_resized = img.resize((IMG_WIDTH, IMG_HEIGHT))
    img_array = image.img_to_array(img_resized)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    # Predict
    predictions = model.predict(img_array)
    predicted_class = class_names[np.argmax(predictions)]
    confidence = np.max(predictions) * 100
    
    # Dynamic header color based on predicted scene
    color = scene_colors.get(predicted_class, "#000000")
    st.markdown(f"<h2 style='color:{color};'>Predicted Scene: {predicted_class}</h2>", unsafe_allow_html=True)
    st.write(f"Confidence: {confidence:.2f}%")
