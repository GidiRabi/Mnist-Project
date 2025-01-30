# Random Forest for MNIST Classification: Code Walkthrough

## 1. **Loading and Preprocessing Data**
- The **MNIST dataset** (handwritten digits 0-9) is loaded.
- Images are **flattened** from **(28×28) → 784** pixel vectors to fit into the Random Forest classifier.
- Pixel values are **normalized** to the [0,1] range for better model performance.

## 2. **Initializing the Random Forest Model**
- The model is configured with:
  - **100 trees (`n_estimators=100`)** to balance accuracy and computation time.
  - **Maximum tree depth of 20 (`max_depth=20`)** to prevent overfitting.
  - **Multi-threading enabled (`n_jobs=-1`)** for faster training.
  - **Random seed (`random_state=42`)** for reproducibility.

## 3. **Training the Model**
- The training process is **timed** to evaluate computational efficiency.
- The model learns decision trees from training images to classify digits.

## 4. **Making Predictions**
- The trained model predicts digit labels for the test set.
- **Inference time** is measured to analyze speed.

## 5. **Evaluating Performance**
- **Overall accuracy** is computed using `accuracy_score()`.
- A **confusion matrix** is plotted to highlight misclassifications.
- A **classification report** is generated to show precision, recall, and F1-score.

## 6. **Analyzing Misclassifications**
- Misclassified samples are **grouped by digit**.
- One **misclassified example per class** is displayed for analysis.
- The number of **misclassified samples per digit** is recorded.

## 7. **Per-Digit Success Rate**
- The **percentage of correctly classified samples per digit** is computed.
- This helps identify which digits Random Forest struggles with.

## 8. **Final Statistics**
- **Training time, inference time, and accuracy** are displayed.
- The **number of misclassified samples per digit** is reported.

## **Summary**
- **Strengths**: Random Forest is easy to use, handles non-linearity well, and requires little preprocessing.
- **Limitations**: Slower on large datasets, struggles with pixel-based data compared to CNNs.
- **Performance trade-offs**: While not as powerful as CNNs, it provides a strong **non-deep learning** baseline for MNIST.

This implementation highlights **Random Forest’s ability to classify images**, showing where it performs well and where improvements could be made.
