import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist # type: ignore
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import seaborn as sns
import time

# Load MNIST dataset
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Normalize pixel values to [0, 1]
train_images = train_images / 255.0
test_images = test_images / 255.0

# Flatten images
train_images_flat = train_images.reshape(train_images.shape[0], -1)
test_images_flat = test_images.reshape(test_images.shape[0], -1)

# Apply PCA to reduce dimensionality (Ensure PCA is fitted ONLY on training data)
pca = PCA(n_components=50, svd_solver='randomized', whiten=True)  # Retain 95%+ variance
pca.fit(train_images_flat)  # Fit only on train data
train_images_pca = pca.transform(train_images_flat)
test_images_pca = pca.transform(test_images_flat)  # Apply same transformation to test data

# Compute the average number of activated pixels per digit (nonzero pixels)
average_active_pixels = {
    digit: np.mean([np.count_nonzero(img) for img in train_images[train_labels == digit]])
    for digit in range(10)
}

# Initialize SVM with RBF kernel and prevent overfitting
model_svm = SVC(kernel='rbf', gamma=0.005, C=0.5, verbose=True)  # Reduced gamma and C

# Measure training time
print("Training SVM...")
start_time = time.time()
model_svm.fit(train_images_pca, train_labels)
training_time = time.time() - start_time
print(f"Training completed in {training_time:.2f} seconds.")

# Check number of support vectors to diagnose overfitting
print(f"Number of Support Vectors per class: {model_svm.n_support_}")

# Measure inference time
print("Running predictions...")
start_time = time.time()
svm_predictions = model_svm.predict(test_images_pca)
inference_time = time.time() - start_time
print(f"Inference completed in {inference_time:.2f} seconds.")

# Evaluate accuracy
svm_accuracy = accuracy_score(test_labels, svm_predictions)
print(f"SVM Accuracy: {svm_accuracy:.4f}")

# Debugging: Ensure the predictions are reasonable
print("First 10 Test Labels: ", test_labels[:10])
print("First 10 Predictions: ", svm_predictions[:10])

# Print the average number of activated pixels for each digit
print("\nAverage Number of Activated Pixels for Each Digit:")
for digit, avg_pixels in average_active_pixels.items():
    print(f"Digit {digit}: {avg_pixels:.2f} pixels")

# Confusion Matrix (to identify frequently misclassified digits)
cm = confusion_matrix(test_labels, svm_predictions)
plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix for SVM')
plt.show()

# Classification Report (precision, recall, F1-score)
print("Classification Report:")
print(classification_report(test_labels, svm_predictions))

# Visualize misclassified digits for each class
misclassified = np.where(test_labels != svm_predictions)[0]
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
        plt.imshow(test_images[idx], cmap='gray')
        plt.title(f"True: {test_labels[idx]}\nPred: {svm_predictions[idx]}")
    else:
        plt.subplot(2, 5, i+1)
        plt.text(0.5, 0.5, f"No misclassified\nfor {i}", ha='center', va='center')
        plt.axis('off')
plt.suptitle('Misclassified Digits by SVM (One Example per Class)')
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
print(f"SVM Model Training Time: {training_time:.2f} seconds")
print(f"SVM Model Testing Time: {inference_time:.2f} seconds")
print(f"SVM Model Test Accuracy: {svm_accuracy * 100:.2f}%")
print("\nMisclassified counts by digit for SVM:")
for i in range(10):
    print(f"Digit {i}: {misclassified_counts[i]}")
print("\nSuccessful classification percentage for SVM by digit:")
for i in range(10):
    print(f"Digit {i}: {success_percentage[i]:.2f}%")
