Training Random Forest...
Training completed in 22.21 seconds.
Running predictions...
Inference completed in 0.09 seconds.
Random Forest Accuracy: 91.19%

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

2025-02-03 15:25:17.686 Python[74684:9501232] +[IMKClient subclass]: chose IMKClient_Modern
2025-02-03 15:25:17.686 Python[74684:9501232] +[IMKInputSession subclass]: chose IMKInputSession_Modern
Classification Report:
              precision    recall  f1-score   support

           0       0.95      0.96      0.95       980
           1       0.96      0.96      0.96      1135
           2       0.90      0.88      0.89      1032
           3       0.83      0.90      0.86      1010
           4       0.94      0.95      0.94       982
           5       0.87      0.78      0.82       892
           6       0.94      0.94      0.94       958
           7       0.94      0.92      0.93      1028
           8       0.87      0.91      0.89       974
           9       0.91      0.90      0.91      1009

    accuracy                           0.91     10000
   macro avg       0.91      0.91      0.91     10000
weighted avg       0.91      0.91      0.91     10000

Random Forest Model Training Time: 22.21 seconds
Random Forest Model Testing Time: 0.09 seconds
Random Forest Model Test Accuracy: 91.19%

Misclassified counts by digit for Random Forest:
Digit 0: 44
Digit 1: 43
Digit 2: 121
Digit 3: 101
Digit 4: 53
Digit 5: 193
Digit 6: 59
Digit 7: 83
Digit 8: 87
Digit 9: 97

Successful classification percentage for Random Forest by digit:
Digit 0: 95.51%
Digit 1: 96.21%
Digit 2: 88.28%
Digit 3: 90.00%
Digit 4: 94.60%
Digit 5: 78.36%
Digit 6: 93.84%
Digit 7: 91.93%
Digit 8: 91.07%
Digit 9: 90.39%