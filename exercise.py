# 1.
# Prompt the user to enter their name
name = input("Enter your name: ")

# Continuously print the capitalized name (infinite loop)
while True:
    print(name.capitalize())

# Continuously prompt the user to enter their name and print the capitalized name
while True:
    name = input("Enter your name: ")
    print(name.capitalize())

# 2.
# Initialize a list of member names
members = ["john smith", "sen play", "dora nacelle"]

# Iterate over each member and print their name in title case
for member in members:
    print(member.title())

# 3.
# Initialize the variable 'country' with the value "India"
country = "India"

# Use a match-case statement to print a greeting based on the country
match country:
    case "USA":
        print("Hello")
    case "India":
        print("Namaste")
    case "Germany":
        print("Hallo")

# 4.
# Initialize a list of colors (as numbers)
colors = [11, 34, 98, 43, 45, 54, 54]

# Iterate over each color and print it
for color in colors:
    print(color)

# 5.
# Prompt the user to enter an amount in dollars and convert the input to a float
dollars = float(input("Enter the amount in dollars :"))

# Define the conversion rate from dollars to euros
rate = 2

# Calculate the amount in euros
euros = dollars * rate

# Print the amount in euros
print("The amount in euros:", euros)

# 6.
# Initialize a list of rankings
ranking = ['John', 'Sen', 'Lisa']

# Iterate over each ranking and prompt the user to enter a rank number, then print the corresponding name
for r in ranking:
    rank = ranking.index(r)
    rank = int(input("Enter rank number:"))
    rank = rank - 1
    print(ranking[rank])
    break

# Prompt the user to enter a rank number and print the corresponding name
rank = int(input("Enter a rank number:")) - 1
name = ranking[rank]
print(name)

# Prompt the user to enter a name and print the corresponding rank number
name = input("Enter a name: ")
rank = ranking.index(name) + 1
print(rank)

# 7.
# Initialize a list of filenames
filenames = ['document', 'report', 'presentation']

# Iterate over each filename with its index and print it in a formatted string
for index, filename in enumerate(filenames):
    print(f"{index}-{filename.capitalize()}.txt")

# 8.
# Initialize a list of IP addresses
ips = ['100.122.133.105', '100.122.133.111']

# Prompt the user to enter the index of the IP they want
index = int(input("Enter the index of the IP you want: "))

# Print the chosen IP address
print("You chose", ips[index])

# 9.
# Initialize a string 'a'
a = "abcd"

# Open a file 'whatever.txt' in write mode and write the string 'a' to the file
file = open("whatever.txt", 'w')
file.writelines(a)

# 10.
# Open the file 'files/todos.txt' in read mode
file = open('files/todos.txt', 'r')

# Read the content of the file and strip any leading/trailing whitespace
content = file.read().strip()

# Print the content
print(content)

# 11.
# Initialize a list of contents and filenames
contents = ["This is file related code",
            "File method codes are reported",
            "File related codes are presented",
            "Done"]

filenames = ["doc.txt", "report.txt", "present.txt"]

# Iterate over each content and filename pair, open the file in write mode, and write the content to the file
for content, filename in zip(contents, filenames):
    file = open(f"{filename}", 'w')
    file.write(content)

# 13.
# Initialize a list of filenames
filenames = ['a.txt', 'b.txt', 'c.txt']

# Iterate over each filename, open the file in read mode, read the content, and print it
for filename in filenames:
    file = open(filename, 'r')
    content = file.read()
    print(content)

# 14.
# Initialize a list of filenames
filenames = ['doc.txt', 'report.txt', 'presentation.txt']

# Iterate over each filename, open the file in write mode, write "Hello" to the file, and close the file
for filename in filenames:
    file = open(filename, 'w')
    file.write("Hello")
    file.close()
