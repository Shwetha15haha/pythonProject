import FreeSimpleGUI as sg  # Use PySimpleGUI for creating the graphical interface
from zip_file_extractor import extract_archive  # Importing the extraction logic

# Set a theme for the window (Black theme in this case)
sg.theme("Black")

# Create a text label widget for selecting the archive file
label1 = sg.Text("Select archive file:")

# Create an input box to show the selected archive file path
input_box_1 = sg.Input(tooltip='Select the file to extract', key='archive', enable_events=True)

# Create a "Choose" button for selecting the archive file
choose_button1 = sg.FileBrowse("Choose", file_types=(("Zip Files", "*.zip"),))

# Create a text label widget for selecting the destination folder
label2 = sg.Text("Select destination folder:")

# Create an input box to show the selected folder path
input_box_2 = sg.Input(tooltip='Select where to extract the files', key='folder', enable_events=True)

# Create a "Choose" button for selecting the destination folder
choose_button2 = sg.FolderBrowse("Choose")

# Create an "Extract" button to initiate the extraction process
extract_button = sg.Button("Extract", bind_return_key=True)

# Create an output text element to show messages (e.g., success or error)
output_label = sg.Text("", key='output', text_color='green')

# Define the layout of the window
layout = [
    [label1, input_box_1, choose_button1],
    [label2, input_box_2, choose_button2],
    [extract_button],
    [output_label]
]

# Create the window with the given title and layout
window = sg.Window('Archive Extractor', layout)

# Main event loop to handle user interactions
while True:
    # Read events (button presses) and the values from the input fields
    event, values = window.read()

    # Close the window if the user presses the "X" button or closes the window
    if event == sg.WIN_CLOSED:
        break

    # If the "Extract" button is pressed
    if event == "Extract":
        # Get the file path for the archive and destination folder from the input fields
        archive_path = values['archive']
        dest_dir = values['folder']

        # Validate if both paths are provided
        if archive_path and dest_dir:
            try:
                # Call the function to extract the archive
                extract_archive(archive_path, dest_dir)

                # Update the output label with a success message
                window['output'].update(value="Extraction completed successfully!", text_color='green')
            except Exception as e:
                # Update the output label with an error message
                window['output'].update(value=f"Error: {e}", text_color='red')
        else:
            # Prompt user to provide valid input if fields are empty
            window['output'].update(value="Please select both an archive file and a destination folder.", text_color='red')

# Close the window when the loop ends
window.close()
