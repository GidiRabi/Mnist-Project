=== Running KNN with k=1 (small complexity) ===
Training KNN with k=1...
Training completed in 0.04 seconds.
Running predictions with k=1...
Inference completed in 9.15 seconds.
KNN Accuracy (k=1): 96.91%
2025-01-28 13:05:33.672 Python[77561:3706970] +[IMKClient subclass]: chose IMKClient_Modern
2025-01-28 13:05:33.673 Python[77561:3706970] +[IMKInputSession subclass]: chose IMKInputSession_Modern
Classification Report (k=1):
              precision    recall  f1-score   support

           0       0.98      0.99      0.99       980
           1       0.97      0.99      0.98      1135
           2       0.98      0.96      0.97      1032
           3       0.96      0.96      0.96      1010
           4       0.97      0.96      0.97       982
           5       0.95      0.96      0.96       892
           6       0.98      0.99      0.98       958
           7       0.96      0.96      0.96      1028
           8       0.98      0.94      0.96       974
           9       0.96      0.96      0.96      1009

    accuracy                           0.97     10000
   macro avg       0.97      0.97      0.97     10000
weighted avg       0.97      0.97      0.97     10000

KNN Model Training Time (k=1): 0.04 seconds
KNN Model Testing Time (k=1): 9.15 seconds
KNN Model Test Accuracy (k=1): 96.91%

Misclassified counts by digit for KNN (k=1):
Digit 0: 7
Digit 1: 6
Digit 2: 40
Digit 3: 40
Digit 4: 38
Digit 5: 32
Digit 6: 14
Digit 7: 36
Digit 8: 54
Digit 9: 42

Successful classification percentage for KNN by digit (k=1):
Digit 0: 99.29%
Digit 1: 99.47%
Digit 2: 96.12%
Digit 3: 96.04%
Digit 4: 96.13%
Digit 5: 96.41%
Digit 6: 98.54%
Digit 7: 96.50%
Digit 8: 94.46%
Digit 9: 95.84%

=== Running KNN with k=5 (medium complexity) ===
Training KNN with k=5...
Training completed in 0.03 seconds.
Running predictions with k=5...
Inference completed in 10.71 seconds.
KNN Accuracy (k=5): 96.88%
Classification Report (k=5):
              precision    recall  f1-score   support

           0       0.96      0.99      0.98       980
           1       0.95      1.00      0.98      1135
           2       0.98      0.96      0.97      1032
           3       0.96      0.97      0.97      1010
           4       0.98      0.96      0.97       982
           5       0.97      0.97      0.97       892
           6       0.98      0.99      0.98       958
           7       0.96      0.96      0.96      1028
           8       0.99      0.94      0.96       974
           9       0.96      0.95      0.95      1009

    accuracy                           0.97     10000
   macro avg       0.97      0.97      0.97     10000
weighted avg       0.97      0.97      0.97     10000

KNN Model Training Time (k=5): 0.03 seconds
KNN Model Testing Time (k=5): 10.71 seconds
KNN Model Test Accuracy (k=5): 96.88%

Misclassified counts by digit for KNN (k=5):
Digit 0: 6
Digit 1: 2
Digit 2: 41
Digit 3: 34
Digit 4: 38
Digit 5: 30
Digit 6: 13
Digit 7: 40
Digit 8: 61
Digit 9: 47

Successful classification percentage for KNN by digit (k=5):
Digit 0: 99.39%
Digit 1: 99.82%
Digit 2: 96.03%
Digit 3: 96.63%
Digit 4: 96.13%
Digit 5: 96.64%
Digit 6: 98.64%
Digit 7: 96.11%
Digit 8: 93.74%
Digit 9: 95.34%

=== Running KNN with k=15 (high complexity) ===
Training KNN with k=15...
Training completed in 0.04 seconds.
Running predictions with k=15...
Inference completed in 10.73 seconds.
KNN Accuracy (k=15): 96.33%
Classification Report (k=15):
              precision    recall  f1-score   support

           0       0.96      0.99      0.98       980
           1       0.94      1.00      0.97      1135
           2       0.98      0.94      0.96      1032
           3       0.96      0.97      0.96      1010
           4       0.97      0.95      0.96       982
           5       0.97      0.97      0.97       892
           6       0.97      0.98      0.98       958
           7       0.95      0.95      0.95      1028
           8       0.99      0.93      0.96       974
           9       0.94      0.95      0.95      1009

    accuracy                           0.96     10000
   macro avg       0.96      0.96      0.96     10000
weighted avg       0.96      0.96      0.96     10000

KNN Model Training Time (k=15): 0.04 seconds
KNN Model Testing Time (k=15): 10.73 seconds
KNN Model Test Accuracy (k=15): 96.33%

Misclassified counts by digit for KNN (k=15):
Digit 0: 10
Digit 1: 4
Digit 2: 64
Digit 3: 35
Digit 4: 48
Digit 5: 29
Digit 6: 15
Digit 7: 48
Digit 8: 67
Digit 9: 47

Successful classification percentage for KNN by digit (k=15):
Digit 0: 98.98%
Digit 1: 99.65%
Digit 2: 93.80%
Digit 3: 96.53%
Digit 4: 95.11%
Digit 5: 96.75%
Digit 6: 98.43%
Digit 7: 95.33%
Digit 8: 93.12%
Digit 9: 95.34%