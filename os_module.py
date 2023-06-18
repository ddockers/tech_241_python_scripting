# Use os to do things

import os

#os.system('echo "Hello World!"')

# Make and change directories

# Create a directory

directory = "test_dir"

parent_dir = "C:/Users/dedo2"

path = os.path.join(parent_dir, directory)

# Create

#os.mkdir(path)

# Put a new file into the directory we just made

filename = "test_file.txt"
filepath = os.path.join(path, filename)

with open(filepath, "w") as file1:
    toFile = "Contents of file are writtten here"
    file1.write(toFile)

print("File" + filename + " created in " + directory + "folder")