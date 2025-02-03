Training CNN...
Epoch 1/5
469/469 ━━━━━━━━━━━━━━━━━━━━ 14s 27ms/step - accuracy: 0.4350 - loss: 1.6560  
Epoch 2/5
469/469 ━━━━━━━━━━━━━━━━━━━━ 14s 30ms/step - accuracy: 0.8322 - loss: 0.5522
Epoch 3/5
469/469 ━━━━━━━━━━━━━━━━━━━━ 15s 33ms/step - accuracy: 0.8779 - loss: 0.4015
Epoch 4/5
469/469 ━━━━━━━━━━━━━━━━━━━━ 16s 33ms/step - accuracy: 0.8964 - loss: 0.3324
Epoch 5/5
469/469 ━━━━━━━━━━━━━━━━━━━━ 16s 33ms/step - accuracy: 0.9123 - loss: 0.2836
Training completed in 74.88 seconds.
Running predictions...
313/313 ━━━━━━━━━━━━━━━━━━━━ 3s 9ms/step  
Inference completed in 3.14 seconds.
CNN Accuracy: 92.49%

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

Classification Report:
              precision    recall  f1-score   support

           0       0.96      0.94      0.95       980
           1       0.98      0.99      0.98      1135
           2       0.89      0.88      0.89      1032
           3       0.90      0.96      0.93      1010
           4       0.89      0.97      0.93       982
           5       0.96      0.87      0.91       892
           6       0.93      0.92      0.92       958
           7       0.89      0.95      0.92      1028
           8       0.93      0.90      0.92       974
           9       0.93      0.84      0.89      1009

    accuracy                           0.92     10000
   macro avg       0.93      0.92      0.92     10000
weighted avg       0.93      0.92      0.92     10000


CNN Model Training Time: 74.88 seconds
CNN Model Testing Time: 3.14 seconds
CNN Model Test Accuracy: 92.49%

Misclassified counts by digit for CNN:
Digit 0: 54
Digit 1: 13
Digit 2: 123
Digit 3: 37
Digit 4: 32
Digit 5: 117
Digit 6: 77
Digit 7: 47
Digit 8: 93
Digit 9: 158

Successful classification percentage for CNN by digit:
Digit 0: 94.49%
Digit 1: 98.85%
Digit 2: 88.08%
Digit 3: 96.34%
Digit 4: 96.74%
Digit 5: 86.88%
Digit 6: 91.96%
Digit 7: 95.43%
Digit 8: 90.45%
Digit 9: 84.34%