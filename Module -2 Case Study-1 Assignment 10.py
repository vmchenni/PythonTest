# 10.By using list comprehension,
# please write a program to
# print the list after removing the value 24 in [12,24,35,24,88,120,155]
listOriginal = [12, 24, 35, 24, 88, 120, 155]

# listOriginal.remove(24)
iValueToBeRemoved = 24

# Removing value from list
for x in listOriginal:
    if x == int(iValueToBeRemoved):
        listOriginal.remove(24)

# Print updated List
print("Updated list is ::-", listOriginal)
