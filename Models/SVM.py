import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import seaborn as sns
import time

# Load MNIST dataset
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Normalize pixel values to [0, 1]
train_images = train_images / 255.0
test_images = test_images / 255.0

# Flatten images for SVM (28x28 -> 784)
train_images_flat = train_images.reshape(train_images.shape[0], -1)
test_images_flat = test_images.reshape(test_images.shape[0], -1)

# Initialize SVM with RBF kernel
model_svm = SVC(kernel='rbf', gamma='scale')

# Measure training time
start_time = time.time()
model_svm.fit(train_images_flat, train_labels)
training_time = time.time() - start_time

# Measure inference time
start_time = time.time()
svm_predictions = model_svm.predict(test_images_flat)
inference_time = time.time() - start_time

# Evaluate accuracy
svm_accuracy = accuracy_score(test_labels, svm_predictions)
print(f"SVM Accuracy: {svm_accuracy:.4f}")
print(f"Training Time: {training_time:.2f} seconds")
print(f"Inference Time: {inference_time:.2f} seconds")

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

# Visualize misclassified digits
misclassified = np.where(test_labels != svm_predictions)[0]
plt.figure(figsize=(10, 5))
for i, idx in enumerate(misclassified[:5]):
    plt.subplot(1, 5, i+1)
    plt.imshow(test_images[idx], cmap='gray')
    plt.title(f"True: {test_labels[idx]}\nPred: {svm_predictions[idx]}")
plt.suptitle('Misclassified Digits by SVM')
plt.show()

# Feature Importance (SVM coefficients are not directly interpretable, but we can analyze support vectors)
# Note: For RBF kernel, feature importance is not straightforward. Use linear kernel for interpretable coefficients.
if model_svm.kernel == 'linear':
    plt.figure(figsize=(10, 5))
    plt.bar(range(784), np.abs(model_svm.coef_[0]))
    plt.title('Feature Importance (SVM Coefficients)')
    plt.xlabel('Pixel Index')
    plt.ylabel('Coefficient Magnitude')
    plt.show()
else:
    print("Feature importance is not directly interpretable with RBF kernel. Use linear kernel for interpretable coefficients.")