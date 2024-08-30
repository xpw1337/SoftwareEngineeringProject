import skimage
from skimage import io, util
# Load image
img = io.imread('image.jpg', as_gray=0)
# Add Gaussian noise to image
img_n = util.random_noise(img, mode='gaussian', var=0.01)
# Print noisy image
io.imshow(img_n)
io.show()