import cv2

# Read the image
image = cv2.imread('universe-space.webp')

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Save the grayscale image
cv2.imwrite('gray_image_uni-space.webp', gray_image)
