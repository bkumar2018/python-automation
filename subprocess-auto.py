import subprocess

# Create a new user
#subprocess.run(["useradd", "-m", "newuser"])

# Check disk usage
disk_usage = subprocess.check_output(["df", "-h"])
print(disk_usage.decode())


# For Linux/MacOS
result = subprocess.run(['ls'], capture_output=True, text=True)
print(result.stdout)

# For Windows, use 'dir'
# result = subprocess.run(['dir'], shell=True, capture_output=True, text=True)
# print(result.stdout)

# Ping google.com
result = subprocess.run(['ping', '-c', '4', 'google.com'], capture_output=True, text=True)
print(result.stdout)


# Try running a command that will fail
# result = subprocess.run(['ls', 'non_existent_file'], capture_output=True, text=True)

# # Capture both stdout and stderr
# print("STDOUT:", result.stdout)
# print("STDERR:", result.stderr)


# Running a shell command (using shell=True)
result = subprocess.run('echo Hello World!', shell=True, capture_output=True, text=True)
print(result.stdout)
