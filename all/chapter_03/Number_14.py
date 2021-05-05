"""
    Binarization with Thresholding

    Image binarization is the process of converting a grayscale image into a binary—a black
    and-white—image. We apply a technique called thresholding to binarize an image. We first
    decide on a threshold value. A pixel value greater than this threshold is changed to 255,
    and a pixel with a lesser value than the threshold is set to 0. The resultant image will
    have only two values of the pixels—0 and 255—which are black-and-white color values. Thus,
    a grayscale image is converted into a black-and-white image (also called a binary image).
"""

# Simple Thresholding

from cv2 import (imread, imshow, waitKey, threshold, THRESH_BINARY, THRESH_BINARY_INV,
                 cvtColor, COLOR_BGR2GRAY)


# Loading the image
original_image = imread("images/Abraham_Lincoln.jpg")
imshow("Original Image", original_image)

# Converting to grayscale
grayscale_image = cvtColor(original_image, COLOR_BGR2GRAY)
imshow("GrayScale Image", grayscale_image)

# Binarize using thresholding
(T, binarized_image) = threshold(grayscale_image, 60, 255, THRESH_BINARY)
imshow("Binarized Image", binarized_image)
