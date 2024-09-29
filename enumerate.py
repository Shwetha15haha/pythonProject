# Iterate over each character in the string "Shwetha" with its index, and print the index (starting from 1) followed by the character
for i, j in enumerate("Shwetha"):
    print(f"{i+1}.{j}")
# output
# 1.S
# 2.h
# 3.w
# 4.e
# 5.t
# 6.h
# 7.a
# -----------------------------------------------------------------------
# Iterate over each sublist in the list of lists with its index, and print the index (starting from 1) followed by the sublist
for i, j in enumerate([["a", "b"], ["c", "d"]]):
    print(f"{i+1}.{j}")
# output :
# 1.['a', 'b']
# 2.['c', 'd']
# -----------------------------------------------------------------------
# Initialize a list of names in the waiting list
waiting_list = ["john", "ben", "sen"]

# Sort the waiting list alphabetically
waiting_list.sort()

# Iterate over each name in the sorted waiting list with its index, and print the index (starting from 1) followed by the capitalized name
for i, j in enumerate(waiting_list):
    print(f"{i+1}.{j.capitalize()}")
# output: 1.Ben
# 2.John
# 3.Sen
# -----------------------------------------------------------------------
# Initialize a list of tuples, where each tuple contains three names
buttons = [('John', 'Sen', 'Moro'), ('Lin', 'Ajay', 'Filip')]

# Iterate over each tuple in the list, unpacking the three names into 'first', 'second', and 'third'
for first, second, third in buttons:
    # Print the three names
    print(first, second, third)
# output :
# John Sen Moro
# Lin Ajay Filip
