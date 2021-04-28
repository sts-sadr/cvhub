"""
    Bitwise Operations

    AND, OR, NOT, XOR
    For grayscale binary images the pixel value 0 means off and value greater than 0 means on.

    AND:
        The bitwise AND operation of two image arrays calculates element-wise conjunction.
        Bitwise AND can also be performed with an array and a scalar.

    OR:
        The bitwise OR operation calculates element-wise disjunction of two arrays or an array and a scalar.

    NOT:
        Bitwise NOT inverts the bit values of its operand.

    XOR:
        A bitwise XOR of the two operands “a” and “b” results in 1 if either but not both “a” or “b”
        is 1; otherwise, the result is 0.
"""

import cv2
import numpy as np


# Creating a circle
circle = cv2.circle(np.zeros((500, 500, 3), dtype="uint8"), (250, 250), 90, (255, 255, 255), -1)
cv2.imshow("A white circle", circle)

# Creating a square
square = cv2.rectangle(np.zeros((500, 500, 3), dtype="uint8"), (250, 250), (100, 100),
                       (255, 255, 255), -1)
cv2.imshow("A white square", square)
