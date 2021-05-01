"""
    Noise reduction using smoothing and blurring

    Gaussian filtering:
        This blurring technique gives a more natural smoothing result compared to the averaging technique.
        In this filtering, we supply a Gaussian kernel instead of a boxed fixed kernel.
        A Gaussian kernel consists of the height, width, and standard deviations in the X and Y directions.
"""

from cv2 import imread, imshow, GaussianBlur, waitKey

# Smoothing using the Gaussian technique

# Loading the image
original_image = imread("images/Albert_Einstein.jpg")
imshow("Original Image", original_image)

# Gaussian blurring using 5x5 kernel and 0 standard deviation to calculate from kernel
filtered_image = GaussianBlur(original_image, (5, 5), 0)
imshow("Gaussian Filtered Image", filtered_image)
waitKey(0)
