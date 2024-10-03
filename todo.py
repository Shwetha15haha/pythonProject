# Creating a custom function to get todos
def get_todos(filepath):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(filepath, todos_arg):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)

while True:
    # Prompt the user to enter an action, convert it to lowercase, and strip any extra spaces
    user_action = input("Type add, show, edit, complete or exit: ").lower().strip()

    # Check if the user action is "add"
    if user_action.startswith('add'):
        # Extract the todo from user input
        todo = user_action[4:]

        # Open the file in read mode and read all lines
        todos = get_todos('files/todos.txt')

        # Append the new todo item to the list, capitalizing the first letter of each word
        todos.append(todo.title() + '\n')

        # Open the file in write mode and write all todos back to the file
        write_todos('files/todos.txt', todos)

    # Check if the user action is "show"
    elif user_action.startswith('show'):
        # Open the file in read mode and read all lines
        print('Your todos list:')
        todos = get_todos('files/todos.txt')

        # Enumerate through the todos and print each one with its index
        for index, todo in enumerate(todos, 1):
            todo = todo.strip('\n')  # Remove the newline character
            print(f"{index}. {todo}")

    # Check if the user action is "edit"
    elif user_action.startswith('edit'):
        # Your code that might raise an ValueError
        try:
            # Extract the number of the todo item to edit
            number = int(user_action[5:]) - 1

            # Open the file in read mode and read all lines
            todos = get_todos('files/todos.txt')

            # Display the existing todos
            print('Here are the existing todos:', todos)

            # Prompt the user to enter a new todo item
            new_todo = input("Enter a new todo: ")

            # Update the specified todo item
            todos[number] = new_todo.title() + '\n'

            # Display the updated todos
            print('Here are the updated todos:', todos)

            # Open the file in write mode and write all todos back to the file
            write_todos('files/todos.txt', todos)

        # This block will execute if a ValueError occurs
        except ValueError:
            print('Your command not valid')

            # Continue to the next iteration of the loop
            continue # Ignore the code below and start from begining with user input

    # Check if the user action is "complete"
    elif user_action.startswith('complete'):
        # Your code that might raise an IndexError
        try:
            # Extract the number of todo item to remove
            number = int(user_action[9:]) - 1

            # Open the file in read mode and read all lines
            todos = get_todos('files/todos.txt')

            # Remove the specified todo item from the list
            todo_to_remove = todos.pop(number).strip()

            # Open the file in write mode and write the remaining todos back to the file
            write_todos('files/todos.txt', todos)

            # Print a message to the user about the removed todo
            print(f"Todo '{todo_to_remove}' is removed from the todo list")

        # This block will execute if an IndexError occurs
        except IndexError:
            print('There is no todo with that number')

            # Continue to the next iteration of the loop
            continue

    # Check if the user action is "exit"
    elif user_action.startswith('exit'):
        # Exit the loop
        break

    # Handle unknown commands
    else:
        print('Unknown command. Please type add, show, edit, complete, or exit.')

print("Bye!")

# i/o :
# Type add, show, edit, complete or exit: add
# Type add, show, edit, complete or exit: show
# Your todos list:
# 1. Sleep On Time
# 2. Code
# 3. Debug
# 4. Chill!Just Relax Buddy
# 5. Eat Chocolate
# 6. Tea
# 7. Read
# 8. Buy Groceries
# 9. Holiday Plan
# 10.
# Type add, show, edit, complete or exit: edit 10
# Here are the existing todos: ['Sleep On Time\n', 'Code\n', 'Debug\n', 'Chill!Just Relax Buddy\n', 'Eat Chocolate\n', 'Tea\n', 'Read\n', 'Buy Groceries\n', 'Holiday Plan\n', '\n']
# Enter a new todo: Watch movie
# Here are the updated todos: ['Sleep On Time\n', 'Code\n', 'Debug\n', 'Chill!Just Relax Buddy\n', 'Eat Chocolate\n', 'Tea\n', 'Read\n', 'Buy Groceries\n', 'Holiday Plan\n', 'Watch Movie\n']
# Type add, show, edit, complete or exit: show
# Your todos list:
# 1. Sleep On Time
# 2. Code
# 3. Debug
# 4. Chill!Just Relax Buddy
# 5. Eat Chocolate
# 6. Tea
# 7. Read
# 8. Buy Groceries
# 9. Holiday Plan
# 10. Watch Movie
# Type add, show, edit, complete or exit: complete 6
# Todo 'Tea' is removed from the todo list
# Type add, show, edit, complete or exit: show
# Your todos list:
# 1. Sleep On Time
# 2. Code
# 3. Debug
# 4. Chill!Just Relax Buddy
# 5. Eat Chocolate
# 6. Read
# 7. Buy Groceries
# 8. Holiday Plan
# 9. Watch Movie
# Type add, show, edit, complete or exit: exit
# Bye!
