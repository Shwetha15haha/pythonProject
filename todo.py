while True:
    # Prompt the user to enter an action, convert it to lowercase, and strip any extra spaces
    user_action = input("Type add, show, edit, complete or exit: ").lower().strip()

    # Check if the user action is "add"
    if user_action.startswith('add'):
        # Extract the todo from user input
        todo = user_action[4:]

        # Open the file in read mode and read all lines
        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        # Append the new todo item to the list, capitalizing the first letter of each word
        todos.append(todo.title() + '\n')

        # Open the file in write mode and write all todos back to the file
        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

    # Check if the user action is "show"
    elif user_action.startswith('show'):
        # Open the file in read mode and read all lines
        print('Your todos list:')
        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        # Enumerate through the todos and print each one with its index
        for index, todo in enumerate(todos, 1):
            todo = todo.strip('\n')  # Remove the newline character
            print(f"{index}. {todo}")

    # Check if the user action is "edit"
    elif user_action.startswith('edit'):
        try:
            # Extract the number of the todo item to edit
            number = int(user_action[5:]) - 1

            # Open the file in read mode and read all lines
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            # Display the existing todos
            print('Here are the existing todos:', todos)

            # Prompt the user to enter a new todo item
            new_todo = input("Enter a new todo: ")

            # Update the specified todo item
            todos[number] = new_todo.title() + '\n'

            # Display the updated todos
            print('Here are the updated todos:', todos)

            # Open the file in write mode and write all todos back to the file
            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

        except ValueError:
            print('Your command not valid')
            user_action = input("Type add, show, edit, complete or exit: ").lower().strip()

    # Check if the user action is "complete"
    elif user_action.startswith('complete'):
        # Extract the number of todo item to remove
        number = int(user_action[9:]) - 1

        # Open the file in read mode and read all lines
        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        # Remove the specified todo item from the list
        todo_to_remove = todos.pop(number).strip()

        # Open the file in write mode and write the remaining todos back to the file
        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

        # Print a message to the user about the removed todo
        print(f"Todo '{todo_to_remove}' is removed from the todo list")

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
