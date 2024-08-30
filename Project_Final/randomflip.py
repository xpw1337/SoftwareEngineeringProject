import numpy as np
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator
from keras.utils import load_img, img_to_array
 
# Preview of the image we will work on
img = load_img('image.jpg')
 
# Random flip
pic = img_to_array(img)
pic_sample = np.expand_dims(pic, axis=0)
 
data = ImageDataGenerator(horizontal_flip=True, vertical_flip=True)
aug_data = data.flow(pic_sample, batch_size=1)
 
fig, axes = plt.subplots(1, 10, figsize=(30, 40))
 
for i in range(10):
  # Accessing each sample
  aug_img = next(aug_data)
  # Converting to unsigned integer
  aug_result = aug_img[0].astype('uint8')
  # Showing augmented images
  axes[i].imshow(aug_result)
  axes[i].axis('off')
plt.show()