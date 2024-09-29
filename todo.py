while True:
    user_action = input("Type add, show, edit, exit or complete: ").lower().strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ")+ "\n"
            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo.title())

            file = open('files/todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case "show":
            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            # new_todo_list = []
            # for item in todos:
            #     new_item = item.strip('\n')
            #     new_todo_list.append(new_item)
            new_todo_list = [item.strip('\n') for item in todos]

            for index, todo in enumerate(new_todo_list, 1):
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
