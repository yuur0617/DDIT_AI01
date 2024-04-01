# 홀/짝을 선택하시오 홀
# 나:홀
# 컴:홀
# 결과:승리
from random import random
import tensorflow as tf
import numpy as np
model = tf.keras.models.load_model('hol1.h5')
mine=input("홀/짝을 선택하시오")
com=""
result=""
pred_rf=None
if mine=="홀":
    pred_rf=model.predict([[1,0]])
else:
    pred_rf=model.predict([[0,1]])

myidx = np.argmax(pred_rf)

if myidx==1:
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


