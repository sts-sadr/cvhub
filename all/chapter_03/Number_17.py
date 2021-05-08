"""
    Gradients and Edge Detection

    Edge detection methods:
        - Finding gradients
        - Canny edge detection

    Finding gradients:
        - Sobel derivatives
        - Laplacian derivatives

    Sobel derivatives:
        The Sobel method is a combination of Gaussian smoothing and Sobel differentiation, which computes
        an approximation of the gradient of an image intensity function. Because of the Gaussian smoothing,
        this method is resistant to noise. We can perform derivatives either in the horizontal or vertical
        direction by passing the arguments xorder and yorder, respectively. The Sobel() function also takes
        an argument ksize that we use to define the kernel size. If we set ksize to -1, OpenCV will internally
        apply a 3×3 Schar filter, which generally gives a better result compared to the 3×3 Sobel filter.
"""

# Sobel derivatives

from cv2 import (imread, imshow, waitKey, cvtColor, COLOR_BGR2GRAY, bilateralFilter,
           Sobel, CV_64F)
from numpy import (uint8, absolute)
