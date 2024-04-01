import tensorflow as tf
import numpy as np

x_train = np.array([
    [1,0,0],
    [0,1,0],
    [0,0,1]
])

y_train = np.array([
    2,0,1
])

model = tf.keras.models.load_model('gawi.h5')

pred = model.predict(x_train)

for idx, p in enumerate(pred):
    print(np.argmax(p),p)
    
x_rf = np.array([
    [0,0,1]
])
pred_rf=model.predict(x_rf)

print(np.argmax(pred_rf))
