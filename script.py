import matplotlib.pyplot as plt
import numpy as np

# Data from your results
models = ["Logistic Regression", "KNN (k=1)", "KNN (k=5)", "KNN (k=15)", 
          "Random Forest", "SVM", "CNN"]
training_times = [31.14, 0.02, 0.01, 0.01, 22.21, 155.85, 93.82]  # in seconds
accuracies = [92.21, 86.01, 86.78, 86.07, 91.19, 92.1, 93.16]  # in %


# Apply small jitter to avoid overlapping (add tiny noise to training times)
training_times_jittered = np.array(training_times)
training_times_jittered[2] += 0.005  # Slightly shift KNN (k=5) to the right

# Create plot
plt.figure(figsize=(8,6))
plt.scatter(training_times_jittered, accuracies, color='blue', s=100, edgecolors='black', alpha=0.8)  # Add edge to markers

# Add labels to each point
for i, model in enumerate(models):
    plt.text(training_times_jittered[i], accuracies[i] + 0.15, model, fontsize=10, ha='right')

# Titles and labels
plt.xlabel("Training Time (seconds)")
plt.ylabel("Accuracy (%)")
plt.title("Training Time vs. Accuracy for Different Models")
plt.grid(True)
plt.xscale("log")  # Log scale for better visualization
plt.xticks([0.01, 0.1, 1, 10, 100, 200], ["0.01s", "0.1s", "1s", "10s", "100s", "200s"])  # Readable scale

# Save the figure
plt.savefig("training_vs_accuracy.png", dpi=300)
plt.show()
