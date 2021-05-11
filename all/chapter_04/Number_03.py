"""
    Histogram Equalizer:
        Histogram equalization is an image processing technique to adjust the contrast of an image.
        It is a method of redistributing the pixel intensities in such a way that the intensities of
        the under-populated pixels are equalized to the intensities of over-populated pixel intensities
"""

from cv2 import (imread, imshow, waitKey, cvtColor, COLOR_BGR2GRAY, calcHist, equalizeHist)
import matplotlib.pyplot as plt


# Loading the image and converting it to grayscale
original_image = imread("images/Bill-Gates.jpg")
grayscale_image = cvtColor(original_image, COLOR_BGR2GRAY)
imshow("GrayScale Image", grayscale_image)

# Calculating the histogram without using equalizer
hist = calcHist([grayscale_image], [0], None, [256], [0, 255])

# Plotting the histogram graph
plt.figure()
plt.title("Grayscale Histogram Without Using Equalizer")
plt.xlabel("Bins")
plt.ylabel("Number of pixels")
plt.plot(hist)
plt.show()

# Equalizing the image
equalized_image = equalizeHist(grayscale_image)
imshow("Equalized Image", equalized_image)
# Calculating the histogram
equalized_hist = calcHist([equalized_image], [0], None, [256], [0, 255])

# Plotting histogram
plt.figure()
plt.title("Grayscale Histogram of Equalized Image")
plt.xlabel("Bins")
plt.ylabel("Number of pixels")
plt.plot(equalized_hist)
plt.show()
waitKey(0)
