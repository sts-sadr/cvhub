# Image cropping

# import statements
import cv2

# Loading image
image_path = "images/918_spyder.jpg"
image = cv2.imread(image_path)
cv2.imshow("Original Image", image)
cv2.waitKey(0)
