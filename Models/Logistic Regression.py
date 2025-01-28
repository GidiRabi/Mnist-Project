import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from tqdm import tqdm
import seaborn as sns
import time

# Load MNIST dataset
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Flatten images for Logistic Regression (28x28 -> 784)
train_images_flat = train_images.reshape(train_images.shape[0], -1) / 255.0
test_images_flat = test_images.reshape(test_images.shape[0], -1) / 255.0

# Initialize Logistic Regression with tuned settings
model_lr = LogisticRegression(
    max_iter=500,          # Lower max iterations to prevent excessive time
    solver='lbfgs',        # Optimized solver for multi-class classification
    n_jobs=-1,             # Use all CPU cores
    verbose=1              # Enable verbose output to track training progress
)

# Measure training time with progress tracking
print("Training Logistic Regression...")
start_time = time.time()
model_lr.fit(train_images_flat, train_labels)
training_time = time.time() - start_time
print(f"Training completed in {training_time:.2f} seconds.")

# Measure inference time
print("Running predictions...")
start_time = time.time()
lr_predictions = model_lr.predict(test_images_flat)
inference_time = time.time() - start_time
print(f"Inference completed in {inference_time:.2f} seconds.")

# Evaluate accuracy
lr_accuracy = accuracy_score(test_labels, lr_predictions)
print(f"Logistic Regression Accuracy: {lr_accuracy * 100:.2f}%")

# Confusion Matrix (to identify frequently misclassified digits)
cm = confusion_matrix(test_labels, lr_predictions)
plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix for Logistic Regression')
plt.show()

# Classification Report (precision, recall, F1-score)
print("Classification Report:")
print(classification_report(test_labels, lr_predictions))

# Visualize misclassified digits for each class
misclassified = np.where(test_labels != lr_predictions)[0]
misclassified_by_class = {i: [] for i in range(10)}

# Group misclassified samples by true label
for idx in misclassified:
    true_label = test_labels[idx]
    misclassified_by_class[true_label].append(idx)

# Plot one misclassified example per class
plt.figure(figsize=(15, 8))
for i in range(10):
    if misclassified_by_class[i]:  # Check if there are misclassified samples for this class
        idx = misclassified_by_class[i][0]  # Take the first misclassified sample for this class
        plt.subplot(2, 5, i+1)
        plt.imshow(test_images[idx].reshape(28, 28), cmap='gray')
        plt.title(f"True: {test_labels[idx]}\nPred: {lr_predictions[idx]}")
    else:
        plt.subplot(2, 5, i+1)
        plt.text(0.5, 0.5, f"No misclassified\nfor {i}", ha='center', va='center')
        plt.axis('off')
plt.suptitle('Misclassified Digits by Logistic Regression (One Example per Class)')
plt.show()

# Calculate misclassified counts by digit
misclassified_counts = {i: 0 for i in range(10)}
for idx in misclassified:
    true_label = test_labels[idx]
    misclassified_counts[true_label] += 1

# Calculate successful classification percentage by digit
success_percentage = {i: 0 for i in range(10)}
for i in range(10):
    total_samples = np.sum(test_labels == i)
    correct_samples = total_samples - misclassified_counts[i]
    success_percentage[i] = (correct_samples / total_samples) * 100

# Print results
print(f"Logistic Regression Model Training Time: {training_time:.2f} seconds")
print(f"Logistic Regression Model Testing Time: {inference_time:.2f} seconds")
print(f"Logistic Regression Model Test Accuracy: {lr_accuracy * 100:.2f}%")
print("\nMisclassified counts by digit for Logistic Regression:")
for i in range(10):
    print(f"Digit {i}: {misclassified_counts[i]}")
print("\nSuccessful classification percentage for Logistic Regression by digit:")
for i in range(10):
    print(f"Digit {i}: {success_percentage[i]:.2f}%")
