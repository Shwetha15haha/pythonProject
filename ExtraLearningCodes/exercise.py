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
file = open("../files/whatever.txt", 'w')
file.writelines(a)

# 10.
# Open the file 'files/todos.txt' in read mode
file = open('../TododAPP/todos.txt', 'r')

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
    with open('../files/data.txt', 'r') as file:
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


# 22.
import random  # Import the random module to generate random numbers

while True:
    # Prompt the user to enter the lower bound of the range
    lower_value = int(input('Enter lower bound: '))
    # Prompt the user to enter the upper bound of the range
    upper_value = int(input('Enter upper bound: '))
    # Generate a random integer within the specified range
    random_whole_number = random.randint(lower_value, upper_value)
    # Print the randomly generated number
    print(f"{random_whole_number} is the random number.")

# Get two numbers from the user and covert them to integers
lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))

# Pick a random int using randrange()
rand = random.randrange(lower_bound, upper_bound + 1)
# We add 1 to upper_bound because randrange does not include the upper_bound number.

print(rand)

# randint(a, b):
# Returns a random integer N such that a <= N <= b.
#
# Both endpoints a and b are inclusive.
#
# Simpler and direct for generating a single random integer within a closed range.
#
# randrange(start, stop[, step]):
# Returns a randomly selected element from the range created by range(start, stop, step).
#
# start is inclusive, but stop is exclusive.
#
# More flexible as it allows you to specify a step parameter, which is the increment (default is 1).


# 23.

"""
This script creates a simple GUI application for compressing files using FreeSimpleGUI.

FreeSimpleGUI is a Python package that enables developers to easily create graphical user interfaces.
The application allows the user to select files for compression, choose a destination folder, and
then compresses the files into a ZIP archive.
"""

import FreeSimpleGUI as sg  # Import FreeSimpleGUI for creating the graphical interface
from zip_file_create import make_archive  # Import the make_archive function for creating the ZIP file

# Create a label for the first section to ask the user to select files for compression
label1 = sg.Text("Select file to compress:")

# Input box where the user can input file paths (this will automatically fill when they select files using the button)
input_box_1 = sg.Input()

# Button that opens a file browser for selecting multiple files to compress
choose_button_1 = sg.FilesBrowse("Choose", key='files')

# Create a label for the second section to ask the user to select the destination folder
label2 = sg.Text("Select destination folder:")

# Input box where the user can input the destination folder path (automatically filled when browsing for folders)
input_box_2 = sg.Input()

# Button that opens a folder browser to select where to save the ZIP file
choose_button_2 = sg.FolderBrowse("Choose", key='folder')

# Create a button to trigger the compression process
compress_button = sg.Button("Compress")

# Text element to display output messages (e.g., "Compression completed")
output_label = sg.Text(key='output')

# Define the layout of the window with all the widgets arranged in rows
layout = [[label1, input_box_1, choose_button_1],
          [label2, input_box_2, choose_button_2],
          [compress_button, output_label]]

# Create the main application window with the title 'File Compressor'
window = sg.Window('File Compressor', layout=layout)

# Main event loop to handle user interactions
while True:
    # Read events (e.g., button presses) and the values entered in the input fields
    event, values = window.read()

    # If the window is closed, exit the loop
    if event == sg.WIN_CLOSED:
        break

    # If the "Compress" button is clicked, start the compression process
    if event == "Compress":
        # Retrieve the file paths entered or selected by the user (separated by semicolons)
        filepaths = values['files'].split(";")

        # Retrieve the destination folder selected by the user
        folder = values['folder']

        # Check if filepaths and folder are valid (non-empty)
        if filepaths and folder:
            # Call the make_archive function to compress the selected files into the chosen folder
            make_archive(filepaths, folder)

            # Update the output label to notify the user that compression is completed
            window["output"].update(value='Compression completed')
        else:
            # Update the output label to notify the user of an error
            window["output"].update(value='Please select files and a destination folder')

# Close the window when the interaction is complete
window.close()


# 24.

"""
This script creates a simple GUI application to convert feet and inches using FreeSimpleGUI.

FreeSimpleGUI is a Python package that enables developers to easily create graphical user interfaces.
"""

import FreeSimpleGUI as sg  # Import FreeSimpleGUI for creating the graphical interface

