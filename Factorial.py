# Factorial of a number to be calculated
number = 5
fact = 1
if number == 0:
    print("Factorial of ", number, " is ", number)
elif number == 1:
    print("Factorial of ", number, " is ", number)
else:
    for num in range(1, number+1):
        fact = fact * num
    print("Factorial of ", number, " is ", fact)

# Check if number is o
if fact % 2 == 0:
    print("Even")
else:
    print("odd")