todos = []

while True:
    user_action = input("Type add, show or exit: ")

    match user_action:
        case "add":
            todo = input("Enter a code: ")
            todos.append(todo.capitalize())
        case "show":
            print(todos)
        case "exit":
            break
print("Bye!")