"""
    HOGs:
        Histograms of oriented gradients (HOGs) are important feature descriptors used
        in computer vision and machine learning for object detection. HOGs describe the
        structural shape and appearance of an object in an image. The HOG algorithm computes
        the occurrences of gradient orientation in localized portions of the image.
"""

# HOG Calculation

from skimage.feature import hog
from cv2 import (imread, imshow, waitKey, resize)

# Loading the image
original_image = imread("images/Bill-Gates.jpg")
imshow("Original Image", original_image)
