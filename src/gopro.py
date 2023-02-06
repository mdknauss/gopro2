import os
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py subdirectory")
    sys.exit()

directory = sys.argv[1]

if not os.path.isdir(directory):
    print(f"{directory} is not a valid directory")
    sys.exit()

# Replace forward slashes with backslashes (if any)
directory = directory.replace('/', '\\')

# Get a list of all the file names in the directory
files = os.listdir(directory)

# Filter the list of file names to only include files that end with "MP4"
files = [file for file in files if file.endswith(".MP4")]

# Sort the list of file names by the timestamp of their creation
files.sort(key=lambda x: os.path.getctime(os.path.join(directory, x)))

# Use a for loop to rename the files in alphabetic order
for i, file in enumerate(files):
    prefix = chr(i + ord('a'))
    os.rename(os.path.join(directory, file), os.path.join(directory, f'{prefix}_{file}'))