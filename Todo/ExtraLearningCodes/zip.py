# Two lists of equal length
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

# Using zip to combine them
combined = zip(names, ages)

# Converting the zip object to a list of tuples
combined_list = list(combined)

print(combined_list)
# Output: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# Iterate over pairs of names and ages, and print each name with its corresponding age
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
# Output: Alice is 25 years old
# Bob is 30 years old
# Charlie is 35 years old
