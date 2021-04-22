# Image cropping

# import statements
import cv2

# Loading image
image_path = "images/918_spyder.jpg"
image = cv2.imread(image_path)
cv2.imshow("Original Image", image)

# Cropping process
cropped_image = image[300:800, 500:1000]
cv2.imshow("Cropped Image", cropped_image)
cv2.waitKey(0)
