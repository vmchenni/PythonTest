clientDetails = []
dictProfession = []
setProfession = set(dictProfession)


def fnReadFileData():
    file = open("bank-data.csv", "r")
    # clientDetailsPerLine=[]
    clientDetailsLocal = []
    # Read file collect details in list
    for line in file:
        # clientDetails.append(line)
        clientDetailsLocal = line.split(",")
        # print("Profession",clientDetailsLocal[2])
        clientDetails.append(clientDetailsLocal)
    # print(clientDetails)


# collect unique profession

def fncollectuniqueprofession():
    for client in clientDetails:
        # print(client[2])
        setProfession.add(client[2])
    # print("Set Value",setProfession)


def isEligible(inputProfession):
    if inputProfession in setProfession:
        print("Eligible")
    else:
        print("Not eligible")


#         Read data from file
fnReadFileData()

# Create set with unique job list
fncollectuniqueprofession()

# Validate input
while (1):
    inputProfession = str(input("Enter profession:- or Enter END to exit:-"))
    if inputProfession == "END":
        print("Exiting....")
        break
    else:
        isEligible(inputProfession)
