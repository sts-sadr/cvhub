# Accessing and manipulating pixels

# importing relevant libraries
import cv2

# image path
image_path = "images/EverLookNeverSee.jpg"
# read or load image from its path
image = cv2.imread(image_path)

# Accessing pixel at (0, 0) location
(b, g, r) = image[0, 0]
print(f"Blue, green and red values at (0, 0); {(b, g, r)}")

# Manipulating pixels and showing modified image
image[20: 150, 20: 150] = (255, 255, 0)
cv2.imshow("Modified image", image)
cv2.waitKey(0)
