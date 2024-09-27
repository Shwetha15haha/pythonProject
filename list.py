mylist = ['a', 'b', 'c']

print(mylist)

print(mylist[0])

print(mylist.index('a'))

mylist.__setitem__(1, 'e')

print(mylist)

print(mylist.__getitem__(1))

# output :
# ['a', 'b', 'c']
# a
# 0
# ['a', 'e', 'c']
# e


upper_case = [word.upper() for word in mylist]
print(upper_case)
# ['A', 'E', 'C']