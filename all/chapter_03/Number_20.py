"""
    Contours

    Contours are curves joining continuous points of the same intensity.
    To detect counters, we do the following:
        1. Convert the image to grayscale
        2. Binarize the image using any of the thresholding methods
        3. Apply the canny edge detection method
        4. Find all the contours using findContours method
        5. Draw contours using drawContours method
"""

# Detecting and drawing contours

from cv2 import (imread, imshow, waitKey, cvtColor, COLOR_BGR2GRAY, threshold, THRESH_BINARY_INV,
                 THRESH_OTSU, Canny, findContours, RETR_EXTERNAL, CHAIN_APPROX_SIMPLE, drawContours)


# Loading the image and converting to grayscale
original_image = imread("images/sudoku.png")
grayscale_image = cvtColor(original_image, COLOR_BGR2GRAY)
imshow("Grayscale Image", grayscale_image)

# Binarizing the image
(T, binarized_image) = threshold(grayscale_image, 0, 255, THRESH_BINARY_INV+THRESH_OTSU)
imshow("Binarized Image", binarized_image)

# Applying canny function
canny_applied = Canny(binarized_image, 0, 255)
imshow("Canny Applied", canny_applied)

# Finding contours
(contours, hierarchy) = findContours(canny_applied, RETR_EXTERNAL, CHAIN_APPROX_SIMPLE)
print(f"Number of contours determined are: {len(contours)}")
