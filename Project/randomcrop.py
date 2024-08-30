from PIL import Image
import random
image = Image.open("image.jpg") # input the image
image = image.resize((1000, 1000)) # resize the image to 300x300
width, height = image.size # get the image size
crop_size = 500 # define the crop size
x = random.randint(0, width - crop_size) # generate a random x coordinate
y = random.randint(0, height - crop_size) # generate a random y coordinate
box = (x, y, x + crop_size, y + crop_size) # define the box parameter
image_c = image.crop(box) # crop the image randomly
image_c.show() # print the cropped image