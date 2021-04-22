# Image translation along the x- and y-axes

# importing relevant libraries
import cv2
import numpy as np


# Loading image
image_path = "./images/918_spyder.jpg"
image = cv2.imread(image_path)

# Defining translation matrix
translation_matrix = np.float32([
    [1, 0, 250],
    [0, 1, 120]
])

# Moving the image
moved_image = cv2.warpAffine(image, translation_matrix,
                             (image.shape[1], image.shape[0]))
cv2.imshow("Moved image", moved_image)
cv2.waitKey(0)
