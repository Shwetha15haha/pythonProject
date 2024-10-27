# Creating a custom function to get todos

FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """Open the text file and
    read list of todos without newline characters
    """
    with open(filepath, 'r') as file_local:
        # Use strip() to remove newline characters and any leading/trailing whitespace
        todos_local = [line.strip() for line in file_local.readlines()]
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write the to-do list to the text file, ensuring each item is followed by a newline."""
    with open(filepath, 'w') as file_local:
        # Add a newline character after each to-do if it doesn't already have one
        file_local.writelines([todo + '\n' if not todo.endswith('\n') else todo for todo in todos_arg])



text = """
Created two custom functions:
get_todos(),
write_todos().
These are called in if/elsif statements.
"""

"""
if __name__ = '__main__':  
the main() function will only be executed if the script is run directly. 
If the script is imported as a module in another script, main() will not be executed.
"""

if __name__ == '__main__':
    print(text)
    print(get_todos())

