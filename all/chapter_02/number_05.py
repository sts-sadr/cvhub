# Drawing a rectangle on an new canvas

# importing relevant libraries
import cv2
import numpy as np

# creating a new canvas
canvas = np.zeros((200, 200, 3), dtype="uint8")
# setting start and end coordinates of the top-left
# and bottom-right  of rectangle
start = (10, 10)
end = (100, 100)
# setting the thickness
thickness = 5

# Drawing rectangle
cv2.rectangle(canvas, start, end, color=(0, 0, 255), thickness=thickness)
# saving the modified image
cv2.imwrite("rec_photo_2.jpg", canvas)
# displaying the modified image
cv2.imshow("Rectangle", canvas)
cv2.waitKey(0)
