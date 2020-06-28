# 2. Write a code which accepts a sequence of words as input and prints the words in a sequence after sorting them alphabetically
x = []
n = input("Enter Length:-")
i = 0
while i < int(n):
    k = input("Enter value:-")
    # append list
    x.append(k)
    i = i+1
x.sort()
print(x)


