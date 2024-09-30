# Prompt the user to enter today's date
date = input("Enter today's date: ")

# Prompt the user to rate their mood from 1 to 10
mood = input("How do you rate your today's mood from 1 to 10? ")

# Prompt the user to share their thoughts
thoughts = input("Let your thoughts flow:\n")

# Open a file in write mode with the name based on the date
with open(f"Journal/{date}.txt", 'w') as file:
    # Write the date to the file
    file.write(f"Date: {date}\n")
    # Write the mood rating to the file
    file.write(f"Mood: {mood}\n\n")
    # Write a header for the thoughts section
    file.write("Thoughts:\n")
    # Write the user's thoughts to the file, capitalizing the first letter
    file.write(thoughts.capitalize() + '\n')

# Open the file in read mode to display its contents
with open(f"Journal/{date}.txt", 'r') as file:
    # Print the contents of the file
    print(file.read())

# i/o :
# Enter today's date: 2024-09-30
# How do you rate your today's mood from 1 to 10? 7
# Let your thoughts flow:
# going well as planned.
# Date: 2024-09-30
# Mood: 7
#
# Thoughts:
# Going well as planned.

