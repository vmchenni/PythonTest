# Encryption and De-Cryption is not implemented, As my machine is not allowing to install packages
# Open database file for reading
file = open("DatabaseForUsers.txt", "r+")

# Collect reference ID from User
print("Enter Reference ID:-")
sReferenceIDFromUser = str(input())

# Collect finger print from user
print("Enter finger print")
sFingerPrintFromUser = str(input())

sList = []
isReferenceIdFound = False

# Traverse through file in search of records
for x in file:
    # print(x)
    sList = x.split("#")
    sReferenceIDFromStorage = sList[0]
    sFingerPrintFromStorage = sList[1]
    if sReferenceIDFromStorage == sReferenceIDFromUser:
        isReferenceIdFound = True
        if sFingerPrintFromStorage == sFingerPrintFromUser:
            print("Fingerprint Matched")
        else:
            print("Finger print not matched")
    # print("Reference ID is ",sReferenceIDFromStorage, "and Finger print is :-", sFingerPrintFromStorage)
if isReferenceIdFound:
    print("Records Found")
else:
    print("Records not found contact reference id issuer")
file.close()
