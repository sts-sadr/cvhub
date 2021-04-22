# Image flipping horizontally, Vertically and then horizontally plus vertically

# import statements
import cv2

# Loading the image
image_path = "images/918_spyder.jpg"
image = cv2.imread(image_path)

# Flip horizontally
flip_horizontally = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flip_horizontally)
cv2.waitKey(-1)

# Flip vertically
flip_vertically = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flip_vertically)
cv2.waitKey(-1)
