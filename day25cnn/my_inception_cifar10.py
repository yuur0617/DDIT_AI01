import tensorflow as tf
from tensorflow import keras
from keras.utils import np_utils
from keras.datasets import cifar10

# MNIST 데이터셋 로드
(x_train, y_train), (x_test, y_test) = cifar10.load_data()


# model = keras.applications.VGG16(weights=None, input_tensor=keras.layers.Input(shape=(32, 32, 3)),input_shape=(32, 32, 3), classes=10)
model = keras.applications.InceptionV3(weights=None, input_tensor=keras.layers.Input(shape=(32, 32, 3)),input_shape=(32, 32, 3), classes=10)


model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.summary()


# 모델 학습
model.fit(x_train, y_train)

# # 모델 평가
test_loss, test_acc = model.evaluate(x_test, y_test)
print('Test accuracy:', test_acc)