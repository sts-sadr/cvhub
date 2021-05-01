"""
    Noise reduction using smoothing and blurring

    Median Blurring:
        Median blurring is an effective technique for reducing salt-and-pepper type of noise.
        Median blurring is similar to mean blurring except that the central value of the kernel
        is replaced by the median of the surrounding pixels.
"""

from cv2 import imread, imshow, waitKey, medianBlur

# Loading the noisy image
noisy_image = imread("images/salt_and_pepper_noise.jpg")
imshow("Noisy Image", noisy_image)

# Performing median filtering
# median filtering using 3x3 kernel
filtered_image_3 = medianBlur(noisy_image, 3)
imshow("Median filtered image kernel=3", filtered_image_3)
