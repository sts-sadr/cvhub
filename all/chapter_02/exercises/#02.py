# Exercise_02: Draw two concentric circles with the outermost circle having a
# radius of 1.5 times the radius of the inner circle.

# importing relevant libraries
import cv2
import numpy as np

# creating a new canvas
canvas = np.zeros((500, 500, 3), dtype="uint8")

# setting circle features
center = (250, 250)
radius_1 = 100
radius_2 = 150
color = (200, 0, 0)
thickness = 1

# drawing circles
cv2.circle(canvas, center, radius_1, color, thickness)
cv2.circle(canvas, center, radius_2, color, thickness)
# displaying modified photo
cv2.imshow("Circle", canvas)
cv2.waitKey(0)
