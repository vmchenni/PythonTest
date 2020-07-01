# 13.Please  write  a  program  to  randomly  generate  a  list  with  5  numbers,
# which  are divisible by 5 and 7 , between 1 and 1000 inclusive.
import random
iIndex=0
list=[]
while iIndex < 5:
    n = random.randint(0, 1000)
    if n % 5 == 0 and n % 7 == 0:
        list.insert(iIndex, n)
        iIndex=iIndex+1
print("Randomly generated list is ", list)