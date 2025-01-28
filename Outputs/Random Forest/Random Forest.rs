Training Random Forest...
Training completed in 13.97 seconds.
Running predictions...
Inference completed in 0.19 seconds.
Random Forest Accuracy: 96.80%
2025-01-28 13:36:20.979 Python[78479:3736092] +[IMKClient subclass]: chose IMKClient_Modern
2025-01-28 13:36:20.979 Python[78479:3736092] +[IMKInputSession subclass]: chose IMKInputSession_Modern
Classification Report:
              precision    recall  f1-score   support

           0       0.97      0.99      0.98       980
           1       0.99      0.99      0.99      1135
           2       0.96      0.97      0.96      1032
           3       0.96      0.96      0.96      1010
           4       0.97      0.97      0.97       982
           5       0.97      0.96      0.97       892
           6       0.97      0.97      0.97       958
           7       0.97      0.96      0.96      1028
           8       0.96      0.95      0.96       974
           9       0.95      0.95      0.95      1009

    accuracy                           0.97     10000
   macro avg       0.97      0.97      0.97     10000
weighted avg       0.97      0.97      0.97     10000

Random Forest Model Training Time: 13.97 seconds
Random Forest Model Testing Time: 0.19 seconds
Random Forest Model Test Accuracy: 96.80%

Misclassified counts by digit for Random Forest:
Digit 0: 10
Digit 1: 13
Digit 2: 35
Digit 3: 37
Digit 4: 30
Digit 5: 34
Digit 6: 24
Digit 7: 45
Digit 8: 45
Digit 9: 47

Successful classification percentage for Random Forest by digit:
Digit 0: 98.98%
Digit 1: 98.85%
Digit 2: 96.61%
Digit 3: 96.34%
Digit 4: 96.95%
Digit 5: 96.19%
Digit 6: 97.49%
Digit 7: 95.62%
Digit 8: 95.38%
Digit 9: 95.34%