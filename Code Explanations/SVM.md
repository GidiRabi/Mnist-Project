# Support Vector Machine (SVM) for MNIST Classification: Code Walkthrough

## 1. **Loading and Preprocessing Data**
- The **MNIST dataset** (handwritten digits 0-9) is loaded.
- Images are **normalized** to the [0,1] range to improve model efficiency.
- Images are **flattened** from **(28×28) → 784** pixel vectors for SVM input.

## 2. **Initializing the SVM Model**
- The **SVM classifier** is configured with:
  - **Radial Basis Function (RBF) kernel** for handling complex decision boundaries.
  - **Automatic gamma scaling** (`gamma='scale'`) for feature importance.
  - **Verbose mode enabled** (`verbose=True`) to monitor training progress.

## 3. **Training the Model**
- The training process is **timed** to evaluate computational performance.
- The SVM learns to separate digit classes by finding an optimal hyperplane.

## 4. **Making Predictions**
- The trained model predicts digit labels for the test set.
- **Inference time** is measured to analyze speed.

## 5. **Evaluating Performance**
- **Overall accuracy** is computed using `accuracy_score()`.
- A **confusion matrix** is plotted to visualize misclassification trends.
- A **classification report** is generated to show precision, recall, and F1-score.

## 6. **Analyzing Misclassifications**
- Misclassified samples are **grouped by digit**.
- One **misclassified example per class** is displayed for analysis.
- The number of **misclassified samples per digit** is recorded.

## 7. **Per-Digit Success Rate**
- The **percentage of correctly classified samples per digit** is computed.
- This highlights digits that are more challenging for SVM to classify.

## 8. **Final Statistics**
- **Training time, inference time, and accuracy** are displayed.
- The **number of misclassified samples per digit** is reported.

## **Summary**
- **Strengths**: SVMs are effective for small to medium-sized datasets and handle non-linearity well.
- **Limitations**: Training time is **significantly longer** than other models, especially on large datasets like MNIST.
- **Performance trade-offs**: While SVMs achieve high accuracy, they are computationally expensive and may not scale well compared to CNNs.

This implementation showcases **SVM’s capability** in digit classification and highlights where it excels and where it struggles.
