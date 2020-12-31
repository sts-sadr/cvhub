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
