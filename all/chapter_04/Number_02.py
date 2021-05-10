# RGB color histogram

from cv2 import (imread, imshow, waitKey, calcHist)
import matplotlib.pyplot as plt


# Loading the image
original_image = imread("images/Bill-Gates.jpg")
imshow("Original Color Image", original_image)

# OpenCV stores color in BGR sequence
colors = ("blue", "green", "red")
# Calculating the histogram
for i, color in enumerate(colors):
    hist = calcHist([original_image], [i], None, [256], [0, 255])
    # plotting the histogram graph
    plt.plot(hist, color=color)

# plotting the histogram
plt.title("RGB Color Histogram")
plt.xlabel("Bins")
plt.ylabel("Number of pixels")
plt.show()
waitKey(0)
