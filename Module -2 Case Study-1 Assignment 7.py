#7.Please write a program which count and print the numbers of each character in a string input by console
# .Example: If the following string is given as input to the program:abcdefgabcThen,
# the output of the program should be:
# a,2
# c,2
# b,2
# e,1
# d,1
# g,1
# f,1
import re
print("Enter a input string:-")
sInputString=str(input())
for x in range(ord('a'), ord('z')+1):
    count = len(re.findall(chr(x), sInputString))
    if count >= 1:
        print(chr(x), count)
    # print(chr(x))
