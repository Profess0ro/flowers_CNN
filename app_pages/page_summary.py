import streamlit as st

def page_summary_body():
    st.image("images/app_pages/flowers.jpg")
    st.header("Project Summary")
    st.info("""
            🌻 **General info:**
            
            A primary school wants to teach children about five of the most common flowers in a more interactive way. 
            They came up with the idea of a "flower-bingo," where children can upload photos 
            (with help from their parents) into an app with a bingo tray.

            The squares in the bingo tray will be marked when a photo of that flower is uploaded. 
            To ensure that the flowers are being marked correctly, 
            the school reached out and wanted an app that can predict flowers from photos.

            As a data analyst, I’ve been tasked with creating a prediction tool for this app that achieves an accuracy of over 80%. 
            To accomplish this, I’m going to build a machine learning classifier using convolutional neural networks (CNNs) 
            to accurately classify flower species based on images.
            """)
    
    st.success("""
               🌹 **Dataset:**
               
                The dataset used for this project consists of 29,360 images of five common flower species: dandelions, daisies, sunflowers, tulips, and roses. 
                The images are classified into these categories, with multiple samples for each flower species. 
                This dataset is publicly available and can be used for educational and research purposes.

                All images in this dataset are licensed under the Creative Commons By-Attribution License.
                [Licence](https://github.com/Profess0ro/flowers_CNN/blob/main/Image_LICENSE.txt)
               """)
    
    st.warning("""
               🌼 **Business requirements:**
                - The client requires analysis and visualization of the dataset.
                - The client expects a machine learning model with an accuracy above 80%.
               """)
    # Link to README file
    st.markdown("Read the full README [here](https://github.com/Profess0ro/flowers_CNN)", unsafe_allow_html=True)
    
    
    

    
    