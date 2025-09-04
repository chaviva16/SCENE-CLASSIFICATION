## Scene Classification App

This is an interactive **Scene Classification** application built with **TensorFlow** and **Streamlit**. Upload a photo—be it buildings, forest, glacier, mountain, sea, 
or street and the app predicts what kind of scene it is. Test it out live here:

**[Open the App](https://scene-classification.streamlit.app/)**

---

##  Features
-  **Simple image uploads** — just drag and drop an image.
-  **Accurate predictions** — classifies scenes into six categories with confidence scores.
-  **Professional design** — clean UI with clear instructions and color-coded feedback.
-  **Fast and responsive** — optimized for deployment with minimal dependencies.

---

##  Supported Scenes
The app currently recognizes:
- `buildings` 🏢  
- `forest` 🌲  
- `glacier` 🏔️  
- `mountain` ⛰️  
- `sea` 🌊  
- `street` 🛣️  

---

##  Tech Stack
- **Python 3.10+**  
- **TensorFlow / Keras** — for model inference  
- **Streamlit** — for the web interface  
- **NumPy & Pillow** — for image processing  
- **Git LFS** — handles the large `.keras` model file efficiently  

---
## project structure
├── app.py # Streamlit application
├── scene_classification_final.keras # Trained model (Git LFS)
├── requirements.txt # Dependencies
├── .gitignore # Files excluded from repo
└── README.md # This file


---

##  How to Run Locally

1. Clone the repository:
    ```bash
    git clone https://github.com/chaviva16/SCENE-CLASSIFICATION.git
    cd SCENE-CLASSIFICATION
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Launch the app:
    ```bash
    streamlit run app.py
    ```

---

##  Deployment

This app is hosted on **Streamlit Community Cloud**. Your `.keras` model is stored using **Git LFS**, so it loads quickly and stays under repository size limits. 
To deploy your own copy:
1. Push the repo to GitHub (make sure Git LFS is active).  
2. Connect it to Streamlit Cloud and it'll automatically deploy.

---

##  Author

- **Otabor Favour Osasere (Chaviva)**  
- Based in Lagos, Nigeria  
- Passionate about building ML apps and sharing them with the world 🤗  
- Connect with me on [GitHub](https://github.com/chaviva16)

---


##  Project Structure

