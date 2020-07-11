# Write a program which can compute the factorial of a given numbers.
# Use recursion to find it. Hint:
# Suppose the following input is supplied to the program:8
# Then, the output should be:40320
iInputValue=int(input("Please enter a value:-"))
fact =1
while iInputValue > 1 :
    fact=fact * iInputValue
    iInputValue=iInputValue-1
print("Factorial Value is :-", fact)