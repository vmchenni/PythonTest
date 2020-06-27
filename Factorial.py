# Factorial of a number to be calculated
number = 5
fact = 1
#   Check if given number is zero
if number == 0:
    print("Factorial of ", number, " is ", number)
#   Check if given number is equal to one
elif number == 1:
    print("Factorial of ", number, " is ", number)
#     Calculate factorial of a number
else:
    for num in range(1, number+1):
        fact = fact * num
    print("Factorial of ", number, " is ", fact)

if fact % 2 == 0:
    print("Even")
else:
    print("odd")