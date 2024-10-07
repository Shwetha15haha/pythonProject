import csv  # Import the csv module for reading CSV files

# Open the CSV file in read mode and convert it to a list of rows
with open('../files/weather.csv', 'r') as file:
    data = list(csv.reader(file))
print(data)  # Print the data to check the content

# Example output:
# [['Station', 'Temperature'], ['Kuala Lumpur', '45'], ['New York', '20'], ['India', '30']]

city = input('Enter a city: ')  # Prompt the user to enter a city name

# Loop through each row in the CSV data
for row in data:
    # If the first element of the row matches the entered city
    if row[0] == city:
        print(row[1])  # Print the corresponding temperature

# Expected workflow:
# Enter a city: India
# Output: 30
