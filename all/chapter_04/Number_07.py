"""
    LBP:
        Local binary patterns (LBP) is a type of feature descriptor for image texture classification.
"""

# LBP Image and Histogram Calculation

from numpy import histogram
from skimage.feature import local_binary_pattern
from cv2 import (imread, imshow, waitKey, resize, cvtColor, COLOR_BGR2GRAY, calcHist)


# Loading the image, resizing and converting to grayscale
original_image = imread("images/Bill-Gates.jpg")
resized_image = resize(original_image, (int(original_image.shape[0] / 5),
                                        int(original_image.shape[1] / 5)))
grayscale_image = cvtColor(resized_image, COLOR_BGR2GRAY)
imshow("GrayScale Image", grayscale_image)
