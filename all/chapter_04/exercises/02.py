"""
    Exercise 02:
        Create a histogram of a masked image
"""

from cv2 import (imread, imshow, waitKey, calcHist)
import matplotlib.pyplot as plt
import numpy as np

# Loading the image
original_image = imread("../images/Bill-Gates.jpg")
imshow("Original Image", original_image)
