# airplane 비행기 : 0
# automobile 자동차 : 1
# bird 새 : 2
# cat 고양이 : 3
# deer 사슴 : 4
# dog 개 : 5
# frog 개구리 : 6
# horse 말 : 7
# ship 배 : 8
# truck 트럭 : 9

from keras.datasets import cifar10

import cv2

(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# print("x_train.shape",x_train.shape)
# print("y_train.shape",y_train.shape)
# print("x_test.shape",x_test.shape)
# print("y_test.shape",y_test.shape)

for i in range(10000):
    cv2.imwrite("img/{}/{}.png".format(y_train[i][0],i), x_train[i]);





