# 11.By using list comprehension, please write a program to print the
# list after removing the 0th,4th,5th numbers in
# [12,24,35,70,88,120,155].
listOriginal = [12, 24, 35, 70, 88, 120, 155]

listUpdated = []
iIndex = 0
for x in listOriginal:
    if iIndex == 0:
        pass
    elif iIndex == 3:
        pass
    elif iIndex == 4:
        pass
    else:
        listUpdated.insert(iIndex, x)
    iIndex = iIndex + 1

print("Updated List ", listUpdated)
