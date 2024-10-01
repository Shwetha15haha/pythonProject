# Prompt the user to enter the password and keep asking
# until the correct password "pass123" is entered
password = input("Enter the password: ")

# while password != "pass123":
#     password = input("Enter the password: ")
# print("Password is correct")

# input :
# Enter the password: 123
# Enter the password: pss
# Enter the password: pass123
# output :
# Password is correct

result =[]
if len(password) >= 8:
    result.append(True)
else:
    result.append(False)

digit = False
for i in password:
    if i.isdigit():
        digit = True
result.append(digit)

upper = False
for i in password:
    if i.isupper():
        upper = True
result.append(upper)

print(result)

if all(result):
    print('Strong Password')
else:
    print('Weak Password')
