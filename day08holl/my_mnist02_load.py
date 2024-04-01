import tensorflow as tf
import numpy as np

x_train = np.array([
    [1,0],
    [0,1]
])

y_train = np.array([
    1,0
])

model = tf.keras.models.load_model('hol.h5')
model.summary()

x_rf = np.array([
    [1,0],
    [0,1]
])
mine=input("홀/짝을 선택하시오")
com=""
result=""
pred_rf=0;
if mine=="홀":
    pred_rf=model.predict([[1,0]])
else:
    pred_rf=model.predict([[0,1]])

print(pred_rf)
if np.argmax(pred_rf)==1:
    com="짝"
else:
    com="홀"
    
if mine==com:
    result="이김"
else:
    result="짐"
    
print("mine",mine)
print("com",com)
print("result",result)
