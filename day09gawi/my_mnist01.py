import tensorflow as tf
import numpy as np

x_train = np.array([
    [1,0,0],
    [0,1,0],
    [0,0,1]
])

y_train = np.array([
    0,1,2
])

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(3,)),
    tf.keras.layers.Dense(512, activation=tf.nn.relu),
    tf.keras.layers.Dense(512, activation=tf.nn.relu),
    tf.keras.layers.Dense(3, activation=tf.nn.softmax)
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)

model.save('gawi.h5')

