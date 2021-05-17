"""
    LBP:
        Local binary patterns (LBP) is a type of feature descriptor for image texture classification.
"""

# LBP Image and Histogram Calculation

from numpy import histogram
from skimage.feature import local_binary_pattern
from cv2 import (imread, imshow, waitKey, resize, cvtColor, COLOR_BGR2GRAY, calcHist)
