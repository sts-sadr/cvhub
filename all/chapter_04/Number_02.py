# RGB color histogram

from cv2 import (imread, imshow, waitKey, calcHist)
import matplotlib.pyplot as plt


# Loading the image
original_image = imread("images/Bill-Gates.jpg")
imshow("Original Color Image", original_image)
