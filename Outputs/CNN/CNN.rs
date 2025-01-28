Epoch 1/5
469/469 ━━━━━━━━━━━━━━━━━━━━ 19s 38ms/step - accuracy: 0.8450 - loss: 0.5213
Epoch 2/5
469/469 ━━━━━━━━━━━━━━━━━━━━ 19s 40ms/step - accuracy: 0.9780 - loss: 0.0703
Epoch 3/5
469/469 ━━━━━━━━━━━━━━━━━━━━ 19s 41ms/step - accuracy: 0.9872 - loss: 0.0452
Epoch 4/5
469/469 ━━━━━━━━━━━━━━━━━━━━ 20s 43ms/step - accuracy: 0.9898 - loss: 0.0322 
Epoch 5/5
469/469 ━━━━━━━━━━━━━━━━━━━━ 22s 48ms/step - accuracy: 0.9928 - loss: 0.0223
Training completed in 99.81 seconds.
Running predictions...
313/313 ━━━━━━━━━━━━━━━━━━━━ 3s 11ms/step 
Inference completed in 3.62 seconds.
CNN Accuracy: 99.02%
Classification Report:
              precision    recall  f1-score   support

           0       0.99      0.99      0.99       980
           1       0.99      1.00      1.00      1135
           2       0.99      0.98      0.99      1032
           3       0.99      0.99      0.99      1010
           4       0.99      0.99      0.99       982
           5       0.98      0.99      0.99       892
           6       1.00      0.98      0.99       958
           7       0.98      0.99      0.99      1028
           8       0.99      0.99      0.99       974
           9       0.99      0.99      0.99      1009

    accuracy                           0.99     10000
   macro avg       0.99      0.99      0.99     10000
weighted avg       0.99      0.99      0.99     10000


CNN Model Training Time: 99.81 seconds
CNN Model Testing Time: 3.62 seconds
CNN Model Test Accuracy: 99.02%

Misclassified counts by digit for CNN:
Digit 0: 6
Digit 1: 2
Digit 2: 16
Digit 3: 9
Digit 4: 6
Digit 5: 6
Digit 6: 19
Digit 7: 8
Digit 8: 11
Digit 9: 15

Successful classification percentage for CNN by digit:
Digit 0: 99.39%
Digit 1: 99.82%
Digit 2: 98.45%
Digit 3: 99.11%
Digit 4: 99.39%
Digit 5: 99.33%
Digit 6: 98.02%
Digit 7: 99.22%
Digit 8: 98.87%
Digit 9: 98.51%