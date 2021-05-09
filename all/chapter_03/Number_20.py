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
