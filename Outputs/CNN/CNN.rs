Training CNN...
Epoch 1/5
469/469 ━━━━━━━━━━━━━━━━━━━━ 16s 32ms/step - accuracy: 0.4251 - loss: 1.6571   
Epoch 2/5
469/469 ━━━━━━━━━━━━━━━━━━━━ 17s 37ms/step - accuracy: 0.8468 - loss: 0.5074
Epoch 3/5
469/469 ━━━━━━━━━━━━━━━━━━━━ 19s 42ms/step - accuracy: 0.8827 - loss: 0.3765
Epoch 4/5
469/469 ━━━━━━━━━━━━━━━━━━━━ 20s 43ms/step - accuracy: 0.9037 - loss: 0.3171
Epoch 5/5
469/469 ━━━━━━━━━━━━━━━━━━━━ 21s 45ms/step - accuracy: 0.9172 - loss: 0.2695
Training completed in 93.82 seconds.
Running predictions...
313/313 ━━━━━━━━━━━━━━━━━━━━ 4s 13ms/step 
Inference completed in 4.24 seconds.
CNN Accuracy: 93.16%

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
2025-02-03 16:29:18.331 Python[77362:9571801] +[IMKClient subclass]: chose IMKClient_Modern
2025-02-03 16:29:18.331 Python[77362:9571801] +[IMKInputSession subclass]: chose IMKInputSession_Modern
Classification Report:
              precision    recall  f1-score   support

           0       0.95      0.96      0.96       980
           1       0.98      0.99      0.98      1135
           2       0.93      0.86      0.89      1032
           3       0.93      0.95      0.94      1010
           4       0.95      0.95      0.95       982
           5       0.84      0.96      0.89       892
           6       0.95      0.91      0.93       958
           7       0.95      0.90      0.93      1028
           8       0.93      0.93      0.93       974
           9       0.89      0.91      0.90      1009

    accuracy                           0.93     10000
   macro avg       0.93      0.93      0.93     10000
weighted avg       0.93      0.93      0.93     10000


CNN Model Training Time: 93.82 seconds
CNN Model Testing Time: 4.24 seconds
CNN Model Test Accuracy: 93.16%

Misclassified counts by digit for CNN:
Digit 0: 35
Digit 1: 16
Digit 2: 148
Digit 3: 46
Digit 4: 46
Digit 5: 39
Digit 6: 89
Digit 7: 99
Digit 8: 72
Digit 9: 94

Successful classification percentage for CNN by digit:
Digit 0: 96.43%
Digit 1: 98.59%
Digit 2: 85.66%
Digit 3: 95.45%
Digit 4: 95.32%
Digit 5: 95.63%
Digit 6: 90.71%
Digit 7: 90.37%
Digit 8: 92.61%
Digit 9: 90.68%