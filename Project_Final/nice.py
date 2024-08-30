from PIL import Image
image = Image.open("image.jpg") # load the image
image_h = image.transpose(Image.FLIP_LEFT_RIGHT) # flip horizontally
image_v = image.transpose(Image.FLIP_TOP_BOTTOM)
image_h.save("car_h.jpg") # save the flipped image in the folder "flipped"
image_v.save("car_v.jpg") # save the flipped image in the folder "flipped"
