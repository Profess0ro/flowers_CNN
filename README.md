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



