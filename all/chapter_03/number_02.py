# Image translation along the x- and y-axes

# importing relevant libraries
import cv2
import numpy as np


# Loading image
image_path = "./images/918_spyder.jpg"
image = cv2.imread(image_path)

# Defining translation matrix
translation_matrix = np.float32([
    [1, 0, 250],  # the movement along the x axis by 250 pixels to the right
    [0, 1, 120]   # the movement along the y axis by 120 pixels down
])

# Moving the image
"""
The last argument is a tuple that has the width and height of the
canvas within which we want to move our image. In this example, we
are keeping the canvas size the same as the original height and width
of the image.
"""
moved_image = cv2.warpAffine(image, translation_matrix,
                             (image.shape[1], image.shape[0]))
cv2.imshow("Moved image", moved_image)
cv2.waitKey(0)
