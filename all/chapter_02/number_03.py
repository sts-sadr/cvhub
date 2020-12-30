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

# setting the color in BGR
color = (255, 0, 0)
# setting the thickness
thickness = 4

# Drawing a line
cv2.line(image, start, end, color, thickness)

# displaying the modified image
cv2.imshow("Modified image", image)
cv2.waitKey(0)
