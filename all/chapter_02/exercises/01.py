# Exercise_01: Drawing a solid circle at the center of the canvas

# importing relevant libraries
import cv2
import numpy as np

# creating a new canvas
canvas = np.zeros((500, 500, 3), dtype="uint8")

# setting circle features
center = (250, 250)
radius = 100
color = (200, 0, 0)
thickness = -1

# drawing circle
cv2.circle(canvas, center, radius, color, thickness)
# displaying modified photo
cv2.imshow("Circle", canvas)
cv2.waitKey(0)
