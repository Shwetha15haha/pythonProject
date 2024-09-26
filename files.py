# Open the file in write mode
with open('example.txt', 'w') as file:
    # Write some content to the file
    file.write('Hello, world!')
# Open the file in append mode
with open('example.txt', 'a') as file:
    # Append some content to the file
    file.write('\nAppended text.')
# Open the file in read mode
with open('example.txt', 'r') as file:
    # Read the entire content of the file
    content = file.read()
    print(content)
# Open the file in read mode
with open('example.txt', 'r') as file:
    # Read each line in the file
    for line in file:
        print(line.strip())  # strip() removes the newline character
member = input("Add a new member: ")

file = open("members.txt", 'r')
existing_members = file.readlines()
file.close()

existing_members.append("\n"+ member)

file = open("members.txt", 'w')
existing_members = file.writelines(existing_members)
file.close()