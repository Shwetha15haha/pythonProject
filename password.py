# Prompt the user to enter the password and keep asking
# until the correct password "pass123" is entered
password = input("Enter the password: ")

while password != "pass123":
    password = input("Enter the password: ")
print("Password is correct")

# input :
# Enter the password: 123
# Enter the password: pss
# Enter the password: pass123
# output :
# Password is correct