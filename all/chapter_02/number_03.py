# Drawing a line on an image

# importing relevant libraries
import cv2

# image path
image_path = "images/EverLookNeverSee.jpg"
# read or load image from its path
image = cv2.imread(image_path)

# setting start and end coordinates
start = (0, 0)
end = (image.shape[1], image.shape[0])