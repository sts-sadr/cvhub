"""
    Canny Edge Detection

    Canny edge detection is one of the most popular edge detection methods in image
    processing. This is a multistep process. It first blurs the image to reduce noise
    and then computes Sobel gradients in the X and Y directions, suppresses the edges
    where nonmaxima is calculated, and finally determines whether a pixel is “edge-like”
    or not by applying hysteresis thresholding.
"""

# Canny Edge Detection

from cv2 import (imread, imshow, waitKey, cvtColor, COLOR_BGR2GRAY, Canny)


# Loading the image and converting to grayscale
original_image = imread("images/sudoku.png")
grayscale_image = cvtColor(original_image, COLOR_BGR2GRAY)
imshow("Grayscale Image", grayscale_image)

# Canny function for edge detection
result = Canny(grayscale_image, 50, 170)
imshow("Canny Applied Image", result)
waitKey(0)
