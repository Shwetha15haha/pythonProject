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

import time

sg.theme('Black')

clock = sg.Text('', key='clock')

# Create a text label widget with an instruction for the user
label = sg.Text("Type in a todo")

# Create an input text box with a tooltip for user guidance and a unique key 'todo' for retrieving its value later
input_box = sg.InputText(tooltip="Enter todo", key='todo')

# Create an 'Add' button to allow users to add new to-dos to the list
add_button = sg.Button("Add")

# Create a list box to display the current to-do items, getting the items using a custom function
# `functions.get_todos()` retrieves the current list of tasks
list_box = sg.Listbox(values=functions.get_todos(),
                      key='todos',  # The key 'todos' is used to retrieve or update the selected to-do
                      enable_events=True,  # Allows events to trigger on selecting an item
                      size=[40, 10])  # Sets the size of the list box

# Create buttons for editing and completing tasks, and for exiting the application
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

# Define the layout of the window, placing widgets in a row-wise order
window = sg.Window('My To-Do App',
                   layout=[
                       [clock],
                       [label],
                       [input_box, add_button],
                       [list_box, edit_button, complete_button],
                       [exit_button]],  # Organize the components in a 2x2 grid
                   font=('Helvetica', 10))  # Font style and size

# Event loop to keep the window open and responsive to user input until the user closes it
while True:
    # `window.read()` listens for user interaction (like button clicks or typing)
    event, values = window.read(timeout=10)

    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    # Print the event and values (for debugging purposes)
    print(event)  # e.g., "Add", "Edit", "todos", etc.
    print(values)  # e.g., {'todo': 'Master python', 'todos': [...]}

    # Handle events using match-case statement
    match event:
        case "Add":
            # Retrieve the current list of to-dos from storage
            todos = functions.get_todos()

            # Retrieve the new to-do item from the input box
            new_todo = values['todo']

            # Append the new to-do item to the existing list
            todos.append(new_todo)

            # Save the updated list of to-dos back to storage
            functions.write_todos(todos)

            # Update the list box in the GUI to display the updated to-do list
            window['todos'].update(values=todos)
            window['todo'].update(value='')

        case "Edit":
            try:
                # Get the to-do item that was selected in the list box
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
                window['todo'].update(value='')

            except IndexError:
                sg.popup("Please select an item to edit", font=('Helvetica', 10))

        case "Complete":
            try:
                # Get the to-do item that was selected for completion
                to_to_complete = values['todos'][0]

                # Retrieve the current list of to-dos
                todos = functions.get_todos()

                # Remove the completed to-do item from the list
                todos.remove(to_to_complete)

                # Save the updated list of to-dos back to storage
                functions.write_todos(todos)

                # Update the list box and clear the input box
                window['todos'].update(values=todos)
                window['todo'].update(value='')

            except IndexError:
                sg.popup("Please select an item to complete", font=('Helvetica', 10))

        case "Exit":
            # Exit the application loop
            break

        case 'todos':
            # Update the input box to display the selected to-do item for editing
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            # Exit the loop if the window is closed
            break

# Close the window after the event loop finishes
window.close()
