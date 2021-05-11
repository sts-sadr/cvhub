# Calculation of Image Statistics from the GLCM

from cv2 import (imread, imshow, waitKey, cvtColor, COLOR_BGR2GRAY)
from skimage.feature import greycomatrix
from numpy import pi


# Reading the image and converting it to grayscale
original_image = imread("images/Bill-Gates.jpg")
grayscale_image = cvtColor(original_image, COLOR_BGR2GRAY)
imshow("Grayscale Image", grayscale_image)
