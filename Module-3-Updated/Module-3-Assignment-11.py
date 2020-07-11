# Write a program that accepts sequence of lines as input and
# prints the lines after making all characters in the sentence capitalized.
# Suppose the following inputis supplied to the program:
mylines = []
while True:
    line = input()
    if line:
        mylines.append(line.upper())
    else:
        break;

for l in mylines:
    print(l)