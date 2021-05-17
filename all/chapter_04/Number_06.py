"""
    HOGs:
        Histograms of oriented gradients (HOGs) are important feature descriptors used
        in computer vision and machine learning for object detection. HOGs describe the
        structural shape and appearance of an object in an image. The HOG algorithm computes
        the occurrences of gradient orientation in localized portions of the image.
"""

# HOG Calculation

from skimage.feature import hog
from cv2 import (imread, imshow, waitKey, resize)

# Loading the image
original_image = imread("images/Bill-Gates.jpg")

# Resizing the image
resized_image = resize(original_image, (int(original_image.shape[0] / 5),
                                        int(original_image.shape[1] / 5)))

# Calculating HOG
(HOG, hog_image) = hog(resized_image, orientations=9, pixels_per_cell=(8, 8),
                       cells_per_block=(2, 2), visualize=True, transform_sqrt=True,
                       block_norm="L2-Hys", feature_vector=True)
print(f"Image Dimension: {resized_image.shape}")
print(f"Feature vector Dimension: {HOG.shape}")

# Displaying the results
imshow("Original Image", original_image)
imshow("Resized Image", resized_image)
imshow("HOG Image", hog_image)
waitKey(0)
