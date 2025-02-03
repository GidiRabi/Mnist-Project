import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import Sequential # type: ignore
from tensorflow.keras.layers import Conv2D, MaxPooling2D, GlobalAveragePooling2D, Dense # type: ignore
from tensorflow.keras.datasets import mnist # type: ignore
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns
import time

# Load MNIST dataset
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Reshape and normalize data for CNN
train_images = train_images.reshape(train_images.shape[0], 28, 28, 1) / 255.0
test_images = test_images.reshape(test_images.shape[0], 28, 28, 1) / 255.0

# One-hot encode labels for CNN
train_labels_onehot = tf.keras.utils.to_categorical(train_labels, 10)
test_labels_onehot = tf.keras.utils.to_categorical(test_labels, 10)

# Compute the average number of activated pixels per digit (nonzero pixels)
average_active_pixels = {
    digit: np.mean([np.count_nonzero(img) for img in train_images[train_labels == digit]])
    for digit in range(10)
}

# Define CNN model with GAP (instead of Flatten)
model_cnn = Sequential([
    Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D(pool_size=(2, 2)),
    Conv2D(64, kernel_size=(3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    GlobalAveragePooling2D(),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

# Compile the model
model_cnn.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Measure training time
print("Training CNN...")
start_time = time.time()
history = model_cnn.fit(train_images, train_labels_onehot, epochs=5, batch_size=128, verbose=1)
training_time = time.time() - start_time
print(f"Training completed in {training_time:.2f} seconds.")

# Measure inference time
print("Running predictions...")
start_time = time.time()
cnn_predictions = np.argmax(model_cnn.predict(test_images), axis=1)
inference_time = time.time() - start_time
print(f"Inference completed in {inference_time:.2f} seconds.")

# Evaluate accuracy
cnn_accuracy = np.mean(cnn_predictions == test_labels)
print(f"CNN Accuracy: {cnn_accuracy * 100:.2f}%")

# Print the average number of activated pixels for each digit
print("\nAverage Number of Activated Pixels for Each Digit:")
for digit, avg_pixels in average_active_pixels.items():
    print(f"Digit {digit}: {avg_pixels:.2f} pixels")

# Confusion Matrix (to identify frequently misclassified digits)
cm = confusion_matrix(test_labels, cnn_predictions)
plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix for CNN')
plt.show()

# Classification Report (precision, recall, F1-score)
print("Classification Report:")
print(classification_report(test_labels, cnn_predictions))

# Visualize misclassified digits for each class
misclassified = np.where(test_labels != cnn_predictions)[0]
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
        plt.title(f"True: {test_labels[idx]}\nPred: {cnn_predictions[idx]}")
    else:
        plt.subplot(2, 5, i+1)
        plt.text(0.5, 0.5, f"No misclassified\nfor {i}", ha='center', va='center')
        plt.axis('off')
plt.suptitle('Misclassified Digits by CNN (One Example per Class)')
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
print(f"\nCNN Model Training Time: {training_time:.2f} seconds")
print(f"CNN Model Testing Time: {inference_time:.2f} seconds")
print(f"CNN Model Test Accuracy: {cnn_accuracy * 100:.2f}%")
print("\nMisclassified counts by digit for CNN:")
for i in range(10):
    print(f"Digit {i}: {misclassified_counts[i]}")
print("\nSuccessful classification percentage for CNN by digit:")
for i in range(10):
    print(f"Digit {i}: {success_percentage[i]:.2f}%")
