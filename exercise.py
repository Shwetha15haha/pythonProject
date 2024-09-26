# 1.
# name = input("Enter your name: ")
#
# while True:
#     print(name.capitalize())
#
# while True:
#     name = input("Enter your name: ")
#     print(name.capitalize())
#
# 2.
# members = ["john smith", "sen play", "dora nacelle"]
#
# for member in members:
#     print(member.title())
#
# 3.
# country = "India"
# match country:
#     case "USA":
#         print("Hello")
#     case "India":
#         print("Namaste")
#     case "Germany":
#         print("Hallo")
#
# 4.
# colors = [11, 34, 98, 43, 45, 54, 54]
#
# for color in colors:
#     print(color)
#
# 5.
# dollars = float(input("Enter the amount in dollars :"))
#
# rate = 2
#
# euros = dollars * rate
#
# print("The amount in euros:", euros)
#
# 6.
# ranking = ['John', 'Sen', 'Lisa']
#
# for r in ranking:
#     rank = ranking.index(r)
#     rank = int(input("Enter rank number:"))
#     rank = rank -1
#     print(ranking[rank])
#     break
#
# rank = int(input("Enter a rank number:"))-1
# name = ranking[rank]
# print(name)
#
# name = input("Enter a name: ")
#
# rank = ranking.index(name)+1
#
# print(rank)
#
# 7.
# filenames = ['document', 'report', 'presentation']
#
# for index, filename in enumerate(filenames):
#     print(f"{index}-{filename.capitalize()}.txt")
#
# 8.
# ips = ['100.122.133.105', '100.122.133.111']
#
# index = int(input("Enter the index of the IP you want: "))
#
# print("You chose",ips[index])
#
# 9.
# a = "abcd"
# file = open("whatever.txt", 'w')
# file.writelines(a)
#
# 10
# file = open('files/todos.txt', 'r')
# content = file.read().strip()
# print(content)
11.
contents = ["This is file related code",
            "File method codes are reported",
            "File related codes are presented",
            "Done"]

filenames = ["doc.txt", "report.txt", "present.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"{filename}",'w')
    file.write(content)
13.
filenames = ['a.txt', 'b.txt', 'c.txt']

for filename in filenames:
    file = open(filename, 'r')
    content = file.read()
    print(content)
14.
filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for filename in filenames:
    file = open(filename, 'w')
    file.write("Hello")
    file.close()