# Automating Image and Video Processing

# Python provides powerful libraries like OpenCV and Pillow for image and video processing tasks. You can automate tasks like resizing, compressing, or applying filters to images, as well as extracting frames from videos or performing video analysis.
    

from PIL import Image

# Open an image
image = Image.open("plant.png")

# Resize the image
resized_image = image.resize((300, 600))

# Save the resized image
resized_image.save("resized_image.png")
