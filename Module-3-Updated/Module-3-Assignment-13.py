
print(int('0b11001000', 2))
myinput=input("EnterValue:-")
myList=myinput.split(",")
divisibleBy5=[]
for i in myList:
    if int(i, 2) % 5 == 0:
        divisibleBy5.append(int(i, 2))
print(divisibleBy5)