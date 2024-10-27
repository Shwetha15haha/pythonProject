# findfiles.py

# Import the glob module for file pattern matching
import glob

# Get a list of all .txt files in the "files" directory that start with 'd'
myfiles = glob.glob("files/d*.txt")
print(myfiles)  # Print the list of matched files
#
# Example output:
# ['files\\data.txt', 'files\\doc.txt']

# Iterate over the list of files
for files in myfiles:
    # Open each file in read mode
    with open(files, 'r') as file:
        # Read the file content and print it, followed by a newline for separation
        print(file.read() + '\n')

# Output :
# temperatures
# 5
# 32
# 38
# 23
# 24
#
# This is file related code