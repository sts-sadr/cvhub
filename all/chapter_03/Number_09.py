"""
    Splitting and merging channels

    Split the image into respective color components
"""

import cv2
import numpy as np


# Loading an image
sample_image = cv2.imread("images/Abraham_Lincoln.jpg")
cv2.imshow("Abraham Lincoln", sample_image)

# Splitting the image into component colors
(b, g, r) = cv2.split(sample_image)

# Displaying the components
cv2.imshow("Blue Image", b)
cv2.imshow("Green Image", g)
cv2.imshow("Red Image", r)
cv2.waitKey(0)
