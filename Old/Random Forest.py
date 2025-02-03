import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
import seaborn as sns
import time

# Load MNIST dataset
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Flatten images for Random Forest (28x28 -> 784)
train_images_flat = train_images.reshape(train_images.shape[0], -1) / 255.0
test_images_flat = test_images.reshape(test_images.shape[0], -1) / 255.0

# Initialize Random Forest
# Parameters are tuned for balance between accuracy and computation time
model_rf = RandomForestClassifier(
    n_estimators=100,  # Number of trees
    max_depth=20,      # Limit the depth of each tree
    random_state=42,   # For reproducibility
    n_jobs=-1          # Use all CPU cores
)

# Measure training time
print("Training Random Forest...")
start_time = time.time()
model_rf.fit(train_images_flat, train_labels)
training_time = time.time() - start_time
print(f"Training completed in {training_time:.2f} seconds.")

# Measure inference time
print("Running predictions...")
start_time = time.time()
rf_predictions = model_rf.predict(test_images_flat)
inference_time = time.time() - start_time
print(f"Inference completed in {inference_time:.2f} seconds.")

# Evaluate accuracy
rf_accuracy = accuracy_score(test_labels, rf_predictions)
print(f"Random Forest Accuracy: {rf_accuracy * 100:.2f}%")

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
    if misclassified_by_class[i]:  # Check if there are misclassified samples for this class
        idx = misclassified_by_class[i][0]  # Take the first misclassified sample for this class
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
