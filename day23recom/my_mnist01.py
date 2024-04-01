import tensorflow as tf
import numpy as np

x_train = np.array([
    [1,0,0,0,0], #짜장
    [0,1,0,0,0], #삼겹살
    [0,0,1,0,0], #전복죽
    [0,0,0,1,0], #킹크랩
    [0,0,0,0,1], #라면
])
y_train = np.array([
    1,2,3,4,0
])

# 3. 모델 구성
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(5, )),
    tf.keras.layers.Dense(512, activation=tf.nn.relu),
    tf.keras.layers.Dense(512, activation=tf.nn.relu),
    tf.keras.layers.Dense(5, activation=tf.nn.softmax)
])

# 4. 모델 컴파일
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 5. 모델 훈련
model.fit(x_train, y_train, epochs=20)

pred = model.predict(x_train)


for i in pred:
    myidx = np.argmax(i)
    print("myidx" , myidx)

x_rf = np.array([
     [1,0,0,0,0]
])

pred_rf = model.predict(x_rf)

print(np.argmax(pred_rf))

model.save('recom.h5')