import cv2
import numpy as np

# Load an image from file
image_path = "C:\\Users\\harpreet\\OneDrive\\Documents\\Desktop\\PYTHON\\PROJECTS\\Hoi\\harry.jpg"
image = cv2.imread(image_path)

# Check if image was successfully loaded
if image is None:
    print(f"Error: Could not open or find the image at '{image_path}'.")
    exit()

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to the grayscale image
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Perform Canny edge detection
edges = cv2.Canny(blurred_image, 50, 150)

# Display the original image
cv2.imshow("Original Image", image)

# Display the grayscale image
cv2.imshow("Grayscale Image", gray_image)

# Display the blurred image
cv2.imshow("Blurred Image", blurred_image)

# Display the edge-detected image
cv2.imshow("Edges", edges)

# Wait for a key press and close all open windows
cv2.waitKey(0)
cv2.destroyAllWindows()
