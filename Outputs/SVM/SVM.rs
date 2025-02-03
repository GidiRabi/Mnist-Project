Training SVM...
*
optimization finished, #iter = 423
obj = -47.429628, rho = -0.333603
nSV = 190, nBSV = 34
*.*
...
... /SVM/Optamizations.rs
...
[LibSVM]Training completed in 33.14 seconds.
Running predictions...
Inference completed in 18.20 seconds.
SVM Accuracy: 0.9833

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

2025-02-03 15:27:19.866 Python[74853:9506377] +[IMKClient subclass]: chose IMKClient_Modern
2025-02-03 15:27:19.866 Python[74853:9506377] +[IMKInputSession subclass]: chose IMKInputSession_Modern
Classification Report:
              precision    recall  f1-score   support

           0       0.98      0.99      0.99       980
           1       0.99      0.99      0.99      1135
           2       0.98      0.98      0.98      1032
           3       0.98      0.99      0.98      1010
           4       0.98      0.98      0.98       982
           5       0.99      0.98      0.98       892
           6       0.99      0.98      0.99       958
           7       0.98      0.98      0.98      1028
           8       0.98      0.99      0.98       974
           9       0.98      0.97      0.97      1009

    accuracy                           0.98     10000
   macro avg       0.98      0.98      0.98     10000
weighted avg       0.98      0.98      0.98     10000

SVM Model Training Time: 33.14 seconds
SVM Model Testing Time: 18.20 seconds
SVM Model Test Accuracy: 98.33%

Misclassified counts by digit for SVM:
Digit 0: 6
Digit 1: 6
Digit 2: 21
Digit 3: 15
Digit 4: 17
Digit 5: 16
Digit 6: 15
Digit 7: 25
Digit 8: 14
Digit 9: 32

Successful classification percentage for SVM by digit:
Digit 0: 99.39%
Digit 1: 99.47%
Digit 2: 97.97%
Digit 3: 98.51%
Digit 4: 98.27%
Digit 5: 98.21%
Digit 6: 98.43%
Digit 7: 97.57%
Digit 8: 98.56%
Digit 9: 96.83%