# import cv2
# import numpy as np
# import os
# import sqlite3
# from sklearn.model_selection import train_test_split
# from keras.models import Sequential
# from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
# from keras.utils import to_categorical
# from keras.callbacks import ModelCheckpoint

# # Load the face images and labels from the directory
# face_images = []
# labels = []

# # Iterate through the images in the dataset directory
# dataset_dir = 'dataset'
# for image_file in os.listdir(dataset_dir):
#     # Load the face image
#     face_image = cv2.imread(os.path.join(dataset_dir, image_file), cv2.IMREAD_GRAYSCALE)
#     face_images.append(face_image)

#     # Extract the label from the image filename
#     label = int(image_file.split('.')[1])  # Use the first part as the label
#     labels.append(label)

# # Convert the labels to categorical format
# labels = to_categorical(labels)

# # Check and adjust the size of images in face_images
# fixed_size = (90, 90)
# resized_images = []
# for img in face_images:
#     if img.shape != fixed_size:
#         resized_img = cv2.resize(img, fixed_size)
#     else:
#         resized_img = img
#     resized_images.append(resized_img)

# # Convert the resized images to numpy array
# face_images = np.array(resized_images).reshape(-1, 90, 90, 1)

# # Split the data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(face_images, labels, test_size=0.2, random_state=42)

# # Create the model
# model = Sequential()
# model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(90, 90, 1)))
# model.add(MaxPooling2D((2, 2)))
# model.add(Flatten())
# model.add(Dense(128, activation='relu'))
# model.add(Dense(4, activation='softmax'))

# # Compile the model
# model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# # Define the checkpoint to save the best model during training
# checkpoint = ModelCheckpoint('face_model.h5', monitor='val_accuracy', save_best_only=True, mode='max', verbose=1)

# # Train the model
# model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, batch_size=32, callbacks=[checkpoint])