"""
    Color Histogram

        A histogram is the distribution of pixel intensities in an image. Typically a histogram is
        visualized in the form of a graph (or chart). The x-axis of this graph represents the pixel
        values (or a range of values), and the y-axis represents the frequency (or count) of pixels
        of a particular value or a range of values. The peak of the graph shows the color with the
        highest number of pixels.
"""

# GrayScale Histogram

from cv2 import (imread, imshow, waitKey, cvtColor, COLOR_BGR2GRAY, calcHist)
import matplotlib.pyplot as plt


# Loading the image and converting to grayscale
original_image = imread("images/Bill-Gates.jpg")
grayscale_image = cvtColor(original_image, COLOR_BGR2GRAY)
imshow("Grayscale Image", grayscale_image)

# Calculating the histogram
hist = calcHist([grayscale_image], [0], None, [256], [0, 255])

# Plotting histogram graph
plt.figure()
plt.title("GrayScale Histogram")
plt.xlabel("Bins")
plt.ylabel("Number of pixels")
plt.plot(hist)
plt.show()
waitKey(0)
