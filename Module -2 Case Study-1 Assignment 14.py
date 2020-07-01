# 14.Write  a  program  to  compute  1/2+2/3+3/4+...+n/n+1
# with  a  given  n  input  by console (n>0).
# Example:If the following n is given as input to the program:5
# Then, the output of the program should be:3.55
print("Enter a number :-")
iNumber=5
iSum = 0.00
iIndex=1
iFirstNumber=1
iSecondNumber=2

while iIndex <= iNumber:
    iValue = iFirstNumber / iSecondNumber
    iSum=iValue+iSum
    iFirstNumber=iSecondNumber
    iSecondNumber=iSecondNumber+1
    iIndex=iIndex+1
print("Value of sum is :-", iSum)


