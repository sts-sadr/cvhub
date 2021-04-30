"""
    Noise reduction using smoothing and blurring

    Smoothing, also called blurring, is an important image processing technique to reduce
    noise present in an image.

    Types of noise that we encounter in an image:
        - Salt and pepper noise
        - Impulse noise
        - Gaussian noise
"""

from cv2 import blur, imread, imshow, waitKey

# Loading the image
original_image = imread("images/918_spyder.jpg")
imshow("Original Image", original_image)

# Defining the kernels
kernel3by3 = (3, 3)
kernel5by5 = (5, 5)
kernel7by7 = (7, 7)

# performing blur process
blurred_3 = blur(original_image, kernel3by3)
blurred_5 = blur(original_image, kernel5by5)
blurred_7 = blur(original_image, kernel7by7)
