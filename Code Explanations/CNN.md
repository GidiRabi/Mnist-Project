# CNN for MNIST Digit Classification: Code Walkthrough

## 1. **Loading and Preprocessing Data**
- The **MNIST dataset** (handwritten digits 0-9) is loaded.
- Images are reshaped to **(28,28,1)** (grayscale) and normalized to **[0,1]** for better training.
- Labels are converted to **one-hot encoding** for multi-class classification.

## 2. **Building the CNN Model**
- A **Sequential** model is created with:
  - **Conv2D (32 filters, 3×3 kernel, ReLU)** – detects patterns in images.
  - **MaxPooling2D (2×2)** – reduces spatial dimensions.
  - **Conv2D (64 filters, 3×3, ReLU)** – extracts deeper features.
  - **MaxPooling2D (2×2)** – further downsamples.
  - **Flatten Layer** – converts feature maps into a 1D array.
  - **Dense (128 neurons, ReLU)** – fully connected layer for learning complex patterns.
  - **Dense (10 neurons, softmax)** – output layer for digit classification.

## 3. **Compiling and Training**
- The model is compiled with:
  - **Optimizer**: `Adam` for adaptive learning.
  - **Loss function**: `categorical_crossentropy` for multi-class classification.
  - **Metric**: `accuracy` to track performance.
- Training runs for **5 epochs** with a **batch size of 128**.
- **Training time** is measured.

## 4. **Evaluating Performance**
- **Predictions** are made on test data.
- **Inference time** is recorded.
- **Overall accuracy** is computed.

## 5. **Confusion Matrix & Classification Report**
- A **confusion matrix** is plotted to visualize misclassified digits.
- A **classification report** (precision, recall, F1-score) is generated.

## 6. **Analyzing Misclassifications**
- **Misclassified samples** are identified and grouped by true label.
- One **misclassified example per digit** is plotted.
- The number of **misclassifications per digit** is calculated.

## 7. **Final Statistics**
- **Training time**, **inference time**, and **overall accuracy** are printed.
- The **per-digit success rate** is computed to analyze performance consistency.

## **Summary**
This CNN model efficiently classifies handwritten digits by learning spatial features. Misclassification analysis helps identify areas for improvement, such as **data augmentation or deeper architectures** to enhance accuracy.
