# Image translation along the x- and y-axes

# importing relevant libraries
import cv2
import numpy as np


# Loading image
image_path = "./images/918_spyder.jpg"
image = cv2.imread(image_path)

# Defining translation matrix
translation_matrix = np.float32([
    [1, 0, 50],
    [0, 1, 20]
])
