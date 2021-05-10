"""
    Exercise 01:
        Plot a histogram of an image with 32 bins
"""

from cv2 import (imread, cvtColor, COLOR_BGR2GRAY, calcHist)
import matplotlib.pyplot as plt


# Loading the image and converting to grayscale
original_image = imread("../images/Bill-Gates.jpg")
grayscale_image = cvtColor(original_image, COLOR_BGR2GRAY)

# Calculating the histogram
hist = calcHist([grayscale_image], [0], None, [32], [0, 255])

# Plotting histogram graph
plt.figure()
plt.title("GrayScale Histogram")
plt.xlabel("Bins")
plt.ylabel("Number of pixels")
plt.plot(hist)
plt.show()
