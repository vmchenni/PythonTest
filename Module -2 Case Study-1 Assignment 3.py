# 3. A website requires a user to input username and password to register.
# Write a program to check the validity of password given by user.
# Following are the criteria for checking password:
#     1. At least 1 letter between [a-z]
#     2. At least 1 number between [0-9]
#     3. At least 1 letter between [A-Z]
#     4. At least 1 character from [$#@]
#     5. Minimum length of transaction password: 6
#     6. Maximum length of transaction password: 12

import re

# lowerchar=('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r' , 's', 't', 'u' , 'v', 'w', 'y' , 'z')
# print(lowerchar)
# print("Enter User Name:-")
# username = str(input())

print("Enter Password:-")
password = str(input())
if len(password) < 6:
    print("username should be more than 6 character")
elif len(password) > 12:
    print("user name should be less than 12 character")
elif not re.search("[a-z]", password):
    print("At least 1 letter between [a-z]")
elif not re.search("[0-9]", password):
    print("At least 1 number between [0-9]")
elif not re.search("[A-Z]", password):
    print("At least 1 letter between [A-Z]")
elif not re.search("[$#@]", password):
    print("At least 1 character from [$#@]")
else:
    print("Your password is ", password)
