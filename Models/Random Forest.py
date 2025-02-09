import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist # type: ignore
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from scipy.stats import skew, kurtosis
import seaborn as sns
import time

# Load MNIST dataset
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Extract statistical features from images
def extract_stat_features(image):
    row_mean = np.mean(image, axis=1)
    col_mean = np.mean(image, axis=0)
    row_var = np.var(image, axis=1)
    col_var = np.var(image, axis=0)
    row_skew = skew(image, axis=1)
    col_skew = skew(image, axis=0)
    row_kurt = kurtosis(image, axis=1)
    col_kurt = kurtosis(image, axis=0)
    return np.concatenate([row_mean, col_mean, row_var, col_var, row_skew, col_skew, row_kurt, col_kurt])

train_features = np.array([extract_stat_features(img) for img in train_images])
test_features = np.array([extract_stat_features(img) for img in test_images])

# Compute the average number of activated pixels per digit (nonzero pixels)
average_active_pixels = {
    digit: np.mean([np.count_nonzero(img) for img in train_images[train_labels == digit]])
    for digit in range(10)
}

# Initialize Random Forest
model_rf = RandomForestClassifier(
    n_estimators=100,  # Number of trees
    max_depth=20,      # Limit the depth of each tree
    random_state=42,   # For reproducibility
    n_jobs=-1          # Use all CPU cores
)

# Measure training time
print("Training Random Forest...")
start_time = time.time()
model_rf.fit(train_features, train_labels)
training_time = time.time() - start_time
print(f"Training completed in {training_time:.2f} seconds.")

# Measure inference time
print("Running predictions...")
start_time = time.time()
rf_predictions = model_rf.predict(test_features)
inference_time = time.time() - start_time
print(f"Inference completed in {inference_time:.2f} seconds.")

# Evaluate accuracy
rf_accuracy = accuracy_score(test_labels, rf_predictions)
print(f"Random Forest Accuracy: {rf_accuracy * 100:.2f}%")

# Print the average number of activated pixels for each digit
print("\nAverage Number of Activated Pixels for Each Digit:")
for digit, avg_pixels in average_active_pixels.items():
    print(f"Digit {digit}: {avg_pixels:.2f} pixels")

# Confusion Matrix (to identify frequently misclassified digits)
cm = confusion_matrix(test_labels, rf_predictions)
plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix for Random Forest')
plt.show()

# Classification Report (precision, recall, F1-score)
print("Classification Report:")
print(classification_report(test_labels, rf_predictions))

# Visualize misclassified digits for each class
misclassified = np.where(test_labels != rf_predictions)[0]
misclassified_by_class = {i: [] for i in range(10)}

# Group misclassified samples by true label
for idx in misclassified:
    true_label = test_labels[idx]
    misclassified_by_class[true_label].append(idx)

# Plot one misclassified example per class
plt.figure(figsize=(15, 8))
for i in range(10):
    if misclassified_by_class[i]:
        idx = misclassified_by_class[i][0]
        plt.subplot(2, 5, i+1)
        plt.imshow(test_images[idx].reshape(28, 28), cmap='gray')
        plt.title(f"True: {test_labels[idx]}\nPred: {rf_predictions[idx]}")
    else:
        plt.subplot(2, 5, i+1)
        plt.text(0.5, 0.5, f"No misclassified\nfor {i}", ha='center', va='center')
        plt.axis('off')
plt.suptitle('Misclassified Digits by Random Forest (One Example per Class)')
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
print(f"Random Forest Model Training Time: {training_time:.2f} seconds")
print(f"Random Forest Model Testing Time: {inference_time:.2f} seconds")
print(f"Random Forest Model Test Accuracy: {rf_accuracy * 100:.2f}%")
print("\nMisclassified counts by digit for Random Forest:")
for i in range(10):
    print(f"Digit {i}: {misclassified_counts[i]}")
print("\nSuccessful classification percentage for Random Forest by digit:")
for i in range(10):
    print(f"Digit {i}: {success_percentage[i]:.2f}%")
