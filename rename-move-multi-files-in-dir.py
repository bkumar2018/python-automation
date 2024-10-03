import os
import shutil

# Define source and destination folders
src_folder = "test_auto/"
dest_folder = "test_dest/"

# Loop through the files in the source folder
for filename in os.listdir(src_folder):
    # Create full path to the file
    src_file = os.path.join(src_folder, filename)
    dest_file = os.path.join(dest_folder, "new_" + filename)

    # Move and rename the file
    shutil.move(src_file, dest_file)

print("Files moved and renamed successfully!")
