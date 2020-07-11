# Write a program that accepts a sequence of whitespace separated words as input and
# prints   the   words   after   removing   all   duplicate   words   and   sorting
# them alphanumerically.
myinputline=input("Enter words seperated by white space")
mylist=myinputline.split(" ")
dictonary={}
myset=set(dictonary)
myset.update(mylist)
print(sorted(myset))