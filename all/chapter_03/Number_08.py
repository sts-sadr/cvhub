"""
    Masking:
        Masking refers to the “hiding” or “filtering” of an image.
        When we mask an image, we hide a portion of the image with some other image.
        In other words, we put our focus on a portion of the image by applying a mask
        on the remaining portion of the image.
"""

import cv2
import numpy as np


# Loading sample image
sample_image = cv2.imread("images/Albert_Einstein.jpg")
cv2.imshow("Albert Einstein", sample_image)
