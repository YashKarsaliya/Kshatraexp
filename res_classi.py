from tensorflow import keras
from keras import Sequential
from keras import layers

num_filters = 32          
max_pool_size = (2,2)       
conv_kernel_size = (3, 3)    
imag_shape = (1500, 2000, 3)
num_classes = 3
drop_prob = 0.5

model = Sequential()
model.add(layers.Conv2D(num_filters, conv_kernel_size[0], conv_kernel_size[1], input_shape=imag_shape, activation='relu'))
model.add(layers.MaxPooling2D(pool_size=max_pool_size))
model.add(layers.Conv2D(num_filters*2, conv_kernel_size[0], conv_kernel_size[1], input_shape=imag_shape, activation='relu'))
model.add(layers.MaxPooling2D(pool_size=max_pool_size))
model.add(layers.Conv2D(num_filters*4, conv_kernel_size[0], conv_kernel_size[1], input_shape=imag_shape, activation='relu'))
model.add(layers.MaxPooling2D(pool_size=max_pool_size))
model.add(layers.Flatten())
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dropout(drop_prob))
model.add(layers.Dense(num_classes, activation='sigmoid'))

train_ds = keras.preprocessing.image_dataset_from_directory(
    "data",
    validation_split=0.2,
    subset="training",
    seed=1,
    image_size=(1500, 2000),
    batch_size=4,
)
val_ds = keras.preprocessing.image_dataset_from_directory(
    "data",
    validation_split=0.2,
    subset="validation",
    seed=1,
    image_size=(1500,2000),
    batch_size=4,
)

model.compile(optimizer='adam', loss='SparseCategoricalCrossentropy')
model.fit(train_ds, epochs=10, validation_data=val_ds)
