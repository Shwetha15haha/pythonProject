user_age = int(input("What is your age?\n"))
parent_permission = input("Do you have your parents' permission? (yes/no)\n").lower().strip()

if user_age > 18:
    print("You are allowed to drink.")
elif user_age < 18 and parent_permission == 'yes':
    print("You can drink this time.")
elif user_age < 18 and parent_permission == 'no':
    print("Not allowed to drink.")
elif user_age == 18 and parent_permission == 'yes':
    print("You are allowed to drink, but be cautious.")
elif user_age == 18 and parent_permission == 'no':
    print("You are allowed to drink, but consider your parents' advice.")
else:
    print("Unknown Age or Permission.")
# 1.
# What is your age?
# 13
# Do you have your parents' permission? (yes/no)
# yes
# You can drink this time.

# 2.
# What is your age?
# 24
# Do you have your parents' permission? (yes/no)
# no
# You are allowed to drink.

# 3.
# What is your age?
# 18
# Do you have your parents' permission? (yes/no)
# no
# You are allowed to drink, but consider your parents' advice.