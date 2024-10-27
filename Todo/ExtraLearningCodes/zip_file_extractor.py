import zipfile  # Importing the zipfile module to work with ZIP archives


# Function to extract a ZIP archive to a destination directory
def extract_archive(archivepath, dest_dir):
    """
    Extracts all the files from a ZIP archive to the specified destination directory.

    Parameters:
    archivepath (str): The full file path of the ZIP archive to be extracted.
    dest_dir (str): Directory where the extracted files will be saved.

    Returns:
    None
    """
    # Opening the ZIP file in 'read' mode to extract its contents
    with zipfile.ZipFile(archivepath, 'r') as archive:
        # Extracting all the contents to the specified destination directory
        archive.extractall(dest_dir)
        print(f"Files have been extracted to {dest_dir}")


# Main block to call the extract_archive function
if __name__ == '__main__':
    # Example usage of extract_archive function
    archive_path = r'C:\Users\moghe\PycharmProjects\pythonProject\Todo\ExtraLearningCodes\dest\compressed.zip'
    destination_dir = r'C:\Users\moghe\PycharmProjects\pythonProject\Todo\ExtraLearningCodes\dest'

    # Extracting the ZIP archive to the destination directory
    extract_archive(archive_path, destination_dir)
