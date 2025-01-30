# Logistic Regression for MNIST Classification: Code Walkthrough

## 1. **Loading and Preprocessing Data**
- The **MNIST dataset** (handwritten digits 0-9) is loaded.
- Images are **flattened** from **(28×28) → 784** pixel vectors to work with Logistic Regression.
- Pixel values are **normalized** to the [0,1] range to improve training stability.

## 2. **Training the Logistic Regression Model**
- The model is initialized using `LogisticRegression()` with:
  - **500 iterations** (`max_iter=500`) to balance speed and convergence.
  - **LBFGS solver** (`solver='lbfgs'`), optimized for multi-class classification.
  - **Multi-threading enabled** (`n_jobs=-1`) to speed up training.
  - **Verbose mode** (`verbose=1`) to track progress.
- **Training time** is recorded for performance evaluation.

## 3. **Making Predictions**
- The trained model predicts digit labels for the test set.
- **Inference time** is recorded to analyze computational efficiency.

## 4. **Evaluating Performance**
- **Overall accuracy** is computed using `accuracy_score()`.
- A **confusion matrix** is plotted to visualize misclassification trends.
- A **classification report** (precision, recall, and F1-score) is generated.

## 5. **Analyzing Misclassifications**
- Misclassified samples are **grouped by digit**.
- One **misclassified example per class** is displayed for visual inspection.
- The number of **misclassified samples per digit** is computed.

## 6. **Per-Digit Success Rate**
- The **percentage of correctly classified samples per digit** is calculated.
- This helps identify digits that are more challenging for Logistic Regression.

## 7. **Final Statistics**
- **Training time, inference time, and overall accuracy** are displayed.
- The **number of misclassified samples per digit** is reported.

## **Summary**
- **Strengths**: Logistic Regression is simple, fast to train, and effective for basic classification.
- **Limitations**: It struggles with digits that have high variability in writing styles (e.g., `4` vs. `9`).
- **Performance trade-offs**: While not as powerful as CNNs, it provides a good baseline for MNIST classification.

This implementation showcases **Logistic Regression’s effectiveness** on MNIST, offering insights into its strengths and areas for improvement.
