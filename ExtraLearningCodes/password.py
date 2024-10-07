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
result = {}

# Check if the password length is at least 8 characters
if len(password) >= 8:
    result['length'] = True
else:
    result['length'] = False

# Check if the password contains at least one digit
digit = any(char.isdigit() for char in password)
result['digits'] = digit

# Check if the password contains at least one uppercase letter
upper = any(char.isupper() for char in password)
result['upper_case'] = upper

# Print the result list
print(result)
print(result.values())

# Check if all conditions are met for a strong password
if all(result.values()):
    print('Strong Password')
else:
    print('Weak Password')

# 1.
# Enter the password: jkqghwdiuk15eo8984
# {'length': True, 'digits': True, 'upper_case': False}
# dict_values([True, True, False])
# Weak Password

# 2.
# Enter the password: Skhkdele566
# {'length': True, 'digits': True, 'upper_case': True}
# dict_values([True, True, True])
# Strong Password

