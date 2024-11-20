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
    st.header("Flower classifier")
    st.info("""
            Here you can try our model live with your own flower image
            """)
    
    uploaded_image = st.file_uploader("Upload a flower image", type=["jpg", "png", "jpeg"])
    
    
    if uploaded_image is not None:
        st.image(uploaded_image, caption="Your uploaded image", use_container_width=True)
        
        image = Image.open(uploaded_image)
        image = image.resize((224, 224))
        image_array = np.array(image) / 255.0
        image_array = np.expand_dims(image_array, axis=0)
        
        prediction = model.predict(image_array)
        
        predicted_class_index = np.argmax(prediction)
        predicted_class = labels[predicted_class_index]
        predicted_confidence = np.max(prediction) * 100
        
        st.info(f"Predicted class: {predicted_class}")
        st.success(f"Predicted confidence: {predicted_confidence:.2f}%")
        
        plt.figure(figsize=(10, 6))
        sns.barplot(x=labels, y=prediction[0], palette='viridis')
        plt.xticks(rotation=90)
        plt.xlabel('Flower Species')
        plt.ylabel('Confidence (%)')
        plt.title('Class prediction')
        
        st.pyplot(plt)