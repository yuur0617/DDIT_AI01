
from keras.utils import np_utils
from keras.datasets import cifar10
from datetime import datetime
import tensorflow as tf



before = datetime.now()

(x_train, y_train), (x_test, y_test) = cifar10.load_data()

x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)

model = tf.keras.models.load_model('cifar10.h5')
model.summary()
pred = model.predict(x_test)

after = datetime.now()

print("after",after, "before",before)
print(after-before)
