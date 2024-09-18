1.
name = input("Enter your name: ")

while True:
    print(name.capitalize())

while True:
    name = input("Enter your name: ")
    print(name.capitalize())

2.
members = ["john smith", "sen plakay", "dora ngacely"]

for member in members:
    print(member.title())

3.
country = "India"
match country:
    case "USA":
        print("Hello")
    case "India":
        print("Namaste")
    case "Germany":
        print("Hallo")

4.
colors = [11, 34, 98, 43, 45, 54, 54]

for color in colors:
    print(color)