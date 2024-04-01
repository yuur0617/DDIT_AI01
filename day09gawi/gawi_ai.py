import tensorflow as tf
import numpy as np
# 가위/바위/보을 선택하시오 가위
# 나:가위
# 컴:보
# 결과:이김

from random import random
model = tf.keras.models.load_model('gawi.h5')
mine = input("가위/바위/보을 선택하시오")
com = ""
result = ""


pred_rf=None
if mine=="가위":
    pred_rf=model.predict([[1,0,0]])
elif mine=="바위":
    pred_rf=model.predict([[0,1,0]])
else :
    pred_rf=model.predict([[0,0,1]])
    
myidx=np.argmax(pred_rf)

if myidx==0:
    com="가위"
elif myidx==1:
    com="바위"
else:
    com="보"

if com == "가위" and mine == "가위"  :  result = "비김"
if com == "가위" and mine == "바위"  :  result = "이김"
if com == "가위" and mine == "보"  :  result = "짐"

if com == "바위" and mine == "가위"  :  result = "짐"
if com == "바위" and mine == "바위"  :  result = "비김"
if com == "바위" and mine == "보"  :  result = "이김"

if com == "보" and mine == "가위"  :  result = "이김"
if com == "보" and mine == "바위"  :  result = "짐"
if com == "보" and mine == "보"  :  result = "비김"

print("나:",mine)
print("컴:",com)
print("결과:",result)

