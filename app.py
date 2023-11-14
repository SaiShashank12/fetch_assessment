from fetch_assessment.pipeline.predict import PredictionPipleline
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse, JSONResponse
import os
import streamlit as st
from PIL import Image

# Title
st.title("Receipt Count Prediction")

# Training section
if st.button("Train Model"):
    try:
        # Run training script (replace 'python main.py' with your actual training script)
        os.system("python main.py")
        image_path = os.path.join(PredictionPipleline().config.root_dir, "training_image.png")
        image = Image.open(image_path)
        st.image(image, caption="Training Results")
        st.success("Training successful!")
    except Exception as e:
        st.error(f"Error Occurred: {e}")

# Prediction section
n_days = st.number_input("Enter number of days for prediction", min_value=1, max_value=100, step=1)
if st.button("Predict"):
    try:
        obj = PredictionPipleline()
        predict = obj.predict(int(n_days))
        st.write(predict)
    except Exception as e:
        st.error(f"Error Occurred: {e}")
