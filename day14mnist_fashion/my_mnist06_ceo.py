# 0    T-shirt/top(티셔츠)    
# 1    Trouser(바지)
# 2    Pullover(풀오버스웨터)    
# 3    Dress(드레스)
# 4    Coat(코드)    
# 5    Sandal(샌들)
# 6    Shirt(셔츠)    
# 7    Sneaker(운동화)
# 8    Bag(가방)    
# 9    Ankle boot(발목 부츠)

import tensorflow as tf
import numpy as np
from tensorflow import keras
import cv2

# MNIST 데이터셋 로드
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()

# 입력 데이터 전처리
x_train = x_train.reshape((60000, 28, 28, 1)) / 255.0
x_test = x_test.reshape((10000, 28, 28, 1)) / 255.0

model = tf.keras.models.load_model('fashion.h5')
model.summary()
pred = model.predict(x_test)

cnt_o=0;
cnt_n=0;

for idx, i in enumerate(x_test):
    myidx = np.argmax(pred[idx])
    goog=y_test[idx]
    if myidx!=goog:
        img2=cv2.imwrite("x/{}_{}_{}.png".format(myidx,goog,idx),x_test[idx]*255)

print(pred.shape)