import imageio
import imgaug as ia
import imgaug.augmenters as iaa
import ipyplot

input_img = imageio.imread('image.jpg')

# Rotate the image by a random angle between -45 and 45 degrees
rotate = iaa.Affine(rotate=(-45, 45))

# Crop the image by a random percentage between 0 and 0.2
crop = iaa.Crop(percent=(0, 0.2))

# Add Gaussian noise to the image with a standard deviation of 10
noise = iaa.AdditiveGaussianNoise(scale=10)

# Invert the colors of the image
invert = iaa.Invert(1.0)

# Apply the augmentations sequentially
augmenter = iaa.Sequential([rotate, crop, noise, invert])
output_img = augmenter.augment_image(input_img)

images_list = [input_img, output_img]
labels = ['Original', 'Augmented']
ipyplot.plot_images(images_list, labels=labels, img_width=180, max_images=20, force_b64=True) # use float or np.float64 instead of np.float
