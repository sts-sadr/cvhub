# Loading, Exploring and Showing an Image

# importing relevant libraries
import cv2

# image path
image_path = "images/EverLookNeverSee.jpg"
# read or load image from its path
image = cv2.imread(image_path)

# image is a Numpy array
print(f"Dimensions of the image: {image.ndim}")
print(f"Image height: {image.shape[0]}")
print(f"Image width: {image.shape[1]}")
print(f"Image channels: {image.shape[2]}")
print(f"Size of the image array: {image.size}")
print(f"data type of pixels: {image.dtype}")

# Display the image and wait until a key is pressed
cv2.imshow("My_Image", image)
cv2.waitKey(0)
