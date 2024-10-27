# Open the file in write mode
with open('../files/example.txt', 'w') as file:
    # Write some content to the file
    file.write('Hello, world!')
# Open the file in append mode
with open('../files/example.txt', 'a') as file:
    # Append some content to the file
    file.write('\nAppended text.')
# Open the file in read mode
with open('../files/example.txt', 'r') as file:
    # Read the entire content of the file
    content = file.read()
    print(content)
# Open the file in read mode
with open('../files/example.txt', 'r') as file:
    # Read each line in the file
    for line in file:
        print(line.strip())  # strip() removes the newline character


# Prompt the user to add a new member
member = input("Add a new member: ")

# Open the file 'members.txt' in read mode
file = open("../files/members.txt", 'r')
# Read all existing members from the file into a list
existing_members = file.readlines()
# Close the file after reading
file.close()

# Append the new member to the list of existing members, adding a newline character before the new member
existing_members.append("\n" + member)

# Open the file 'members.txt' in write mode to update it
file = open("../files/members.txt", 'w')
# Write the updated list of members back to the file
file.writelines(existing_members)
# Close the file after writing
file.close()