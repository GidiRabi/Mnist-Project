Key Notes
Random Forest Training vs. Inference Time:
Training is slower than KNN but faster than CNN or SVM for large datasets like MNIST.
Inference is faster than KNN because predictions involve only traversing trees, not calculating distances.
Random Forest Accuracy:
Generally higher than KNN but may not match CNN's performance due to the lack of spatial feature learning.
Interpretability:
Random Forest provides insights into feature importance (e.g., pixel regions important for classification). You can extend the code to visualize feature importances if needed.
Strengths of Random Forest:
Robust to noise and outliers.
Handles large datasets well with minimal preprocessing.
Misclassification Analysis:
Similar to KNN, Random Forest may struggle with digits that have overlapping features (e.g., 5 vs. 6, 4 vs. 9).
