import cv2

# Read the image
image = cv2.imread('universe-space.webp')

# Resize the image to 300x300 pixels
resized_image = cv2.resize(image, (300, 300))

# Save the resized image
cv2.imwrite('resized_universe-space.webp', resized_image)
