# Loading, Exploring and Showing an Image

# importing relevant modules
from cv2 import imread, imshow, waitKey

# Image path
image_path = "images/EverLookNeverSee.jpg"
# Read or load image from its path
image = imread(image_path)

# Image is a Numpy array
print(f"Dimensions of the image: {image.ndim}")
print(f"Image height: {image.shape[0]}")
print(f"Image width: {image.shape[1]}")
print(f"Image channels: {image.shape[2]}")
print(f"Size of the image array: {image.size}")
print(f"data type of pixels: {image.dtype}")

# Display the image and wait until a key is pressed
imshow("My_Image", image)
waitKey(0)
