#5 Design a code which will find the given number is Palindrome number or not.
print("Enter a number:-")
strOriginal = str(input())
strUpdated = strOriginal [::-1]
if strUpdated == strOriginal:
    print("Number ",strOriginal," is Palindrom")
else:
    print("Number ", strOriginal, " is not a  Palindrom")
