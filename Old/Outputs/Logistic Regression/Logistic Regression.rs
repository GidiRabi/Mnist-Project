Training Logistic Regression...
[Parallel(n_jobs=-1)]: Using backend LokyBackend with 8 concurrent workers.
Training completed in 44.45 seconds.
Running predictions...
Inference completed in 0.03 seconds.
Logistic Regression Accuracy: 92.60%
2025-01-28 13:59:46.242 Python[79351:3758895] +[IMKClient subclass]: chose IMKClient_Modern
2025-01-28 13:59:46.242 Python[79351:3758895] +[IMKInputSession subclass]: chose IMKInputSession_Modern
Classification Report:
              precision    recall  f1-score   support

           0       0.95      0.98      0.96       980
           1       0.96      0.98      0.97      1135
           2       0.93      0.90      0.91      1032
           3       0.90      0.91      0.91      1010
           4       0.94      0.94      0.94       982
           5       0.90      0.87      0.88       892
           6       0.94      0.95      0.95       958
           7       0.93      0.92      0.93      1028
           8       0.88      0.88      0.88       974
           9       0.91      0.92      0.91      1009

    accuracy                           0.93     10000
   macro avg       0.93      0.92      0.92     10000
weighted avg       0.93      0.93      0.93     10000

Logistic Regression Model Training Time: 44.45 seconds
Logistic Regression Model Testing Time: 0.03 seconds
Logistic Regression Model Test Accuracy: 92.60%

Misclassified counts by digit for Logistic Regression:
Digit 0: 22
Digit 1: 25
Digit 2: 101
Digit 3: 87
Digit 4: 60
Digit 5: 115
Digit 6: 47
Digit 7: 80
Digit 8: 119
Digit 9: 84

Successful classification percentage for Logistic Regression by digit:
Digit 0: 97.76%
Digit 1: 97.80%
Digit 2: 90.21%
Digit 3: 91.39%
Digit 4: 93.89%
Digit 5: 87.11%
Digit 6: 95.09%
Digit 7: 92.22%
Digit 8: 87.78%
Digit 9: 91.67%