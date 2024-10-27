"""
This module demonstrates how to use the shutil module to create a zip archive.

The shutil module offers a number of high-level operations on files and collections of files. In particular, functions are provided which support file copying and removal.
"""

import shutil  # Import the shutil module for high-level file operations

# Create a ZIP archive from the 'files' directory, and name it 'output.zip'
shutil.make_archive('files/weather.csv', 'zip', '../files')
