# Drawing a rectangle on an image

# importing relevant libraries
import cv2

# image path
image_path = "images/EverLookNeverSee.jpg"
# read or load image from its path
image = cv2.imread(image_path)

# setting the start and end coordinates of top-left
# and bottom-right of the rectangle
start = (30, 30)
end = (370, 370)

# setting the color and thickness of the outline
color = (0, 255, 0)
thickness = 2
