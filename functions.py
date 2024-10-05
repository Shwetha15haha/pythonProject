# Creating a custom function to get todos
def get_todos(filepath='files/todos.txt'):
    """Open the text file and
    read list of todos
     """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath='files/todos.txt'):
    """Write the to do list to text file """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)

text = """
Created two custom functions:
get_todos(),
write_todos().
These are called in if/elsif statements.
"""

print(text)
