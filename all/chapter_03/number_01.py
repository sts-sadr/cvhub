# Calculating the aspect ratio and resizing the image

# importing relevant libraries
import cv2
import numpy as np

# loading image
image_path = "images/918_spyder.jpg"
image = cv2.imread(image_path)

# getting image shape which returns height, width and channels
# as a tuple and then calculating the aspect ratio
(h, w) = image.shape[:2]
aspect_ratio = w / h

# resizing the image to decrease height by half of the original image
# Note: pixel values must be integers.
height = int(0.5 * h)
width = int(height * aspect_ratio)
# new image dimension as a tuple
dimension = (height, width)
resized_image = cv2.resize(image, dimension, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized Image", resized_image)
