date = input("Enter today's date: ")
mood = input("How do you rate your today's mood from 1 to 10? ")
thoughts = input("Let your thoughts flow:\n")

with open(f"Journal/{date}.txt", 'w') as file:
    file.write(f"Date: {date}\n")
    file.write(f"Mood: {mood}\n\n")
    file.write("Thoughts:\n")
    file.write(thoughts.capitalize() + '\n')

with open(f"Journal/{date}.txt", 'r') as file:
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

