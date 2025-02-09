import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist # type: ignore
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
import seaborn as sns
import time

# Load MNIST dataset
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Extract column-wise and row-wise features
def extract_features(image):
    row_means = np.mean(image, axis=1)
    col_means = np.mean(image, axis=0)
    row_vars = np.var(image, axis=1)
    col_vars = np.var(image, axis=0)
    return np.concatenate([row_means, col_means, row_vars, col_vars])

train_features = np.array([extract_features(img) for img in train_images])
test_features = np.array([extract_features(img) for img in test_images])

# Compute the average number of activated pixels per digit (nonzero pixels)
average_active_pixels = {
    digit: np.mean([np.count_nonzero(img) for img in train_images[train_labels == digit]])
    for digit in range(10)
}

# Define k values for small, medium, and high complexity
k_values = {"small": 1, "medium": 5, "high": 15}

for complexity, k in k_values.items():
    print(f"\n=== Running KNN with k={k} ({complexity} complexity) ===")

    # Initialize KNN with the specific k value
    model_knn = KNeighborsClassifier(n_neighbors=k, n_jobs=-1)

    # Measure training time
    print(f"Training KNN with k={k}...")
    start_time = time.time()
    model_knn.fit(train_features, train_labels)
    training_time = time.time() - start_time
    print(f"Training completed in {training_time:.2f} seconds.")

    # Measure inference time
    print(f"Running predictions with k={k}...")
    start_time = time.time()
    knn_predictions = model_knn.predict(test_features)
    inference_time = time.time() - start_time
    print(f"Inference completed in {inference_time:.2f} seconds.")

    # Evaluate accuracy
    knn_accuracy = accuracy_score(test_labels, knn_predictions)
    print(f"KNN Accuracy (k={k}): {knn_accuracy * 100:.2f}%")

    # Print the average number of activated pixels for each digit
    print("\nAverage Number of Activated Pixels for Each Digit:")
    for digit, avg_pixels in average_active_pixels.items():
        print(f"Digit {digit}: {avg_pixels:.2f} pixels")

    # Confusion Matrix
    cm = confusion_matrix(test_labels, knn_predictions)
    plt.figure(figsize=(10, 8))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False)
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.title(f'Confusion Matrix for KNN (k={k}, {complexity} complexity)')
    plt.show()

    # Classification Report
    print(f"Classification Report (k={k}):")
    print(classification_report(test_labels, knn_predictions))

    # Visualize misclassified digits for each class
    misclassified = np.where(test_labels != knn_predictions)[0]
    misclassified_by_class = {i: [] for i in range(10)}

    for idx in misclassified:
        true_label = test_labels[idx]
        misclassified_by_class[true_label].append(idx)

    plt.figure(figsize=(15, 8))
    for i in range(10):
        if misclassified_by_class[i]:
            idx = misclassified_by_class[i][0]
            plt.subplot(2, 5, i + 1)
            plt.imshow(test_images[idx].reshape(28, 28), cmap='gray')
            plt.title(f"True: {test_labels[idx]}\nPred: {knn_predictions[idx]}")
        else:
            plt.subplot(2, 5, i + 1)
            plt.text(0.5, 0.5, f"No misclassified\nfor {i}", ha='center', va='center')
            plt.axis('off')
    plt.suptitle(f'Misclassified Digits by KNN (k={k}, {complexity} complexity)')
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
    print(f"KNN Model Training Time (k={k}): {training_time:.2f} seconds")
    print(f"KNN Model Testing Time (k={k}): {inference_time:.2f} seconds")
    print(f"KNN Model Test Accuracy (k={k}): {knn_accuracy * 100:.2f}%")
    print(f"\nMisclassified counts by digit for KNN (k={k}):")
    for i in range(10):
        print(f"Digit {i}: {misclassified_counts[i]}")
    print(f"\nSuccessful classification percentage for KNN by digit (k={k}):")
    for i in range(10):
        print(f"Digit {i}: {success_percentage[i]:.2f}%")
