Training Logistic Regression...
[Parallel(n_jobs=-1)]: Using backend LokyBackend with 8 concurrent workers.
Training completed in 31.14 seconds.
Running predictions...
Inference completed in 0.03 seconds.
Logistic Regression Accuracy: 92.21%

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

2025-02-03 15:19:42.580 Python[74546:9498147] +[IMKClient subclass]: chose IMKClient_Modern
2025-02-03 15:19:42.580 Python[74546:9498147] +[IMKInputSession subclass]: chose IMKInputSession_Modern
Classification Report:
              precision    recall  f1-score   support

           0       0.95      0.97      0.96       980
           1       0.96      0.98      0.97      1135
           2       0.92      0.89      0.90      1032
           3       0.90      0.91      0.91      1010
           4       0.94      0.93      0.93       982
           5       0.89      0.87      0.88       892
           6       0.94      0.95      0.95       958
           7       0.93      0.92      0.92      1028
           8       0.87      0.88      0.88       974
           9       0.91      0.92      0.91      1009

    accuracy                           0.92     10000
   macro avg       0.92      0.92      0.92     10000
weighted avg       0.92      0.92      0.92     10000

Logistic Regression Model Training Time: 31.14 seconds
Logistic Regression Model Testing Time: 0.03 seconds
Logistic Regression Model Test Accuracy: 92.21%

Misclassified counts by digit for Logistic Regression:
Digit 0: 32
Digit 1: 27
Digit 2: 112
Digit 3: 88
Digit 4: 67
Digit 5: 118
Digit 6: 48
Digit 7: 84
Digit 8: 118
Digit 9: 85

Successful classification percentage for Logistic Regression by digit:
Digit 0: 96.73%
Digit 1: 97.62%
Digit 2: 89.15%
Digit 3: 91.29%
Digit 4: 93.18%
Digit 5: 86.77%
Digit 6: 94.99%
Digit 7: 91.83%
Digit 8: 87.89%
Digit 9: 91.58%