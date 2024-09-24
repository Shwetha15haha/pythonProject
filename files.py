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
