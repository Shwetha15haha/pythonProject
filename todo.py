todos = []

while True:
    user_action = input("Type add, show, edit, exit or complete: ").lower().strip()

    match user_action:
        case "add":
            todo = input("Enter a code: ")
            todos.append(todo.title())
        case "show":
            print("Your to do lists:")
            for index, todo in enumerate(todos, 1):
                print(f"{index}. {todo}")
        case "edit":
            number = int(input("Enter the number of todo to edit: "))-1
            new_todo = input("Enter a new to do: ")
            todos[number] = new_todo.title()
        case "complete":
            number = int(input("Enter the number of todo to complete: "))-1
            todos.pop(number)
        case "exit":
            break
        case _:
            print("Unknown command. Please type add, show, or exit.")
print("Bye!")

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
