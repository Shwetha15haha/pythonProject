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
file = open("files/whatever.txt", 'w')
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

# 15.
# # Transforming strings in filenames list using list comprehension
filenames = ['1.doc', '2.report', '3.presentation']
filenames = [filename.replace('.', '-') + '.txt' for filename in filenames]
print(filenames)
# output : ['1-doc.txt', '2-report.txt', '3-presentation.txt']

# 16.
# Handing error
try:
    width = float(input('Enter the width of rectangle: '))
    length = float(input('Enter the length of rectangle: '))
    if width == length:
        exit('That looks like a square')
    area = length * width
    print('Area:', area)

except ValueError:
    print('Please enter a number')


# Enter the width of rectangle: 2
# Enter the length of rectangle: 3
# Area: 6.0

# Enter the width of rectangle: two
# Please enter a number

# Enter the width of rectangle: 5
# Enter the length of rectangle: 5
# That looks like a square

# 17.
def get_average():
    # Open the file 'data.txt' in read mode
    with open('files/data.txt', 'r') as file:
        # Read all lines from the file
        data = file.readlines()

        # Skip the first line (assuming it's a header) and convert the rest to floats
        data_values = data[1:]
        data_values = [float(i) for i in data_values]

        # Calculate the average of the data values
        average_local = sum(data_values) / len(data_values)

    # Return the calculated average
    return average_local


# Call the function and store the result in 'average'
average = get_average()

# Print the average value
print(average)


# input :
# temperatures
# 5
# 32
# 38
# 23
# 24
# output :
# 24.4

# 18.

# Define a function named get_max
def get_max():
    # Create a list of grades
    grades = [9.6, 9.2, 9.7]

    # Find the maximum value in the grades list using the max() function
    maximum = max(grades)

    # Return the maximum value
    return maximum


# Call the get_max() function and print the result
print(get_max())

# output: 9.7


# 19.
# Prompt the user to enter a value for feet and inches
feet_inches = input('Enter feet and inches: ')


# Define a function to convert feet and inches to meters
def parse(feet_inches):
    # Split the input string into two parts: feet and inches
    parts = feet_inches.split(".")
    # Convert the feet part to a float
    feet = float(parts[0])
    # Convert the inches part to a float
    inches = float(parts[1])
    # Return feet and inches
    return {'feet': feet, 'inches': inches}


def convert(feet, inches):
    # Calculate the total meters by converting feet to meters and inches to meters
    meters = feet * 0.3048 + inches * 0.0254
    # Return the result in meters
    return meters


# Call the convert function with the user input and store the result
parsed = parse(feet_inches)

result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result}")

# Check if the result is less than 1 meter
if result < 1:
    # If the result is less than 1 meter, print that the kid is too small
    print('Kid is too small.')
else:
    # If the result is 1 meter or more, print that the kid can use the slide
    print('Kid can use the slide')


# Enter feet and inches: 5.10
# 5.0 feet and 10.0 is equal to 1.778
# Kid can use the slide


# 20.

def water_state(temperature):
    if temperature <= 0:
        return 'Solid'
    elif temperature < 100:
        return 'Liquid'
    else:
        return 'Gas'


print(water_state(0))
# Output : Solid


# 21.
import json  # Import the json module to work with JSON data

# Open the JSON file in read mode
with open('questions.json', 'r') as file:
    content = file.read()  # Read the entire content of the file into a string

# Parse the JSON string into a Python object (list of dictionaries)
data = json.loads(content)

print(data)  # Print the data to verify the content

# Iterate over each question in the data
for question in data:
    # Print the question text
    print(question["question_text"])
    # Enumerate through the options and print each option with its corresponding number
    for index, option in enumerate(question["options"]):
        print(f"{index + 1}.{option}")
    # Prompt the user to enter their answer (convert to integer)
    user_choice = int(input('Enter your answer: '))
    # Store the user's choice in the question dictionary
    question["user_choice"] = user_choice

# initialize the score variable to 0 for calculating the final score
score = 0

# Iterate over each question in the data to check the user's answers
for index, question in enumerate(data):
    # Compare the user's choice with the correct answer
    if question["user_choice"] == question["correct_answer"]:
        score += 1  # Increment the score if the answer is correct
        result = 'Correct Answer'
    else:
        result = 'Wrong Answer'
    # Prepare the result message with question number, result, user's answer, and correct answer
    message = f"{index + 1}:{result}.Your answer:{question['user_choice']}," \
              f"Correct answer: {question['correct_answer']}"
    print(message)  # Print the result message for each question

# Print the final score along with the total number of questions
print(score, '/', len(data))

# Example questions JSON structure:
# [{'question_text': 'What are Dolphins?', 'options': ['Amphibians', 'Fish', 'Mammals', 'Birds'], 'correct_answer': 3},
# {'question_text': "What occupies most of the earth's surface?", 'options': ['Lands', 'Water'], 'correct_answer': 2}]

# [{'question_text': 'What are Dolphins?', 'options': ['Amphibians', 'Fish', 'Mammals', 'Birds'], 'correct_answer': 3}, {'question_text': "What occupies most of the earth's surface?", 'options': ['Lands', 'Water'], 'correct_answer': 2}]
# What are Dolphins?
# 1.Amphibians
# 2.Fish
# 3.Mammals
# 4.Birds
# Enter your answer: 1
# What occupies most of the earth's surface?
# 1.Lands
# 2.Water
# Enter your answer: 2
# 1:Wrong Answer.Your answer:1,Correct answer: 3
# 2:Correct A
