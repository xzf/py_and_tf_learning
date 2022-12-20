import tensorflow as tf
print(tf.__version__)

mnist = tf.keras.datasets.fashion_mnist

(training_images, training_labels) ,  (test_images, test_labels) = mnist.load_data()

training_images = training_images/255.0
test_images = test_images/255.0

model = tf.keras.models.Sequential([tf.keras.layers.Flatten(),
                                    tf.keras.layers.Dense(1024, activation=tf.nn.relu),
                                    tf.keras.layers.Dense(10, activation=tf.nn.softmax)])

model.compile(optimizer = 'adam',
              loss = 'sparse_categorical_crossentropy')

model.fit(training_images, training_labels, epochs=5)

model.evaluate(test_images, test_labels)

classifications = model.predict(test_images)
print(classifications[0])
print(test_labels[0])

#model = keras.Sequential([keras.layers.Dense(units=1,input_shape=[1])])
#model.compile(optimizer='sgd',loss='mean_squared_error')
#
#xs =np.array([-1,0,1,2,3,4],dtype=float)
#ys =np.array([-3,-1,1,3,5,7],dtype=float)
#
#model.fit(xs,ys,epochs=500)
#print(model.predict([10.0]))
#[[18.985994]]
