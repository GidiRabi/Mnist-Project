import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.utils import to_categorical
import time

# Load the MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Preprocess the data
x_train = x_train.reshape(-1, 28, 28, 1).astype('float32') / 255.0
x_test = x_test.reshape(-1, 28, 28, 1).astype('float32') / 255.0

y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# Build the CNN model
model = Sequential([
    Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D(pool_size=(2, 2)),
    Conv2D(64, kernel_size=(3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Train the model and measure runtime
start_time = time.time()
history = model.fit(x_train, y_train,
                    batch_size=128,
                    epochs=10,
                    validation_split=0.2)
training_time = time.time() - start_time
print(f"Training completed in {training_time:.2f} seconds")

# Evaluate the model on the test set
start_time = time.time()
test_loss, test_accuracy = model.evaluate(x_test, y_test)
testing_time = time.time() - start_time
print(f"Test Accuracy: {test_accuracy * 100:.2f}%")
print(f"Testing completed in {testing_time:.2f} seconds")

# Get the model's predictions for the test set
y_pred = model.predict(x_test)
y_pred_classes = np.argmax(y_pred, axis=1)  # Predicted class labels
y_true_classes = np.argmax(y_test, axis=1)  # True class labels

# Calculate successful classification percentage for each digit
successful_classification = {}
for digit in range(10):
    total = np.sum(y_true_classes == digit)
    correct = np.sum((y_true_classes == digit) & (y_pred_classes == digit))
    percentage = (correct / total) * 100 if total > 0 else 0
    successful_classification[digit] = percentage

print("Successful classification percentage for each digit:")
for digit, percentage in successful_classification.items():
    print(f"Digit {digit}: {percentage:.2f}%")

# Save the model
model.save('mnist_cnn_model.keras')

# Plot training and validation accuracy
plt.figure(figsize=(10, 6))
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Training and Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

