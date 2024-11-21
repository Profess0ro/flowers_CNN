import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import tensorflow as tf
import pickle
import matplotlib.pyplot as plt
import seaborn as sns


version = 'v2'
model_path = f"outputs/{version}/flower_prediction_model.h5"
model = load_model(model_path)

with open(f"outputs/{version}/labels.pkl", "rb") as f:
    labels = pickle.load(f)
    

def page_classifier_body():
    st.header("Flower Classifier")
    st.info("""
            Upload an image of a flower to see the predicted class along with the confidence level. 
            You will also see a barplot showing the model's confidence across all categories. 
            """)

    uploaded_image = st.file_uploader("Upload a flower image", type=["jpg", "png", "jpeg"])

    if uploaded_image is not None:
        st.image(uploaded_image, caption="Your uploaded image", use_container_width=True)
        
        # Prepare the image
        image = Image.open(uploaded_image)
        image = image.resize((224, 224))
        image_array = np.array(image) / 255.0
        image_array = np.expand_dims(image_array, axis=0)
        
        # Make predictions
        prediction = model.predict(image_array)
        
        predicted_class_index = np.argmax(prediction)
        predicted_class = labels[predicted_class_index]
        predicted_confidence = np.max(prediction) * 100
        
        st.info(f"Predicted class: {predicted_class}")
        st.success(f"Predicted confidence: {predicted_confidence:.2f}%")
        
        # Plot prediction barplot
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(x=labels, y=prediction[0], palette='viridis', ax=ax)
        ax.set_xticklabels(labels, rotation=90)
        ax.set_xlabel('Flower Species')
        ax.set_ylabel('Confidence (%)')
        ax.set_title('Class Prediction')
        
        # Add percentages above each bar
        for i, value in enumerate(prediction[0]):
            ax.text(i, value + 0.01, f"{value * 100:.1f}%", ha='center', va='bottom')
        
        st.pyplot(fig)
