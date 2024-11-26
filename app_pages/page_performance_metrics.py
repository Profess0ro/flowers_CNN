import streamlit as st
import json
import pandas as pd


version = 'v2'
def page_performance_body():
    st.header("ML performance metrics")
    
    st.subheader("Image frequency through datasets")
    st.image(f"outputs/{version}/labels_distribution_sets.png")
    
    st.subheader("Model training history")
    st.image(f"outputs/{version}/training_history.png")
    
    evaluation_path = f"outputs/{version}/model_evaluation.json"
    try:
        with open(evaluation_path, "r") as file:
            evaluation_data = json.load(file)
            
            st.subheader("Model evaluation")
            
            st.info(f"Weighted F1-score: **{evaluation_data['f1_score_weighted']:.3f}**")
            
            st.subheader("Classification Report")
            report = evaluation_data['classification_report']
            
            class_report_df = pd.DataFrame(report).T.drop(['accuracy'], errors='ignore')
            st.dataframe(class_report_df.style.format('{:.3f}'))
            
            st.subheader("Confusion matrix")            
            st.image(f"outputs/{version}/confusion_matrix.png")
            
    except FileNotFoundError:
        st.error(f"The file {evaluation_path} does not exist.")
    except Exception as e:
        st.error(f"An error occured: {e}")

    st.warning("""
        As shown in the confusion matrix, the model has difficulty distinguishing between tulips and roses, 
        often misclassifying images of one as the other. For a more detailed analysis and potential solutions, 
        please refer to the README file.
    """)