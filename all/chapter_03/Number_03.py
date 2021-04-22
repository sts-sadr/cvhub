# Image rotation around the center of the image

import cv2

# Loading the image
image_path = "images/918_spyder.jpg"
image = cv2.imread(image_path)
(h, w) = image.shape[:2]

# Defining the rotation matrix
center = (h // 2, w // 2)
angle = -45
scale = 1.0
rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)

# Rotating the image
rotated_image = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]))

cv2.imshow("Rotated Image", rotated_image)
cv2.waitKey(0)
