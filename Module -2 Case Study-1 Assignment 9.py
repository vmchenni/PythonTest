# 39.With a given list [12,24,35,24,88,120,155,88,120,155],
# write a program to print this list after removing all duplicate values
# with original order reserved

listOriginal = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]

set1 = set()
# Creating set to remove duplicates
for x in listOriginal:
    set1.add(x)
#     Set with unique values
print("Set with unique values", set1)

# Adding set elements to list
list2 = []
iIndex = 0
for x in set1:
    list2.insert(iIndex, x)
    iIndex = iIndex + 1

print("Reversed list is :- ", list2[::-1])
