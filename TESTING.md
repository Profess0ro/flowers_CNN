# Manual tests on streamlit dashboard

<details>
<summary>The menu</summary>
<br>
<img src="images/testing/menu.png">

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Navigate to Dataset distribution | When clicking on "Dataset distribution", the page with dataset distribution will show | Clicked on "Dataset distribution" | The page with dataset info was shown | Pass |
| Navigate to Flower classifier | When clicking on "Flower classifier", the page where users can upload image for prediction will show | Clicked on "Flower classifier" | The page where users can upload images was shown | Pass |
| Navigate to Project hypotheses | When clicking on "Project hypotheses", the page with the projects hypotheses will show  | Clicked on "Project hypotheses" | The page where all information about the projects hypotheses was shown | Pass |
| Navigate to ML Performance metrics | When clicking on "ML Performance metrics", the page with the models performance will show | Clicked on "ML Performance metrics" | The page with the models performance metrics was shown | Pass |
| Navigate to Project Summary | When clicking on "Project Summary", the page with the summary will show | Clicked on "Project Summary" | The page with a summary of the project was shown | Pass |

</details>


## Issue with the model
<details>
<summary>Predicting roses and tulips</summary>

<img src="outputs/v2/flower_similarity_heatmap.png"><br>
As we can see in this heatmap, the colors in the categories of tulips and roses are nearest eachother. This makes the prediction between these two categories the hardest for this model. And if we look at the classification report and the confusion matrix, this also shows that the model having problems with predicting these two categories.

<img src="images/readme/classification_report.png"><br>
<img src="outputs/v2/confusion_matrix.png"><br>

**Here are some examples when the model predicts with barely majority and with the wrong category:**<br><br>
<img src="images/readme/confusion_1a.jpg" width=50% height="auto"><img src="images/readme/confusion_2a.jpg" width=50% height="auto"><br>
<img src="images/readme/confusion_1b.png" width=50% height="auto"><img src="images/readme/confusion_2b.png" width=50% height="auto"><br>
These examples barely have majority on the right class. <br>But here are a prediction that shows roses instead of tulips that are on the image:<br>
<img src="images/readme/confusion_3a.jpg" width=50% height=50%><img src="images/readme/confusion_3b.png" width=50% height="auto"><br> 
</details>