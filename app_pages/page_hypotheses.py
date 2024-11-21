import streamlit as st

def page_hypotheses_body():
    st.header("Project Hypotheses and Validation")
    
    st.info("""
            **Hypothesis 1:** Will the model struggle to distinguish flowers with similar colors?  
            - To address this, we increased the number of kernels in the later layers of the CNN to assess whether the performance improves.
            """)
    
    st.warning("""
               **Observation:** When analyzing the color distribution of the dataset, roses and tulips had the most similar color profiles.  
               This was reflected in the model's predictions, where these two categories were mixed up more frequently, though not significantly.  

               **Experiment:** We increased the kernel size in all layers from 3x3 to 5x5 to test its impact on accuracy.  
               **Result:** The overall accuracy improved by 0.01, and approximately 60 additional images were correctly classified.  
               While the improvement is marginal, it suggests that kernel size may play a role in differentiating visually similar flowers.
               """)
    
    
    st.info("""
            **Hypothesis 2:** A deep learning model using a Convolutional Neural Network (CNN) can effectively classify different flower species.  
            - The model will be trained using a CNN architecture, and its performance will be evaluated on a test dataset.
            """)

    st.success("""
                **Result:** The CNN model successfully classified all images with high accuracy.  
                This demonstrates that the chosen architecture is effective for this task, leveraging spatial features to distinguish between flower types.
                """)
    
    
    st.info("""
            **Hypothesis 3:** A balanced dataset will improve the model's performance.  
            - The model will be trained on both unbalanced and balanced datasets (using oversampling) to compare their accuracy and F1-score.
            """)

    st.warning("""
               **Result:** Balancing the dataset (oversampling the smaller categories) did not significantly impact the model's performance.  
               Both accuracy and F1-score showed a difference of less than 0.01.  
               Despite the largest category containing 7,184 images and the smallest category 5,064 images, the model handled the imbalance well.
               """)
    
    
    st.info("""
            **Hypothesis 4:** Tuning hyperparameters will improve the model's performance.  
            - The initial model will use basic settings.  
            - Adjustments to hyperparameters and architecture will be tested to achieve better accuracy and F1-score.
            """)

    st.warning("""
               **Result:** The only adjustment that maintained performance while reducing the size of the `.h5` file was lowering the number of layers.  
               The final model achieved an accuracy of **0.82** and an F1-score of **0.82** with a more compact architecture.  
               
               **Tested adjustments that did not improve performance:**  
               - **Increased kernel size:** Caused a slight decrease in performance.  
               - **Replaced Flatten with GlobalAveragePooling2D and added BatchNormalization:**  
               - Accuracy dropped from 0.84 to **0.70**.  
               - F1-score dropped from 0.82 to **0.69**.  
               - **Augmentation adjustments (increased values and added brightness):**  
               - Accuracy decreased to **0.71**.  
               - F1-score decreased to **0.68**.
               """)

    


