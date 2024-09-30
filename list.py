# Initialize the list with elements 'a', 'b', and 'c'
mylist = ['a', 'b', 'c']

# Print the entire list
print(mylist)

# Print the first element of the list
print(mylist[0])

# Print the index of the element 'a' in the list
print(mylist.index('a'))

# Set the element at index 1 to 'e' using the __setitem__ method
mylist.__setitem__(1, 'e')

# Print the updated list
print(mylist)

# Print the element at index 1 using the __getitem__ method
print(mylist.__getitem__(1))

# output :
# ['a', 'b', 'c']
# a
# 0
# ['a', 'e', 'c']
# e


# Create a new list 'upper_case' with each word from 'mylist' converted to uppercase
upper_case = [word.upper() for word in mylist]

# Print the list of uppercase words
print(upper_case)
# output : ['A', 'E', 'C']

# list comprehension method
names = ["john smith", "jay santi", "eva kuki"]
names = [name.title() for name in names]
print(names)
# output : ['John Smith', 'Jay Santi', 'Eva Kuki']