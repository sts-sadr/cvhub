# Addition of two images

# import statements
import cv2


# Loading images
image_1_path = "images/Abraham_Lincoln.jpg"
image_2_path = "images/Albert_Einstein.jpg"

image_1 = cv2.imread(image_1_path)
image_2 = cv2.imread(image_2_path)


# Resizing the images to make them of the same dimension
resized_images_1 = cv2.resize(image_1, (800, 800), interpolation=cv2.INTER_AREA)
resized_images_2 = cv2.resize(image_2, (800, 800), interpolation=cv2.INTER_AREA)


# Addition process
result = cv2.add(resized_images_1, resized_images_2)

# # Displaying the images in order to see differences
cv2.imshow("Resized image 1", resized_images_1)
cv2.imshow("Resized image 2", resized_images_2)
cv2.imshow("Addition result", result)
cv2.waitKey(0)
