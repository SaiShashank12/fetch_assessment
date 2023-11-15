from fetch_assessment.pipeline.predict import PredictionPipleline
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse, JSONResponse
import os
import streamlit as st
from PIL import Image
import json

# Title
st.title("Receipt Count Prediction")

def display_collapsible_json(data, level=0):
    if isinstance(data, dict):
        for key, value in data.items():
            with st.expander(key, expanded=False):
                display_collapsible_json(value, level + 1)
    elif isinstance(data, list):
        for item in data:
            display_collapsible_json(item, level + 1)
    else:
        st.write(data)

# Training section
if st.button("Train Model"):
    try:
        # Run training script (replace 'python main.py' with your actual training script)
        os.system("python main.py")

        # Assuming that the training script saves two images: 'train.png' and 'test.png'
        train_image_path = os.path.join(PredictionPipleline().config.root_dir, "train.png")
        test_image_path = os.path.join(PredictionPipleline().config.root_dir, "test.png")

        # Create two columns for the images
        col1, col2 = st.columns(2)

        # Display training image in the first column
        with col1:
            train_image = Image.open(train_image_path)
            st.image(train_image, caption="Training Results")

        # Display testing image in the second column
        with col2:
            test_image = Image.open(test_image_path)
            st.image(test_image, caption="Testing Results")
        result_json_path = os.path.join(PredictionPipleline().config.root_dir, "result.json")
        if os.path.exists(result_json_path):
            with open(result_json_path, 'r') as file:
                result_data = json.load(file)
                display_collapsible_json(result_data)


        else:
            st.warning("result.json not found.")
        st.success("Training successful!")
    except Exception as e:
        st.error(f"Error Occurred: {e}")

# Prediction section
#get 
n_days = st.number_input("Enter number of days for prediction", min_value=1, max_value=100, step=1)
if st.button("Predict"):
    try:
        obj = PredictionPipleline()
        predict = obj.predict(int(n_days))
        st.write(predict)
    except Exception as e:
        st.error(f"Error Occurred: {e}")
