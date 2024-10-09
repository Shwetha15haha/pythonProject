"""
This module demonstrates how to create a simple GUI application for managing to-dos using FreeSimpleGUI.

FreeSimpleGUI is a Python package that enables developers to easily create graphical user interfaces.
This application allows users to:
    - Add new to-dos to a list
    - Edit existing to-dos from the list
    - View and interact with the list using a graphical interface.
"""

# Import custom functions from another module (typically includes functions to get and write todos)
import functions

# Import FreeSimpleGUI for creating the graphical interface
import FreeSimpleGUI as sg

# Create a text label widget with an instruction for the user
label = sg.Text("Type in a todo")

# Create an input text box with a tooltip for user guidance and a unique key 'todo' for retrieving its value later
input_box = sg.InputText(tooltip="Enter todo", key='todo')

# Create an 'Add' button to allow users to add new to-dos to the list
add_button = sg.Button("Add")

# Create a list box to display the current to-do items, getting the items using a custom function
# `functions.get_todos()` `enable_events=True` ensures that when a list item is clicked, it triggers an event
list_box = sg.Listbox(values=functions.get_todos(),
                      key='todos',  # The key 'todos' is used to retrieve or update the selected to-do
                      enable_events=True,  # Allows events to trigger on selecting an item
                      size=[40, 10])  # Sets the size of the list box

# Create an 'Edit' button to allow users to edit selected to-do items
edit_button = sg.Button("Edit")

# Define the layout of the window, placing widgets in a row-wise order
# The window includes the label, input box, 'Add' button, list box, and 'Edit' button
window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=('Helvetica', 10))  # Font style and size

# Event loop to keep the window open and responsive to user input until the user closes it
while True:
    # `window.read()` listens for user interaction (like button clicks or typing)
    # `event` is the type of interaction (button click, window close, etc.)
    # `values` contains data from input fields keyed by their 'key'
    event, values = window.read()

    # Print the event and values (for debugging purposes)
    print(event)  # e.g., "Add", "Edit", "todos", etc.
    print(values)  # e.g., {'todo': 'Master python', 'todos': [...]}

    # Print the selected to-do items (debugging)
    print(values["todos"])

    # Handle events using match-case statement (similar to switch-case in other languages)
    match event:
        case "Add":
            # If the "Add" button is clicked:
            # Retrieve the current list of to-dos from storage (using a custom function)
            todos = functions.get_todos()

            # Retrieve the new to-do item from the input box
            new_todo = values['todo']

            # Append the new to-do item to the existing list of to-dos
            todos.append(new_todo)

            # Save the updated list of to-dos back to storage (using a custom function)
            functions.write_todos(todos)

            # Update the list box in the GUI to display the updated to-do list
            window['todos'].update(values=todos)

        case "Edit":
            # If the "Edit" button is clicked:
            # Get the to-do item that was selected in the list box (first selected item in the list)
            todo_to_edit = values['todos'][0]

            # Get the new to-do text from the input box
            new_todo = values['todo']

            # Retrieve the current list of to-dos
            todos = functions.get_todos()

            # Find the index of the selected to-do item in the list
            index = todos.index(todo_to_edit)

            # Replace the selected to-do item with the new value
            todos[index] = new_todo

            # Save the updated list of to-dos back to storage
            functions.write_todos(todos)

            # Update the list box to reflect the edited to-do item
            window['todos'].update(values=todos)

        case 'todos':
            # If a to-do is selected in the list box:
            # Update the input box to display the selected to-do item (for possible editing)
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            # If the user closes the window, exit the loop and close the application
            break

# Close the window once the event loop has finished
window.close()
