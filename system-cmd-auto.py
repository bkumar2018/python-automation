import subprocess

# Run a system command (e.g., list files in a directory)
command = subprocess.run(['ls', '-l'], capture_output=True, text=True)

# Print the output of the command
print(command.stdout)
