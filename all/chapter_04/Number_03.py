"""
    Histogram Equalizer:
        Histogram equalization is an image processing technique to adjust the contrast of an image.
        It is a method of redistributing the pixel intensities in such a way that the intensities of
        the under-populated pixels are equalized to the intensities of over-populated pixel intensities
"""

from cv2 import (imread, imshow, waitKey, cvtColor, COLOR_BGR2GRAY, calcHist, equalizeHist)
import matplotlib.pyplot as plt
