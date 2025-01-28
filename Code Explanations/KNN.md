Key Questions Answered
How does computation time compare between models?
KNN Training: Almost instant because it simply stores the training data.
KNN Inference: Very slow because predictions require computing distances to all training points for every test point.
Does the added complexity of CNN justify its improved accuracy?
KNN is simple but less efficient and less accurate compared to CNN for image data. CNN complexity is justified when handling spatial features.
Which digits are frequently misclassified?
Check the confusion matrix to identify problematic digits. Similar-looking digits like 3 vs. 5 or 7 vs. 1 may appear here as well.
Why are certain digits harder to classify?
KNN struggles with overlapping digits in high-dimensional space, where distances may not reflect meaningful differences (curse of dimensionality).
Which model brings the best overall results for this dataset?
CNN > SVM > KNN in terms of accuracy and scalability for MNIST. KNN is better for small datasets with low-dimensional features.
How do models perform when visualized through graphs and statistical analysis?
Misclassification heatmaps and success percentages provide insights into KNN's performance compared to SVM and CNN.
Trade-offs between simplicity, accuracy, and computational cost:
KNN: Simple to implement but computationally expensive for inference and less accurate.
CNN: Complex but highly efficient for large-scale image data due to feature learning and GPU acceleration.