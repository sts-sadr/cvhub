"""
    Noise reduction using smoothing and blurring

    Median Blurring:
        Median blurring is an effective technique for reducing salt-and-pepper type of noise.
        Median blurring is similar to mean blurring except that the central value of the kernel
        is replaced by the median of the surrounding pixels.
"""

from cv2 import imread, imshow, waitKey, medianBlur
