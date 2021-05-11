# Calculation of Image Statistics from the GLCM

from cv2 import (imread, cvtColor, COLOR_BGR2GRAY)
from skimage.feature import greycomatrix, greycoprops
from numpy import pi


# Reading the image and converting it to grayscale
original_image = imread("images/Bill-Gates.jpg")
grayscale_image = cvtColor(original_image, COLOR_BGR2GRAY)

# Calculating GLCM
glcm = greycomatrix(grayscale_image, [2], [0, pi / 2])

# Calculating the contrast
contrast = greycoprops(glcm)
print(f"Contrast: {contrast}")

# Calculating dissimilarity
dissimilarity = greycoprops(glcm, prop="dissimilarity")
print(f"Dissimilarity: {dissimilarity}")

# Calculating homogeneity
homogeneity = greycoprops(glcm, prop="homogeneity")
print(f"Homogeneity: {homogeneity}")

# Calculating ASM
ASM = greycoprops(glcm, prop="ASM")
print(f"ASM: {ASM}")

# Calculating energy
energy = greycoprops(glcm, prop="energy")
print(f"Energy: {energy}")

# Calculating correlation
correlation = greycoprops(glcm, prop="correlation")
print(f"correlation: {correlation}")
