# 4. Write a program that accepts a sentence and calculate the number of letters and digits
print("Enter sentence:-")
numberOfDigit = 0
numberOfChar = 0
myString = str(input())
for k in myString:
     if k.isalpha():
         numberOfChar = numberOfChar+1
     elif k.isdigit():
         numberOfDigit=numberOfDigit+1
     else:
         pass
print("Number of Char:-", numberOfChar)
print("Number of digits:-", numberOfDigit)

