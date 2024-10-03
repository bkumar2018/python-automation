import os
# import subprocess

# Define the directory path and the prefix to add
directory = "test_auto/"
prefix = "renamed_"


# # Running a simple shell command
# result = subprocess.run(['touch file{1..3}.txt'], capture_output=True, text=True)

# # Output the result
# print(result.stdout)


# Loop through all the files in the directory
for filename in os.listdir(directory):
    # Construct the new name
    new_name = prefix + filename
    # Rename the file
    os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))

print("Files renamed successfully!")
