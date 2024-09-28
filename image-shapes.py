import cv2

# Read the image
image = cv2.imread('universe-space.webp')

# Draw a blue rectangle
cv2.rectangle(image, (50, 50), (200, 200), (255, 0, 0), 2)

# Draw a red circle
cv2.circle(image, (300, 300), 50, (0, 0, 255), -1)

# Add some text
cv2.putText(image, 'OpenCV', (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

# Save the image with drawings
cv2.imwrite('universe-space-image_with_shapes.webp', image)
