todos = []

while True:
    user_action = input("Type add, show or exit: ").lower().strip()

    match user_action:
        case "add":
            todo = input("Enter a code: ")
            todos.append(todo.capitalize())
        case "show":
            for item in todos:
                print(item)
        case "exit":
            break
        case _:
            print("Unknown command. Please type add, show, or exit.")
print("Bye!")

# The match statement in Python is a control flow construct introduced in Python 3.10. It allows for pattern matching, which is similar to a switch-case statement in other languages but more powerful.
# In your example, the match statement is used to compare the value of user_action against different cases. Depending on the value, a corresponding block of code is executed.

# match variable:
#     case "value1":
#         # do something
#     case "value2":
#         # do something else
#     case _:
#         # default case if no match
