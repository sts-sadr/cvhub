# Accessing and manipulating pixels

# Importing relevant modules
from cv2 import imread, imshow, waitKey

# Image path
image_path = "images/EverLookNeverSee.jpg"
# Read or load image from its path
image = imread(image_path)

# Accessing pixel at (0, 0) location
(b, g, r) = image[0, 0]
print(f"Blue, green and red values at (0, 0); {(b, g, r)}")

# Manipulating pixels and showing modified image
image[20: 150, 20: 150] = (255, 255, 0)
imshow("Modified image", image)
waitKey(0)
