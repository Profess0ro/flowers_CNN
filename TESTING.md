


## Issue with the model

<img src="outputs/v2/flower_similarity_heatmap.png"><br>
As we can see in this heatmap, the colors in the categories of tulips and roses are nearest eachother. This makes the prediction between these two categories the hardest for this model. And if we look at the classification report and the confusion matrix, this also shows that the model having problems with predicting these two categories.

<img src="images/readme/classification_report.png"><br>
<img src="outputs/v2/confusion_matrix.png"><br>

**Here are some examples when the model predicts with barely majority and with the wrong category:**<br><br>
<img src="images/readme/confusion_1a.jpg" width=50% height="auto"><img src="images/readme/confusion_2a.jpg" width=50% height="auto"><br>
<img src="images/readme/confusion_1b.png" width=50% height="auto"><img src="images/readme/confusion_2b.png" width=50% height="auto"><br>
These examples barely have majority on the right class. <br>But here are a prediction that shows roses instead of tulips that are on the image:<br>
<img src="images/readme/confusion_3a.jpg" width=50% height=50%><img src="images/readme/confusion_3b.png" width=50% height="auto"><br> 