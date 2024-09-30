import os

# Define the directory and the prefix
directory = 'file-names/'
prefix = 'new_'

# Loop through all files in the directory
for filename in os.listdir(directory):
    # Create the new file name with prefix
    new_name = prefix + filename
    # Rename the file
    os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))

print("Files renamed successfully!")
