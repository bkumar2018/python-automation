
# Opening and reading a file

with open('file.txt', "w") as file:
    file.write("This is a new file using python.")
    file.close()


with open('file.txt', "r") as file:
    data = file.read()
    print(data)
    file.close()