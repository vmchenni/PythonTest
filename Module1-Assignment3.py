#Write a program, whichwill find all the numbers between 1000 and 3000 (both included) such that each digit of a number is an even number. The numbers obtained should be printed in a comma separated sequence on a single line.
i = 1000
j = 0
A = []
for k in range(1000, 3000):
    if k % 2 == 0:
        A.append(k)
    # print(i)
    i = i+1

print(A)