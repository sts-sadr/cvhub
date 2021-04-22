# Image rotation around the center of the image

import cv2

# Loading the image
image_path = "images/918_spyder.jpg"
image = cv2.imread(image_path)
(h, w) = image.shape[:2]
