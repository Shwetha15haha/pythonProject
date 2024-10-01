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

# Initialize the result list
result = []

# Check if the password length is at least 8 characters
if len(password) >= 8:
    result.append(True)
else:
    result.append(False)

# Check if the password contains at least one digit
digit = any(char.isdigit() for char in password)
result.append(digit)

# Check if the password contains at least one uppercase letter
upper = any(char.isupper() for char in password)
result.append(upper)

# Print the result list
print(result)

# Check if all conditions are met for a strong password
if all(result):
    print('Strong Password')
else:
    print('Weak Password')

# 1.
# Enter the password: jkqghwdiuk15eo8984
# [True, True, False]
# Weak Password

# 2.
# Enter the password: Skhkdele566
# [True, True, True]
# Strong Password

