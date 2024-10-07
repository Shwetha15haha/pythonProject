# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Initialize an empty list to store country names
countries = []

# Start an infinite loop to continuously prompt the user for input
while True:
    # Prompt the user to enter a country name
    country = input("Enter the country: ")
    # Add the entered country name to the list 'countries'
    countries.append(country)
    # Print the updated list of countries
    print(countries)
#i/o
# Enter the country: india
# ['india']
# Enter the country: usa
# ['india', 'usa']
# Enter the country: australia
# ['india', 'usa', 'australia']
# Enter the country: