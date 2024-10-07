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

# Create an input text box with a tooltip for user guidance
input_box = sg.InputText(tooltip="Enter todo")

# Create an 'Add' button to add new to-dos
add_button = sg.Button("Add")

# Define the layout of the window with the label, input box, and button
window = sg.Window('My To-Do App', layout=[[label], [input_box, add_button]])

# Display the window and wait for user interaction
window.read()

# Close the window when the interaction is complete
window.close()
