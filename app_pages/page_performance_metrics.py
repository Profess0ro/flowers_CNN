import streamlit as st

version = 'v2'
def page_performance_body():
    st.header("ML performance metrics")
    
    st.image(f"outputs/{version}/color_distribution_by_flower_type.png")
    st.image(f"outputs/{version}/flower_similarity_heatmap.png")