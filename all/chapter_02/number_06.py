# Drawing a circle on an new canvas

# importing relevant libraries
import cv2
import numpy as np

# creating a new canvas
canvas = np.zeros((500, 500, 3), dtype="uint8")

# setting circle features
center = (250, 250)
radius = 100
color = (0, 0, 255)
thickness = 10

# drawing circle
cv2.circle(canvas, center, radius, color, thickness)
# saving modified image
cv2.imwrite("circle_photo.jpg", canvas)
# displaying modified photo
cv2.imshow("Circle", canvas)
cv2.waitKey(0)
