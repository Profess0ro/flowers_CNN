# Flower image predictor

## Dataset content

The dataset contains 29360 images with 5 different types of flowers, and can be found at [kaggle.com](https://www.kaggle.com/) : [Flower dataset](https://www.kaggle.com/datasets/kurito/).<br>All images in this archive are licensed under the Creative Commons By-Attribution License. <br>To see all the photographers listed, [read this](Image_LICENSE.txt).

## Business requirements

A primary school is interested in using a "Flower bingo" so that the children can learn about some of the most common flowers in a more fun and creative way. <br>The company that develops the app for the primary school wants a machine classifier that has high prediction accuracy.<br> The company also provided a suggested dataset of images.

- The client requires that the dataset are studied and results are visualised.
- The client wants us to develop a machine learning model that can predict with an accuracy higher than 80%.
- The Client needs a dashboard where they can try our model with live images.


## Hypotheses and how to validate them


1. Will the model have problems to seperate flowers that has the same color?<br>- We will add the amount of kernels in the later layers to see if the performance will improve.

2. A deep learning model with convolutional neaural network (CNN) should handle the classification of the different flowers
<br>- We will use CNN to train the model then test the performance

3. Does a balanced set of the image dataset make a better result?
<br>- We will try the model with unbalanced and balanced sets and then compare the results.

4. Tuning the hyperparameters will improve the performance of the model.
<br>- Test with basic settings then tune to get a better score.

## The rationale to map the business requirements to the data visualizations and ML tasks

### Purpose and goals with the project

The project is to create a "Flower bingo"-app to help school children learn to recognize common flowers. Meeting the clients requirements and delivering a user-friendly solution requires specific data and visualization steps as well as machine learning models to achive the expected performance.

1.  **Visualization of the dataset for insight and understanding.**
<br>The client wish an analysis and visualization of the dataset, to achieve this we will:<br>- *Image frequency of all categories:* <br>We will visualize the amount of all images through all categories to get a insight if the dataset is balanced or not. Unbalanced categories can affect the performance.
<br>- *Color distribution:* <br>An analysis of the colors will be visualized to determine if the colors are suffiectly distinct between the flower types. This is important if the dataset has many flowers with the same colors.

2.  **Build a machine learning model for classification of the flowers.**
<br>The client demands a model with atleast 80% accuracy to ensure that the app can deliver correct predictions.<br>- *Choice of model:*<br>
We have chosen a convolutional neaural network (CNN) as these are known for their strength in image classification. The CNN will be trained to identify the different visual patterns of the flowers.<br>- *Validation:*<br>
To meet the high demand of the accuracy we will test the model with different hyperparameter settings and document the result of each version. The performance of the deployed version will be shown at the dashboard.

3. **Dashboard for interaction and testing with new data**
<br>An important part of the requirements is an interactive dashboard so the users can test the model with their own images.<br>- *Implementation of the model test interface:*<br>The dashboard will integrate a feature where the user can upload an image and get instant feedback on which flower it is.<br>- *Galleries with each flower:*<br>The dashboard will have a page where the user can choose a flower and then see a gallery with random images of that flower.