# Create a text label widget for entering feet
label1 = sg.Text("Enter Feet:")
# Create an input text box for feet value
input_box_1 = sg.Input()

# Create a text label widget for entering inches
label2 = sg.Text("Enter inches:")
# Create an input text box for inches value
input_box_2 = sg.Input()

# Create a button to initiate the conversion process
convert_button = sg.Button("Convert")

# Define the layout of the window with all widgets arranged in rows
window = sg.Window('Converter', layout=[[label1, input_box_1],
                                        [label2, input_box_2],
                                        [convert_button]])

# Display the window and wait for user interaction
window.read()

# Close the window when the interaction is complete
window.close()


# 25.
#
# import FreeSimpleGUI as sg
#
# label = sg.Text("What are dolphins?")
# option1 = sg.Radio("Amphibians", group_id="question1")
# option2 = sg.Radio("Fish", group_id="question1")
# option3 = sg.Radio("Mammals", group_id="question1")
# option4 = sg.Radio("Birds", group_id="question1")
#
# window = sg.Window("Quiz",
#                    layout=[[label],
#                            [option1,
#                             option2,
#                             option3,
#                             option4],
#                            ])
#
# window.read()
# window.close()
###############################################################################################
# import FreeSimpleGUI as sg
#
# label = sg.Text("What are dolphins?")
# option1 = sg.Radio("Amphibians", group_id="question1")
# option2 = sg.Radio("Fish", group_id="question1")
# option3 = sg.Radio("Mammals", group_id="question1")
# option4 = sg.Radio("Birds", group_id="question1")
#
# window = sg.Window("Quiz",
#                    layout=[[label],
#                            [option1],
#                            [option2],
#                            [option3],
#                            [option4],
#                            ])
#
# window.read()
# window.close()

#
# 26.

import FreeSimpleGUI as sg  # Import FreeSimpleGUI for creating the graphical interface

# Create a text label widget for entering feet
label1 = sg.Text("Enter Feet:")

# Create an input text box for feet value, with a tooltip for guidance
input_box_1 = sg.Input(tooltip='Enter feet', key='feet')

# Create a text label widget for entering inches
label2 = sg.Text("Enter Inches:")

# Create an input text box for inches value, with a tooltip for guidance
input_box_2 = sg.Input(tooltip='Enter inches', key='inch')

# Create a button to initiate the conversion process
convert_button = sg.Button("Convert")

# Text element to display output messages (conversion result or error)
output_label = sg.Text(key='output', size=(40, 1))

# Define the layout of the window with all widgets arranged in rows
layout = [[label1, input_box_1],
          [label2, input_box_2],
          [convert_button,
          output_label]]  # Add a new row for the output label

# Create the window with the given title and layout
window = sg.Window('Feet and Inches to Meters Converter', layout)

# Main event loop to handle user interactions
while True:
    # Read events (e.g., button presses) and the values entered in the input fields
    event, values = window.read()

    # If the user closes the window, break the loop and exit
    if event == sg.WIN_CLOSED:
        break
    # If the "Convert" button is pressed, attempt to perform the conversion
    elif event == 'Convert':
        try:
            # Read the values entered by the user and convert them to float
            feet = float(values['feet'])
            inch = float(values['inch'])

            # Convert feet and inches to meters
            convert_meter = ((feet * 12) + inch) * 0.0254
            # Format the result to two decimal places and update the output label
            convert_meter = f"= {convert_meter:.2f} meters"
            window["output"].update(value=convert_meter)
        except ValueError:
            # If input is invalid, display an error message and clear entered value
            window["output"].update(value='Invalid input! Please enter numeric values.')
            window["feet"].update(value='')
            window["inch"].update(value='')

# Close the window when the loop ends
window.close()


# ('Convert', {'feet': '3', 'inch': '4'})
# 3.0 feet.
# 4.0 inch.
# Conversion value: 1.016m.


# 27. Adding each country name in new file

countries = ["Albania", "Belgium", "Canada", "Denmark", "Ethiopia", "France"]
filenames = ['a.txt', 'b.txt', 'c.txt', 'd.txt', 'e.txt', 'f.txt']

for country, filename in zip(countries, filenames):
    with open(filename, 'w') as file:
        file.writelines(country)
