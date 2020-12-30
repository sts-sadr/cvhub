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