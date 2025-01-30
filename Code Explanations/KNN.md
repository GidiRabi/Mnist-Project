# K-Nearest Neighbors (KNN) for MNIST Classification: Code Walkthrough

## 1. **Loading and Preprocessing Data**
- The **MNIST dataset** (handwritten digits 0-9) is loaded.
- Images are **flattened** from **(28×28) → 784** pixel vectors to be used in KNN.
- Pixel values are **normalized** to the [0,1] range for better model performance.

## 2. **Defining KNN Models**
- KNN models are trained for three different **complexity levels**:
  - **k=1** (small complexity) – nearest single neighbor.
  - **k=5** (medium complexity) – considers 5 nearest neighbors.
  - **k=15** (high complexity) – considers 15 neighbors.

## 3. **Training the KNN Model**
- The model is initialized with `KNeighborsClassifier(n_neighbors=k)`.
- **Training time** is measured to compare complexity across different k values.

## 4. **Making Predictions**
- The trained KNN model predicts digit labels for the test set.
- **Inference time** is recorded to analyze computational cost.

## 5. **Evaluating Performance**
- **Overall accuracy** is computed using `accuracy_score()`.
- A **confusion matrix** is plotted to analyze misclassification patterns.
- A **classification report** is generated to show precision, recall, and F1-score.

## 6. **Analyzing Misclassifications**
- Misclassified images are **grouped by digit**.
- One **misclassified sample per digit** is displayed for visual inspection.
- The number of **misclassified samples per digit** is calculated.

## 7. **Per-Digit Performance Analysis**
- The **percentage of correctly classified samples per digit** is computed.
- **Success rates** help identify which digits are harder for KNN to classify.

## 8. **Final Statistics**
- **Training time, inference time, and accuracy** are printed for each k value.
- The **number of misclassified samples per digit** is displayed.

## **Summary**
- **Low k (e.g., 1)**: Faster but more sensitive to noise.
- **Medium k (e.g., 5)**: Balances accuracy and robustness.
- **High k (e.g., 15)**: Smoother decision boundary but can blur details.
- **Performance trade-offs**: KNN is simple but computationally expensive for large datasets. It works well on MNIST but struggles with similar-looking digits.

By evaluating different k values, this implementation provides insights into KNN’s strengths and weaknesses for digit classification.
