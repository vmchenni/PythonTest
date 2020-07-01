# 12.By using list comprehension, please write a program to print the list after removing delete
# numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].
listOriginal = [12, 24, 35, 70, 88, 120, 155]
listUpdated = []
iIndex = 0;
for i in listOriginal:
    print()
    if i % 5 == 0:
        pass
    elif i % 7 == 0:
        pass
    else:
        listUpdated.insert(iIndex, i)
        iIndex = iIndex + 1
print("Updated list is :-", listUpdated)
