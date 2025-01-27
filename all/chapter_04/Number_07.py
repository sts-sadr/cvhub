"""
    LBP:
        Local binary patterns (LBP) is a type of feature descriptor for image texture classification.
"""

# LBP Image and Histogram Calculation

from numpy import histogram
import matplotlib.pyplot as plt
from skimage.feature import local_binary_pattern
from cv2 import (imread, imshow, waitKey, resize, cvtColor, COLOR_BGR2GRAY, calcHist)


# Loading the image, resizing and converting to grayscale
original_image = imread("images/Bill-Gates.jpg")
resized_image = resize(original_image, (int(original_image.shape[0] / 5),
                                        int(original_image.shape[1] / 5)))
grayscale_image = cvtColor(resized_image, COLOR_BGR2GRAY)
imshow("GrayScale Image", grayscale_image)

# Calculating histogram of grayscale image
grayscale_hist = calcHist(grayscale_image, [0], None, [256], [0, 255])

# Plotting the histogram of grayscale image
plt.figure()
plt.title("Histogram of grayscale image")
plt.plot(grayscale_hist, color="r")
plt.show()

# Calculating LBP image and histogram
radius = 3
points = 3 * 8
lbp = local_binary_pattern(grayscale_image, points, radius, method="default")
lbp_hist, _ = histogram(lbp, density=True, bins=256, range=(0, 255))

# Plotting histogram of LBP image
plt.figure()
plt.title("Histogram of lbp image")
plt.plot(lbp_hist, color="g")
plt.show()

# Displaying LBP Image
imshow("LBP Image", lbp)
waitKey(0)
