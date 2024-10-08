"""
This module demonstrates how to create a simple GUI application for managing to-dos using FreeSimpleGUI.

FreeSimpleGUI is a Python package that enables developers to easily create graphical user interfaces.
"""

# Import custom functions from another module
import functions

# Import FreeSimpleGUI for creating the graphical interface
import FreeSimpleGUI as sg

# Create a text label widget with the instruction
label = sg.Text("Type in a todo")

# Create an input text box with a tooltip for user guidance and unique key for retrieval
input_box = sg.InputText(tooltip="Enter todo", key='todo')

# Create an 'Add' button to add new to-dos
add_button = sg.Button("Add")

list_box = sg.Listbox(values=functions.get_todos(),
                      key='todos',
                      enable_events=True,
                      size=[40, 10])

edit_button = sg.Button("Edit")

# Define the layout of the window with the label, input box,button and font
# window = sg.Window('My To-Do App', layout=[[label], [input_box, add_button]])
window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button], [list_box,edit_button]],
                   font=('Helvetica', 10))

# Display the window and wait for user interaction

# Event loop to display the window and wait for user interaction
while True:
    event, values = window.read()
    print(event)
    print(values)
    # Handle events using a match-case statement
    match event:
        case "Add":
            # Get the current list of to-dos from the functions module
            todos = functions.get_todos()
            # Retrieve the new to-do item from the input box
            new_todo = values['todo']
            # Append the new to-do item to the list
            todos.append(new_todo)
            # Write the updated list of to-dos back to storage
            functions.write_todos(todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = todos
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case sg.WIN_CLOSED:
            # Break the loop if window is closed
            break

# Close the window when the interaction is complete
window.close()

# Add
# {'todo': 'Master python'}