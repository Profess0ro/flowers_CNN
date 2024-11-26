# Flower image predictor

<img src="images/flowers.jpg"><br>

[Link to live page](https://flower-bingo.onrender.com/)


- [Dataset content](#dataset-content)<br>
- [Business requirements](#business-requirements)<br>
- [Hypotheses](#hypotheses-and-how-to-validate-them)<br>
- [The rationale map](#the-rationale-to-map-the-business-requirements-to-the-data-visualizations-and-ml-tasks)<br>
- [Dashboard design](#dashboard-design)<br>
- [Deployment](#deployment)<br>
- [Packages used](#packages-used)<br>
- [Problems encounterd](#problems-encountered)<br>
- [Resources](#resources)<br>
- [Credits](#credits)<br>


## Dataset content

The dataset contains 29360 images with 5 different types of flowers, and can be found at [Flower dataset](https://www.kaggle.com/datasets/kurito/flower-photos).<br>The flower species that are represented are: daisys, dandelions, sunflowers, roses and tulips.<br>All images in this archive are licensed under the Creative Commons By-Attribution License. <br>To see all the photographers listed, [read this](Image_LICENSE.txt).

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


## Dashboard design

### Page 1: Project summary
This page will show an overview of the project.
- General info and business requirements
- Small summary about the dataset
- Link to this README file for further information.

### Page 2: Dataset distribution
This page will show the how the dataset is built with:
- Image distribution of all categories
- Color diffirentials through all images

### Page 3: Flower classification
This page will allow the user to get a class prediction of their images.
- Image uploader
- Image prediction: Shows the prediction result with a barplot showing the prediction percentage through all 5 classes.

### Page 4: Project hypotheses and validation
This page will present all the hypotheses 
- Hypotheses statements
- Process to validate each hypothesis
- Present the outcomes of each hypothesis

### Page 5: ML performance metrics
This page will display all performance result and metrics to show it´s effectiveness.
- Model history with learning curve for training and validation sets.
- Performance metrics with accuracy and confusion matrix
- Summary if the performance meets the demands.

<hr>

## Deployment

### GitHub
1. Log in to your GitHub account.
2. Create a repository by click on 'New' at the repositories page.
3. Go into your repository [This repository](https://github.com/Profess0ro/flowers_CNN) and click on 'Code' and copy the link.
4. Open VS code and choose 'Clone git repository..' now paste the link in the command file at the top: `https://github.com/Profess0ro/flowers_CNN.git` and choose a local storage in the window that pops up.

### Deploy in development environment

1. Open your repository `https://github.com/Profess0ro/flowers_CNN.git` with your choice of workspace (VS code or GitPod)
2. Install required dependencies with	`pip3 -r requirements.txt`
3. If any package additions been made, don´t forget to use `pip3 freeze > requirements.txt`
4. Run this app with the command `streamlit run app.py`
5. Commit and push to GitHub.

### Render

Renders have been used instead of Heroku for this deployment. Since the packages only was larger than Heroku´s slug size of 500Mb. Render are a little bit slower hosting site, but it works for showing this project.

1. Create or log in to your account at [Render](https://render.com/)
2. Click on "+ New" and select "New static site"
3. Choose "Public Git Repository" and paste your URL to the repository. For this project: "https://github.com/Profess0ro/flowers_CNN"
4. Click on "Connect"
5. Fill in follow fields:<br>- name<br>- branch<br>- build command<br>- publish directory<br>- start command (streamlit run app.py)
6. Click on "Deploy static site"

## Packages used

- [joblib](https://pypi.org/project/joblib/) - A library for saving, loading, and parallelizing Python objects, optimized for large data.<br>
- [jsonschema](https://python-jsonschema.readthedocs.io/en/stable/) - Validates JSON data against a defined schema to ensure correct structure and format <br>
- [keras](https://pypi.org/project/keras/) - A high-level neural networks API for building and training deep learning models.<br>
- [matplotlib](https://pypi.org/project/matplotlib/) - A library for creating static visualizations in Python.<br>
- [numpy](https://pypi.org/project/numpy/2.0.2/) - A library for numerical computing, providing support for arrays and mathematical operations.<br>
- [opencv-python](https://pypi.org/project/opencv-python/) - A library for computer vision tasks like image processing, object detection, and video analysis.<br>
- [pandas](https://pypi.org/project/pandas/) -  A library for data manipulation and analysis, offering data structures like DataFrames and Series.<br>
- [pillow](https://pypi.org/project/pillow/) - A library for image processing tasks like opening, editing, and saving image files.<br>
- [scikit-learn](https://pypi.org/project/scikit-learn/) - A machine learning library providing tools for data preprocessing, model training, and evaluation.<br>
- [scipy](https://pypi.org/project/scipy/) - A library for scientific and technical computing, offering functions for optimization, integration, and signal processing.<br>
- [seaborn](https://pypi.org/project/seaborn/) - A data visualization library built on Matplotlib, providing high-level interfaces for drawing attractive and informative statistical graphics.<br>
- [streamlit](https://pypi.org/project/streamlit/) - A framework for building interactive web apps for data science and machine learning projects with minimal coding.<br>
- [tensorboard](https://pypi.org/project/tensorboard/) - A tool for visualizing and monitoring TensorFlow model training, including metrics like loss, accuracy, and model graphs.<br>
- [tensorboard-data-server](https://pypi.org/project/tensorboard-data-server/) - A lightweight server for managing and serving TensorBoard logs, enabling efficient visualization of training data.<br>
- [tensorflow](https://pypi.org/project/tensorflow/) - An open-source machine learning framework for building and deploying deep learning models, supporting neural networks and other ML tasks.<br>


## Problems encountered

1. **Slow model run** <br>Started model run without rescaling to preferred image size (224 x 224). Instead ran the model with original size and the performance was really bad!<br>**- Solution:** added `input_shape=(224, 224, 3)` to the model and the performance greatly increased, aslo the runtime went down very much!

2. **Pushing large amount to GitHub**<br> Since the images total size is over 2Gb when having both raw and balanced image sets. The commits I´ve made for a while didn´t upload since I´ve overrided the standardlimit of 2Gb per push.<br>**Solution:** Copied my files on the computer then made a hard reset. Then copied the files with changes and then added `inputs/` in `.gitignore`

## Resources

- [Flower image on app page](https://unsplash.com/photos/selective-focus-photography-red-and-yellow-petaled-flowers-3NBp815cd5Q)<br>
- [Emojis for dashboard](https://emojipedia.org/)<br>
- [Image dataset](https://www.kaggle.com/datasets/kurito/flower-photos)

## Credits

- Credits to all the loving and sharing people in [the swedish slack channel](https://app.slack.com/client/T0L30B202/C03J2BCURV3)<br>
- Extra cred to [Niclas](https://app.slack.com/client/T0L30B202/D07LLC9HRLZ) for helping me clarify some uncertainties.
