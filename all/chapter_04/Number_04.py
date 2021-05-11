"""
    GLCM:
        The gray-level co-occurrence matrix (GLCM) is the distribution of simultaneously
        occurring pixel values within a given offset. An offset is the position (distance
        and direction) of adjacent pixels. As the name implies, the GLCM is always calculated
        for a grayscale image.
"""

from cv2 import (imread, imshow, waitKey, cvtColor, COLOR_BGR2GRAY)
import skimage.feature as sk
