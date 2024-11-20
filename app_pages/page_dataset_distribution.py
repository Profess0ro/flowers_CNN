import streamlit as st

version = 'v2'

def page_dataset_body():
    st.header("Dataset")
    
    if st.checkbox(
        'Display image distribution through all flower species'
    ):
        st.image(f"outputs/{version}/labels_distribution_raw.png")
        st.warning(""" 
            💐 Distribution of images through all species:  
            Daisy: 5064 images  
            Dandelion: 7184 images  
            Roses: 5128 images  
            Sunflowers: 5592 images  
            Tulips: 6392 images
        """)

    if st.checkbox(
        'Display the color variation through all images'
    ):
        st.image(f"outputs/{version}/color_distribution_by_flower_type.png")
        st.success("""
                   This scatterplot visualizes the largest variations in image colors. 
                   Instead of representing colors using the three RGB channels, PCA reduces 
                   this to two dimensions (PC1 and PC2), which capture the most significant 
                   differences in color distribution across all images.
                   """)
        st.image(f"outputs/{version}/flower_similarity_heatmap.png")
        st.success("""
                   This heatmap helps to visually compare how much the color 
                   distribution differs between the various flower types in the dataset. 
                   It shows which flowers are closer in terms of their visual appearance 
                   (based on their color profiles) and which are more distinct.  
                   The higher the value, the greater the difference in the color distributions 
                   between the flowers.
                   """)
