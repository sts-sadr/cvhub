"""
    Gradients and Edge Detection

    Laplacian Derivatives:
        The Laplacian operator calculates the second derivative of the pixel intensity function to
        determine the edges in the image. The Laplacian operator calculates the gradients based on
        the following equation:

            Laplacian(f) = \frac{\partial^2f}{\partial x^2} + \frac{\partial^2f}{\partial y^2}
"""

# Laplacian derivative

from cv2 import (imread, imshow, waitKey, cvtColor, COLOR_BGR2GRAY, bilateralFilter, Laplacian, CV_64F)
from numpy import uint8, absolute
