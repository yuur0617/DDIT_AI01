import tensorflow as tf
import numpy as np

x_train = np.array([
    [1,0],
    [0,1]
])

y_train = np.array([
    0,1
])

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(2,)),
    tf.keras.layers.Dense(512, activation=tf.nn.relu),
    tf.keras.layers.Dense(512, activation=tf.nn.relu),
    tf.keras.layers.Dense(2, activation=tf.nn.softmax)
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)

model.save('hol1.h5')

pred = model.predict(x_train)

for idx, p in enumerate(pred):
    print(np.argmax(p),p)
    
x_rf = np.array([
    [1,0]
])
pred_rf=model.predict(x_rf)

print(np.argmax(pred_rf))
