# Creating a custom function to get todos

FILEPATH = 'files/todos.txt'
def get_todos(filepath=FILEPATH):
    """Open the text file and
    read list of todos
     """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write the to do list to text file """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


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
