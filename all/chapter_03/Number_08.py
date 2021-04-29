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

# Creating a rectangular mask
mask_image = cv2.rectangle(np.zeros(sample_image.shape[:2], dtype="uint8"), (50, 50),
                           (int(sample_image.shape[1]) - 50, int(sample_image.shape[0] / 2) - 50),
                           (255, 255, 255), -1)
cv2.imshow("Mask Image", mask_image)
