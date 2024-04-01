import tensorflow as tf
import numpy as np
from tensorflow import keras

# MNIST 데이터셋 로드
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# 입력 데이터 전처리
x_train = x_train.reshape((60000, 28, 28, 1)) / 255.0
x_test = x_test.reshape((10000, 28, 28, 1)) / 255.0

# 모델 구성
model = keras.Sequential([
    keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
    keras.layers.MaxPooling2D((2,2)),
    keras.layers.Flatten(),
    keras.layers.Dense(10, activation='softmax')
])

# 모델 컴파일
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 모델 학습
model.fit(x_train, y_train)

pred = model.predict(x_test)
cnt_o=0;
cnt_n=0;
for idx, i in enumerate(y_test):
    myidx = np.argmax(pred[idx])
    goog=y_test[idx]
    if myidx==goog:
        cnt_o+=1
    else :
        cnt_n+=1
print("cnt_o",cnt_o)
print("cnt_n",cnt_n)
print("cnt",cnt_o+cnt_n)
