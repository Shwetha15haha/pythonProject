while True:
    # Prompt the user to enter an action and convert it to lowercase and strip any extra spaces
    user_action = input("Type add, show, edit, exit or complete: ").lower().strip()

    # Match the user action to the corresponding case
    match user_action:
        case "add":
            # Prompt the user to enter a new todo item
            todo = input("Enter a todo: ") + "\n"

            # Open the file in read mode and read all lines
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            # Append the new todo item to the list, capitalizing the first letter of each word
            todos.append(todo.title())

            # Open the file in write mode and write all todos back to the file
            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

        case "show":
            # Open the file in read mode and read all lines
            print('Your todos list:')
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            # Enumerate through the todos and print each one with its index
            for index, todo in enumerate(todos, 1):
                todo = todo.strip('\n')  # Remove the newline character
                print(f"{index}. {todo}")

        case "edit":
            # Prompt the user to enter the number of the todo item to edit
            number = int(input("Enter the number of todo to edit: ")) - 1

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

        case "complete":
            # Prompt the user to enter the number of the todo item to complete
            number = int(input("Enter the number of todo to complete: ")) - 1

            # Open the file in read mode and read all lines
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()
            todo_to_remove = todos[number].strip()
            # Remove the specified todo item from the list
            todos.pop(number)

            # Open the file in write mode and write the remaining todos back to the file
            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)
            # Printing message to user about removed todo
            message = f"Todo {todo_to_remove} is removed from todo list"
            print(message)

        case "exit":
            # Exit the loop
            break

        case _:
            # Handle unknown commands
            print("Unknown command. Please type add, show, edit, complete, or exit.")

print("Bye!")

# i/o :
# Type add, show, edit, exit or complete: add
# Enter a todo: Eat chocolate
# Type add, show, edit, exit or complete: show
# Your todos list:
# 1. Eat Healthy
# 2. Sleep
# 3. Code
# 4. Debug
# 5. Chill , Just Relax
# 6. Eat Chocolate
# Type add, show, edit, exit or complete: edit
# Enter the number of todo to edit: 5
# Here are the existing todos: ['Eat Healthy\n', 'Sleep\n', 'Code\n', 'Debug\n', 'Chill , Just Relax\n', 'Eat Chocolate\n']
# Enter a new todo: chill!just relax buddy
# Here are the updated todos: ['Eat Healthy\n', 'Sleep\n', 'Code\n', 'Debug\n', 'Chill!Just Relax Buddy\n', 'Eat Chocolate\n']
# Type add, show, edit, exit or complete: show
# Your todos list:
# 1. Eat Healthy
# 2. Sleep
# 3. Code
# 4. Debug
# 5. Chill!Just Relax Buddy
# 6. Eat Chocolate
# Type add, show, edit, exit or complete: complete
# Enter the number of todo to complete: 1
# Todo Eat Healthy is removed from todo list
# Type add, show, edit, exit or complete: show
# Your todos list:
# 1. Sleep
# 2. Code
# 3. Debug
# 4. Chill!Just Relax Buddy
# 5. Eat Chocolate
# Type add, show, edit, exit or complete: exit
# Bye!



# The match statement in Python is a control flow construct introduced in Python 3.10.
# It allows for pattern matching, which is similar to a switch-case statement in other languages but more powerful.
# In your example, the match statement is used to compare the value of user_action against different cases.
# Depending on the value, a corresponding block of code is executed.

# match variable:
#     case "value1":
#         # do something
#     case "value2":
#         # do something else
#     case _:
#         # default case if no match
