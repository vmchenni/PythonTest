# Write a program which will find all such numbers
# which are divisible by 7
# but are not a multiple of 5
# , between 2000 and 3200 (both included). The numbers obtained should be printed in acomma-separated sequence on a single line

for x in range(2000 - 1, 3000 + 1):
    if x % 7 == 0 and x % 5 != 0:
        print(x, end=" ")
