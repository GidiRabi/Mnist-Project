optimization finished, #iter = 1611
obj = -512.352528, rho = -2.967860
nSV = 2407, nBSV = 2348
Total nSV = 27518
[LibSVM]Training completed in 155.85 seconds.
Number of Support Vectors per class: [2049 1863 2762 3114 2845 3395 2253 2695 3167 3375]
Running predictions...
Inference completed in 52.52 seconds.
SVM Accuracy: 0.921

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
2025-02-03 16:20:25.724 Python[76746:9559975] +[IMKClient subclass]: chose IMKClient_Modern
2025-02-03 16:20:25.724 Python[76746:9559975] +[IMKInputSession subclass]: chose IMKInputSession_Modern
Classification Report:
              precision    recall  f1-score   support

           0       0.96      0.98      0.97       970
           1       0.97      0.99      0.98      1132
           2       0.94      0.91      0.93       962
           3       0.92      0.92      0.92      1010
           4       0.91      0.95      0.93       982
           5       0.92      0.90      0.91       892
           6       0.95      0.96      0.95       912
           7       0.94      0.92      0.93      1028
           8       0.92      0.91      0.92       974
           9       0.92      0.90      0.91      1009

    accuracy                           0.94     10000
   macro avg       0.94      0.94      0.94     10000
weighted avg       0.94      0.94      0.94     10000

SVM Model Training Time: 155.85 seconds
SVM Model Testing Time: 52.52 seconds
SVM Model Test Accuracy: 92.103%

Misclassified counts by digit for SVM:
Digit 0: 25
Digit 1: 20
Digit 2: 180
Digit 3: 77
Digit 4: 100
Digit 5: 86
Digit 6: 36
Digit 7: 79
Digit 8: 85
Digit 9: 97

Successful classification percentage for SVM by digit:
Digit 0: 97.44%
Digit 1: 98.23%
Digit 2: 82.57%
Digit 3: 92.38%
Digit 4: 89.83%
Digit 5: 90.36%
Digit 6: 96.24%
Digit 7: 92.32%
Digit 8: 91.27%
Digit 9: 90.39%