
=== Running KNN with k=1 (small complexity) ===
Training KNN with k=1...
Training completed in 0.02 seconds.
Running predictions with k=1...
Inference completed in 1.85 seconds.
KNN Accuracy (k=1): 86.01%

Average Number of Activated Pixels for Each Digit:
Digit 0: 191.97 pixels
Digit 1: 85.85 pixels
Digit 2: 168.81 pixels
Digit 3: 163.34 pixels
Digit 4: 141.81 pixels
Digit 5: 152.33 pixels
Digit 6: 156.93 pixels
Digit 7: 131.40 pixels
Digit 8: 173.32 pixels
Digit 9: 143.03 pixels

2025-02-03 15:15:19.825 Python[74191:9492382] +[IMKClient subclass]: chose IMKClient_Modern
2025-02-03 15:15:19.825 Python[74191:9492382] +[IMKInputSession subclass]: chose IMKInputSession_Modern
Classification Report (k=1):
              precision    recall  f1-score   support

           0       0.88      0.94      0.91       980
           1       0.87      0.98      0.92      1135
           2       0.86      0.83      0.84      1032
           3       0.79      0.78      0.78      1010
           4       0.93      0.90      0.91       982
           5       0.79      0.65      0.71       892
           6       0.91      0.93      0.92       958
           7       0.88      0.90      0.89      1028
           8       0.80      0.78      0.79       974
           9       0.85      0.88      0.87      1009

    accuracy                           0.86     10000
   macro avg       0.86      0.86      0.86     10000
weighted avg       0.86      0.86      0.86     10000

KNN Model Training Time (k=1): 0.02 seconds
KNN Model Testing Time (k=1): 1.85 seconds
KNN Model Test Accuracy (k=1): 86.01%

Misclassified counts by digit for KNN (k=1):
Digit 0: 54
Digit 1: 22
Digit 2: 179
Digit 3: 222
Digit 4: 102
Digit 5: 316
Digit 6: 66
Digit 7: 101
Digit 8: 219
Digit 9: 118

Successful classification percentage for KNN by digit (k=1):
Digit 0: 94.49%
Digit 1: 98.06%
Digit 2: 82.66%
Digit 3: 78.02%
Digit 4: 89.61%
Digit 5: 64.57%
Digit 6: 93.11%
Digit 7: 90.18%
Digit 8: 77.52%
Digit 9: 88.31%

=== Running KNN with k=5 (medium complexity) ===
Training KNN with k=5...
Training completed in 0.01 seconds.
Running predictions with k=5...
Inference completed in 1.70 seconds.
KNN Accuracy (k=5): 86.78%

Average Pixel Intensity for Each Digit:
Digit 0: 44.2168
Digit 1: 19.3797
Digit 2: 37.9887
Digit 3: 36.0902
Digit 4: 30.9482
Digit 5: 32.8311
Digit 6: 35.0120
Digit 7: 29.2046
Digit 8: 38.2898
Digit 9: 31.2604
Classification Report (k=5):
              precision    recall  f1-score   support

           0       0.85      0.96      0.90       980
           1       0.82      0.98      0.89      1135
           2       0.88      0.87      0.87      1032
           3       0.79      0.83      0.81      1010
           4       0.94      0.90      0.92       982
           5       0.89      0.62      0.73       892
           6       0.94      0.92      0.93       958
           7       0.89      0.89      0.89      1028
           8       0.86      0.77      0.81       974
           9       0.86      0.90      0.88      1009

    accuracy                           0.87     10000
   macro avg       0.87      0.86      0.86     10000
weighted avg       0.87      0.87      0.87     10000

KNN Model Training Time (k=5): 0.01 seconds
KNN Model Testing Time (k=5): 1.70 seconds
KNN Model Test Accuracy (k=5): 86.78%

Misclassified counts by digit for KNN (k=5):
Digit 0: 44
Digit 1: 19
Digit 2: 139
Digit 3: 172
Digit 4: 98
Digit 5: 335
Digit 6: 72
Digit 7: 111
Digit 8: 228
Digit 9: 104

Successful classification percentage for KNN by digit (k=5):
Digit 0: 95.51%
Digit 1: 98.33%
Digit 2: 86.53%
Digit 3: 82.97%
Digit 4: 90.02%
Digit 5: 62.44%
Digit 6: 92.48%
Digit 7: 89.20%
Digit 8: 76.59%
Digit 9: 89.69%

=== Running KNN with k=15 (high complexity) ===
Training KNN with k=15...
Training completed in 0.01 seconds.
Running predictions with k=15...
Inference completed in 2.07 seconds.
KNN Accuracy (k=15): 86.07%

Average Pixel Intensity for Each Digit:
Digit 0: 44.2168
Digit 1: 19.3797
Digit 2: 37.9887
Digit 3: 36.0902
Digit 4: 30.9482
Digit 5: 32.8311
Digit 6: 35.0120
Digit 7: 29.2046
Digit 8: 38.2898
Digit 9: 31.2604
Classification Report (k=15):
              precision    recall  f1-score   support

           0       0.85      0.94      0.90       980
           1       0.78      0.98      0.87      1135
           2       0.90      0.86      0.88      1032
           3       0.79      0.81      0.80      1010
           4       0.95      0.90      0.92       982
           5       0.91      0.60      0.72       892
           6       0.93      0.92      0.93       958
           7       0.89      0.89      0.89      1028
           8       0.83      0.76      0.80       974
           9       0.85      0.90      0.88      1009

    accuracy                           0.86     10000
   macro avg       0.87      0.86      0.86     10000
weighted avg       0.87      0.86      0.86     10000

KNN Model Training Time (k=15): 0.01 seconds
KNN Model Testing Time (k=15): 2.07 seconds
KNN Model Test Accuracy (k=15): 86.07%

Misclassified counts by digit for KNN (k=15):
Digit 0: 54
Digit 1: 22
Digit 2: 149
Digit 3: 187
Digit 4: 101
Digit 5: 361
Digit 6: 78
Digit 7: 113
Digit 8: 232
Digit 9: 96

Successful classification percentage for KNN by digit (k=15):
Digit 0: 94.49%
Digit 1: 98.06%
Digit 2: 85.56%
Digit 3: 81.49%
Digit 4: 89.71%
Digit 5: 59.53%
Digit 6: 91.86%
Digit 7: 89.01%
Digit 8: 76.18%
Digit 9: 90.49%