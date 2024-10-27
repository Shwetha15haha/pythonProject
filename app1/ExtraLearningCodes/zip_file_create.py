import zipfile  # Importing the zipfile module to work with ZIP files
import pathlib  # Importing pathlib to handle file system paths in an OS-independent way


# Function to create a ZIP archive from a list of file paths
def make_archive(filepaths, dest_dir):
    """
    Compresses multiple files into a ZIP archive.

    Parameters:
    filepaths (list): List of file paths to be added to the ZIP archive.
    dest_dir (str): Directory where the compressed ZIP file will be saved.

    Returns:
    None
    """
    # Define the destination path where the ZIP file will be created, named "compressed.zip"
    dest_path = pathlib.Path(dest_dir, "compressed.zip")

    # Create a new ZIP file in 'write' mode
    with zipfile.ZipFile(dest_path, 'w') as archive:
        # Iterate over each file path in the provided list
        for filepath in filepaths:
            # Convert each filepath to a pathlib.Path object to ensure compatibility across OS
            filepath = pathlib.Path(filepath)
            # Add the file to the archive, using the file's name (without the full path)
            archive.write(filepath, arcname=filepath.name)


# Main block to call the make_archive function
if __name__ == '__main__':
    # Example: Compressing a list of files into a ZIP file located in the 'dest' directory
    make_archive(filepaths=['main.py'], dest_dir='dest')
