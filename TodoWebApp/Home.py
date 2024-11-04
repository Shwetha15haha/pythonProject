"""
Detailed Explanation:
Imports:
import streamlit as st: Imports the Streamlit library for building the web app UI.
import functions: Imports the functions module, which likely contains utility functions to get and write the list of todos.

Get Todos:
todos = functions.get_todos(): This calls the get_todos() function from the functions module to fetch the current list of todos (likely stored in a file or database).

Add Todo Function:
def add_todo(): This function adds a new todo to the list.
st.session_state['new_todo']: Streamlit uses session_state to store interactive widget values. Here, it fetches the value from the input field that the user typed in.
todos.append(todo): Adds the new todo to the list of existing todos.
functions.write_todos(todos): Saves the updated list of todos using the write_todos() function from the functions module.
st.session_state['new_todo'] = '': Resets the input field so the user can type a new todo without the old one remaining in the field.

App Layout:
st.title('Todo App'): This displays the main title of the app as "Todo App".
st.subheader('For personal use'): This is a smaller title indicating the app is for personal use.
st.write('Jot down everything you need to do now'): A simple description telling the user what to do.

Display Todos as Checkboxes:
for index, todo in enumerate(todos): Loops over the todos list and displays each todo as a checkbox.
checkbox = st.checkbox(todo, key=todo): For each todo, a checkbox is created. The key=todo ensures each checkbox has a unique identifier.
if checkbox: When a user checks a checkbox (i.e., marks a task as done), the following steps are executed:
todos.pop(index): Removes the completed todo from the list.
functions.write_todos(todos): Updates the stored todos by saving the updated list.
del st.session_state[todo]: Removes the todo from the session state (removing any internal reference).
st.rerun(): Reruns the Streamlit app to immediately reflect changes in the UI after modifying the todos list.

Adding New Todos:
st.text_input(label='', placeholder='Enter to do....', on_change=add_todo, key='new_todo'): Creates an input field where users can type a new todo.
on_change=add_todo: When the user hits enter after typing in the input box, the add_todo function is called to process the new todo.
key='new_todo': The input's value is stored in st.session_state under the key 'new_todo'.

"""
import streamlit as st  # Importing the Streamlit library for building the web app
import functions  # Importing custom functions that handle todo operations

# Fetch the list of existing todos using a function from the 'functions' module.
todos = functions.get_todos()

# Define a function to add a new todo item.
def add_todo():
    todo = st.session_state['new_todo']  # Accessing the new todo from session state
    todos.append(todo)  # Add the new todo to the list of todos
    functions.write_todos(todos)  # Save the updated todo list using a function
    st.session_state['new_todo'] = ''  # Reset the input field by clearing the session state

# Set the title and subheader of the Streamlit app
title = st.title('Todo App')  # Display the main title of the app
st.subheader('For personal use')  # Subheading to indicate it's a personal app
# st.write('Jot down everything you need to do now')  # A short description of what the app does

st.markdown('''
    :red[Jot] :orange[down] :green[everything] :blue[you] :violet[need]
    :rainbow[todo] :blue-background[now] .''')

# Iterate over the list of todos and display each as a checkbox
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)  # Display a checkbox for each todo item
    if checkbox:  # If the checkbox is checked, remove the todo item
        todos.pop(index)  # Remove the checked todo from the list
        functions.write_todos(todos)  # Save the updated list back using the custom function
        del st.session_state[todo]  # Delete the todo from session state
        st.rerun()  # Rerun the app to reflect the changes instantly

# Input field to add a new todo, triggered when the user presses enter
text = st.text_input(label='',
              placeholder='Enter to do....',
              key='new_todo')  # Use 'new_todo' as the session state key

# Add button to add new to do
st.button("Add", type="primary", on_click=add_todo)

# Execute bash command
# streamlit run Home.py

