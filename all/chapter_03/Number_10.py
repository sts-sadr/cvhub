"""
    Noise reduction using smoothing and blurring

    Smoothing, also called blurring, is an important image processing technique to reduce
    noise present in an image.

    Types of noise that we encounter in an image:
        - Salt and pepper noise
        - Impulse noise
        - Gaussian noise

    Mean filtering or averaging:
        Taking a small portion of image(called kernel and sliding window) then moving this
        window from left to right and from top to bottom. The pixel at the center of this
        kernel(matrix) is replaced by the average of all the pixels surrounding it.
"""

# Smoothing and/or blurring by mean filtering or averaging

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

# Displaying the results
imshow("Blurred 3x3", blurred_3)
imshow("Blurred 5x5", blurred_5)
imshow("Blurred 7x7", blurred_7)
waitKey(0)
