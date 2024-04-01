import tensorflow as tf
import numpy as np

# {'name':'짜장','label':0,'arr':[1,0,0,0,0]},
# {'name':'삼겹살','label':1,'arr':[0,1,0,0,0]},
# {'name':'전복죽','label':2,'arr':[0,0,1,0,0]},
# {'name':'킹크랩','label':3,'arr':[0,0,0,1,0]},
# {'name':'라면','label':4,'arr':[0,0,0,0,1]}

x_train = np.array([
    [1,0,0,0,0],
    [0,1,0,0,0],
    [0,0,1,0,0],
    [0,0,0,1,0],
    [0,0,0,0,1]
])

y_train = np.array([
    1,2,3,4,0
])

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(5,)),
    tf.keras.layers.Dense(512, activation=tf.nn.relu),
    tf.keras.layers.Dense(512, activation=tf.nn.relu),
    tf.keras.layers.Dense(5, activation=tf.nn.softmax)
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=20)
model.save('recom.h5')


pred = model.predict(x_train)

for p in pred:
    myidx = np.argmax(p)
    print("myidx",myidx,p)

x_rf = np.array([
    [1,0,0,0,0]
])    
pred_rf = model.predict(x_rf)

print(np.argmax(pred_rf))





