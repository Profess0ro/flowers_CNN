import streamlit as st

def page_dataset_body():
    st.header("Dataset")
    st.image("../outputs/v2/labels_distribution_raw.png")
    st.info("""
            daisy: 5064 images
            dandelion: 7184 images
            roses: 5128 images
            sunflowers: 5592 images
            tulips: 6392 images
            """)
    st.image("../outputs/v2/color_distribution_by_flower_type.png")