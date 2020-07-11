myString="Hello world!"
iUpper=0
iLower=0
for i in myString:
    if i.isupper() :
        iUpper=iUpper+1
    elif i.islower():
        iLower=iLower+1
print("UPPER CASE:-",iUpper)
print("LOWER CASE:-",iLower)