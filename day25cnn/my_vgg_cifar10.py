import tensorflow as tf
from tensorflow import keras
from keras.utils import np_utils
from keras.datasets import cifar10

# MNIST 데이터셋 로드
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# 입력 데이터 전처리
# x_train = x_train.reshape((-1, 32, 32, 3)) 
# x_test = x_test.reshape((-1, 32, 32, 3)) 


# x_train = x_train.astype('float32') / 255.0
# y_train = np_utils.to_categorical(y_train)

model = keras.applications.VGG16(weights=None, input_tensor=keras.layers.Input(shape=(32, 32, 3)),input_shape=(32, 32, 3), classes=10)


model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.summary()


# 모델 학습
model.fit(x_train, y_train)

# # 모델 평가
test_loss, test_acc = model.evaluate(x_test, y_test)
print('Test accuracy:', test_acc)