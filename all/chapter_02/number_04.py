# Drawing a rectangle on an image

# importing relevant libraries
import cv2

# image path
image_path = "images/EverLookNeverSee.jpg"
# read or load image from its path
image = cv2.imread(image_path)

# setting the start and end coordinates of top-left
# and bottom-right of the rectangle
start = (85, 50)
end = (300, 300)

# setting the color and thickness of the outline
color = (0, 255, 0)
thickness = 2

# drawing the rectangle
cv2.rectangle(image, start, end, color, thickness)
# saving the modified image
cv2.imwrite("rec_photo.jpg", image)
# displaying the modified image
cv2.imshow("Rectangle", image)
cv2.waitKey(0)
